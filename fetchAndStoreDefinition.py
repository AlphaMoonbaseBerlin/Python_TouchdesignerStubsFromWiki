import requests
import json

def fetchItemNames():
    cacheFile = Path("itemsCache.json")

    if cacheFile.is_file(): 
        return json.loads( cacheFile.read_text() )
    
    continueToken = {}
    items = []
    while True:
        print("Fetching page query", continueToken)
        params= {
                "action" : "query",
                "format" : "json",
                "list"  : "categorymembers",
                "cmtitle" : "Category:Python_Reference",
                }
        if continueToken: params.update( continueToken )
        response = requests.get(
            "https://docs.derivative.ca/api.php",
            params = params 
            )
        response.raise_for_status()
        result = response.json()
        for categoryMember in result["query"]["categorymembers"]:
            items.append( categoryMember )

        if 'continue' not in result:
            break
        continueToken = result.get("continue")
    cacheFile.write_text(
        json.dumps( items, indent=4)
    )
    return items

from pathlib import Path
import wikitextparser

def fetchDefinitions( items ):
    cacheFile = Path("definitionCache.json")

    if cacheFile.is_file(): 
        return json.loads( cacheFile.read_text() )
    result = []
    for item in items:
        params = {
            "action" : "parse",
            "prop" : "wikitext",
            "page" : item["title"],
            "format" : "json"
        }
        print("fetching", item["title"])
        response = requests.get(
            "https://docs.derivative.ca/api.php",
            params = params 
            )
        for parsedResult in response.json()["parse"]["wikitext"].values():
            result.append(parsedResult)
   
    cacheFile.write_text(
        json.dumps( result, indent=4)
    )
    return result
import utils
def createDefinitionDict( definitions ):
    cacheFile = Path("definitionDictCache.json")

    #if cacheFile.is_file(): 
    #   return json.loads( cacheFile.read_text() )
    
    outputdict = {}

    for definition in definitions:
        wikiObject = wikitextparser.parse( definition )
        className = "NoLabelFound"
        classDict = {
            "members" : [],
            "methods" : [],
            "inherits": set()}
        for template in wikiObject.templates:
            templateDict = {
                argument.name : argument.value.strip() for argument in template.arguments
            }
           
            templateName = template.name.strip()

            if templateName == "TDClassSummary":
                className = templateDict["label"]
                classDict.update( templateDict )

            if templateName == "OPClassSummary":
                classDict["label"] = f"{templateDict['OPtype']}{templateDict['OPfamily']}"
                className = f"{templateDict['OPtype']}{templateDict['OPfamily']}"
            
            if templateName == "ClassInheritance":
               # print(f"Class Inheriteance for { className } from {templateDict['class']}")
                classDict["inherits"].add(templateDict["class"])
            if templateName in ["ClassMember"]:
                classDict["members"].append(templateDict)
            if templateName in ["ClassMethod"]:
                classDict["methods"].append(templateDict)
        outputdict[className] = classDict

    #We will have to order this. The file gets large and pylance has issues making sense of the order.

    cacheFile.write_text(
        json.dumps( outputdict, indent=4, cls=utils.SetEncoder )
    )
    return outputdict
         


def writeBultinFile(definitionDict):
    builtinsFileHandler = Path("types", "__builtins__.py")
    builtinsFileHandler.parent.mkdir( parents=True, exist_ok=True)
    try:
        builtinsFileHandler.unlink()
    except FileNotFoundError:
        pass
    builtinsFileHandler.touch()
    with builtinsFileHandler.open("wt") as builtinsFile:
        builtinsFile.truncate(0)
        builtinsFile.write("from typing import Annotated\n")

        for element in definitionDict.values():
            if not "label" in element:
                continue
            builtinsFile.write(
                f"class {element['label']}({','.join(element['inherits'])}):\n"
            )

            #Summary needs to be cleared up a little. They are all over the place!

            #builtinsFile.write(
            #   f'\t"""{element.get("summary", element.get("label"))}"""\n'
            #)
            for member in element["members"]:

                #Again, same is true for texts here, also types sometimes are inconsisten.

                #builtinsFile.write(
                #    f'\t{member["name"]}:Annotated[{member["type"] or "any"},"""{member["text"]}"""]\n'
                #)   
                builtinsFile.write(
                    f'\t{member["name"]}:any\n'
                )   
                
            builtinsFile.write("\tpass")
            builtinsFile.write("\n\n\n")
            
def main():
    items = fetchItemNames()
    definitions = fetchDefinitions( items )
    definitionDict = createDefinitionDict( definitions )
    writeBultinFile( definitionDict )


if __name__ == "__main__":
    main()
        
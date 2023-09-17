import requests
import json
from pathlib import Path
import wikitextparser
import utils
#data fetching
def fetchItemNames():
    cacheFile = Path("cache/itemsCache.json")

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
def fetchDefinitions( items ):
    cacheFile = Path("cache/definitionCache.json")

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

#data creation
def defaultClassDict( label = ""):
    return {
            "label" : label or "NotSet",
            "members" : [],
            "methods" : [],
            "subclasses" : {},
            "inherits": [] }
def createDefinitionDict( definitions ):
    cacheFile = Path("cache/definitionDictCache.json")

    if cacheFile.is_file(): 
       return json.loads( cacheFile.read_text() )
    
    outputdict = {}

    for definition in definitions:
        wikiObject = wikitextparser.parse( definition )
        className = "NoLabelFound"
        classDict = defaultClassDict()
        
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
                if templateDict["class"] in classDict["inherits"]: continue
                classDict["inherits"].append(templateDict["class"])
            if templateName in ["ClassMember"]:
                classDict["members"].append(templateDict)
            if templateName in ["ClassMethod"]:
                classDict["methods"].append(templateDict)
        
        pathName = className.split(".")

        if len(pathName) <= 1:
            outputdict[className] = classDict
        else:
            nextDict = outputdict.setdefault( pathName.pop(0), defaultClassDict() )
            for everyOtherEnty in pathName:
                nextSubclass:dict = nextDict["subclasses"]
                nextDict = nextSubclass.setdefault( everyOtherEnty, defaultClassDict(label = everyOtherEnty))
                classDict["label"] = everyOtherEnty
            nextDict.update( classDict )
            
            

    #We will have to order this. The file gets large and pylance has issues making sense of the order.

    cacheFile.write_text(
        json.dumps( outputdict, indent=4, cls=utils.SetEncoder )
    )
    return outputdict

#data handling
def sortDefinitionDict( defnitions:dict):
    sortedList = []
    for key, value in defnitions.items():
        keyIndex = 0
        for inheritance in value["inherits"] + [member["type"] for member in value["members"]]:
            try:
                foundIndex = sortedList.index(inheritance)
            except ValueError:
                continue
            if foundIndex > keyIndex: keyIndex = foundIndex
        #if we cannot find anything but have inheritance, move to the bac!
        keyIndex = (keyIndex or len(sortedList)*bool(value["inherits"])) + 1
        print("Inserting", key, "at", keyIndex)
        sortedList.insert(keyIndex, key)
    for key in sortedList:
        defnitions[key]["inherits"] = defnitions[key]["inherits"]
    return {key : defnitions[key] for key in sortedList}
def clearDefinitionDict( definitionDict):
    for classDefinition in definitionDict.values():
        classDefinition["summary"] = classDefinition.get("summary", "").replace('"', "'")
        for member in classDefinition["members"]:
            member["text"] = member["text"].replace('"', "'")
            if member["type"] in definitionDict: continue
            try:
                eval( member["type"] ) is type
            except:
                member["type"] = "any"

        for method in classDefinition["methods"]:
            method["text"] = method["text"].replace('"', "'")
            method["call"] = method["call"].replace("..", ", *args")
            method["call"] = method["call"].replace("...", ", *args")
            print(method["call"])
            if method["returns"] in definitionDict: continue
            try:
                eval( method["returns"] ) is type
            except:
                method["returns"] = "any"

    
    return definitionDict

#datawriting
def writeClassAsModuleToFile( element, fileHandler, depth = 0):
    for member in element["members"]:
        writeMemberToFile( member, fileHandler )
    for method in element["methods"]:
        writeMethodToFile( method, fileHandler  )
    pass

def writeMemberToFile(member, fileHandler, depth = 0):
    annotation = utils.trim( member["text"] )
    offset = "\t" * depth
    fileHandler.write(
             f'{offset}{member["name"]} : {member["type"] or "any"}\n'
        )     
    fileHandler.write(
            f'{offset}"""{annotation}"""\n'
        )
    
def writeMethodToFile(member, fileHandler, depth = 0):
    offset = "\t"*depth
    annotation = utils.trim(member["text"])
    
    fileHandler.write(
             f'{offset}def {member["call"]} -> {member["returns"] or "any"}: \n'
    )     
    fileHandler.write(
            f'{offset}\t"""{annotation}"""\n'
    )
    fileHandler.write(f"{offset}\tpass\n")

def writeClassToFile( element, fileHandler, depth = 0):
    offset = "\t" * depth
    fileHandler.write(
       f"{offset}class {element['label']}({','.join(element['inherits'])}):\n"
    )
    fileHandler.write(
       f'\t{offset}"""{element.get("summary", element.get("label"))}"""\n'
    )
    for member in element["members"]:
        writeMemberToFile(member, fileHandler, depth=depth+1)

    for method in element["methods"]:
        writeMethodToFile( method, fileHandler, depth=depth+1)

    for subclass in element["subclasses"].values():
        writeClassToFile(subclass, fileHandler, depth=depth+1)

    fileHandler.write(f"{offset}\tpass")
    fileHandler.write(f"{offset}\n\n\n")
def writeBultinFile(definitionDict):
    builtinsFileHandler = Path("typings", "__builtins__.pyi")
    builtinsFileHandler.parent.mkdir( parents=True, exist_ok=True)
    
    with builtinsFileHandler.open("wt") as builtinsFile:
        builtinsFile.write("from td import *\n")

        for element in definitionDict.values():
            if not "label" in element:
                continue
            writeClassToFile( element, builtinsFile)

def writeTDModule(definitionDict):
    builtinsFileHandler = Path("typings", "td.py")
    builtinsFileHandler.parent.mkdir( parents=True, exist_ok=True)

    with builtinsFileHandler.open("wt") as builtinsFile:
        writeClassAsModuleToFile( definitionDict["td"], builtinsFile )

           
def main():
    items = fetchItemNames()
    definitions = fetchDefinitions( items )
    definitionDict = createDefinitionDict(  definitions ) 
    cleanDefinitionDict = clearDefinitionDict( definitionDict )
    sortedDefinition = sortDefinitionDict( cleanDefinitionDict )
    writeTDModule( sortedDefinition )
    writeBultinFile( sortedDefinition )


if __name__ == "__main__":
    main()
        
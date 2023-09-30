import requests
import json
from pathlib import Path
import wikitextparser
import utils


# Generic DataFetching
def fetchCategoryNames(label):
    cacheFile = Path(f"cache/{label}NamesCache.json")
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
                "cmtitle" : f"Category:{label}",
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

def fetchItems(label, items):
    cacheFile = Path(f"cache/{label}DefinitionCache.json")

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
        try:
            for parsedResult in response.json()["parse"]["wikitext"].values():
                result.append(parsedResult)
        except json.JSONDecodeError:
            print("Error decoding Response", item["title"])
   
    cacheFile.write_text(
        json.dumps( result, indent=4)
    )
    return result

#####parameterFetching
def fetchOperatorPages():
    families = ["COMPs", "TOPs", "CHOPs", "SOPs", "DATs", "MATs"]
    outputList = []
    for familyMember in families:
        outputList = outputList + fetchCategoryNames( familyMember )
    return outputList

def fetchOperatorDocs( items ):
    return fetchItems( "OperatorDocs", items )

#####ClassFetching
def fetchClassPages():
    return [ item for item in fetchCategoryNames( "Python_Reference" ) if not item["title"].startswith("Experimental") ]

def fetchClassDefinitions( items ):
    return fetchItems("Python_Reference", items)

def stringToDictList( wikiString):
    try:
        return [ templateToDict( template ) for template in 
                    wikitextparser.parse( wikiString ).templates ]
    except: 
        print("Failed to parsse Wikistring", wikiString)
        return []
    
def templateToDict( template ):
    return { argument.name : argument.value.strip() for argument in template.arguments }

#####data creation
### Classes
def defaultClassDict( label = ""):
    return {
            "label" : label or "NotSet",
            "members" : [],
            "methods" : [],
            "subclasses" : {},
            "inherits": []
             }

def deepTemplateToDict( potentialWikiString:str):
    try:
        wikiObject = wikitextparser.parse( potentialWikiString )        
        for template in wikiObject.templates:
            return {
                argument.name : deepTemplateToDict( argument.value.strip() ) for argument in template.arguments
            }
    except:
        return potentialWikiString
    
def createClassDefinitionDict( definitions ):
    cacheFile = Path("cache/classDefinitionDictCache.json")

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
        #Adding default parameters!
        parameters = [f"parameter.{classDict['label']}"] + [f"parameter.{inherit}" for inherit in classDict["inherits"]]
        classDict["members"].append( {
                "text": f"Parameters of { ' & '.join( parameters )}",
                "type": "|".join( parameters),
                "name": "par"
        })
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

def dictGetUnion( dictionary, *args):
    return dictionary.get(*args[0], dictGetUnion(dictionary, *args[1:]))

### Parameter
def defaultParameterDict():
    return {
        "text": "", 
        "type": "",
        "name": "",
        "items" : []
    }

parameterExpander = {
    "Default" : [ { "suffix" : "", "type" : "any"}],
    "Float" : [ { "suffix" : "", "type" : "float" } ],
    "OP"    : [ {"suffix" : "", "type" : "OP"}],
    "CHOP"    : [ {"suffix" : "", "type" : "CHOP"}],
    "COMP"    : [ {"suffix" : "", "type" : "COMP"}],
    "TOP"    : [ {"suffix" : "", "type" : "TOP"}],
    "MAT"    : [ {"suffix" : "", "type" : "MAT"}],
    "Int"   : [ { "suffix" : "", "type" : "int" } ],
    "Str"   : [ { "suffix" : "", "type" : "str" } ],
    "XYZ"   : [ { "suffix" : "x", "type" : "float" }, 
               { "suffix" : "y", "type" : "float" },
                { "suffix" : "z", "type" : "float" } ],
    "RGB"   : [ { "suffix" : "r", "type" : "float" }, 
               { "suffix" : "g", "type" : "float" },
                { "suffix" : "b", "type" : "float" } ],
    "RGBA"   : [ { "suffix" : "r", "type" : "float" }, 
               { "suffix" : "g", "type" : "float" },
                { "suffix" : "b", "type" : "float" },
                 { "suffix" : "a", "type" : "float" } ],
    "Menu"  : [{ "suffix" : "", "type" : "str" } ],
    "StrMenu"  : [{ "suffix" : "", "type" : "str" } ],
    "XY"   : [ { "suffix" : "x", "type" : "float" }, 
               { "suffix" : "y", "type" : "float" }],
    "WH"   : [ { "suffix" : "w", "type" : "float" }, 
               { "suffix" : "h", "type" : "float" }],
    "Toggle" : [{ "suffix" : "", "type" : "bool" }],
    "File" : [{ "suffix" : "", "type" : "str" }],
    "Folder" : [{ "suffix" : "", "type" : "str" }],
}

def createParTypeDefinitionDict():
    outputDict = {}
    for key, value in parameterExpander.items():
        parTypeClassDict = defaultClassDict()
        parTypeClassDict["label"] = f"{key}Par"
        parTypeClassDict["inherits"] = ["Par"]
        parTypeClassDict["members"] = [{
                "text": "Read or set the value.",
                "type": value[0]["type"],
                "name": "val"     
            }]
        outputDict[f"{key}Par"] = parTypeClassDict
    return outputDict

def createParDefinitionDict( definitions ):
    cacheFile = Path("cache/parDefinitionDictCache.json")

    if cacheFile.is_file(): 
       return json.loads( cacheFile.read_text() )
    
    outputdict = {}

    for definition in definitions:
        wikiObject = wikitextparser.parse( definition )
        className = ""
        classDict = defaultClassDict()
        collectedParameters = {}
        for template in wikiObject.templates:
            templateDict = templateToDict( template )
           
            templateName = template.name.strip()
            
            if templateName == "Summary":
                className = templateDict["opClass"].split("_")[0]
                classDict["label"] = className
                classDict.update( templateDict )
                
            if templateName == "ParameterPage":
                pageParameters = stringToDictList( templateDict["items"])
                
                for parameter in pageParameters:
                    if parameter is None: 
                        print("Parameter is None. FOR WHATEVER REASON!")
                        continue

                    #So we are fetching the paameterType. 
                    if parameter.get("itemName", ""): continue
                    parameterType = parameter.get("parType", "Default")
                    expandedPrameterDef = parameterExpander.get( parameterType, parameterExpander["Default"] )
                    parameterTypeString = f"{parameterType}Par"
                    
                    for expanded in expandedPrameterDef :
                        
                        className       = className or f"{parameter.get('opType', '')}{parameter['opFamily']}"
                        parameterName   = parameter.get("parName", "")
                        
                        expandedName    = f"{parameterName}{expanded['suffix']}"
                        
                        if parameterType in ("Menu", "StrMenu"):
                            
                            menuClassName = f"{className}{expandedName}{parameterType}"
                            subclassObject = defaultClassDict( label = menuClassName )
                            subclassObject["inherits"] = [f"{parameterType}Par"]
                            items = [ f"\"{item['itemName']}\"" for item in stringToDictList( parameter.get("parItems", "") ) ] or ['"*"']
                            
                            subclassObject["members"].append({
                                "text" : "Set the menuValue",
                                "type" : f"Literal[{','.join(items)}]",
                                "name" : "val"
                            })
                            
                            parameterTypeString = menuClassName
                            outputdict[menuClassName] = subclassObject

                        parameterDict = collectedParameters.setdefault(expandedName, defaultParameterDict() )
                        parameterDict["text"] = f'{parameter.get("parType", "")} : {parameter.get("parSummary", "")}' 
                        parameterDict["type"] = parameterTypeString
                        parameterDict["name"] = expandedName
            
        classDict = outputdict.get( className, classDict)
        classDict["members"] = classDict["members"] + list( collectedParameters.values() )
        outputdict[className] = classDict
            
    #We will have to order this. The file gets large and pylance has issues making sense of the order.

    #cacheFile.write_text(
    #    json.dumps( outputdict, indent=4, cls=utils.SetEncoder )
    #)
    return outputdict

#####data handling
def sortClassDefinitionDicts( defnitions:dict):
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
        keyIndex = (keyIndex or len(sortedList) * bool(value["inherits"])) + 1
        print("Inserting", key, "at", keyIndex)
        sortedList.insert(keyIndex, key)
    for key in sortedList:
        defnitions[key]["inherits"] = defnitions[key]["inherits"]
    return {key : defnitions[key] for key in sortedList}

def clearDefinitionDict( definitionDict):
    for classDefinition in definitionDict.values():
        classDefinition["summary"] = wikiToMD( classDefinition.get("summary", "") )
        for member in classDefinition["members"]:
            member["text"] = wikiToMD( member["text"] )
            if member["type"] in definitionDict: continue
            try:
                eval( member["type"] ) is type
            except:
                #member["type"] = "any"
                pass

        for method in classDefinition["methods"]:
            method["text"] = wikiToMD( method["text"] )
            method["call"] = method["call"].replace("...", ", *args")
            method["call"] = method["call"].replace("..", ", *args")
            if method["returns"] in definitionDict: continue
            try:
                eval( method["returns"] ) is type
            except:
                method["returns"] = "any"

    return definitionDict

def makeClassCall( text ):
    return re.sub(r"\(", "(self, ", text)

def wikiToMD( text ):
    text = text.replace('"', "'")
    text = text.replace(":*", ": *")
    text = text.replace("\n", "\n\n")
    # YOU CANT PARSE HTML COPY pasta here.....
    text = re.sub(r"<syntaxhighlight (lang=('\w*'|\w*))+>((.|\n)*?)<\/syntaxhighlight>", r"```\2\n\3\n```\n", text)
    #text = re.sub(r"<blockquote></blockquote>")
    text = re.sub(r"<code>(.*)</code>", r"```\1```", text)
    
    text = text.replace("*", "* ")
    return text
import re

#####datawriting
def writeClassAsModuleToFile( element, fileHandler, depth = 0):
    for member in element["members"]:
        writeMemberToFile( member, fileHandler )
    for method in element["methods"]:
        writeMethodToFile( method, fileHandler  )
    pass

def writeMemberToFile(member, fileHandler, depth = 0):
    annotation = utils.trim( member["text"] )
    annotation = member["text"]
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
        method["call"] = makeClassCall( method["call"] )
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
        builtinsFile.write("import parameter\n")
        builtinsFile.write("import parameterTypes\n")
        for element in definitionDict.values():
            if not "label" in element:
                continue
            writeClassToFile( element, builtinsFile)

def writeParameterTypeFile( definitionDict):
    parameterFileHandler = Path("typings", "parameterTypes.py")
    parameterFileHandler.parent.mkdir( parents=True, exist_ok=True)
    
    with parameterFileHandler.open("wt") as parameterFile:
        for element in definitionDict.values():
            if not "label" in element:
                continue
            writeClassToFile( element, parameterFile)

def writeParameterFile(definitionDict):
    builtinsFileHandler = Path("typings", "parameter.py")
    builtinsFileHandler.parent.mkdir( parents=True, exist_ok=True)
    
    with builtinsFileHandler.open("wt") as builtinsFile:
        builtinsFile.write("from parameterTypes import *\n")
        builtinsFile.write("from typing import Literal\n")
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
    classPages = fetchClassPages()
    classDefinitions = fetchClassDefinitions( classPages )
    classDefinitionDicts = createClassDefinitionDict(  classDefinitions ) 
    cleanedClassDefinitionDict = clearDefinitionDict( classDefinitionDicts )
    sortedClassDefinitionDict = sortClassDefinitionDicts( cleanedClassDefinitionDict )
    writeTDModule( sortedClassDefinitionDict )
    writeBultinFile( sortedClassDefinitionDict )

    operatorPages = fetchOperatorPages()
    operatorDefinition = fetchOperatorDocs( operatorPages )
    parameterDefinitionDicts = createParDefinitionDict( operatorDefinition )
    writeParameterFile( clearDefinitionDict( parameterDefinitionDicts) )
    writeParameterTypeFile( createParTypeDefinitionDict() )
if __name__ == "__main__":
    main()
        
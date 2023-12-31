import sys
def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)
import json
class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
    

class node:
    children: list

    def __init__(self, value = None) -> None:
        self.children = {}
        self.value = value

    def findEntry(self, entry:str, depth = 0):
        if entry in self.children: 
            print("Found", entry)
            return depth, self.children[entry]
        currentDepth = 0
        
        for child in self.children.values():
            currentDepth, potentialChildNode = child.findEntry(entry, depth = depth + 1)
            if potentialChildNode: return currentDepth, potentialChildNode
        return currentDepth, None
    
    def traverse(self):
        for child in self.children.values():
            for child in child.traverse():
                yield child
        yield self
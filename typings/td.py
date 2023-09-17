me : OP
"""Reference to the current [[OP Class|operator]] that is being executed or evaluated. This can be used in parameter expressions, or DAT scripts."""
absTime : any
"""Reference to the [[AbsTime Class|AbsTime]] object."""
app : any
"""Reference to the [[App Class|application]] installation."""
ext : any
"""Reference to the extension searching object. See [[extensions]] for more information."""
families : dict
"""A dictionary containing a list of [[OP Class|operator]] types for each operator family. 

```python


for a in families['SOP']:

	# do something with a


```
"""
licenses : any
"""Reference to the currently installed [[Licenses Class|licences]]."""
mod : any
"""Reference to the [[MOD Class|Module On Demand]] object."""
monitors : any
"""Reference to the group of available [[Monitors Class|monitors]]."""
op : OP
"""The operator finder object, for accessing operators through paths or shortcuts. '''Note:''' a version of this method that searches relative to a specific operator is also in [[OP Class]].



```op(pattern1, pattern2..., includeUtility=False) &rarr; [[OP Class|OP]] or None```

<blockquote>

Returns the first OP whose path matches the given pattern, relative to ```root```. Will return None if nothing is found. Multiple patterns may be specified which are all added to the search. Numeric OP ids may also be used.

*  ```pattern``` - Can be string following the [[Pattern Matching]] rules, specifying which OP to return, or an integer, which must be an OP Id. Multiple patterns can be given, the first matching OP will be returned.

*  ```includeUtility``` '''(Optional)''' - if True, allow [[Network_Utilities:_Comments,_Network_Boxes,_Annotates|Utility nodes]] to be returned. If False, Utility operators will be ignored.



```python


b = op('project1')

b = op('foot* ', 'hand* ')

b = op(154)


```


</blockquote>

```op.shortcut &rarr; OP```

<blockquote>

:An operator specified with by a [[Global OP Shortcut]]. If no operator exists an exception is raised. These shortcuts are global, and must be unique. That is, cutting and pasting an operator with a Global OP Shortcut specified will lead to a name conflict. One shortcut must be renamed in that case. Furthermore, only components can be given Global OP Shortcuts.

: * ```shortcut``` - Corresponds to the Global OP Shortcut parameter specified in the target operator.

```python


b = op.Videoplayer 


```


To list all Global OP Shortcuts:

```python


for x in op:

	print(x)


```


</blockquote>"""
parent : OP
"""The [[Parent Shortcut|Parent Shortcut]] object, for accessing parent components through indices or shortcuts.

    

'''Note:''' a version of this method that searches from a specific operator is also in [[OP Class]].



```parent(n)  OP or None```



The nth parent of the current operator. If n not specified, returns the parent. If n = 2, returns the parent of the parent, etc. If no parent exists at that level, None is returned.

* n - (Optional) n is the number of levels up to climb. When n = 1 it will return the operator's parent.

```python


p = parent(2) #grandfather


```


```parent.shortcut  OP```



A parent component specified with a shortcut. If no parent exists an exception is raised.

* shortcut - Corresponds to the [[Parent Shortcut]] parameter specified in the target parent.

```python


   n = parent.Videoplayer


```


See also Parent Shortcut for more examples."""
iop : OP
"""The Internal Operator Shortcut object, for accessing internal shortcuts.

    

'''Note:''' a version of this method that searches from a specific operator is also in [[OP Class]]."""
ipar : OP
"""The Internal Operator Parameter Shortcut object, for accessing internal shortcuts.

    

'''Note:''' a version of this method that searches from a specific operator is also in [[OP Class]]."""
project : any
"""Reference to the [[Project Class|project session]]."""
root : OP
"""Reference to the topmost root [[OP Class|operator]]."""
runs : any
"""Reference to the [[Runs Class|runs]] object, which contains delayed executions."""
sysinfo : any
"""Reference to the [[SysInfo Class|system information]]."""
ui : any
"""Reference to the [[UI Class|ui options]]."""
def ops(pattern1, pattern2, *args, includeUtility=False) -> list: 
	"""Returns a (possibly empty) list of OPs that match the patterns, relative to this OP.

Multiple patterns may be provided. Numeric OP ids may also be used.

* pattern - Can be string following the [[Pattern Matching]] rules, specifying which OPs to return, or an integer, which must be an OP Id. Multiple patterns can be given and all matched OPs will be returned.

Note a version of this method that searches relative to an operator is also in the [[OP Class]].

```python


newlist = n.ops('arm* ', 'leg* ', 'leg5/foot* ')


```"""
	pass
def passive(OP) -> OP: 
	"""Returns a passive version of the [[OP Class|operator]]. Passive OPs do not cook before their members are accessed."""
	pass
def run(script, arg1, arg2, *args, endFrame=False, fromOP=None, asParameter=False, group=None, delayFrames=0, delayMilliSeconds=0, delayRef=me) -> Run: 
	"""[[Run Class|Run]] the script, returning a [[Run Class|Run]] object which can be used to optionally modify its execution. This is most often used to run a script with a delay, as specified in the delayFrames or delayMilliSeconds arguments. See [[Run Command Examples]] for more info.

* script - A string that is the script code to execute.

* arg - (Optional) One or more arguments to be passed into the script when it executes. They are accessible in the script using a tuple named args.

* endFrame - (Keyword, Optional) If True, the execution will be delayed until the end of the current frame.

* fromOP - (Keyword, Optional) Specifies an optional [[OP Class|operator]] from which the execution will be run relative to.

* asParameter - (Keyword, Optional) When fromOP used, run relative to a parameter of fromOP.

* group - (Keyword, Optional) Can be used to specify a string label for the group of Run objects this belongs to. This label can then be used with the [[Runs Class|td.runs]] object to modify its execution.

* delayFrames - (Keyword, Optional) The number of frames to wait before executing the script.

* delayMilliSeconds - (Keyword, Optional) The number of milliseconds to wait before executing the script. This value is rounded to the nearest frame.

* delayRef - (Keyword, Optional) Specifies an optional [[OP Class|operator]] from which the delay time is derived. You can use your own [[Time COMP|independent time component]] or ```op.TDResources```, a built-in independent time component."""
	pass
def fetchStamp(key, default) -> any: 
	"""Return an object from the global stamped parameters. If the item is not found, the default is returned instead. Parameters can be stamped with the [[Copy SOP]].

* key - The name of the entry to retrieve.

* default - If no item is found then the passed value is returned instead.

```python


v = fetchStamp('sides', 3)


```"""
	pass
def var(varName) -> str: 
	"""Find the value for the given [[Variables|variable]]."""
	pass
def varExists(varName) -> bool: 
	"""Returns true if the [[Variables|variable]] is defined."""
	pass
def varOwner(varName) -> any: 
	"""Returns the [[OP Class|operator]] that defines the [[Variables|variable]], or None if it's not defined."""
	pass
def isMainThread() -> bool: 
	"""Is True when called from the main application editing thread. Any calls that access operators, etc., must be called from the main thread."""
	pass
def clear() -> None: 
	"""Clear the textport of all text."""
	pass

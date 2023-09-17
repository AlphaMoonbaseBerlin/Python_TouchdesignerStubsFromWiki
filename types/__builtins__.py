from typing import Annotated
class abletonlinkCHOP(CHOP,OP):
	pass


class VFSFile():
	name:Annotated[str,"""Get or set the name of the file. This name can include slashes but should not include leading slashes."""]
	size:Annotated[int,"""Get the size of the file data."""]
	date:Annotated[any,"""Get the modified date of the file in the form of a datetime Python object."""]
	virtualPath:Annotated[str,"""Get the virtual path of the file. Returns a String formatted for fetching the file data from VFS in operators such as the Movie File In TOP. Format is <code>vfs:<path to owner>:<filename></code>."""]
	originalFilePath:Annotated[str,"""Get the original file path on disk. If the VFSFile was created from a bytearray and not a file on disk then this will be empty."""]
	owner:Annotated[OP,"""Get the OP owner."""]
	byteArray:Annotated[bytearray,"""Get or set the file data as a bytearray."""]
	pass


class VFS():
	owner:Annotated[OP,"""Get the OP owner."""]
	pass


class Vertex():
	index:Annotated[int,"""The vertex position in its [[Prim Class|primitive]]."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	point:Annotated[any,"""Get or set the [[Point Class|point]] to which the vertex refers."""]
	prim:Annotated[any,"""The [[Prim Class|prim]] to which the vertex belongs."""]
	pass


class Vector():
	x:Annotated[float,"""Gets or sets the X component of the vector."""]
	y:Annotated[float,"""Gets or sets the Y component of the vector."""]
	z:Annotated[float,"""Gets or sets the Z component of the vector."""]
	pass


class Undo():
	globalState:Annotated[bool,"""Is global undo enabled or not."""]
	redoStack:Annotated[list,"""A list of names for redo operations available."""]
	state:Annotated[bool,"""Is undo enabled or not."""]
	undoStack:Annotated[list,"""A list of names for undo operations available."""]
	pass


class UI():
	clipboard:Annotated[str,"""Get or set the operating system clipboard text contents."""]
	colors:Annotated[any,"""Access to the application [[Colors Class|colors]]."""]
	dpiBiCubicFilter:Annotated[bool,"""Get or set the global DPI scale filtering mode of TouchDesigner windows. True means bi-cubic, False means linear."""]
	masterVolume:Annotated[float,"""Get or set the master audio output volume. A value of 0 is no output, while a value of 1 is full output."""]
	options:Annotated[any,"""Access to the application [[Options Class|options]]."""]
	panes:Annotated[any,"""Access to the set of all [[Panes Class|panes]]."""]
	performMode:Annotated[bool,"""Get or set [[Perform Mode]].  Set to True to go into Perform Mode, False to go into [[Designer Mode]]."""]
	preferences:Annotated[any,"""Access to the application [[Preferences Class|preferences]], which can also be access through the [[Preferences Dialog]]."""]
	redrawMainWindow:Annotated[bool,"""Get or set whether the main window should redraw. The main window is either the main network editor, or the perform window."""]
	rolloverOp:Annotated[OP,"""Operator currently under the mouse in a network editor."""]
	rolloverPar:Annotated[any,"""Parameter currently under the mouse in a parameter dialog."""]
	rolloverPanel:Annotated[any,"""returns the latest panel to get a rollover event. Takes into account click through, depth order, and other panel settings."""]
	lastChopChannelSelected:Annotated[any,"""Last [[Channel|CHOP channel]] selected via mouse."""]
	showPaletteBrowser:Annotated[bool,"""Get or set display of the palette browser."""]
	status:Annotated[str,"""Get or set the status message.
<syntaxhighlight lang=python>
ui.status = 'Operation Complete'
</syntaxhighlight>"""]
	undo:Annotated[any,"""Acess to application undo functions."""]
	windowWidth:Annotated[int,"""Get the app window width."""]
	windowHeight:Annotated[int,"""Get the app window height."""]
	windowX:Annotated[int,"""Get the app window X position."""]
	windowY:Annotated[int,"""Get the app window Y position."""]
	pass


class Textport():
	pass


class TextLine():
	glyph:Annotated[int,"""The index of the glyph that represents this text line."""]
	fontIndex:Annotated[int,"""The index of the font that the glyph belongs to. Glyphs are not interchangable between fonts."""]
	text:Annotated[str,"""The text for this line."""]
	origin:Annotated[any,"""A tdu.Position object that gives the baseline origin of the line of text."""]
	lineWidth:Annotated[float,"""The width of the format box of this line of text."""]
	pass


class tdu():
	fileTypes:Annotated[dict,"""A dictionary of all supported file types, organized by category.
<syntaxhighlight lang=python>
# example of various file types accepted by Movie File In TOP
tdu.fileTypes['movie']
tdu.fileTypes['image']
</syntaxhighlight>
<syntaxhighlight lang=python>
# other file types
tdu.fileTypes['audio']
</syntaxhighlight>
Note: Acceptable file types can be both uppercase and lowercase, so if <code>suffix</code> is a suffix string, you need to force it to lowercase by using <code>suffix.lower()</code>:
<syntaxhighlight lang=python>
for suffix.lower() in tdu.fileTypes['movie']:
        print(suffix)
</syntaxhighlight>"""]
	Matrix:Annotated[any,"""The [[Matrix Class|Matrix]] definition class."""]
	Position:Annotated[any,"""The [[Position Class|Position]] definition class."""]
	Vector:Annotated[any,"""The [[Vector Class|Vector]] definition class."""]
	Quaternion:Annotated[any,"""The [[Quaternion Class|Quaternion]] definition class."""]
	Color:Annotated[any,"""The [[Color Class|Color]] definition class."""]
	Dependency:Annotated[any,"""The [[Dependency Class|Dependency]] definition class."""]
	FileInfo:Annotated[any,"""The FileInfo object takes a file path and has a few utility properties to provide additional information. It is derived from str, so will work as a Python string, but can be differentiated from a regular string by using <code>isinstance(tdu.FileInfo)</code>.
Utility properties include:
*path: filepath string
*ext: string after and including "."
*fileType: the TD filetype (from tdu.fileTypes)
*absPath: the absolute path to filepath
*dir: the containing directory of filepath
*exists: exists in file-system
*isDir: is a directory in the file-system
*isFile: is a file in the file-system
*baseName: the name of the final element in the path"""]
	ArcBall:Annotated[any,"""The [[ArcBall Class|ArcBall]] definition class."""]
	Camera:Annotated[any,"""The [[Camera Class|Camera]] definition class."""]
	debug:Annotated[any,"""Helper module for the builtin debug statement. [[Debug_module|Documentation.]]"""]
	class Timecode():
		countdown:Annotated[tdu.Timecode,"""Return a Timecode Object of the difference between the length and the current time. If a custom length is not specified then it will use a default: 23:59:59:ff for SMPTE and 99:59:59:ff."""]
		dropFrame:Annotated[bool,"""True if the Timecode is drop-frame, False otherwise."""]
		fps:Annotated[float,"""Get or set the framerate (in frames per second) of the Timecode."""]
		frame:Annotated[int,"""The Timecode frame: 0 to fps-1"""]
		hour:Annotated[int,"""The Timecode hour: 0 to 99 if non-SMPTE, 0 to 23 otherwise."""]
		minute:Annotated[int,"""The Timecode minute: 0 to 59."""]
		second:Annotated[int,"""The Timecode second: 0 to 59."""]
		negative:Annotated[bool,"""True if the Timecode is negative, and False otherwise. Always False if the Timecode is following SMPTE standard."""]
		smpte:Annotated[bool,"""True if the Timecode is SMPTE standard, and False otherwise. SMPTE Timecodes cannot be negative and cannot exceed 24 hours."""]
		text:Annotated[string,"""Get the text format of the Timecode."""]
		totalFrames:Annotated[int,"""The total number of Timecode frames, which is calculated from the hour, minute, second, frame values. Whether or not the Timecode is drop frame will also affect the value."""]
		totalSeconds:Annotated[float,"""The total number of Timecode seconds, which is calculated from the hour, minute, second, frame values. Whether or not the Timecode is drop frame will also affect the value."""]
		pass	


	pass


class td():
	me:Annotated[OP,"""Reference to the current [[OP Class|operator]] that is being executed or evaluated. This can be used in parameter expressions, or DAT scripts."""]
	absTime:Annotated[any,"""Reference to the [[AbsTime Class|AbsTime]] object."""]
	app:Annotated[any,"""Reference to the [[App Class|application]] installation."""]
	ext:Annotated[any,"""Reference to the extension searching object. See [[extensions]] for more information."""]
	families:Annotated[dict,"""A dictionary containing a list of [[OP Class|operator]] types for each operator family.
<syntaxhighlight lang=python>
for a in families['SOP']:
        # do something with a
</syntaxhighlight>"""]
	licenses:Annotated[any,"""Reference to the currently installed [[Licenses Class|licences]]."""]
	mod:Annotated[any,"""Reference to the [[MOD Class|Module On Demand]] object."""]
	monitors:Annotated[any,"""Reference to the group of available [[Monitors Class|monitors]]."""]
	op:Annotated[OP,"""The operator finder object, for accessing operators through paths or shortcuts. '''Note:''' a version of this method that searches relative to a specific operator is also in [[OP Class]].

<code>op(pattern1, pattern2..., includeUtility=False) &rarr; [[OP Class|OP]] or None</code>
<blockquote>
Returns the first OP whose path matches the given pattern, relative to <code>root</code>. Will return None if nothing is found. Multiple patterns may be specified which are all added to the search. Numeric OP ids may also be used.
* <code>pattern</code> - Can be string following the [[Pattern Matching]] rules, specifying which OP to return, or an integer, which must be an OP Id. Multiple patterns can be given, the first matching OP will be returned.
* <code>includeUtility</code> '''(Optional)''' - if True, allow [[Network_Utilities:_Comments,_Network_Boxes,_Annotates|Utility nodes]] to be returned. If False, Utility operators will be ignored.

<syntaxhighlight lang=python>
b = op('project1')
b = op('foot*', 'hand*')
b = op(154)
</syntaxhighlight>
</blockquote>
<code>op.shortcut &rarr; OP</code>
<blockquote>
:An operator specified with by a [[Global OP Shortcut]]. If no operator exists an exception is raised. These shortcuts are global, and must be unique. That is, cutting and pasting an operator with a Global OP Shortcut specified will lead to a name conflict. One shortcut must be renamed in that case. Furthermore, only components can be given Global OP Shortcuts.
:*<code>shortcut</code> - Corresponds to the Global OP Shortcut parameter specified in the target operator.
<syntaxhighlight lang=python>
b = op.Videoplayer
</syntaxhighlight>
To list all Global OP Shortcuts:
<syntaxhighlight lang=python>
for x in op:
        print(x)
</syntaxhighlight>
</blockquote>"""]
	parent:Annotated[OP,"""The [[Parent Shortcut|Parent Shortcut]] object, for accessing parent components through indices or shortcuts.

'''Note:''' a version of this method that searches from a specific operator is also in [[OP Class]].

<code>parent(n)  OP or None</code>

The nth parent of the current operator. If n not specified, returns the parent. If n = 2, returns the parent of the parent, etc. If no parent exists at that level, None is returned.
*n - (Optional) n is the number of levels up to climb. When n = 1 it will return the operator's parent.
<syntaxhighlight lang=python>
p = parent(2) #grandfather
</syntaxhighlight>
<code>parent.shortcut  OP</code>

A parent component specified with a shortcut. If no parent exists an exception is raised.
*shortcut - Corresponds to the [[Parent Shortcut]] parameter specified in the target parent.
<syntaxhighlight lang=python>
   n = parent.Videoplayer
</syntaxhighlight>
See also Parent Shortcut for more examples."""]
	iop:Annotated[OP,"""The Internal Operator Shortcut object, for accessing internal shortcuts.

'''Note:''' a version of this method that searches from a specific operator is also in [[OP Class]]."""]
	ipar:Annotated[OP,"""The Internal Operator Parameter Shortcut object, for accessing internal shortcuts.

'''Note:''' a version of this method that searches from a specific operator is also in [[OP Class]]."""]
	project:Annotated[any,"""Reference to the [[Project Class|project session]]."""]
	root:Annotated[OP,"""Reference to the topmost root [[OP Class|operator]]."""]
	runs:Annotated[any,"""Reference to the [[Runs Class|runs]] object, which contains delayed executions."""]
	sysinfo:Annotated[any,"""Reference to the [[SysInfo Class|system information]]."""]
	ui:Annotated[any,"""Reference to the [[UI Class|ui options]]."""]
	pass


class SysInfo():
	numCPUs:Annotated[int,"""The number of CPUs/cores on the system."""]
	ram:Annotated[float,"""Amount of available RAM memory."""]
	numMonitors:Annotated[int,"""The number of monitors."""]
	xres:Annotated[int,"""The system's current monitor resolution width."""]
	yres:Annotated[int,"""The system's current monitor resolution height."""]
	tfs:Annotated[str,"""The path to the TFS directory."""]
	MIDIInputs:Annotated[any,"""A list of all MIDI Input device names."""]
	MIDIOutputs:Annotated[any,"""A list of all MIDI Output device names."""]
	pass


class Sequence():
	owner:Annotated[OP,"""The OP to which this object belongs."""]
	numBlocks:Annotated[int,"""Get or set the total number of parameter blocks in this sequence."""]
	maxBlocks:Annotated[int,"""The maximum number of blocks allowed in the sequence, or None if limitless."""]
	blocks:Annotated[set,"""The set of all blocks in this sequence. A block is a set of parameters which can be repeated in an operator."""]
	pass


class Segment():
	beginFrames:Annotated[int,"""The beginning point of the segment expressed in frames."""]
	beginSamples:Annotated[int,"""The beginning point of the segment expressed in samples."""]
	beginSeconds:Annotated[float,"""The beginning point of the segment expressed in seconds."""]
	custom:Annotated[any,"""Ordered dictionary of all the extra column values associated with the segment."""]
	cycle:Annotated[bool,"""Whether or not the segment will repeat itself."""]
	cycleEndAlertFrames:Annotated[int,"""The amount of time before cycling the callback will be executed, expressed in frames."""]
	cycleEndAlertSamples:Annotated[int,"""The amount of time before cycling the callback will be executed, expressed in samples."""]
	cycleEndAlertSeconds:Annotated[float,"""The amount of time before cycling the callback will be executed, expressed in seconds."""]
	cycleLimit:Annotated[bool,"""Whether or not the segment will repeat itself indefinitely."""]
	delayFrames:Annotated[int,"""The delay portion of the segment expressed in frames."""]
	delaySamples:Annotated[int,"""The delay portion of the segment expressed in samples."""]
	delaySeconds:Annotated[float,"""The delay portion of the segment expressed in seconds."""]
	lengthFrames:Annotated[int,"""The length portion of the segment expressed in frames."""]
	lengthSamples:Annotated[int,"""The length portion of the segment expressed in samples."""]
	lengthSeconds:Annotated[float,"""The length portion of the segment expressed in seconds."""]
	maxCycles:Annotated[int,"""The maximum number of repetitions."""]
	owner:Annotated[any,"""The OP to which this object belongs."""]
	row:Annotated[int,"""Named tuple of all the parameter or column values describing the segment."""]
	speed:Annotated[float,"""The speed multiplier of the segment."""]
	index:Annotated[int,"""The numeric index of this segment."""]
	pass


class Runs():
	pass


class Run():
	active:Annotated[bool,"""Get or set whether or not this script will execute once its target frame is reached."""]
	group:Annotated[any,"""Get or set the group label associated with this script."""]
	isCell:Annotated[bool,"""Returns true when the source is a [[Cell Class|cell]], from a Cell.run() call."""]
	isDAT:Annotated[bool,"""Returns true when the source is a [[DAT Class|DAT]], from a DAT.run() call."""]
	isString:Annotated[bool,"""Returns true when the source is a string, from a td module run() call"""]
	path:Annotated[OP,"""The [[OP Class|operator]] location from which this script will execute."""]
	remainingFrames:Annotated[int,"""Get or set the remaining number of frames before the execution will occur."""]
	remainingMilliseconds:Annotated[int,"""Get or set the remaining number of milliseconds before the execution will occur."""]
	source:Annotated[any,"""The source of the run. It will be either a [[DAT Class|DAT]], [[Cell Class|cell]], or string."""]
	pass


class Quaternion():
	x:Annotated[float,"""Get or set the x component of the quaternion."""]
	y:Annotated[float,"""Get or set the y component of the quaternion."""]
	z:Annotated[float,"""Get or set the z component of the quaternion."""]
	w:Annotated[float,"""Get or set the w component of the quaternion."""]
	pass


class Project():
	folder:Annotated[str,"""The folder at which the project resides."""]
	name:Annotated[str,"""The filename under which the project is saved."""]
	saveVersion:Annotated[str,"""The [[App Class|App]] version number when the project was last saved."""]
	saveBuild:Annotated[str,"""The [[App Class|App]] build number when the project was last saved."""]
	saveTime:Annotated[str,"""The time and date the project was last saved."""]
	saveOsName:Annotated[str,"""The [[App Class|App]] operating system name when the project was last saved."""]
	saveOsVersion:Annotated[str,"""The [[App Class|App]] operating system version when the project was last saved."""]
	saveOSName:Annotated[str,"""The [[App Class|App]] operating system name when the project was last saved."""]
	saveOSVersion:Annotated[str,"""The [[App Class|App]] operating system version when the project was last saved."""]
	paths:Annotated[dict,"""A dictionary which can be used to define URL-syntax path prefixes, enabling you to move your media to different locations easily. This dictionary is saved and loaded in the <code>.toe</code> file.  Example: Run <code>project.paths['movies'] = 'C:/MyMovies'</code>, and reference it with a parameter expression: <code>movies://butterfly.jpg</code>. To manually convert between expanded and collapsed paths, use <code>tdu.collapsePath()</code> and <code>tdu.expandPath</code> from the [[Tdu Module]], for example <code>tdu.expandPath('movies://butterfly.jpg')</code> expands to <code>C:/MyMovies/butterfly.jpg</code>. If you already have your paths setup, choosing files from file browsers in OPs will create paths using these shortcuts rather than full paths. Additionally, to enable you to have different media locations on different machines, you can put a JSON file in the same folder as your <code>.toe</code> that gets read on startup. This will override any existing locations saved in projects.paths to the new machine specific file paths specified in the .json. Only existing entries in <code>project.paths</code> will be used. If the .json contains path names not specified in <code>project.paths</code>, those will be ignored. It would contain something like <code>{ "project.paths": { "movies": "M:/MyMovies" } }</code>. If your <code>.toe</code> file is called <code>MyProject.10.toe</code>, the JSON file must be called <code>MyProject.Settings.json</code>. The idea is that this .json would be unique to machines, and not commited to version control or shared between machines."""]
	cookRate:Annotated[float,"""Get or set the maximum number of frames processed each second. In general you should not need to use this. It is preferred to look at the FPS of the root component to know the cooking rate. Individual [[COMP Class|components]] may have their own rates, specified by rate.
<syntaxhighlight lang=python>
a = project.cookRate # get the current cook rate
project.cookRate = 30 # set the cook rate to 30 FPS
</syntaxhighlight>
Note: This is displayed and set in the user interface at the bottom-left: the "FPS" field."""]
	realTime:Annotated[bool,"""Get or set the real time cooking state. When True, frames may be skipped in order to maintain the cookRate. When False, all frames are processed sequentially regardless of duration. This is useful to render movies out using the Movie File Out TOP without dropping any frames for example.
<syntaxhighlight lang=python>
a = project.realTime
project.realTime = False # turn off real time playback.
</syntaxhighlight>"""]
	isPrivate:Annotated[bool,"""True when the project networks cannot be directly viewed."""]
	isPrivateKey:Annotated[bool,"""True when the private networks are accessible by a pass phrase."""]
	cacheParameters:Annotated[bool,"""Cache parameter values instead of always evaluating."""]
	externalToxModifiedInProject:Annotated[bool,"""Callback for when an external tox has been modified in the current project and there are other instances of the same tox loaded elsewhere in the project."""]
	externalToxModifiedOnDisk:Annotated[bool,"""Callback for when an external tox file has been modified on disk."""]
	windowOnTop:Annotated[bool,"""Get or set the window on top state."""]
	windowStartMode:Annotated[any,"""Get or set the window start mode.
The mode is one of: <code>WindowStartMode.AUTO</code>, <code>WindowStartMode.FULL</code>, <code>WindowStartMode.LEFT</code>, <code>WindowStartMode.RIGHT</code> or <code>WindowStartMode.CUSTOM</code>."""]
	windowDraw:Annotated[bool,"""Get or set the window drawing state."""]
	windowStartCustomWidth:Annotated[int,"""Get or set the window start width. Only used when windowStartMode is <code>WindowStartMode.CUSTOM</code>."""]
	windowStartCustomHeight:Annotated[int,"""Get or set the window start height. Only used when windowStartMode is <code>WindowStartMode.CUSTOM</code>."""]
	windowStartCustomX:Annotated[int,"""Get or set the window start X position. Only used when windowStartMode is <code>WindowStartMode.CUSTOM</code>."""]
	windowStartCustomY:Annotated[int,"""Get or set the window start Y position. Only used when windowStartMode is <code>WindowStartMode.CUSTOM</code>."""]
	performOnStart:Annotated[bool,"""Get or set the perform on start state."""]
	performWindowPath:Annotated[OP,"""Get or set the perform window path."""]
	resetAudioOnDeviceChange:Annotated[bool,"""Get or set whether audio devices momentarily reset when devices are added or removed to the system."""]
	pass


class ProductEntry():
	licenseType:Annotated[int,"""Returns the license type for this product entry on the dongle."""]
	updateDate:Annotated[any,"""The date the product entry is valid until. Returns a tuple in the form (YYYY, MM, DD)."""]
	version:Annotated[str,"""The version of TouchDesigner this dongle product entry is valid for."""]
	pass


class Prims():
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	pass


class Prim():
	center:Annotated[any,"""Get or set the barycentric coordinate of this primitive. It is expressed as a tdu.Position object."""]
	index:Annotated[int,"""The primitive index in the list."""]
	normal:Annotated[any,"""The calculated normal vector of this primitive, expressed as a tdu.Vector object."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	weight:Annotated[float,"""The associated weight of the primitive. Only certain primitives, such as those created by the [[Metaball SOP]] can modify this value from its default of 2.0."""]
	direction:Annotated[any,"""A normalized vector pointing from the centroid of the SOP to the centroid of this primitive."""]
	min:Annotated[any,"""The minimum coordinates of this primitive along each dimension, expressed as a tdu.Position object."""]
	max:Annotated[any,"""The maximum coordinates of this primitive along each dimension, expressed as a tdu.Position object."""]
	size:Annotated[any,"""The size of this primitive along each dimension, expressed as a tdu.Position object."""]
	pass


class Preferences():
	defaults:Annotated[dict,"""A dictionary of preferences with their default values."""]
	pass


class Position():
	x:Annotated[float,"""Gets or sets the X component of the position."""]
	y:Annotated[float,"""Gets or sets the Y component of the position."""]
	z:Annotated[float,"""Gets or sets the Z component of the position."""]
	pass


class Points():
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	pass


class Point():
	index:Annotated[int,"""The point index in the list."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	P:Annotated[any,"""The coordinates as [[AttributeData Class|AttributeData]]. Individual components can be read or written with the [] operator.
<syntaxhighlight lang=python>
point.P[0] = 5
point.P = (1,0,1)
</syntaxhighlight>"""]
	x:Annotated[float,"""Get or set x coordinate value. This is the same as P[0]."""]
	y:Annotated[float,"""Get or set y coordinate value. This is the same as P[1]."""]
	z:Annotated[float,"""Get or set z coordinate value. This is the same as P[2]."""]
	normP:Annotated[any,"""The normalized position of this point within the bounding box of the SOP. Will always be in the range [0,1]. Expressed as tdu.Position object."""]
	pass


class Peer():
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	port:Annotated[int,"""The network port associated with the peer."""]
	address:Annotated[str,"""The network address associated with the peer."""]
	hostname:Annotated[str,"""The network hostname associated with the peer."""]
	pass


class ParGroupUnit():
	unit:Annotated[any,"""The unit parameter in this ParGroupUnit object."""]
	pass


class ParGroupPulse():
	pass


class ParGroupCollection():
	owner:Annotated[OP,"""The OP to which this object belongs."""]
	pass


class ParGroup():
	bindExpr:Annotated[tuple,"""Get or set expressions that return a Parameter object. This can be used to bind this parameter's constant values to the referenced parameters.

Example:
<syntaxhighlight lang=python>p.bindExpr = ("op('geo1').par.tx", "op('geo1').par.ty", "op('geo1').par.tz")</syntaxhighlight>
        Note the outside quotes, as bindExpr is an expression, not an object."""]
	bindMaster:Annotated[tuple,"""The objects to which this parameter is bound to, possibly None."""]
	bindRange:Annotated[bool,"""Get or set parameter's range binding state. If True, min, max, clampMin, clampMax, normMin, normMax, normVal values will be based on master bind parameter. Can only be set on Custom Parameters."""]
	bindReferences:Annotated[tuple,"""The (possibly empty) lists of objects which bind to this parameter."""]
	clampMax:Annotated[tuple,"""Get or set the parameter's numerical clamping behaviors. If set to <syntaxhighlight lang=python inline=true>clampMax = True</syntaxhighlight>, the parameter will clamp on the upper end at the value specified in max Can only be set on Custom Parameters."""]
	clampMin:Annotated[tuple,"""Get or set the parameter's numerical clamping behaviors. If set to <syntaxhighlight lang=python inline=true>clampMin = True</syntaxhighlight>, the parameter will clamp on the lower end at the value specified in min Can only be set on Custom Parameters."""]
	collapsable:Annotated[bool,"""Returns True if the parameter is collapsable."""]
	collapser:Annotated[bool,"""Returns True if the parameter is a parent of collapsable parameters (ie. a collapser)."""]
	default:Annotated[tuple,"""Get or set the parameter's default values. Can only be set on Custom Parameters. Only one of default, defaultExpr can be set."""]
	defaultExpr:Annotated[tuple,"""Get or set the parameter's default expressions. Can only be set on Custom Parameters. Only one of default, defaultExpr can be set.
<syntaxhighlight lang=python>
# value defaults to this expression.
op('base1').parGroup.Size.defaultExpr = ('me.time.frame', 'me.time.frame', 'me.time.frame')
</syntaxhighlight>"""]
	enable:Annotated[bool,"""Get or set the parameter's enable state. Can only be set on Custom Parameters."""]
	enableExpr:Annotated[any,"""Get or set an expression that controls the enable state for this parameter group.
<syntaxhighlight lang=python>
p.enableExpr = "me.par.X.menuIndex == 5"
</syntaxhighlight>
Note the outside quotes, as this is an expression, not an object."""]
	exportOP:Annotated[tuple,"""The operators exporting to this parameter."""]
	exportSource:Annotated[any,"""The objects exporting to this parameter. Examples: Cell, Channel or None."""]
	expr:Annotated[tuple,"""Get or set the non-evaluated expressions only. To get the parameter's current values, regardless of the Parameter Mode (constant, expression, export or bound), use the eval() method described below.
<syntaxhighlight lang=python>
op('geo1').parGroup.t.expr = ('absTime.frame', 'absTime.frame', 'absTime.frame')
# set to match current frame
</syntaxhighlight>
When setting this member, the parameter will also be placed in expression mode. See mode member below.
'''NOTE:''' For convenience, the expression is placed in double-quotes so you can safely put in expressions containing single quotes. 'a' and "a" have the same effect of enclosing strings in python."""]
	help:Annotated[any,"""Get or set a custom parameter's help text. To see any parameter's help, rollover the parameter while holding the Alt key."""]
	isDefault:Annotated[bool,"""True when the parameter value, expression and mode are in their default settings."""]
	isCustom:Annotated[bool,"""True for Custom Parameters."""]
	isFloat:Annotated[bool,"""True for floating point numeric parameters."""]
	isInt:Annotated[bool,"""True for integer numeric parameters."""]
	isMenu:Annotated[bool,"""True for menu parameters."""]
	isMomentary:Annotated[bool,"""True for momentary parameters."""]
	isNumber:Annotated[bool,"""True for numeric parameters."""]
	isOP:Annotated[bool,"""True for OP parameters."""]
	isPulse:Annotated[bool,"""True for pulse parameters."""]
	isPython:Annotated[bool,"""True for python parameters."""]
	isString:Annotated[bool,"""True for string parameters."""]
	isToggle:Annotated[bool,"""True for toggle parameters."""]
	label:Annotated[any,"""Get or set the parameter's label.
<syntaxhighlight lang=python>
op('myOperator').parGroup.Custompar.label = 'Translate'
</syntaxhighlight>
Can only be set on Custom Parameters."""]
	max:Annotated[tuple,"""Get or set the parameter's numerical maximum values. The parameter's values will be clamped at that maximum if <syntaxhighlight lang=python inline=true>clampMax = True</syntaxhighlight>. Can only be set on Custom Parameters."""]
	menuIndex:Annotated[tuple,"""Get or set a tuple of menu constant values by their indices."""]
	menuLabels:Annotated[tuple,"""Get or set a tuple of lists of all possible menu choice labels. In the case of non menu parameters, None(s) are returned. Can only be set on Custom Parameters."""]
	menuNames:Annotated[tuple,"""Get or set a tuple of lists of all possible menu choice names. In the case of non menu parameters, None(s) are returned. Can only be set on Custom Parameters."""]
	menuSource:Annotated[tuple,"""Get or set a tuple of expressions that returns objects with <code>.menuItems</code> <code>.menuNames</code> members.  This can be used to create a custom menu whose entries dynamically follow that of another menu for example."""]
	min:Annotated[tuple,"""Get or set the parameter's numerical minimum values. The parameter's values will be clamped at that minimum if <syntaxhighlight lang=python inline=true>clampMin = True</syntaxhighlight> for the particular Par. Can only be set on Custom Parameters."""]
	mode:Annotated[tuple,"""Get or set the parameter's evaluation modes.
<syntaxhighlight lang=python>
op('geo1').parGroup.t.mode = (ParMode.EXPRESSION, ParMode.EXPRESSION, ParMode.EXPRESSION)
</syntaxhighlight>
The modes are one of:  <code>ParMode.CONSTANT</code>, <code>ParMode.EXPRESSION</code>, or <code>ParMode.EXPORT</code>, or <code>ParMode.BIND</code>.
See [[Parameter_Dialog#Working_with_Parameter_Modes]] for more information."""]
	name:Annotated[any,"""Get or set the parameter's unique name.
<syntaxhighlight lang=python
>op('myOperator').parGroup.Custompar.name = 'Translate'
</syntaxhighlight>
Can only be set on Custom Parameters."""]
	normMax:Annotated[tuple,"""Get or set the parameter's maximum slider values if the parameter is a numerical slider. Can only be set on Custom Parameters."""]
	normMin:Annotated[tuple,"""Get or set the parameter's minimum slider values if the parameter is a numerical slider. Can only be set on Custom Parameters."""]
	normVal:Annotated[tuple,"""Get or set the parameter's values as a normalized slider position. Can only be set on Custom Parameters."""]
	order:Annotated[int,"""Get or set the parameter's position on the parameter page.  Can only be set on Custom Parameters."""]
	owner:Annotated[OP,"""The OP to which this object belongs."""]
	page:Annotated[Page,"""Get or set the parameter page the custom parameter is part of. Can only be set on Custom Parameters."""]
	password:Annotated[bool,"""Get or set the parameter's password mode. When True all text is rendered as asterisks. Can only be set on Custom string, int or float parameters. Custom Parameters."""]
	prevMode:Annotated[tuple,"""The parameter's previous evaluation modes."""]
	readOnly:Annotated[bool,"""Get or set the parameter's read only status. When True the parameter cannot be modified through the UI, only scripting."""]
	displayOnly:Annotated[bool,"""Get or set the parameter's displayOnly state. Can only be set on Custom Parameters."""]
	sequence:Annotated[any,"""The set of sequential parameter blocks this parameter belongs to, or None."""]
	startSection:Annotated[bool,"""Get or set the parameter's separator status. When True a visible separator is drawn between this parameter and the ones preceding it. Can only be set on Custom Parameters."""]
	style:Annotated[any,"""Describes the behavior and contents of the custom parameter. Example 'Float', 'Int', 'Pulse', 'XYZ', etc."""]
	subLabel:Annotated[tuple,"""Returns the names of the sub-label."""]
	val:Annotated[tuple,"""Get or set the constant values of the parameter only. To get the parameter's current values, regardless of the Parameter Modes (<code>constant</code>, <code>expression</code>, <code>export</code> or <code>bound</code>), use the eval() method described below.
<syntaxhighlight lang=python>
op('geo1').parGroup.t.val   # the constant values
op('geo1').parGroup.t.eval()   # the evaluated parameter
op('geo1').parGroup.t.val = (1,2,3)
op('geo1').parGroup.t = (1,2,3)  #equivalent to above, more concise form
</syntaxhighlight>
When setting this member, the parameter will also be placed in constant mode.  See mode member below.
To set a menu value by its index, use the menuIndex member as described below."""]
	valid:Annotated[bool,"""True if the referenced parameter currently exists, False if it has been deleted."""]
	index:Annotated[int,"""The parameter's order in the list."""]
	pass


class ParCollection():
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	pass


class Par():
	valid:Annotated[bool,"""True if the referenced parameter currently exists, False if it has been deleted."""]
	val:Annotated[any,"""Get or set the constant value of the parameter only. To get the parameter's current value, regardless of the [[Parameter Mode]] (constant, expression, export or bound), use the <syntaxhighlight lang=python inline>eval()</syntaxhighlight> method described below.
<syntaxhighlight lang=python>
op('geo1').par.tx.val   # the constant value
op('geo1').par.tx.eval()   # the evaluated parameter
op('geo1').par.tx.val = 5
op('geo1').par.tx = 5  # equivalent to above, more concise form
op('parexec1').par.op = [parent(), parent(2)] # you can assign a list of ops to a parameter that allows multiple operators
</syntaxhighlight>
When setting this member, the parameter will also be placed in constant mode.  See mode member below.
To set a menu value by its index, use the <code>menuIndex</code> member as described below."""]
	expr:Annotated[str,"""Get or set the non-evaluated expression only. To get the parameter's current value, regardless of the [[Parameter Mode]] (constant, expression, export or bound), use the <syntaxhighlight lang=python inline>eval()</syntaxhighlight> method described below.
<syntaxhighlight lang=python>
op('geo1').par.tx.expr = 'absTime.frame'  #set to match current frame
</syntaxhighlight>
When setting this member, the parameter will also be placed in expression mode. See mode member below.
'''NOTE:''' For convenience, the expression is placed in double-quotes so you can safely put in expressions containing single quotes. 'a' and "a" have the same effect of enclosing strings in python."""]
	enableExpr:Annotated[str,"""Get or set an expression that controls the enable state for this parameter.
<syntaxhighlight lang=python>
p.enableExpr = "me.par.X.menuIndex == 5"
# Note the outside quotes, as this is an expression, not an object.
</syntaxhighlight>"""]
	exportOP:Annotated[any,"""The [[OP Class|operator]] exporting to this parameter."""]
	exportSource:Annotated[any,"""The object exporting to this parameter. Examples: [[Cell Class|Cell]], [[Channel Class|Channel]] or None."""]
	bindExpr:Annotated[any,"""Get or set an expression that returns a Parameter object. This can be used to bind this parameter's constant value to the referenced parameter.
<syntaxhighlight lang=python>p.bindExpr = "op('geo1').par.tx"</syntaxhighlight>
Note the outside quotes, as bindExpr is an expression, not an object."""]
	bindMaster:Annotated[any,"""The object to which this parameter is bound to, possibly None."""]
	bindReferences:Annotated[list,"""The (possibly empty) list of objects which bind to this parameter."""]
	bindRange:Annotated[bool,"""Get or set parameter's range binding state. If True, min, max, clampMin, clampMax, normMin, normMax, normVal values will be based on master bind parameter. Can only be set on Custom Parameters."""]
	hidden:Annotated[bool,"""Get the parameter's hidden status. When True the parameter is considered obsolete or irrelevant and should not be modified. They are not shown in the dialog but only maintained for backward compatibility."""]
	index:Annotated[int,"""A unique identifier for the parameter.  May change in the case of custom parameters."""]
	vecIndex:Annotated[int,"""The parameter's vector index. For example, <syntaxhighlight lang=python inline>op('geo1').par.tz</syntaxhighlight> would have a value of 2."""]
	name:Annotated[str,"""Get or set the parameter's unique name.
<syntaxhighlight lang=python>
op('myOperator').par.Custompar.name = 'Translate'
</syntaxhighlight>
Can only be set on [[Custom Parameters]]."""]
	label:Annotated[str,"""Get or set the parameter's label.
<syntaxhighlight lang=python>
op('myOperator').par.Custompar.label = 'Translate'
</syntaxhighlight>
Can only be set on [[Custom Parameters]]."""]
	subLabel:Annotated[str,"""Returns the name of the sub-label."""]
	startSection:Annotated[bool,"""Get or set the parameter's separator status. When <code>True</code> a visible separator is drawn between this parameter and the ones preceding it. Can only be set on [[Custom Parameters]]."""]
	displayOnly:Annotated[bool,"""Get or set the parameter's displayOnly state. Can only be set on Custom Parameters."""]
	readOnly:Annotated[bool,"""Get or set the parameter's read only status. When <code>True</code> the parameter cannot be modified through the UI, only scripting."""]
	help:Annotated[str,"""Get or set a custom parameter's help text. To see any parameter's help, rollover the parameter while holding the Alt key. For built-in parameters this can be used to get the parameter's help text."""]
	tuplet:Annotated[any,"""The tuplet of parameters this parameter belongs to. A tuplet is typically a set of parameters sharing one line on a parameter dialog, example: Translate (x, y, z)."""]
	tupletName:Annotated[str,"""The tuplet name of a parameter.  Example: The tuplet name of a (tx,ty,tz) translate parameter is t."""]
	parGroup:Annotated[any,"""The [[ParGroup]] of parameters this parameter belongs to. A ParGroup is a set of parameters sharing one line on a parameter dialog with a common label, example: Translate (x, y, z).."""]
	min:Annotated[any,"""Get or set the parameter's numerical minimum value. The parameter's value will be clamped at that minimum if clampMin = True. Can only be set on [[Custom Parameters]]."""]
	max:Annotated[any,"""Get or set the parameter's numerical maximum value. The parameter's value will be clamped at that maximum if clampMax = True. Can only be set on [[Custom Parameters]]."""]
	clampMin:Annotated[bool,"""Get or set the parameter's numerical clamping behavior. If set to clampMin = True, the parameter will clamp on the lower end at the value specified in min Can only be set on [[Custom Parameters]]."""]
	clampMax:Annotated[bool,"""Get or set the parameter's numerical clamping behavior. If set to clampMax = True, the parameter will clamp on the upper end at the value specified in max Can only be set on [[Custom Parameters]]."""]
	default:Annotated[any,"""Get or set the parameter's default value. Can only be set on [[Custom Parameters]].  Only one of default, defaultExpr can be set."""]
	defaultExpr:Annotated[str,"""Get or set the parameter's default expression. Can only be set on [[Custom Parameters]].  Only one of default, defaultExpr can be set.
<syntaxhighlight lang=python>
# value defaults to this expression.
op('base1').par.Size.defaultExpr = 'me.time.frame'
</syntaxhighlight>"""]
	normMin:Annotated[float,"""Get or set the parameter's minimum slider value if the parameter is a numerical slider. Can only be set on [[Custom Parameters]]."""]
	normMax:Annotated[float,"""Get or set the parameter's maximum slider value if the parameter is a numerical slider. Can only be set on [[Custom Parameters]]."""]
	normVal:Annotated[float,"""Get or set the parameter's value as a normalized slider position. Can only be set on [[Custom Parameters]]."""]
	enable:Annotated[bool,"""Get or set the parameter's enable state. Can only be set on [[Custom Parameters]]."""]
	order:Annotated[int,"""Get or set the parameter's position on the parameter page.  Can only be set on [[Custom Parameters]]."""]
	page:Annotated[any,"""Get or set the parameter page the custom parameter is part of. Can only be set on [[Custom Parameters]]."""]
	password:Annotated[bool,"""Get or set the parameter's password mode. When True all text is rendered as asterisks. Can only be set on Custom string, int or float parameters. [[Custom Parameters]]."""]
	mode:Annotated[any,"""Get or set the parameter's evaluation mode.
<syntaxhighlight lang=python>
op('geo1').par.tx.mode = ParMode.EXPRESSION
</syntaxhighlight>
The mode is one of:  <code>ParMode.CONSTANT</code>, <code>ParMode.EXPRESSION</code>, or <code>ParMode.EXPORT</code>, or <code>ParMode.BIND</code>.
See [[Parameter_Dialog#Working_with_Parameter_Modes]] for more information."""]
	prevMode:Annotated[any,"""The parameter's previous evaluation mode."""]
	menuNames:Annotated[list,"""Get or set a list of all possible menu choice names. In the case of non menu parameters, None is returned. Can only be set on [[Custom Parameters]]."""]
	menuLabels:Annotated[list,"""Get or set a list of all possible menu choice labels. In the case of non menu parameters, None is returned. Can only be set on [[Custom Parameters]]."""]
	menuIndex:Annotated[int,"""Get or set a menu constant value by its index."""]
	menuSource:Annotated[str,"""Get or set an expression that returns an object with .menuItems .menuNames members.  This can be used to create a custom menu whose entries dynamically follow that of another menu for example. Simple menu sources include another parameter with a menu c, an object created by [[Tdu Module|tdu.TableMenu]], or an object created by [[TDFunctions|TDFunctions.parMenu]].
<syntaxhighlight lang=python>
p.menuSource = "op('audiodevin1').par.device"
</syntaxhighlight>
Note the outside quotes, as menuSource is an expression, not an object."""]
	collapser:Annotated[bool,"""Returns True if the parameter is a parent of collapsable parameters (ie. a collapser)."""]
	collapsable:Annotated[bool,"""Returns True if the parameter is collapsable."""]
	sequence:Annotated[set,"""The set of [[Sequence Class|sequential]] parameter blocks this parameter belongs to, or None."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	styleCloneImmune:Annotated[bool,"""Get or set the parameter's style clone immunity. When <code>False</code>, the parameter definition is matched to any matching master parameter its operator is cloned to. When <code>True</code>, it is left unchanged."""]
	lastScriptChange:Annotated[tuple,"""Return information about when this parameter was last modified by a script. Cleared when the parameter is updated via the UI.
<syntaxhighlight lang=python>
python >>> op('/level1').par.invert.lastScriptChange
SetInfo(dat=type:textDAT path:/text1, function='<module>', line=1, frame=300061, timeStamp=1613150878)
</syntaxhighlight>"""]
	isDefault:Annotated[bool,"""True when the parameter value, expression and mode are in their default settings."""]
	isCustom:Annotated[bool,"""True for [[Custom Parameters]]."""]
	isPulse:Annotated[bool,"""True for pulse parameters."""]
	isMomentary:Annotated[bool,"""True for momentary parameters."""]
	isMenu:Annotated[bool,"""True for menu parameters."""]
	isNumber:Annotated[bool,"""True for numeric parameters."""]
	isFloat:Annotated[bool,"""True for floating point numeric parameters."""]
	isInt:Annotated[bool,"""True for integer numeric parameters."""]
	isOP:Annotated[bool,"""True for OP parameters."""]
	isPython:Annotated[bool,"""True for python parameters."""]
	isString:Annotated[bool,"""True for string parameters."""]
	isToggle:Annotated[bool,"""True for toggle parameters."""]
	style:Annotated[str,"""Describes the behavior and contents of the custom parameter. Example <code>'Float'</code>, <code>'Int'</code>, <code>'Pulse'</code>, <code>'XYZ'</code>, etc."""]
	pass


class Panes():
	current:Annotated[any,"""The currently selected [[Pane Class|pane]]."""]
	pass


class PanelValue():
	name:Annotated[str,"""The name of the panel value. See [[Panel Value]] for the list of possible names. name is a string."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	val:Annotated[any,"""Get or set the panel value."""]
	valid:Annotated[bool,"""True if the referenced panel value currently exists, False if it has been deleted."""]
	pass


class Panel():
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs.

In addition to the above, this object contains a member for each panel value in the component.
<syntaxhighlight lang=python>
a = op('button1').panel.u
</syntaxhighlight>"""]
	pass


class Pane():
	owner:Annotated[COMP,"""Get or set the [[COMP Class|component]] this pane points to."""]
	id:Annotated[int,"""A unique numeric identifier."""]
	link:Annotated[int,"""Get or set the numeric link index."""]
	enable:Annotated[bool,"""Get or set mouse and keyboard interactivity on the pane."""]
	maximize:Annotated[bool,"""Enable or disable the pane maximize state."""]
	name:Annotated[str,"""Get or set the pane name."""]
	ratio:Annotated[float,"""Get or set the split proportion of the pane, if the pane was previously split."""]
	bottomLeft:Annotated[any,"""The coordinates of the bottom left corner, expressed in both pixels and uv offsets, in a named tuple."""]
	topRight:Annotated[any,"""The coordinates of the top right corner, expressed in both pixels and uv offsets, in a named tuple."""]
	type:Annotated[any,"""The enumerated type of the pane. Example: NetworkEditor.
The enumeration is called PaneType and consists of:
*PaneType.NETWORKEDITOR
*PaneType.PANEL
*PaneType.GEOMETRYVIEWER
*PaneType.TOPVIEWER
*PaneType.CHOPVIEWER
*PaneType.ANIMATIONEDITOR
*PaneType.PARAMETERS
*PaneType.TEXTPORT"""]
	pass


class Page():
	name:Annotated[bool,"""Get or set the name of the page."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	parGroups:Annotated[list,"""A list of [[ParGroup Class|parameter groups]] on this page. A ParGroup is the set of parameters on one line."""]
	parTuplets:Annotated[list,"""The list of [[Par Class|parameter]] tuplets on this page. A [[tuplet]] is the set of parameters on one line."""]
	pars:Annotated[list,"""The list of [[Par Class|parameters]] on this page."""]
	index:Annotated[int,"""The numeric index of this page."""]
	isCustom:Annotated[bool,"""Boolean for whether this page is custom or not."""]
	pass


class Options():
	pass


class OP():
	valid:Annotated[bool,"""True if the referenced operator currently exists, False if it has been deleted."""]
	id:Annotated[int,"""Unique id for the operator. This id can also be passed to the op() and ops() methods. Id's are not consistent when a file is re-opened, and will change if the OP is copied/pasted, changes OP types, deleted/undone. The id will not change if the OP is renamed though. Its data type is integer."""]
	name:Annotated[str,"""Get or set the operator name."""]
	path:Annotated[str,"""Full path to the operator."""]
	digits:Annotated[int,"""Returns the numeric value of the last consecutive group of digits in the name, or None if not found. The digits can be in the middle of the name if there are none at the end of the name."""]
	base:Annotated[str,"""Returns the beginning portion of the name occurring before any digits."""]
	passive:Annotated[bool,"""If true, operator will not cook before its access methods are called.  To use a passive version of an operator n, use passive(n)."""]
	curPar:Annotated[any,"""The parameter currently being evaluated. Can be used in a parameter expression to reference itself."""]
	time:Annotated[OP,"""[[timeCOMP Class|Time Component]] that defines the operator's time reference."""]
	ext:Annotated[any,"""The object to search for parent [[Extensions|extensions]].
<syntaxhighlight lang="python">
me.ext.MyClass
</syntaxhighlight>"""]
	mod:Annotated[any,"""Get a [[MOD Class|module on demand]] object that searches for DAT modules relative to this operator."""]
	pages:Annotated[list,"""A list of all built-in pages."""]
	parGroup:Annotated[tuple,"""An intermediate [[ParGroupCollection Class|parameter collection]] object, from which a specific [[ParGroup Class|parameter group]] can be found.
<syntaxhighlight lang="python">
n.parGroup.t
# or
n.parGroup['t']
</syntaxhighlight>"""]
	par:Annotated[any,"""An intermediate [[ParCollection Class|parameter collection]] object, from which a specific [[Par Class|parameter]] can be found.
<syntaxhighlight lang="python">
n.par.tx
# or
n.par['tx']
</syntaxhighlight>"""]
	builtinPars:Annotated[list or par,"""A list of all [[Par Class|built-in parameters]]."""]
	customParGroups:Annotated[any,"""A list of all [[ParGroup Class|ParGroups]], where a ParGroup is a set of parameters all drawn on the same line of a dialog, sharing the same label."""]
	customPars:Annotated[any,"""A list of all [[Par Class|custom parameters]]."""]
	customPages:Annotated[list,"""A list of all [[Page Class|custom pages]]."""]
	customTuplets:Annotated[list,"""A list of all parameter tuplets, where a tuplet is a set of parameters all drawn on the same line of a dialog, sharing the same label."""]
	replicator:Annotated[any,"""The [[replicatorCOMP Class|replicatorCOMP]] that created this operator, if any."""]
	storage:Annotated[dict,"""[[Storage]] is dictionary associated with this operator. Values stored in this dictionary are persistent, and saved with the operator. The dictionary attribute is read only, but not its contents. Its contents may be manipulated directly with methods such as OP.fetch() or OP.store() described below, or examined with an [[Examine DAT]]."""]
	tags:Annotated[list,"""Get or set a set of user defined strings. [[Tag|Tags]] can be searched using OP.findChildren() and the [[OP Find DAT]].
The set is a regular python set, and can be accessed accordingly:
<syntaxhighlight lang="python">
n.tags = ['effect', 'image filter']
n.tags.add('darken')
</syntaxhighlight>"""]
	children:Annotated[list,"""A list of [[OP Class|operators]] contained within this operator. Only [[COMP Class|component]] operators have children, otherwise an empty list is returned."""]
	numChildren:Annotated[int,"""Returns the number of children contained within the operator. Only [[COMP Class|component]] operators have children."""]
	numChildrenRecursive:Annotated[int,"""Returns the number of operators contained recursively within this operator. Only [[COMP Class|component]] operators have children."""]
	op:Annotated[any,"""The operator finder object, for accessing operators through paths or shortcuts. '''Note:''' a version of this method that searches relative to '/' is also in the global [[td Module|td module]].

<code>'''op(pattern1, pattern2..., includeUtility=False)'''</code> &rarr; <code class="return">[[OP Class|OP]] or None</code>
<blockquote>
Returns the first OP whose path matches the given pattern, relative to the inside of this operator. Will return None if nothing is found. Multiple patterns may be specified which are all added to the search. Numeric OP ids may also be used.
* <code>pattern</code> - Can be string following the [[Pattern Matching]] rules, specifying which OP to return, or an integer, which must be an OP Id. Multiple patterns can be given, the first matching OP will be returned.
* <code>includeUtility</code> '''(Optional)''' - if True, allow [[Network_Utilities:_Comments,_Network_Boxes,_Annotates|Utility nodes]] to be returned. If False, Utility operators will be ignored.

<syntaxhighlight lang="python">
b = op('project1')
b = op('foot*', 'hand*') #comma separated
b = op('foot* hand*')  #space separated
b = op(154)
</syntaxhighlight>
</blockquote>
<code>'''op.shortcut'''</code> &rarr; <code>OP</code>
<blockquote>
:An operator specified with by a [[Global OP Shortcut]]. If no operator exists an exception is raised. These shortcuts are global, and must be unique. That is, cutting and pasting an operator with a Global OP Shortcut specified will lead to a name conflict. One shortcut must be renamed in that case. Furthermore, only components can be given Global OP Shortcuts.
:*<code>shortcut</code> - Corresponds to the Global OP Shortcut parameter specified in the target operator.
<syntaxhighlight lang="python">
b = op.Videoplayer
</syntaxhighlight>
To list all Global OP Shortcuts:
<syntaxhighlight lang="python">
for x in op:
        print(x)
</syntaxhighlight>
</blockquote>"""]
	parent:Annotated[OP,"""The [[Parent Shortcut|Parent Shortcut]] object, for accessing parent components through indices or shortcuts.
'''Note:''' ''a version of this method that searches relative to the current operator is also in the global [[td Module|td module]].''

<code class="python">parent(n)</code> &rarr; <code class="return">OP or None</code>
<blockquote>
The nth parent of this operator. If n not specified, returns the parent. If n = 2, returns the parent of the parent, etc. If no parent exists at that level, None is returned.
*n - (Optional) n is the number of levels up to climb. When n = 1 it will return the operator's parent.
<syntaxhighlight lang="python">
p = parent(2) #grandfather
</syntaxhighlight>
</blockquote>
<code class="python">parent.shortcut</code> &rarr; <code class="return">OP</code>
<blockquote>
A parent component specified with a shortcut. If no parent exists an exception is raised.
*shortcut - Corresponds to the [[Parent Shortcut]] parameter specified in the target parent.
<syntaxhighlight lang="python">
n = parent.Videoplayer
</syntaxhighlight>
See also Parent Shortcut for more examples.</blockquote>"""]
	iop:Annotated[OP,"""The Internal Operator Shortcut object, for accessing internal shortcuts. See also [[Internal Operators]].

'''Note:''' a version of this method that searches relative to the current operator is also in the global [[td Module]]."""]
	ipar:Annotated[OP,"""The Internal Operator Parameter Shortcut object, for accessing internal shortcuts.  See also [[Internal Parameters]].

'''Note:''' a version of this method that searches relative to the current operator is also in the global [[td Module]]."""]
	currentPage:Annotated[any,"""Get or set the currently displayed parameter page. It can be set by setting it to another page or a string label.
<syntaxhighlight lang="python">n.currentPage = 'Common'</syntaxhighlight>"""]
	activeViewer:Annotated[bool,"""Get or set [[Viewer Active Flag]]."""]
	allowCooking:Annotated[bool,"""Get or set [[Cooking Flag]]. Only COMPs can disable this flag."""]
	bypass:Annotated[bool,"""Get or set [[Bypass Flag]]."""]
	cloneImmune:Annotated[bool,"""Get or set [[Immune Flag|Clone Immune Flag]]."""]
	current:Annotated[bool,"""Get or set [[Current Flag]]."""]
	display:Annotated[bool,"""Get or set [[Display Flag]]."""]
	expose:Annotated[bool,"""Get or set the [[Expose Flag]] which hides a node from view in a network."""]
	lock:Annotated[bool,"""Get or set [[Lock Flag]]."""]
	selected:Annotated[bool,"""Get or set [[Selected Flag]]. This controls if the node is part of the network selection. (yellow box around it)."""]
	python:Annotated[bool,"""Get or set parameter expression language as python."""]
	render:Annotated[bool,"""Get or set [[Render Flag]]."""]
	showCustomOnly:Annotated[bool,"""Get or set the Show Custom Only Flag which controls whether or not non custom parameters are display in[[Parameter Dialog | parameter dialogs]]."""]
	showDocked:Annotated[bool,"""Get or set [[Docking|Show Docked Flag]]. This controls whether this node is visible or hidden when it is docked to another node."""]
	viewer:Annotated[bool,"""Get or set [[Viewer Flag]]."""]
	color:Annotated[any,"""Get or set color value, expressed as a 3-tuple, representing its red, green, blue values. To convert between color spaces, use the built in colorsys module."""]
	comment:Annotated[str,"""Get or set comment string."""]
	nodeHeight:Annotated[int,"""Get or set node height, expressed in [[NetworkEditor Class|network editor]] units."""]
	nodeWidth:Annotated[int,"""Get or set node width, expressed in [[NetworkEditor Class|network editor]] units."""]
	nodeX:Annotated[int,"""Get or set node X value, expressed in [[NetworkEditor Class|network editor]] units, measured from its left edge."""]
	nodeY:Annotated[int,"""Get or set node Y value, expressed in [[NetworkEditor Class|network editor]] units, measured from its bottom edge."""]
	nodeCenterX:Annotated[int,"""Get or set node X value, expressed in [[NetworkEditor Class|network editor]] units, measured from its center."""]
	nodeCenterY:Annotated[int,"""Get or set node Y value, expressed in [[NetworkEditor Class|network editor]] units, measured from its center."""]
	dock:Annotated[OP,"""Get or set the [[OP Class|operator]] this operator is docked to.  To clear docking, set this member to None."""]
	docked:Annotated[list,"""The (possibly empty) list of [[OP Class|operators]] docked to this node."""]
	inputs:Annotated[list,"""List of input [[OP Class|operators]] (via left side connectors) to this operator. To get the number of inputs, use len(OP.inputs)."""]
	outputs:Annotated[list,"""List of output [[OP Class|operators]] (via right side connectors) from this operator."""]
	inputConnectors:Annotated[list,"""List of input [[Connector Class|connectors]] (on the left side) associated with this operator."""]
	outputConnectors:Annotated[list,"""List of output [[Connector Class|connectors]] (on the right side) associated with this operator."""]
	cookFrame:Annotated[float,"""Last frame at which this operator cooked."""]
	cookTime:Annotated[float,"""'''Deprecated''' Duration of the last measured cook (in milliseconds)."""]
	cpuCookTime:Annotated[float,"""Duration of the last measured cook in CPU time (in milliseconds)."""]
	cookAbsFrame:Annotated[float,"""Last absolute frame at which this operator cooked."""]
	cookStartTime:Annotated[float,"""Last offset from frame start at which this operator cook began, expressed in milliseconds."""]
	cookEndTime:Annotated[float,"""Last offset from frame start at which this operator cook ended, expressed in milliseconds.  Other operators may have cooked between the start and end time.  See the cookTime member for this operator's specific cook duration."""]
	cookedThisFrame:Annotated[bool,"""True when this operator has cooked this frame."""]
	cookedPreviousFrame:Annotated[bool,"""True when this operator has cooked the previous frame."""]
	childrenCookTime:Annotated[float,"""'''Deprecated''' The total accumulated cook time of all children of this operator during the last frame. Zero if the operator is not a [[COMP Class|COMP]] and/or has no children."""]
	childrenCPUCookTime:Annotated[float,"""The total accumulated cook time of all children of this operator during the last frame. Zero if the operator is not a [[COMP Class|COMP]] and/or has no children."""]
	childrenCookAbsFrame:Annotated[float,"""'''Deprecated''' The absolute frame on which childrenCookTime is based."""]
	childrenCPUCookAbsFrame:Annotated[float,"""The absolute frame on which childrenCPUCookTime is based."""]
	gpuCookTime:Annotated[float,"""Duration of GPU operations during the last measured cook (in milliseconds)."""]
	childrenGPUCookTime:Annotated[float,"""The total accumulated GPU cook time of all children of this operator during the last frame. Zero if the operator is not a COMP and/or has no children."""]
	childrenGPUCookAbsFrame:Annotated[float,"""The absolute frame on which childrenGPUCookTime is based."""]
	totalCooks:Annotated[int,"""Number of times the operator has cooked."""]
	cpuMemory:Annotated[int,"""The approximate amount of CPU memory this Operator is using, in bytes."""]
	gpuMemory:Annotated[int,"""The amount of GPU memory this OP is using, in bytes."""]
	type:Annotated[str,"""Operator type as a string. Example: 'oscin'."""]
	subType:Annotated[str,"""Operator subtype. Currently only implemented for [[Component|components]]. May be one of: 'panel', 'object', or empty string in the case of base components."""]
	OPType:Annotated[str,"""Python operator class type, as a string. Example: 'oscinCHOP'. Can be used with COMP.create() method."""]
	label:Annotated[str,"""Operator type label. Example: 'OSC In'."""]
	icon:Annotated[str,"""Get the letters used to create the operator's icon."""]
	family:Annotated[str,"""Operator family. Example: CHOP. Use the global dictionary families for a list of each operator type."""]
	isFilter:Annotated[bool,"""True if operator is a filter, false if it is a generator."""]
	minInputs:Annotated[int,"""Minimum number of inputs to the operator."""]
	maxInputs:Annotated[int,"""Maximum number of inputs to the operator."""]
	isMultiInputs:Annotated[bool,"""True if inputs are ordered, false otherwise. Operators with an arbitrary number of inputs have unordered inputs, example [[Merge CHOP]]."""]
	visibleLevel:Annotated[int,"""Visibility level of the operator. For example, expert operators have visibility level 1, regular operators have visibility level 0."""]
	isBase:Annotated[bool,"""True if the operator is a Base (miscellaneous) [[Component|component]]."""]
	isCHOP:Annotated[bool,"""True if the operator is a [[CHOP]]."""]
	isCOMP:Annotated[bool,"""True if the operator is a [[Component|component]]."""]
	isDAT:Annotated[bool,"""True if the operator is a [[DAT]]."""]
	isMAT:Annotated[bool,"""True if the operator is a [[MAT|Material]]."""]
	isObject:Annotated[bool,"""True if the operator is an [[object]]."""]
	isPanel:Annotated[bool,"""True if the operator is a [[Panel]]."""]
	isSOP:Annotated[bool,"""True if the operator is a [[SOP]]."""]
	isTOP:Annotated[bool,"""True if the operators is a [[TOP]]."""]
	licenseType:Annotated[str,"""Type of [[License Class|License]] required for the operator."""]
	pass


class TOP(OP):
	width:Annotated[int,"""Texture width, measured in pixels."""]
	height:Annotated[int,"""Texture height, measured in pixels."""]
	aspect:Annotated[float,"""Texture aspect ratio, width divided by height."""]
	aspectWidth:Annotated[float,"""Texture aspect ratio, width."""]
	aspectHeight:Annotated[float,"""Texture aspect ratio, height."""]
	depth:Annotated[int,"""Texture depth, when using a 3 dimensional texture."""]
	gpuMemory:Annotated[int,"""The amount of GPU memory this TOP is using, in bytes."""]
	curPass:Annotated[int,"""The current cooking pass iteration, beginning at 0. The total can be set with the 'Passes' parameter on the operator's common page."""]
	isTOP:Annotated[bool,"""True if the operators is a TOP."""]
	pass


class zedTOP(TOP,OP):
	pass


class webrenderTOP(TOP,OP):
	loaded:Annotated[bool,"""The loaded state of the current webpage."""]
	pass


class viosoTOP(TOP,OP):
	pass


class videostreamoutTOP(TOP,OP):
	streamURL:Annotated[str,"""The URL to connect to this operator's stream."""]
	pass


class videostreaminTOP(TOP,OP):
	connectionsFailed:Annotated[int,"""The number of times this operator has failed to make a connection to any URL."""]
	connectionsLost:Annotated[int,"""The number of times this operator has lost a connection it has previous successfully established."""]
	frameTime:Annotated[float,"""The timestamp of the currently shown frame, in seconds."""]
	isConnected:Annotated[bool,"""True if connected to target URL."""]
	isConnecting:Annotated[bool,"""True if attempting to connect to target URL."""]
	isOddField:Annotated[bool,"""When de-interlacing, this tells if the odd field is currently being shown."""]
	videoHeight:Annotated[int,"""Height of the movie, in pixels."""]
	videoWidth:Annotated[int,"""Width of the movie, in pixels."""]
	pass


class videodeviceoutTOP(TOP,OP):
	pass


class videodeviceinTOP(TOP,OP):
	isConnected:Annotated[bool,"""True if any device is currently streaming to this operator.."""]
	inputSignalFormat:Annotated[any,"""If available for the current Library, returns a string for the input signal format. This string can be used to set the 'Signal Format' menu on the Video Device Out TOP."""]
	timecode:Annotated[any,"""If the device supports timecode, then returns a Timecode object for the latest received frame. see [[Timecode Class]]."""]
	pass


class underTOP(TOP,OP):
	pass


class transformTOP(TOP,OP):
	pass


class touchoutTOP(TOP,OP):
	pass


class touchinTOP(TOP,OP):
	pass


class timemachineTOP(TOP,OP):
	pass


class tileTOP(TOP,OP):
	pass


class thresholdTOP(TOP,OP):
	pass


class texture3dTOP(TOP,OP):
	pass


class textTOP(TOP,OP):
	curText:Annotated[str,"""Current text contents, when used with a [[Field COMP]]."""]
	cursorEnd:Annotated[int,"""Get or set cursor end position, when used with a [[Field COMP]]."""]
	cursorStart:Annotated[int,"""Get or set cursor start position, when used with a [[Field COMP]]."""]
	fontDescender:Annotated[int,"""The descender of the current font, in pixels. This is the distance from the baseline to the bottom of lowest hanging character in the font. This value does not change based on the currently displayed text."""]
	selectedText:Annotated[str,"""Selected contents, when used with a [[Field COMP]]."""]
	textHeight:Annotated[int,"""Calculated height of text, in pixels. This value does '''not''' changes based on the particular of characters in the string. It only depends on the number of lines, line spacing, positioning and font metrics of the font."""]
	textWidth:Annotated[int,"""Calculated width of text, in pixels. This value '''does''' change depending on the particular characters in the string. Different characters have difference advance widths, and this value is the sum of all the advance widths of the characters."""]
	numLines:Annotated[int,"""Get the number of lines of the outputted text, after operations such as word-wrap have been applied."""]
	ascender:Annotated[float,"""The ascender of the font, as described by the font's metrics."""]
	descender:Annotated[float,"""The descender of the font, as described by the font's metrics."""]
	capHeight:Annotated[float,"""The cap height of the font, as described by the font's metrics. This is usually the height of a capital H."""]
	xHeight:Annotated[float,"""The x height of the font, as described by the font's metrics. This is usually the height of a lower case x."""]
	lineGap:Annotated[float,"""The suggested gap between lines, as described by the font's metrics."""]
	pass


class syphonspoutoutTOP(TOP,OP):
	pass


class syphonspoutinTOP(TOP,OP):
	pass


class switchTOP(TOP,OP):
	pass


class svgTOP(TOP,OP):
	pass


class subtractTOP(TOP,OP):
	pass


class substanceTOP(TOP,OP):
	pass


class substanceselectTOP(TOP,OP):
	pass


class ssaoTOP(TOP,OP):
	pass


class SOP(OP):
	compare:Annotated[bool,"""Get or set [[Compare Flag]]."""]
	template:Annotated[bool,"""Get or set [[Template Flag]]."""]
	points:Annotated[any,"""The set of [[Points Class|points]] contained in this SOP."""]
	prims:Annotated[any,"""The set of [[Prims Class|primitives]] contained in this SOP."""]
	numPoints:Annotated[int,"""The number of [[Points Class|points]] contained in this SOP."""]
	numVertices:Annotated[int,"""The number of [[Vertex Class|vertices]] contained in all primitives within this SOP."""]
	numPrims:Annotated[int,"""The number of [[Prims Class|primitivies]] contained in this SOP."""]
	pointAttribs:Annotated[any,"""The set of point [[Attributes Class|attributes]] defined in this SOP."""]
	primAttribs:Annotated[any,"""The set of primitive [[Attributes Class|attributes]] defined in this SOP."""]
	vertexAttribs:Annotated[any,"""The set of vertex [[Attributes Class|attributes]] defined in this SOP."""]
	pointGroups:Annotated[dict,"""Returns a dictionary of point [[Group Class|groups]] defined for this SOP."""]
	primGroups:Annotated[dict,"""Returns a dictionary of primitive [[Group Class|groups]] defined for this SOP."""]
	center:Annotated[any,"""Get or set the barycentric coordinate of this operator's geometry. It is expressed as a [[Position Class|Position]]."""]
	min:Annotated[any,"""The minimum coordinates of this operator's geometry along each dimension, expressed as a [[Position Class|Position]]."""]
	max:Annotated[any,"""The maximum coordinates of this operator's geometry along each dimension, expressed as [[Position Class|Position]]."""]
	size:Annotated[any,"""The size of this operator's geometry along each dimension, expressed as a [[Position Class|Position]]."""]
	isSOP:Annotated[bool,"""True if the operator is a SOP."""]
	pass


class zedSOP(OP,SOP):
	pass


class wireframeSOP(OP,SOP):
	pass


class vertexSOP(OP,SOP):
	inputColor:Annotated[any,"""The current point or vertex color being evaluated, from the first input, or a default if not present, expressed as a 4-tuple."""]
	inputColor2:Annotated[any,"""The current point or vertex color being evaluated, from the second input, or a default if not present, expressed as a 4-tuple."""]
	inputNormal:Annotated[any,"""The current point or vertex normal being evaluated, from the first input, or a default if not present, expressed as a 3-tuple."""]
	inputNormal2:Annotated[any,"""The current point or vertex normal being evaluated, from the second input, or a default if not present, expressed as a 3-tuple."""]
	inputTexture:Annotated[any,"""The current point or vertex texture being evaluated, from the first input, or a default if not present, expressed as a 3-tuple."""]
	inputTexture2:Annotated[any,"""The current point or vertex texture being evaluated, from the second input, or a default if not present, expressed as a 3-tuple."""]
	inputVertex:Annotated[Vertex,"""The current [[Vertex Class|vertex]] being evaluated, from the first input."""]
	inputVertex2:Annotated[Vertex,"""The current [[Vertex Class|vertex]] being evaluated, from the second input."""]
	pass


class twistSOP(OP,SOP):
	pass


class tubeSOP(OP,SOP):
	pass


class tristripSOP(OP,SOP):
	pass


class trimSOP(OP,SOP):
	pass


class transformSOP(OP,SOP):
	pass


class trailSOP(OP,SOP):
	pass


class traceSOP(OP,SOP):
	pass


class torusSOP(OP,SOP):
	pass


class textureSOP(OP,SOP):
	pass


class textSOP(OP,SOP):
	numLines:Annotated[int,"""Get the number of lines of the outputted text, after operations such as word-wrap have been applied."""]
	ascender:Annotated[float,"""The ascender of the font, as described by the font's metrics."""]
	descender:Annotated[float,"""The descender of the font, as described by the font's metrics."""]
	capHeight:Annotated[float,"""The cap height of the font, as described by the font's metrics. This is usually the height of a capital H."""]
	xHeight:Annotated[float,"""The x height of the font, as described by the font's metrics. This is usually the height of a lower case x."""]
	lineGap:Annotated[float,"""The suggested gap between lines, as described by the font's metrics."""]
	numGlyphs:Annotated[int,"""The number of glyphs that were generated. Note that this isn't nessesarily the number of characters (code points) in the original string."""]
	pass


class switchSOP(OP,SOP):
	pass


class sweepSOP(OP,SOP):
	inputVertex:Annotated[Vertex,"""The current [[Vertex Class|vertex]] being evaluated, along the backbone input."""]
	pass


class surfsectSOP(OP,SOP):
	pass


class superquadSOP(OP,SOP):
	pass


class subdivideSOP(OP,SOP):
	pass


class stitchSOP(OP,SOP):
	pass


class spriteSOP(OP,SOP):
	pass


class springSOP(OP,SOP):
	pass


class sphereSOP(OP,SOP):
	pass


class sortSOP(OP,SOP):
	pass


class slopeTOP(TOP,OP):
	pass


class skinSOP(OP,SOP):
	pass


class sharedmemoutTOP(TOP,OP):
	pass


class sharedmeminTOP(TOP,OP):
	pass


class sequenceblendSOP(OP,SOP):
	pass


class selectTOP(TOP,OP):
	pass


class selectSOP(OP,SOP):
	pass


class scriptSOP(OP,SOP):
	pass


class screenTOP(TOP,OP):
	pass


class screengrabTOP(TOP,OP):
	pass


class scalabledisplayTOP(TOP,OP):
	cameraTransform:Annotated[any,"""Gets the loaded camera transform [[Matrix Class|matrix]] for the configuration. This should be referenced in the 'Xform Matrix/CHOP/DAT' parameter of the [[Camera COMP]]."""]
	projection:Annotated[any,"""Gets the loaded projection [[Matrix Class|matrix]] for the configuration. This should be referenced in the 'Proj Matrix/CHOP/DAT' parameter of the [[Camera COMP]], with the 'Projection' set to 'Custom Projection Matrix'."""]
	pass


class rgbtohsvTOP(TOP,OP):
	pass


class rgbkeyTOP(TOP,OP):
	pass


class revolveSOP(OP,SOP):
	pass


class resolutionTOP(TOP,OP):
	pass


class resampleSOP(OP,SOP):
	pass


class reorderTOP(TOP,OP):
	pass


class renderTOP(TOP,OP):
	pass


class renderselectTOP(TOP,OP):
	pass


class renderpassTOP(TOP,OP):
	pass


class remapTOP(TOP,OP):
	pass


class refineSOP(OP,SOP):
	pass


class rectangleTOP(TOP,OP):
	pass


class rectangleSOP(OP,SOP):
	pass


class realsenseTOP(TOP,OP):
	pass


class raySOP(OP,SOP):
	pass


class rampTOP(TOP,OP):
	pass


class railsSOP(OP,SOP):
	pass


class projectSOP(OP,SOP):
	pass


class projectionTOP(TOP,OP):
	pass


class profileSOP(OP,SOP):
	pass


class primitiveSOP(OP,SOP):
	inputColor:Annotated[any,"""The current primitive color being evaluated or a default if not present, expressed as a 4-tuple."""]
	inputPrim:Annotated[Prim,"""The current [[Prim Class|primitive]] being evaluated."""]
	pass


class prefiltermapTOP(TOP,OP):
	pass


class polystitchSOP(OP,SOP):
	pass


class polysplineSOP(OP,SOP):
	pass


class polyreduceSOP(OP,SOP):
	pass


class polypatchSOP(OP,SOP):
	pass


class polyloftSOP(OP,SOP):
	pass


class pointSOP(OP,SOP):
	inputColor:Annotated[any,"""The current point color being evaluated, from the first input, or a default if not present, expressed as a 4-tuple."""]
	inputColor2:Annotated[any,"""The current point color being evaluated, from the second input, or a default if not present, expressed as a 4-tuple."""]
	inputNormal:Annotated[any,"""The current point normal being evaluated, from the first input, or a default if not present, expressed as a 3-tuple."""]
	inputNormal2:Annotated[any,"""The current point normal being evaluated, from the second input, or a default if not present, expressed as a 3-tuple."""]
	inputPoint:Annotated[Point,"""The current [[Point Class|point]] being evaluated, from the first input."""]
	inputPoint2:Annotated[Point,"""The current [[Point Class|point]] being evaluated, from the second input."""]
	inputTexture:Annotated[any,"""The current point texture being evaluated, from the first input, or a default if not present, expressed as a 3-tuple."""]
	inputTexture2:Annotated[any,"""The current point texture being evaluated, from the second input, or a default if not present, expressed as a 3-tuple."""]
	pass


class photoshopinTOP(TOP,OP):
	isConnected:Annotated[bool,"""Is true if the operator is connected to a running instance of Photoshop."""]
	isReceivingUpdates:Annotated[bool,"""Is true if the operator is receiving image update. It will get updates when it's not locked to a particular document, or if it is locked and the document is opened in that Photoshop instance."""]
	pass


class particleSOP(OP,SOP):
	pass


class packTOP(TOP,OP):
	pass


class overTOP(TOP,OP):
	pass


class outTOP(TOP,OP):
	pass


class outSOP(OP,SOP):
	pass


class outsideTOP(TOP,OP):
	pass


class opviewerTOP(TOP,OP):
	pass


class openvrTOP(TOP,OP):
	pass


class openvrSOP(OP,SOP):
	pass


class opencolorioTOP(TOP,OP):
	pass


class Monitors():
	primary:Annotated[int,"""The primary [[Monitor Class|monitor]] display."""]
	width:Annotated[int,"""The width of the combined monitor area, measured in pixels."""]
	height:Annotated[int,"""The height of the combined monitor area, measured in pixels."""]
	left:Annotated[int,"""The leftmost edge of the combined monitor area, measured in pixels."""]
	right:Annotated[int,"""The rightmost edge of the combined monitor area, measured in pixels."""]
	top:Annotated[int,"""The topmost position of the combined monitor area, measured in pixels."""]
	bottom:Annotated[int,"""The bottommost position of the combined monitor area, measured in pixels."""]
	pass


class Monitor():
	index:Annotated[int,"""The monitor position in the list."""]
	isPrimary:Annotated[bool,"""Returns true, if this monitor is the primary display."""]
	isAffinity:Annotated[bool,"""Returns true, if this monitor is connected to the GPU that has been selected for GPU Affinity. Always True if GPU Affinity is not used."""]
	width:Annotated[int,"""The width of the monitor area, measured in pixels."""]
	height:Annotated[int,"""The height of the monitor area, measured in pixels."""]
	left:Annotated[int,"""The position of left edge of the monitor area, measured in pixels."""]
	right:Annotated[int,"""The position of right edge of the monitor area, measured in pixels."""]
	top:Annotated[int,"""The position of top edge of the monitor area, measured in pixels."""]
	bottom:Annotated[int,"""The position of bottom edge of the monitor area, measured in pixels."""]
	displayName:Annotated[str,"""The unique display name associated with this monitor."""]
	description:Annotated[str,"""A description of the monitor or its display adapter."""]
	dpiScale:Annotated[float,"""The DPI Scaling factor the monitor is current set to."""]
	scaledWidth:Annotated[int,"""The width of the monitor area, measured in points."""]
	scaledHeight:Annotated[int,"""The height of the monitor area, measured in points."""]
	scaledLeft:Annotated[int,"""The position of left edge of the monitor area, measured in points."""]
	scaledRight:Annotated[int,"""The position of right edge of the monitor area, measured in points."""]
	scaledTop:Annotated[int,"""The position of top edge of the monitor area, measured in points."""]
	scaledBottom:Annotated[int,"""The position of bottom edge of the monitor area, measured in points."""]
	serialNumber:Annotated[str,"""The serial number name associated with this monitor. May be blank."""]
	refreshRate:Annotated[float,"""The refresh rate the monitor is currently running at."""]
	pass


class MOD():
	pass


class Matrix():
	vals:Annotated[float,"""Get or set the set of Matrix values."""]
	rows:Annotated[any,"""The list of Matrix rows, each a list of values."""]
	cols:Annotated[any,"""The list of Matrix columns, each a list of values."""]
	pass


class ListAttributes():
	pass


class ListAttribute():
	bgColor:Annotated[any,"""Get or set background color."""]
	bottomBorderInColor:Annotated[any,"""Get or set inside bottom color."""]
	bottomBorderOutColor:Annotated[any,"""Get or set outside bottom color."""]
	colStretch:Annotated[bool,"""Get or set column stretchiness. When True, colWidth specifies minimum width."""]
	colWidth:Annotated[float,"""Get or set column width, expressed in pixels."""]
	draggable:Annotated[bool,"""Get or set whether or not cell is draggable."""]
	editable:Annotated[bool,"""Get or set whether or not contents are editable. When True, contents can be edited by clicking on the cell."""]
	focus:Annotated[bool,"""Returns True if the cell/row/column/table is currently being edited."""]
	fontFile:Annotated[any,"""Get or set font file. VFS embedded files supported as well."""]
	fontBold:Annotated[bool,"""Get or set whether or not text is rendered in bold font."""]
	fontFace:Annotated[str,"""Get or set font face. Example 'verdana'."""]
	fontItalic:Annotated[bool,"""Get or set whether or not text is rendered italicized."""]
	fontSizeX:Annotated[float,"""Get or set font horizontal size."""]
	fontSizeY:Annotated[float,"""Get or set font vertical size. If not specified, uses fontSizeX."""]
	sizeInPoints:Annotated[bool,"""Get or set text size units. When True size is in points, when False it is in pixels."""]
	help:Annotated[str,"""Get or set help string when rolling over the cell."""]
	leftBorderInColor:Annotated[any,"""Get or set inside left color."""]
	leftBorderOutColor:Annotated[any,"""Get or set outside left color."""]
	radio:Annotated[bool,"""Returns true if the mouse last selected the cell/row/column/table."""]
	rightBorderInColor:Annotated[any,"""Get or set inside right color."""]
	rightBorderOutColor:Annotated[any,"""Get or set outside right color."""]
	rollover:Annotated[bool,"""Returns true if the mouse is currently over the cell/row/column/table."""]
	rowHeight:Annotated[float,"""Get or set row height, expressed in pixels."""]
	rowIndent:Annotated[float,"""Get or set row indent, expressed in pixels."""]
	rowStretch:Annotated[bool,"""Get or set row stretchiness. When True, rowWidth specifies minimum width."""]
	select:Annotated[bool,"""Returns true if the mouse is currently pressed over the cell/row/column/table."""]
	text:Annotated[str,"""Get or set contents."""]
	textColor:Annotated[any,"""Get or set text color.  Color values must be a tuple with four numeric entries corrresponding to red, green, blue, alpha ie:  (0.3, 06, 0.1, 1.0)"""]
	textJustify:Annotated[any,"""Get or set text justification. Value is one of: JustifyType.TOPLEFT, JustifyType.TOPCENTER, JustifyType.TOPRIGHT, JustifyType.CENTERLEFT, JustifyType.CENTER, JustifyType.CENTERRIGHT, JustifyType.BOTTOMLEFT, JustifyType.BOTTOMCENTER, JustifyType.BOTTOMRIGHT"""]
	textOffsetX:Annotated[float,"""Get or set horizontal text offset."""]
	textOffsetY:Annotated[float,"""Get or set vertical text offset."""]
	top:Annotated[any,"""Get or set background image [[TOP Class|TOP]]."""]
	topBorderInColor:Annotated[any,"""Get or set inside top color."""]
	topBorderOutColor:Annotated[any,"""Get or set outside top color."""]
	wordWrap:Annotated[bool,"""Get or set word wrapping."""]
	pass


class Licenses():
	disablePro:Annotated[bool,"""When True, the application will run as though no Pro licenses are available.  This can be used to test compatibility with lesser licenses. (See also: [[App Class#Methods|app.addNonCommercialLimit]])"""]
	dongles:Annotated[list,"""Get the list of dongles connected to the system."""]
	machine:Annotated[str,"""The computer machine name."""]
	systemCode:Annotated[str,"""The unique computer system code."""]
	isPro:Annotated[bool,"""When True, the application is running with a Pro license. It is recommended to use this and isNonCommerical over the type method."""]
	isNonCommercial:Annotated[bool,"""When True, the application is running with a Non-Commercial license. It is recommended to use this and isPro over the type method."""]
	type:Annotated[str,"""The highest ranking license type of all installed licenses, some products being 'Pro', 'Non-Commercial', 'Commercial'. See also app.product in [[App Class]]."""]
	pass


class License():
	index:Annotated[int,"""The license index in the list."""]
	isEnabled:Annotated[bool,"""True if the license is locally enabled (That is, it has never been disabled)."""]
	isRemotelyDisabled:Annotated[bool,"""True if the license has been remotely disabled."""]
	key:Annotated[str,"""The key sequence."""]
	remoteDisableDate:Annotated[any,"""The date the license was remotely disabled, expressed as a tuple (year, month, day)."""]
	status:Annotated[int,"""The numeric status code. Negative values indicate the license is not applicable to the current application. A value of zero indicates it does."""]
	statusMessage:Annotated[str,"""A description of the status code."""]
	systemCode:Annotated[str,"""The system code associated with this license."""]
	type:Annotated[str,"""The license type, e.g. some products being 'Pro', 'Non-Commercial', 'Commercial'. See also app.product in [[App Class]]"""]
	updateExpiryDate:Annotated[any,"""The date updates for this license expires, expressed as a tuple (year, month, day)."""]
	version:Annotated[int,"""The numeric license version."""]
	pass


class InputPoint():
	color:Annotated[Color,"""The color for this point. This is different from the Cd attribute, since it can come from a Vertex if there is no color on the inputPoint itself."""]
	normP:Annotated[Position,"""The normalized position of this point within the bounding box of the SOP. Will always be in the range [0,1]. Expressed as tdu.Position object."""]
	normal:Annotated[Vector,"""The normal for this point. This is different from the N attribute, since it can come from a Vertex or from the destination point, if there is no normal on the inputPoint itself."""]
	sopCenter:Annotated[Position,"""Get the barycentric coordinate of the geometry the inputPoint is a part of. This is faster than other methods to get the center of a SOP's geometry due to internal optimizations. It is expressed as a tdu.Position."""]
	pass


class Group():
	default:Annotated[tuple,"""The default values associated with this Group. It returns a tuple item of group points."""]
	name:Annotated[str,"""Set/gets the group name."""]
	owner:Annotated[OP,"""Gets the owner of this group."""]
	pass


class FileInfo():
	pass


class DongleList():
	pass


class Dongle():
	serialNumber:Annotated[str,"""Dongle Serial Number."""]
	pass


class Dependency():
	val:Annotated[any,"""The value associated with this object. Referencing this value in an expression will cause the operator to become dependent on its value. Setting this value will cause those operators to be recooked as necessary."""]
	peekVal:Annotated[any,"""This returns the same value as .val but does not create a dependency on the value."""]
	callbacks:Annotated[list,"""A modifiable list of functions. When the Dependency object is modified, it calls each function on the list. Each function is called with a single argument which is a dictionary containing the following:
* 'dependency'- The Dependency that was modified.
* 'prevVal' - The previous value if available.
* 'callback' - This callback function."""]
	ops:Annotated[list,"""A list of [[OP Class|operators]] currently dependent on the object."""]
	listAttributes:Annotated[list,"""A list of [[ListAttribute Class|list attributes]] currently dependent on the object."""]
	pass


class debug():
	style:Annotated[any,"""A namespace containing information about how to process <code>debug</code> statements. This data is not meant to be changed directly. Instead, use the setStyle function below."""]
	pass


class CUDAMemoryShape():
	width:Annotated[int,"""Get/Set the width in pixels of the memory."""]
	height:Annotated[int,"""Get/Set the height in pixels of the memory."""]
	numComps:Annotated[int,"""Get/Set the number of color components per pixel of the memory."""]
	dataType:Annotated[any,"""Get/Set the data type of each color component, as a numpy data type. E.g numpy.uint8, numpy.float32. Note that for uint8 data types, the channel ordering will be BGRA for 4 component textures. It will be RGBA however for other data types."""]
	pass


class CUDAMemory():
	ptr:Annotated[any,"""Returns the raw memory pointer address for the CUDA memory."""]
	size:Annotated[int,"""Returns the size of the CUDA Memory, in bytes."""]
	shape:Annotated[CUDAMemoryShape,"""Returns the [[CUDAMemoryShape Class]] describing this CUDA memory. See the help for that class for notes about channel order for different data types."""]
	pass


class Connector():
	index:Annotated[int,"""The numeric index of this connector."""]
	isInput:Annotated[bool,"""True when the connector is an input."""]
	isOutput:Annotated[bool,"""True when the connector is an output."""]
	inOP:Annotated[OP,"""Will return any input operators (e.g. [[inSOP Class|inSOP]], [[inCHOP Class|inCHOP]]) associated with this connector.  This only applies to regular operator connections attached to components."""]
	outOP:Annotated[OP,"""Will return any output operators (e.g. [[outSOP Class|outSOP]], [[outCHOP Class|outCHOP]]) associated with this connector.  This only applies to regular operator connections attached to components."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	connections:Annotated[list,"""The list of [[Connector Class|connector objects]] connected to this object."""]
	description:Annotated[str,"""A description for this connection. Example: 'Color Image'."""]
	pass


class Colors():
	pass


class Color():
	r:Annotated[float,"""Gets or sets the red component of the color."""]
	g:Annotated[float,"""Gets or sets the green component of the color."""]
	b:Annotated[float,"""Gets or sets the blue component of the color."""]
	a:Annotated[float,"""Gets or sets the alpha component of the color."""]
	pass


class Channel():
	valid:Annotated[bool,"""True if the referenced chanel value currently exists, False if it has been deleted."""]
	index:Annotated[int,"""The numeric index of the channel."""]
	name:Annotated[str,"""The name of the channel."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	exports:Annotated[list,"""The (possibly empty) list of [[Par Class|parameters]] this channel currently exports to."""]
	vals:Annotated[list,"""Get or set the full list of [[Channel Class|Channel]] values. Modifying [[Channel Class|Channel]] values can only be done in Python within a [[scriptCHOP Class|Script CHOP]]."""]
	pass


class Cell():
	valid:Annotated[bool,"""True if the referenced cell currently exists, False if it has been deleted."""]
	row:Annotated[int,"""The numeric row of the cell."""]
	col:Annotated[int,"""The numeric column of the cell."""]
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	val:Annotated[any,"""Get or set the cell contents, which are always stored as a string value."""]
	pass


class Camera():
	dir:Annotated[any,"""Get or set the direction of the camera as a vector that points towards the target. Up is considered to be (0,1,0)."""]
	pivot:Annotated[any,"""Get or set the 3D point in space where the camera will pivot around or towards."""]
	position:Annotated[any,"""Get or set the 3D point in space where the camera is located."""]
	pass


class Bounds():
	pass


class Body():
	index:Annotated[int,"""The index of this Body in its [[Actor COMP]] (owner)."""]
	owner:Annotated[OP,"""The [[Actor COMP]] to which this body belongs."""]
	rotate:Annotated[any,"""Get or set the body's rotation in world space."""]
	translate:Annotated[any,"""Get or set the body's translation in world space."""]
	angularVelocity:Annotated[any,"""Get or set the body's angular velocity."""]
	linearVelocity:Annotated[any,"""Get or set the body's linear velocity."""]
	pass


class Bodies():
	pass


class Bezier():
	anchors:Annotated[list,"""Returns the list of anchor [[Vertex Class|vertices]]."""]
	basis:Annotated[list,"""Return the bezier basis as a list of float values."""]
	closed:Annotated[bool,"""Get or set whether the curve is closed or open."""]
	order:Annotated[float,"""Return the bezier order. The order is one more than the degree."""]
	segments:Annotated[list,"""Returns a list of segments, where each segment is a list of [[Vertex Class|vertices]]."""]
	tangents:Annotated[list,"""Returns the tangents as a list of [[Vertex Class|vertex]] pairs."""]
	pass


class NotSet():
	pass


class Attributes():
	owner:Annotated[any,"""The [[OP Class|OP]] to which this object belongs."""]
	pass


class AttributeData():
	owner:Annotated[any,"""The [[OP Class|OP]] to which this object belongs."""]
	val:Annotated[any,"""The set of values contained within this object.  Dependent on the type of attribute, it may return a float, integer, string, tuple, [[Position Class|Position]], or [[Vector Class|Vector]].  For example Normal attribute data is expressed as a [[Vector Class|Vector]], while [[Position Class|Position]] attribute data is expressed as a Position."""]
	pass


class Attribute():
	owner:Annotated[OP,"""The [[OP Class|OP]] to which this object belongs."""]
	name:Annotated[str,"""The name of this attribute."""]
	size:Annotated[int,"""The number of values associated with this attribute. For example, a normal attribute has a size of 3."""]
	type:Annotated[any,"""The type associated with this attribute: float, integer or string."""]
	default:Annotated[any,"""The default values associated with this attribute. Dependent on the type of attribute, it may return a float, integer, string, tuple, [[Position Class|Position]], or [[Vector Class|Vector]]."""]
	pass


class ArcBall():
	pass


class App():
	architecture:Annotated[str,"""The architecture of the compile.  Generally 32 or 64 bit."""]
	binFolder:Annotated[str,"""Installation folder containing the binaries."""]
	build:Annotated[str,"""Application build number."""]
	compileDate:Annotated[any,"""The date the application was compiled, expressed as a tuple (year, month, day)."""]
	configFolder:Annotated[str,"""Installation folder containing configuration files."""]
	desktopFolder:Annotated[str,"""Current user's desktop folder."""]
	enableOptimizedExprs:Annotated[bool,"""Get or set if Python expression optimization is enabled. Defaults to True every time TouchDesigner starts."""]
	experimental:Annotated[bool,"""Returns true if the App is an experimental build, false otherwise."""]
	installFolder:Annotated[str,"""Main installation folder."""]
	launchTime:Annotated[float,"""Total time required to launch and begin playing the toe file, measured in seconds."""]
	logExtensionCompiles:Annotated[bool,"""Get or set if extra messages for starting and ending compiling extensions is sent to the textport. Additional error stack will be printed if compilation fails.  Defaults to False every time TouchDesigner starts."""]
	osName:Annotated[str,"""The operating system name."""]
	osVersion:Annotated[str,"""The operating system version."""]
	power:Annotated[bool,"""Get or set the overall processing state of the process. When True, processing is enabled.  When False processing is halted. This is identical to pressing the power button on the main interface. This has a greater effect than simply pausing or stopping the playbar.
<syntaxhighlight lang=python>
app.power = False #turn off the power button.
</syntaxhighlight>"""]
	preferencesFolder:Annotated[str,"""Folder where the preferences file is located."""]
	product:Annotated[str,"""Type of executable the project is running under. Values are 'TouchDesigner', 'TouchPlayer' or 'TouchEngine'."""]
	recentFiles:Annotated[list,"""Get or set the list of most recently saved or loaded files."""]
	samplesFolder:Annotated[str,"""Installation folder containing configuration files."""]
	paletteFolder:Annotated[str,"""Installation folder containing palette files."""]
	userPaletteFolder:Annotated[str,"""Folder where custom user palettes are located."""]
	version:Annotated[str,"""Application version number."""]
	windowColorBits:Annotated[int,"""The number of color bits per color channel the TouchDesigner window is running at. By default this will be 8-bits per channel, but can be increased to 10-bits by settings env var TOUCH_10_BIT_COLOR=1. Only works on displays that support 10-bit color."""]
	pass


class Actors():
	pass


class AbsTime():
	frame:Annotated[float,"""Absolute total number of frames played since the application started.  Paused only with the power On/Off or with power()
<syntaxhighlight lang=python>
Example: absTime.frame
Example: tdu.rand(absTime.frame + .1) # a unique random number that is consistent across all nodes, changing every frame
</syntaxhighlight>"""]
	seconds:Annotated[float,"""Absolute total seconds played since the application started. Paused only with the power On/Off or with power()."""]
	step:Annotated[float,"""Number of absolute frames elapsed between start of previous and current frame. When this value is greater than 1, the system is dropping frames."""]
	stepSeconds:Annotated[float,"""Absolute time elapsed between start of previous and current frame."""]
	pass


class addSOP(OP,SOP):
	pass


class addTOP(TOP,OP):
	pass


class alembicSOP(OP,SOP):
	pass


class alignSOP(OP,SOP):
	pass


class ambientlightCOMP(OP,ObjectCOMP,COMP):
	pass


class analyzeCHOP(CHOP,OP):
	pass


class analyzeTOP(TOP,OP):
	pass


class angleCHOP(CHOP,OP):
	pass


class animationCOMP(OP,COMP):
	pass


class antialiasTOP(TOP,OP):
	pass


class armSOP(OP,SOP):
	pass


class artnetDAT(DAT,OP):
	pass


class attributeCHOP(CHOP,OP):
	pass


class attributecreateSOP(OP,SOP):
	pass


class attributeSOP(OP,SOP):
	pass


class audiobandeqCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class audiodeviceinCHOP(CHOP,OP):
	pass


class audiodeviceoutCHOP(CHOP,OP):
	pass


class audiodynamicsCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class audiofileinCHOP(CHOP,OP):
	pass


class audiofilterCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class audiomovieCHOP(CHOP,OP):
	hasAudio:Annotated[bool,"""True if the movie has audio."""]
	playbackRate:Annotated[float,"""The current movie playback rate."""]
	pass


class audiooscillatorCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class audioparaeqCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class audioplayCHOP(CHOP,OP):
	pass


class audiorenderCHOP(CHOP,OP):
	pass


class audiospectrumCHOP(CHOP,OP):
	pass


class audiostreaminCHOP(CHOP,OP):
	pass


class audiostreamoutCHOP(CHOP,OP):
	pass


class audiowebrenderCHOP(CHOP,OP):
	pass


class baseCOMP(OP,COMP):
	pass


class basisSOP(OP,SOP):
	pass


class beatCHOP(CHOP,OP):
	pass


class blacktraxCHOP(CHOP,OP):
	pass


class blendCHOP(CHOP,OP):
	pass


class blendCOMP(OP,ObjectCOMP,COMP):
	pass


class blendSOP(OP,SOP):
	pass


class blobtrackTOP(TOP,OP):
	pass


class blurTOP(TOP,OP):
	pass


class boneCOMP(OP,ObjectCOMP,COMP):
	pass


class bonegroupSOP(OP,SOP):
	pass


class booleanSOP(OP,SOP):
	pass


class boxSOP(OP,SOP):
	pass


class bridgeSOP(OP,SOP):
	pass


class buttonCOMP(OP,PanelCOMP,COMP):
	pass


class cacheselectTOP(TOP,OP):
	pass


class cacheSOP(OP,SOP):
	pass


class cacheTOP(TOP,OP):
	pass


class camerablendCOMP(OP,ObjectCOMP,COMP):
	pass


class cameraCOMP(OP,ObjectCOMP,COMP):
	pass


class capSOP(OP,SOP):
	pass


class captureregionSOP(OP,SOP):
	pass


class captureSOP(OP,SOP):
	pass


class carveSOP(OP,SOP):
	pass


class channelmixTOP(TOP,OP):
	pass


class CHOP(OP):
	numChans:Annotated[int,"""The number of channels."""]
	numSamples:Annotated[int,"""Get or set the number of samples (or indices) per channel. You can change the number of samples by setting this value, only in a [[scriptCHOP Class|scriptCHOP]]."""]
	start:Annotated[float,"""Get or set the start index of the channels. This can be modified only when the CHOP is a [[scriptCHOP Class|scriptCHOP]]."""]
	end:Annotated[float,"""Get or set the end index of the channels. This can be modified only when the CHOP is a [[scriptCHOP Class|scriptCHOP]]."""]
	rate:Annotated[float,"""Get or set the sample rate of the CHOP. This can be modified only when the CHOP is a [[scriptCHOP Class|scriptCHOP]]."""]
	isTimeSlice:Annotated[bool,"""Get or set the last cooked [[Time Slicing|Time Slice]] value. True if the CHOP last cooked as a Time Slice. This can be modified only when the CHOP is a [[scriptCHOP Class|scriptCHOP]]"""]
	export:Annotated[bool,"""Get or set [[Export Flag]]."""]
	exportChanges:Annotated[int,"""Number of times the export mapping information has changed."""]
	isCHOP:Annotated[bool,"""True if the operator is a CHOP."""]
	pass


class zedCHOP(CHOP,OP):
	pass


class waveCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class warpCHOP(CHOP,OP):
	pass


class trimCHOP(CHOP,OP):
	pass


class triggerCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class transformCHOP(CHOP,OP):
	pass


class trailCHOP(CHOP,OP):
	pass


class touchoutCHOP(CHOP,OP):
	pass


class touchinCHOP(CHOP,OP):
	pass


class toptoCHOP(CHOP,OP):
	pass


class timesliceCHOP(CHOP,OP):
	pass


class timerCHOP(CHOP,OP):
	beginFrame:Annotated[list,"""Get a list of begin values in frames. 0-based."""]
	beginSample:Annotated[list,"""Get a list of begin values in samples. 0-based."""]
	beginSeconds:Annotated[list,"""Get a list of begin values in seconds."""]
	cumulativeFrames:Annotated[int,"""Get the cumulative time expressed in frames. See <code>.cumulativeSeconds</code>."""]
	cumulativeSample:Annotated[int,"""Get the cumulative time expressed in samples. See <code>.cumulativeSeconds</code>."""]
	cumulativeSamples:Annotated[int,"""Get the cumulative time expressed in samples. See <code>.cumulativeSeconds</code>."""]
	cumulativeSeconds:Annotated[float,"""Get the cumulative time expressed in seconds. It counts from 0 when you Start. Unlike <code>.runningSeconds</code>, it is slowed/sped by the Speed parameter, and paused by the Play parameter. It continues to increase if there is any looping, jumping or scrubbing around."""]
	cumulativeTimecode:Annotated[any,"""Get the cumulative time as a Timecode Object. See [[Timecode Class]]. See <code>.cumulativeSeconds</code>."""]
	masterFrames:Annotated[int,"""Get or set the master time expressed in frames. 0-based. See <code>.masterSeconds</code>."""]
	masterFrame:Annotated[int,"""Get or set the master time expressed in frames. 0-based. See <code>.masterSeconds</code>."""]
	masterSamples:Annotated[int,"""Get or set the master time expressed in samples. See <code>.masterSeconds</code>."""]
	masterSample:Annotated[int,"""Get or set the master time expressed in samples. See <code>.masterSeconds</code>."""]
	masterSeconds:Annotated[float,"""Get or set the master time expressed in seconds. It counts from 0 when you Start, <code>.masterSeconds</code> is slowed/sped by the Speed parameter, and paused by the Play parameter. It jumps to the appropriate time when you scrub. This is the main clock in the Timer CHOP and can be set directly using python (<code>OP.masterSeconds = ''val''</code>), or use the <code>.goTo()</code> function which has more options. When multi-segments are specified to the Timer CHOP, it reflects the time as if you ran through the segments without interrupting it. If in any segment Cycle is on and Cycle Limit is off, it calculates as if the cycle runs only once."""]
	masterFraction:Annotated[float,"""Get or set the master time expressed in fractional form. See <code>.masterSeconds</code>."""]
	masterTimecode:Annotated[any,"""Get or set the master time expressed as a Timecode Object. See [[Timecode Class]]. See <code>.masterSeconds</code>."""]
	cycle:Annotated[float,"""Get or set the cycle index of the current segment."""]
	fraction:Annotated[float,"""Get the time index in fractional form, same as the <code>timer_fraction</code> channel. Used in the callbacks, it's more up-to-date to the current frame. (When using segments, it's the first segment)."""]
	playingFrames:Annotated[int,"""Get the playing time expressed in frames. 0-based. See <code>.playingSeconds</code>."""]
	playingSample:Annotated[int,"""Get the playing time expressed in samples. See <code>.playingSeconds</code>."""]
	playingSamples:Annotated[int,"""Get the playing time expressed in samples. See <code>.playingSeconds</code>."""]
	playingSeconds:Annotated[float,"""Get the playing time expressed in seconds. It counts from 0 when you Start. it is unaffected by the Speed parameter, but unlike <code>.runningSeconds</code>, it is paused by the Play parameter. It continues to increase if there is any looping, jumping or scrubbing around."""]
	playingTimecode:Annotated[any,"""Get the playing time as a Timecode Object. See [[Timecode Class]]. See <code>.playingSeconds</code>."""]
	runningFraction:Annotated[float,"""Get the running time index expressed in fractional form. See <code>.runningSeconds</code>. This will be an estimate as the actual length is approximated on start."""]
	runningFrames:Annotated[float,"""Get the running time expressed in frames. 0-based. See <code>.runningSeconds</code>."""]
	runningFrame:Annotated[float,"""Get the running time expressed in frames. 0-based. See <code>.runningSeconds</code>."""]
	runningSamples:Annotated[float,"""Get the running time index expressed in samples. See <code>.runningSeconds</code>."""]
	runningSample:Annotated[float,"""Get the running time index expressed in samples. See <code>.runningSeconds</code>."""]
	runningSeconds:Annotated[float,"""Get the running time expressed in seconds. It keeps counting up after Start and is not affected by changing the Speed or pausing Play or scrubbing. It is basically the "wall clock" after pressing Start. (You normally don't set the value, use <code>.masterSeconds</code>.)  It doesn't reset to 0 until you Initialize or Start again."""]
	runningTimecode:Annotated[any,"""Get the running time index as a Timecode Object. See [[Timecode Class]]. See <code>.runningSeconds</code>."""]
	runningLengthFrames:Annotated[float,"""Get the running length expressed in frames."""]
	runningLengthSamples:Annotated[float,"""Get the running length expressed in samples."""]
	runningLengthSeconds:Annotated[float,"""Get the running length expressed in seconds."""]
	runningLengthTimecode:Annotated[any,"""Get the running length as a Timecode Object. See [[Timecode Class]]."""]
	segment:Annotated[float,"""Get or set the segment index."""]
	segments:Annotated[list,"""Get the list of segments."""]
	timecode:Annotated[any,"""Get the master timecode. See [[Timecode Class]]."""]
	pass


class timelineCHOP(CHOP,OP):
	timecode:Annotated[any,"""Get a Timecode object for the timecode data representation of the current timeline frame. See [[Timecode Class]]."""]
	pass


class tabletCHOP(CHOP,OP):
	pass


class syncoutCHOP(CHOP,OP):
	pass


class syncinCHOP(CHOP,OP):
	timecode:Annotated[any,"""Get a Timecode object for the timecode data representation of the last received index. See [[Timecode Class]]."""]
	pass


class switchCHOP(CHOP,OP):
	pass


class stretchCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class springCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class spliceCHOP(CHOP,OP):
	pass


class speedCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class sortCHOP(CHOP,OP):
	pass


class soptoCHOP(CHOP,OP):
	pass


class slopeCHOP(CHOP,OP):
	pass


class shuffleCHOP(CHOP,OP):
	pass


class shiftCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class sharedmemoutCHOP(CHOP,OP):
	pass


class sharedmeminCHOP(CHOP,OP):
	pass


class serialCHOP(CHOP,OP):
	pass


class sequencerCHOP(CHOP,OP):
	pass


class selectCHOP(CHOP,OP):
	pass


class scurveCHOP(CHOP,OP):
	chanIndex:Annotated[any,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class scriptCHOP(CHOP,OP):
	timeSliceDefault:Annotated[bool,"""Get the default [[Time Slice]] for the [[Script CHOP]]. Equal to the first input's <code>isTimeSlice</code>."""]
	pass


class scanCHOP(CHOP,OP):
	pass


class resampleCHOP(CHOP,OP):
	pass


class replaceCHOP(CHOP,OP):
	pass


class reorderCHOP(CHOP,OP):
	pass


class renderpickCHOP(CHOP,OP):
	pickedSOP:Annotated[OP,"""The [[SOP Class|SOP]] that was last picked."""]
	pass


class renameCHOP(CHOP,OP):
	pass


class recordCHOP(CHOP,OP):
	pass


class realsenseCHOP(CHOP,OP):
	pass


class pulseCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class posistagenetCHOP(CHOP,OP):
	pass


class pipeoutCHOP(CHOP,OP):
	pass


class pipeinCHOP(CHOP,OP):
	pass


class performCHOP(CHOP,OP):
	pass


class patternCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""The index of the current [[Channel Class|channel]] being evaluated. For example, if Pattern generates three channels you can put <code>[1, 3, 7][me.chanIndex]</code> in the Amplitude parameter to customize the amplitude for each channel."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class parameterCHOP(CHOP,OP):
	pass


class panelCHOP(CHOP,OP):
	pass


class overrideCHOP(CHOP,OP):
	pass


class outCHOP(CHOP,OP):
	pass


class oscoutCHOP(CHOP,OP):
	pass


class oscinCHOP(CHOP,OP):
	pass


class openvrCHOP(CHOP,OP):
	pass


class oculusriftCHOP(CHOP,OP):
	pass


class oculusaudioCHOP(CHOP,OP):
	pass


class objectCHOP(CHOP,OP):
	pass


class nullCHOP(CHOP,OP):
	pass


class noiseCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class natnetinCHOP(CHOP,OP):
	pass


class mouseoutCHOP(CHOP,OP):
	pass


class mouseinCHOP(CHOP,OP):
	pass


class midioutCHOP(CHOP,OP):
	pass


class midiinmapCHOP(CHOP,OP):
	pass


class midiinCHOP(CHOP,OP):
	pass


class mergeCHOP(CHOP,OP):
	pass


class mathCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class ltcoutCHOP(CHOP,OP):
	timecode:Annotated[any,"""Get a Timecode object for the timecode data representation of the LTC Out CHOP. See [[Timecode Class]]."""]
	pass


class ltcinCHOP(CHOP,OP):
	timecode:Annotated[any,"""Get a Timecode object for the timecode data representation of the LTC In CHOP. See [[Timecode Class]]."""]
	pass


class lookupCHOP(CHOP,OP):
	pass


class logicCHOP(CHOP,OP):
	pass


class limitCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class lfoCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class leuzerod4CHOP(CHOP,OP):
	pass


class leapmotionCHOP(CHOP,OP):
	pass


class lagCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class kinectCHOP(CHOP,OP):
	pass


class keyframeCHOP(CHOP,OP):
	pass


class keyboardinCHOP(CHOP,OP):
	pass


class joystickCHOP(CHOP,OP):
	pass


class joinCHOP(CHOP,OP):
	pass


class inversekinCHOP(CHOP,OP):
	pass


class inversecurveCHOP(CHOP,OP):
	pass


class interpolateCHOP(CHOP,OP):
	pass


class infoCHOP(CHOP,OP):
	pass


class inCHOP(CHOP,OP):
	pass


class holdCHOP(CHOP,OP):
	pass


class hokuyoCHOP(CHOP,OP):
	pass


class hogCHOP(CHOP,OP):
	pass


class heliosdacCHOP(CHOP,OP):
	pass


class handleCHOP(CHOP,OP):
	pass


class gestureCHOP(CHOP,OP):
	pass


class functionCHOP(CHOP,OP):
	pass


class filterCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class fileoutCHOP(CHOP,OP):
	pass


class fileinCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	curVal:Annotated[float,"""The current value of the sample being overridden."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	pass


class feedbackCHOP(CHOP,OP):
	pass


class fanCHOP(CHOP,OP):
	pass


class extendCHOP(CHOP,OP):
	pass


class expressionCHOP(CHOP,OP):
	chanIndex:Annotated[any,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	inputVal:Annotated[any,"""The current value of the input sample being evaluated.  To access channels from other inputs use the [[OP_Class#Connection|operator's inputs]]. Example:  me.inputs[1]['chan4'] will access chan4 of the second input."""]
	sampleIndex:Annotated[any,"""The index of the current sample being evaluated."""]
	pass


class eventCHOP(CHOP,OP):
	pass


class etherdreamCHOP(CHOP,OP):
	pass


class envelopeCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class dmxoutCHOP(CHOP,OP):
	pass


class dmxinCHOP(CHOP,OP):
	timecode:Annotated[any,"""Get a Timecode object for the last ArtTimeCode packet received. See [[Timecode Class]]."""]
	pass


class deleteCHOP(CHOP,OP):
	pass


class delayCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class dattoCHOP(CHOP,OP):
	inputCell:Annotated[any,"""The current input [[Cell Class|cell]] being evaluated. From the [[Cell Class|cell]] you can get its row, column and value. e.g. me.inputCell.val or use the specific members listed below."""]
	inputCol:Annotated[any,"""The current input colunn being evaluated."""]
	inputRow:Annotated[any,"""The current input row being evaluated."""]
	inputTable:Annotated[OP,"""The current input [[DAT Class|DAT]] being evaluated."""]
	pass


class cycleCHOP(CHOP,OP):
	pass


class crossCHOP(CHOP,OP):
	pass


class cplusplusCHOP(CHOP,OP):
	pass


class countCHOP(CHOP,OP):
	pass


class copyCHOP(CHOP,OP):
	chanIndex:Annotated[int,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	sampleIndex:Annotated[int,"""The index of the current sample being evaluated."""]
	copyIndex:Annotated[int,"""The current copy index, beginning at zero."""]
	pass


class constantCHOP(CHOP,OP):
	pass


class compositeCHOP(CHOP,OP):
	chanIndex:Annotated[any,"""<code>me.chanIndex</code> can be used in any parameter to give a different value for each [[Channel Class|channel]] being generated, for example <code>[3, 4, 5][me.chanIndex]</code>."""]
	pass


class clockCHOP(CHOP,OP):
	timecode:Annotated[any,""""Get a Timecode object representation of the hour, minute, second, and msec components.""""]
	pass


class clipCHOP(CHOP,OP):
	pass


class clipblenderCHOP(CHOP,OP):
	clipA:Annotated[OP,"""The clip being executed or blended from."""]
	clipB:Annotated[OP,"""The clip being blended into."""]
	currentClip:Annotated[OP,"""Clip A before the start of a transition, clip B otherwise."""]
	currentFrame:Annotated[float,"""The frame index of the current clip output."""]
	currentTime:Annotated[float,"""The time value of the current clip output."""]
	endBlendTime:Annotated[float,"""The time at which the transition is complete."""]
	isBlending:Annotated[bool,"""True if the output is transitioning between clips."""]
	isQueued:Annotated[bool,"""True if transitions are delayed until current transition completes."""]
	isTriggerWaiting:Annotated[bool,"""True if there is a pending triggered transition."""]
	lastClipA:Annotated[float,"""Last value of clip A."""]
	lastClipB:Annotated[float,"""Last value of clip B."""]
	nextClip:Annotated[OP,"""The next clip to be sequenced."""]
	startBlendTime:Annotated[float,"""The time the transition will start."""]
	triggerClip:Annotated[OP,"""The clip ."""]
	pass


class chopexecuteDAT(DAT,OP):
	pass


class choptoDAT(DAT,OP):
	pass


class choptoSOP(OP,SOP):
	pass


class choptoTOP(TOP,OP):
	pass


class chromakeyTOP(TOP,OP):
	pass


class circleSOP(OP,SOP):
	pass


class circleTOP(TOP,OP):
	pass


class claySOP(OP,SOP):
	pass


class clipDAT(DAT,OP):
	pass


class clipSOP(OP,SOP):
	pass


class COMP(OP):
	extensions:Annotated[any,"""A list of [[Extensions|extensions]] attached to this component."""]
	extensionsReady:Annotated[any,"""True unless the extensions are currently compiling. Can be used to avoid accessing promoted members prematurely during an extension initialization function."""]
	internalOPs:Annotated[any,"""A dictionary of [[Internal_Operators|internal operator shortcuts]] found in this component. See also [[OP_Class#General|OP.iop]]"""]
	internalPars:Annotated[any,"""A dictionary of [[Internal_Parameters|internal parameters shortcuts]] found in this component. See also [[OP_Class#General|OP.ipar]]"""]
	clones:Annotated[any,"""A list of all [[COMP Class|components]] cloned to this component."""]
	componentCloneImmune:Annotated[any,"""Get or set [[Immune Flag|component clone Immune flag]]. This works together with the cloneImmune member of the [[OP_Class]]. When componentCloneImmune is True, everything inside the clone is [[immune]]. When componentCloneImmune is False, it uses the [[OP_Class]] cloneImmune member to determine if just the component is immune (its parameters etc, but not the component's network inside)."""]
	vfs:Annotated[any,"""An intermediate [[VFS Class|VFS object]] from which embedded [[VFSFile Class|VFSFile objects]] can be accessed. For more information see [[Virtual File System]]."""]
	dirty:Annotated[any,"""True if the contents of the component need to be saved."""]
	externalTimeStamp:Annotated[any,"""Time stamp of the external tox file when it was last saved or loaded."""]
	currentChild:Annotated[OP,"""The child [[OP Class|operator]] that is currently selected. To make an operator current, use its own [[OP Class#Common Flags|OP.current]] method."""]
	selectedChildren:Annotated[any,"""The list of currently selected [[OP Class|children]]. To change an individual operator's selection state, use its own [[OP Class#Common Flags|OP.selected]] method."""]
	cpuCookTime:Annotated[float,"""Duration of the last measured cook in CPU time (in milliseconds)."""]
	childrenCPUCookTime:Annotated[float,"""The total accumulated cook time of all children of this operator during the last frame. Zero if the operator is not a COMP and/or has no children."""]
	childrenCPUCookAbsFrame:Annotated[int,"""The absolute frame on which childrenCookTime is based."""]
	gpuMemory:Annotated[int,"""The amount of GPU memory this OP is using, in bytes."""]
	pickable:Annotated[any,"""Get or set [[Pickable Flag|pickable flag]]."""]
	utility:Annotated[any,"""Get or set utility flag."""]
	isCOMP:Annotated[any,"""True if the operator is a component."""]
	isPrivate:Annotated[any,"""True if the the component contents cannot be directly viewed."""]
	isPrivacyActive:Annotated[any,"""True if the component is private, and privacy is active. When inactive the contents can be temporarily viewed."""]
	isPrivacyLicensed:Annotated[any,"""True if the component is private and if the required CodeMeter license is present to run it."""]
	privacyFirmCode:Annotated[int,"""The CodeMeter firm code needed to use this private component. 0 if this component is not private using a CodeMeter dongle."""]
	privacyProductCode:Annotated[int,"""The CodeMeter product code needed to use this private component. 0 if this component is not private using a CodeMeter dongle."""]
	privacyDeveloperName:Annotated[any,"""The name of the developer of this private component."""]
	privacyDeveloperEmail:Annotated[any,"""The email of the developer of this private component."""]
	inputCOMPs:Annotated[any,"""List of input [[COMP Class|components]] to this component through its top connector."""]
	inputCOMPConnectors:Annotated[any,"""List of input [[Connector Class|connectors]] (on the top) associated with this component."""]
	outputCOMPs:Annotated[any,"""List of output [[COMP Class|components]] from this component through its bottom connector."""]
	outputCOMPConnectors:Annotated[any,"""List of output [[Connector Class|connectors]] (on the bottom) associated with this component."""]
	pass


class windowCOMP(OP,COMP):
	scalingMonitorIndex:Annotated[int,"""The index of the monitor whose DPI scale is being used to for the Window. This is the usually the monitor the window is covering the most."""]
	isBorders:Annotated[bool,"""True if the window is bordered."""]
	isFill:Annotated[bool,"""True if the window will stretch its contents to fill its specified area."""]
	isOpen:Annotated[bool,"""True when window is open."""]
	width:Annotated[int,"""Window width. Expressed in points or pixels, depending on the DPI Scaling parameter of the Window COMP."""]
	height:Annotated[int,"""Window height. Expressed in points or pixels, depending on the DPI Scaling parameter of the Window COMP."""]
	x:Annotated[int,"""Window X coordinate relative to the bottom left of the main monitor. Expressed in points or pixels, depending on the DPI Scaling parameter of the Window COMP."""]
	y:Annotated[int,"""Window Y coordinate relative to the bottom left of the main monitor. Expressed in points or pixels, depending on the DPI Scaling parameter of the Window COMP."""]
	contentX:Annotated[int,"""X position of left edge of the windows contents. Ignores borders if they are present. Expressed in points or pixels, depending on the 'DPI Scaling' parameter setting."""]
	contentY:Annotated[int,"""Y position of bottom edge of the windows contents. Ignores borders if they are present. Expressed in points or pixels, depending on the 'DPI Scaling' parameter setting."""]
	contentWidth:Annotated[int,"""Width of windows contents. Ignores borders if they are present. Expressed in points or pixels, depending on the 'DPI Scaling' parameter setting."""]
	contentHeight:Annotated[int,"""Height of windows contents. Ignores borders if they are present. Expressed in points or pixels, depending on the 'DPI Scaling' parameter setting."""]
	pass


class timeCOMP(OP,COMP):
	frame:Annotated[float,"""Get or set the current frame output by this component."""]
	seconds:Annotated[float,"""Get or set the current time output by this component (expressed in seconds)."""]
	rate:Annotated[float,"""Get or set the frames per second, (or rate)."""]
	play:Annotated[bool,"""Get or set whether the component is playing."""]
	timecode:Annotated[str,"""Get or set the current timecode generated by this component."""]
	start:Annotated[float,"""Get or set start of main frame range."""]
	end:Annotated[float,"""Get or set end of main frame range."""]
	rangeStart:Annotated[float,"""Get or set start of sub frame range. Must be within main start, end range"""]
	rangeEnd:Annotated[float,"""Get or set end of sub frame range. Must be within main start, end range."""]
	loop:Annotated[bool,"""Get or set whether the timeline loops."""]
	independent:Annotated[float,"""Get or set whether the timeline runs independently of other timelines."""]
	tempo:Annotated[float,"""Get or set beats per minute."""]
	signature1:Annotated[int,"""Get or set time signature, first value."""]
	signature2:Annotated[int,"""Get or set time signature, second value."""]
	pass


class replicatorCOMP(OP,COMP):
	curItem:Annotated[OP,"""Reference to the current [[operator]] replicant."""]
	pass


class PanelCOMP(OP,COMP):
	panel:Annotated[any,"""The [[Panel Class|Panel]] from which [[Panel Value|Panel Values]] and the [[PanelValue Class]] may be accessed. (The second form is usually sufficient.)
<syntaxhighlight lang=python>
v = op('button1').panel.u.val
v = op('button1').panel.u
</syntaxhighlight>"""]
	panelRoot:Annotated[OP,"""The panelCOMP at the top of the panel hierarchy."""]
	panelChildren:Annotated[list,"""The children panelCOMPs of this operator."""]
	x:Annotated[int,"""The panel's x coordinate, as measured in pixels."""]
	y:Annotated[int,"""The panel's y coordinate, as measured in pixels."""]
	width:Annotated[int,"""The panel's width, as measured in pixels."""]
	height:Annotated[int,"""The panel's height, as measured in pixels."""]
	marginX:Annotated[int,"""The panel's x coordinate adjusted by margins as measured in pixels."""]
	marginY:Annotated[int,"""The panel's y coordinate adjusted by margins, as measured in pixels."""]
	marginWidth:Annotated[int,"""The panel's width adjusted by margins, as measured in pixels."""]
	marginHeight:Annotated[int,"""The panel's height adjusted by margins, as measured in pixels."""]
	pass


class tableCOMP(OP,PanelCOMP,COMP):
	pass


class sliderCOMP(OP,PanelCOMP,COMP):
	pass


class selectCOMP(OP,PanelCOMP,COMP):
	pass


class parameterCOMP(OP,PanelCOMP,COMP):
	minWidth:Annotated[int,"""The minimum width the parameter dialog can be drawn at before scaling is required."""]
	pass


class opviewerCOMP(OP,PanelCOMP,COMP):
	pass


class ObjectCOMP(OP,COMP):
	localTransform:Annotated[any,"""The current local transform of the Object. This is the combination of both the parameters from the Xform and Pre-Xform page, without taking into account any parent or constraint transforms. See also [[Matrix Class]], [[Position Class]] and [[Vector Class]]."""]
	worldTransform:Annotated[any,"""The current world transform of the Object."""]
	pass


class sharedmemoutCOMP(OP,ObjectCOMP,COMP):
	pass


class sharedmeminCOMP(OP,ObjectCOMP,COMP):
	pass


class nullCOMP(OP,ObjectCOMP,COMP):
	pass


class listCOMP(OP,PanelCOMP,COMP):
	attribs:Annotated[any,"""The table [[ListAttribute Class|attributes]]. The members of these attributes can be directly written to / updated with new values. Any row/col or cell attributes defined will override these values. Define global per-table attributes here.
<syntaxhighlight lang=python>
n.tableAttribs.fontFace = 'Verdana'
n.tableAttribs.bgColor = (0,0.3,0,1) #dark green background
</syntaxhighlight>"""]
	colAttribs:Annotated[any,"""The set of row [[ListAttributes Class|attributes]]. Accessed by row index.  The members of these attributes can be directly written to / updated with new values and take priority over any attribute members defined a the table level.
<syntaxhighlight lang=python>
n.colAttribs[4].colWidth = 100
n.colAttribs[4].bgColor = (0,0.6,0,1) #highlight entire column in bright green
</syntaxhighlight>"""]
	rowAttribs:Annotated[any,"""The set of row [[ListAttributes Class|attributes]]. Accessed by row index. The members of these attributes can be directly written to / updated with new values and take priority over any attribute members defined a the table level.
<syntaxhighlight lang=python>
n.rowAttribs[3].rowHeight = 50
</syntaxhighlight>"""]
	cellAttribs:Annotated[any,"""The set of cell [[ListAttributes Class|attributes]]. Accessed by row and column. The members of these attributes can be directly written to / updated with new values and take priority over any attribute members defined at the row/col or table level.
<syntaxhighlight lang=python>
n.cellAttribs[3,4].text = 'Fade'
n.cellAttribs[3,4].bgColor = (0.5,0,0,1) #highlight this cell red
</syntaxhighlight>"""]
	displayAttribs:Annotated[any,"""The set of attributes actually displayed in the cell. They are a combination of the cell/row/col/table attributes described above. Accessed by row and column.  When combining attributes, cell attributes take priority over row and column attributes, which themselves take priority over table attributes.
<syntaxhighlight lang=python>n.displayAttribs[3,4].bgColor #the resulting background color for this specific cell</syntaxhighlight>"""]
	focusCol:Annotated[int,"""Last column with focus for editing."""]
	focusRow:Annotated[int,"""Last row with focus for editing."""]
	radioCol:Annotated[int,"""The last selected column."""]
	radioRow:Annotated[int,"""The last selected row."""]
	rolloverCol:Annotated[int,"""The last column rolled over."""]
	rolloverRow:Annotated[int,"""The last row rolled over."""]
	selectCol:Annotated[int,"""The currently selected column."""]
	selectRow:Annotated[int,"""The currently selected row."""]
	selectionBorderColor:Annotated[any,"""Get or set the border color for the separate selection, expressed as a 4-tuple, representing its red, green, blue and alpha value."""]
	selectionColor:Annotated[any,"""Get or set the background color for the separate selection, expressed as a 4-tuple, representing its red, green, blue and alpha value."""]
	selections:Annotated[any,"""Get or set the row and column coordinates for separate selection formatting, expressed as a list of 4-tuples, each representing startrow, startcol, endrow, endcol."""]
	dragRow:Annotated[int,"""The currently dragged row."""]
	dragCol:Annotated[int,"""The currently dragged column."""]
	pass


class lightCOMP(OP,ObjectCOMP,COMP):
	pass


class handleCOMP(OP,ObjectCOMP,COMP):
	pass


class geometryCOMP(OP,ObjectCOMP,COMP):
	pass


class fieldCOMP(OP,PanelCOMP,COMP):
	pass


class environmentlightCOMP(OP,ObjectCOMP,COMP):
	pass


class containerCOMP(OP,PanelCOMP,COMP):
	pass


class compositeTOP(TOP,OP):
	pass


class constantMAT(OP,MAT):
	pass


class constantTOP(TOP,OP):
	pass


class convertDAT(DAT,OP):
	pass


class convertSOP(OP,SOP):
	pass


class convolveTOP(TOP,OP):
	pass


class copySOP(OP,SOP):
	copyIndex:Annotated[int,"""The current copy index, beginning at zero."""]
	copyTotal:Annotated[int,"""The total number of copies."""]
	inputPoint:Annotated[int,"""The current [[Point Class|point]] being evaluated, of the template."""]
	pass


class cornerpinTOP(TOP,OP):
	pass


class cplusplusSOP(OP,SOP):
	pass


class cplusplusTOP(TOP,OP):
	pass


class creepSOP(OP,SOP):
	pass


class cropTOP(TOP,OP):
	pass


class crossTOP(TOP,OP):
	pass


class cubemapTOP(TOP,OP):
	pass


class curveclaySOP(OP,SOP):
	pass


class curvesectSOP(OP,SOP):
	pass


class DAT(OP):
	export:Annotated[bool,"""Get or set [[Export Flag]]"""]
	module:Annotated[any,"""Retrieve the contents of the DAT as a module. This allows for functions in the module to be called directly. E.g n.module.function(arg1, arg2)"""]
	numRows:Annotated[int,"""Number of rows in the DAT table."""]
	numCols:Annotated[int,"""Number of columns in the DAT table."""]
	text:Annotated[str,"""Get or set contents. Tables are treated as tab delimited columns, newline delimited rows."""]
	editingFile:Annotated[str,"""The path to the current file used by external editors."""]
	isTable:Annotated[bool,"""True if the DAT contains table formatted data."""]
	isText:Annotated[bool,"""True if the DAT contains text formatted data. (ie, not table formatted)."""]
	isEditable:Annotated[bool,"""True if the DAT contents can be edited (Text DATs, Table DATs, locked DATs etc)."""]
	isDAT:Annotated[bool,"""True if the operator is a DAT."""]
	locals:Annotated[dict,"""Local dictionary used during python execution of scripts in this DAT. The dictionary attribute is read only, but not its contents. Its contents may be manipulated directly with scripts, or with an [[Examine DAT]]."""]
	jsonObject:Annotated[dict,"""Parses the DAT as json and returns a python object."""]
	pass


class xmlDAT(DAT,OP):
	pass


class websocketDAT(DAT,OP):
	pass


class webDAT(DAT,OP):
	downloadCurrent:Annotated[int,"""Total bytes downloaded so far."""]
	downloadFraction:Annotated[float,"""Fraction of downloaded size to total size."""]
	downloadTotal:Annotated[int,"""Total size for download, expressed in bytes."""]
	queryContentEncoding:Annotated[str,"""Query Content Encoding, as returned from HTML query."""]
	queryContentLength:Annotated[int,"""Query Content Length, as returned from HTML query."""]
	queryContentType:Annotated[str,"""Query Content Type, as returned from HTML query."""]
	queryContentTypeCharset:Annotated[str,"""Query Content Type character set, as returned from HTML query."""]
	pass


class udtoutDAT(DAT,OP):
	pass


class udtinDAT(DAT,OP):
	pass


class udpoutDAT(DAT,OP):
	pass


class udpinDAT(DAT,OP):
	pass


class tuioinDAT(DAT,OP):
	pass


class transposeDAT(DAT,OP):
	pass


class touchoutDAT(DAT,OP):
	pass


class touchinDAT(DAT,OP):
	pass


class textDAT(DAT,OP):
	pass


class tcpipDAT(DAT,OP):
	pass


class tableDAT(DAT,OP):
	subRow:Annotated[int,"""Current row index for Table expressions."""]
	subCol:Annotated[int,"""Current col index for Table expressions."""]
	fillName:Annotated[any,"""Current header name for Table expressions."""]
	pass


class switchDAT(DAT,OP):
	pass


class substituteDAT(DAT,OP):
	inputCell:Annotated[Cell,"""The current input [[Cell Class|cell]] being evaluated. From the [[Cell Class|cell]] you can get its row, column and value. e.g. me.inputCell.val or use the specific members listed below."""]
	inputCol:Annotated[any,"""The current input colunn being evaluated."""]
	inputRow:Annotated[any,"""The current input row being evaluated."""]
	inputTable:Annotated[OP,"""The current input [[DAT Class|DAT]] being evaluated.
<syntaxhighlight lang=python>
me.inputCell.val # value in cell
me.inputTable[2,3].val # cell row 2, column 3
me.inputTable[me.inputRow, me.inputCol-1].val # cell in previous column
me.inputCell.offset(0, -1) # alternative syntax for previous column
</syntaxhighlight>"""]
	pass


class sortDAT(DAT,OP):
	pass


class soptoDAT(DAT,OP):
	pass


class serialDAT(DAT,OP):
	pass


class selectDAT(DAT,OP):
	inputCell:Annotated[Cell,"""The current input [[Cell Class|cell]] being evaluated. From the [[Cell Class|cell]] you can get its row, column and value. e.g. me.inputCell.val or use the specific members listed below."""]
	inputCol:Annotated[any,"""The current input column being evaluated."""]
	inputRow:Annotated[any,"""The current input row being evaluated."""]
	inputTable:Annotated[OP,"""The current input [[DAT Class|DAT]] being evaluated.
<syntaxhighlight lang=python>
me.inputCell.val #value in cell
me.inputTable[2,3].val #cell row 2, column 3
me.inputTable[me.inputRow, me.inputCol-1].val #cell in previous column
me.inputCell.offset(0, -1) #alternative syntax for previous column
</syntaxhighlight>"""]
	pass


class scriptDAT(DAT,OP):
	pass


class reorderDAT(DAT,OP):
	pass


class performDAT(DAT,OP):
	pass


class parameterexecuteDAT(DAT,OP):
	pass


class panelexecuteDAT(DAT,OP):
	pass


class outDAT(DAT,OP):
	pass


class oscoutDAT(DAT,OP):
	pass


class oscinDAT(DAT,OP):
	pass


class opfindDAT(DAT,OP):
	pass


class opexecuteDAT(DAT,OP):
	pass


class nullDAT(DAT,OP):
	pass


class multitouchinDAT(DAT,OP):
	pass


class mqttclientDAT(DAT,OP):
	isConnected:Annotated[bool,"""Return True if connected to a broker, and False if not."""]
	pass


class monitorsDAT(DAT,OP):
	pass


class midiinDAT(DAT,OP):
	pass


class midieventDAT(DAT,OP):
	pass


class mergeDAT(DAT,OP):
	pass


class keyboardinDAT(DAT,OP):
	pass


class insertDAT(DAT,OP):
	subRow:Annotated[int,"""Current row index for Insert DAT Table expressions."""]
	subCol:Annotated[int,"""Current col index for Insert DAT Table expressions."""]
	fillName:Annotated[str,"""Current header name for Insert DAT Table expressions."""]
	pass


class infoDAT(DAT,OP):
	pass


class indicesDAT(DAT,OP):
	pass


class inDAT(DAT,OP):
	pass


class folderDAT(DAT,OP):
	pass


class fileoutDAT(DAT,OP):
	writeCount:Annotated[int,"""The number of times data has been written. This can be used to create an incrementing filename."""]
	pass


class fileinDAT(DAT,OP):
	pass


class fifoDAT(DAT,OP):
	pass


class executeDAT(DAT,OP):
	pass


class examineDAT(DAT,OP):
	pass


class evaluateDAT(DAT,OP):
	exprCell:Annotated[any,"""The current expression [[Cell Class|cell]] being evaluated.  From the [[Cell Class|cell]] you can get its row, column and value. e.g. me.exprCell.val or use the specific members listed below.  Too see how a [[Cell Class]] such as me.exprCell is automatically converted to a string or number in an expression see [[Cell Class#Casting to a Value|Casting to a Value]]."""]
	exprCol:Annotated[any,"""The current expression column being evaluated."""]
	exprRow:Annotated[any,"""The current expression row being evaluated."""]
	exprTable:Annotated[any,"""The input [[DAT Class|DAT]] containing the expressions."""]
	inputCell:Annotated[any,"""The current input [[Cell Class|cell]] being evaluated. From the [[Cell Class|cell]] you can get its row, column and value. e.g. me.inputCell.val or use the specific members listed below.  To see how a [[Cell Class]] such as me.inputCell is automatically converted to a string or number in an expression see [[Cell Class#Casting to a Value|Casting to a Value]]."""]
	inputCol:Annotated[any,"""The current input column being evaluated."""]
	inputRow:Annotated[any,"""The current input row being evaluated."""]
	inputTable:Annotated[any,"""The input [[DAT Class|DAT]] containing the source values."""]
	pass


class etherdreamDAT(DAT,OP):
	pass


class errorDAT(DAT,OP):
	pass


class datexecuteDAT(DAT,OP):
	pass


class dattoSOP(OP,SOP):
	pass


class deformSOP(OP,SOP):
	pass


class deleteSOP(OP,SOP):
	inputPoint:Annotated[int,"""The current [[Point Class|point]] being evaluated. Can only be used in the parameters for this SOP."""]
	inputPrim:Annotated[int,"""The current [[Prim Class|primitive]] being evaluated. Can only be used in the parameters for this SOP."""]
	pass


class depthMAT(OP,MAT):
	pass


class depthTOP(TOP,OP):
	pass


class differenceTOP(TOP,OP):
	pass


class directxinTOP(TOP,OP):
	pass


class directxoutTOP(TOP,OP):
	pass


class displaceTOP(TOP,OP):
	pass


class divideSOP(OP,SOP):
	pass


class edgeTOP(TOP,OP):
	pass


class embossTOP(TOP,OP):
	pass


class extrudeSOP(OP,SOP):
	pass


class facetSOP(OP,SOP):
	pass


class feedbackTOP(TOP,OP):
	pass


class fileinSOP(OP,SOP):
	pass


class filletSOP(OP,SOP):
	pass


class fitSOP(OP,SOP):
	pass


class fitTOP(TOP,OP):
	pass


class flipTOP(TOP,OP):
	pass


class fontSOP(OP,SOP):
	pass


class forceSOP(OP,SOP):
	pass


class fractalSOP(OP,SOP):
	pass


class glslMAT(OP,MAT):
	compileResult:Annotated[str,"""The latest compile result."""]
	pass


class glslmultiTOP(TOP,OP):
	compileResult:Annotated[str,"""The latest compile result."""]
	pass


class glslTOP(TOP,OP):
	compileResult:Annotated[str,"""The latest compile result."""]
	pass


class gridSOP(OP,SOP):
	pass


class groupSOP(OP,SOP):
	inputPoint:Annotated[Point,"""The current [[Point Class|point]] being evaluated."""]
	inputPrim:Annotated[Prim,"""The current [[Prim Class|primitive]] being evaluated."""]
	pass


class holeSOP(OP,SOP):
	pass


class hsvadjustTOP(TOP,OP):
	pass


class hsvtorgbTOP(TOP,OP):
	pass


class inMAT(OP,MAT):
	pass


class insideTOP(TOP,OP):
	pass


class inSOP(OP,SOP):
	pass


class inTOP(TOP,OP):
	pass


class inversecurveSOP(OP,SOP):
	pass


class isosurfaceSOP(OP,SOP):
	curPos:Annotated[any,"""The current [[Position Class|position]] of the surface."""]
	pass


class joinSOP(OP,SOP):
	pass


class jointSOP(OP,SOP):
	pass


class kinectSOP(OP,SOP):
	pass


class kinectTOP(TOP,OP):
	pass


class latticeSOP(OP,SOP):
	pass


class layoutTOP(TOP,OP):
	pass


class leapmotionTOP(TOP,OP):
	pass


class levelTOP(TOP,OP):
	pass


class limitSOP(OP,SOP):
	pass


class lineSOP(OP,SOP):
	pass


class linethickSOP(OP,SOP):
	pass


class lodSOP(OP,SOP):
	pass


class lookupTOP(TOP,OP):
	pass


class lsystemSOP(OP,SOP):
	pass


class lumablurTOP(TOP,OP):
	pass


class lumalevelTOP(TOP,OP):
	pass


class magnetSOP(OP,SOP):
	pass


class MAT(OP):
	isMAT:Annotated[bool,"""True if the operator is a Material."""]
	pass


class wireframeMAT(OP,MAT):
	pass


class switchMAT(OP,MAT):
	pass


class selectMAT(OP,MAT):
	pass


class pointspriteMAT(OP,MAT):
	pass


class phongMAT(OP,MAT):
	pass


class pbrMAT(OP,MAT):
	pass


class outMAT(OP,MAT):
	pass


class nullMAT(OP,MAT):
	pass


class materialSOP(OP,SOP):
	pass


class mathTOP(TOP,OP):
	pass


class matteTOP(TOP,OP):
	pass


class mergeSOP(OP,SOP):
	pass


class Mesh(Prim):
	closedU:Annotated[bool,"""Returns True if the mesh is closed in U, False otherwise."""]
	closedV:Annotated[bool,"""Returns True if the mesh is closed in V, False otherwise."""]
	numRows:Annotated[int,"""Number of rows in the mesh."""]
	numCols:Annotated[int,"""Number of columns in the mesh."""]
	pass


class metaballSOP(OP,SOP):
	pass


class mirrorTOP(TOP,OP):
	pass


class modelSOP(OP,SOP):
	pass


class monochromeTOP(TOP,OP):
	pass


class moviefileinTOP(TOP,OP):
	fileHeight:Annotated[int,"""Height of the movie, in pixels."""]
	fileWidth:Annotated[int,"""Width of the movie, in pixels."""]
	hasAudio:Annotated[bool,"""True if the movie contains audio."""]
	hasDecodeErrors:Annotated[bool,"""True if any frames failed to decode, likely due to file corruption. Currently only works on Hap codec files."""]
	index:Annotated[float,"""Current movie index."""]
	indexFraction:Annotated[float,"""Current movie index expressed as a fraction of total length."""]
	isFullyPreRead:Annotated[bool,"""True if the movie has pre-read all of its Pre-Read frames and is ready to play. For single images this is true when the image is ready to be shown. When a movie is playing, this member will flip between True and False as its pre-read frames get consumed/refilled. When a movie isn't playing forward, this member can tell you if the movie is in an optimal state to start playing back from its currently selected frame/cued frame."""]
	isInvalid:Annotated[bool,"""True if the movie has failed to load."""]
	isLastFrame:Annotated[bool,"""True if the movie is currently showing its last frame."""]
	isLoopFrame:Annotated[bool,"""True if the movie has just looped and is showing the first frame after a loop."""]
	isOddField:Annotated[bool,"""True if the current displayed de-interlaced frame is the odd field."""]
	isOpen:Annotated[bool,"""True if the file has been opened."""]
	isOpening:Annotated[bool,"""True when the file is opening."""]
	isFileOpening:Annotated[bool,"""Returns true while the file header is being read."""]
	isPreloading:Annotated[bool,"""True when the file is preloading."""]
	lastIndexUploaded:Annotated[float,"""The index of the if the last frame uploaded to the GPU."""]
	numHeaders:Annotated[int,"""Returns the number of key-value pairs in the file's header."""]
	numImages:Annotated[float,"""The number of images in the movie."""]
	numSeconds:Annotated[float,"""The number of seconds in the movie."""]
	rate:Annotated[float,"""The movie sample rate."""]
	sourceChannels:Annotated[tuple,"""A list of the available channels in the file e.g. R, G, B, A for typical color images."""]
	start:Annotated[float,"""The start index of the movie."""]
	trueIndex:Annotated[float,"""The actual current index of the movie, disregarding trimming and other options."""]
	trueNumImages:Annotated[float,"""The actual number of images contained in the movie, not affected by trimming."""]
	timecode:Annotated[any,"""Get a Timecode object for the timecode data representation of the true current index of the movie. See [[Timecode Class]]."""]
	pass


class moviefileoutTOP(TOP,OP):
	writeCount:Annotated[any,"""The number of files that have been written. This can be used to create an incrementing file name."""]
	curSeqIndex:Annotated[any,"""The current index of the last written image on disk."""]
	fileSuffix:Annotated[str,"""Returns the generated file suffix. It will be generated based on the values of the parameters Unique Suffix and N, plus the file extension. It will take one of two forms: <code>''N''.''ext''</code> or <code>''N''.''i''.''ext''</code> where <code>''N''</code> is the suffix index (uniquely generated if Unique Suffix is enabled), <code>''i''</code> is the image sequence index (used only for the image sequence type), and <code>''ext''</code> is the image/movie extension."""]
	pass


class multiplyTOP(TOP,OP):
	pass


class ndiinTOP(TOP,OP):
	pass


class ndioutTOP(TOP,OP):
	pass


class NetworkEditor(Pane):
	showBackdropCHOPs:Annotated[bool,"""Enable or disable [[CHOP]] viewers as backdrops."""]
	showBackdropGeometry:Annotated[bool,"""Enable or disable [[SOP]] and [[Geometry Object|Geometry object]] viewers as backdrops."""]
	showBackdropTOPs:Annotated[bool,"""Enable or disable [[TOP]] viewers as backdrops."""]
	showColorPalette:Annotated[bool,"""Enable or disable display of the operator color palette selector."""]
	showDataLinks:Annotated[bool,"""Enable or disable disable of operator data links."""]
	showList:Annotated[bool,"""Control display of operators as a list, or connected nodes."""]
	showNetworkOverview:Annotated[bool,"""Enable or disable display of the network overview."""]
	showParameters:Annotated[bool,"""Enable or disable display of the currently selected operator parameters."""]
	straightLinks:Annotated[bool,"""Control display of operator links as straight or curved."""]
	x:Annotated[float,"""Get or set the x coordinate of the network editor area,  where 1 unit = 1 pixel when zoom = 1."""]
	y:Annotated[float,"""Get or set the y coordinate of the network editor area, where 1 unit = 1 pixel when zoom = 1."""]
	zoom:Annotated[float,"""Get or set the zoom factor of the network editor area, where a zoom factor of 1 draws each node at its unscaled resolution."""]
	pass


class noiseSOP(OP,SOP):
	pass


class noiseTOP(TOP,OP):
	pass


class normalmapTOP(TOP,OP):
	pass


class nullSOP(OP,SOP):
	pass


class nullTOP(TOP,OP):
	pass


class objectmergeSOP(OP,SOP):
	pass


class oculusriftTOP(TOP,OP):
	pass


class Poly(Prim):
	closed:Annotated[bool,"""Returns True if the poly is closed, False otherwise."""]
	pass



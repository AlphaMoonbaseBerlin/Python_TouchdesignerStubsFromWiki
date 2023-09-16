from typing import Annotated
class abletonlinkCHOP(CHOP,OP):
	pass


class AbsTime():
	frame:any
	seconds:any
	step:any
	stepSeconds:any
	pass


class Actors():
	pass


class addSOP(OP,SOP):
	pass


class addTOP(TOP,OP):
	pass


class alembicSOP(OP,SOP):
	pass


class alignSOP(OP,SOP):
	pass


class ambientlightCOMP(COMP,ObjectCOMP,OP):
	pass


class analyzeCHOP(CHOP,OP):
	pass


class analyzeTOP(TOP,OP):
	pass


class angleCHOP(CHOP,OP):
	pass


class animationCOMP(COMP,OP):
	pass


class antialiasTOP(TOP,OP):
	pass


class App():
	architecture:any
	binFolder:any
	build:any
	compileDate:any
	configFolder:any
	desktopFolder:any
	enableOptimizedExprs:any
	experimental:any
	installFolder:any
	launchTime:any
	logExtensionCompiles:any
	osName:any
	osVersion:any
	power:any
	preferencesFolder:any
	product:any
	recentFiles:any
	samplesFolder:any
	paletteFolder:any
	userPaletteFolder:any
	version:any
	windowColorBits:any
	pass


class ArcBall():
	pass


class armSOP(OP,SOP):
	pass


class artnetDAT(DAT,OP):
	pass


class Attribute():
	owner:any
	name:any
	size:any
	type:any
	default:any
	pass


class attributeCHOP(CHOP,OP):
	pass


class attributecreateSOP(OP,SOP):
	pass


class AttributeData():
	owner:any
	val:any
	pass


class Attributes():
	owner:any
	pass


class attributeSOP(OP,SOP):
	pass


class audiobandeqCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class audiodeviceinCHOP(CHOP,OP):
	pass


class audiodeviceoutCHOP(CHOP,OP):
	pass


class audiodynamicsCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class audiofileinCHOP(CHOP,OP):
	pass


class audiofilterCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class audiomovieCHOP(CHOP,OP):
	hasAudio:any
	playbackRate:any
	pass


class audiooscillatorCHOP(CHOP,OP):
	chanIndex:any
	pass


class audioparaeqCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
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


class baseCOMP(COMP,OP):
	pass


class basisSOP(OP,SOP):
	pass


class beatCHOP(CHOP,OP):
	pass


class Bezier():
	anchors:any
	basis:any
	closed:any
	order:any
	segments:any
	tangents:any
	pass


class blacktraxCHOP(CHOP,OP):
	pass


class blendCHOP(CHOP,OP):
	pass


class blendCOMP(COMP,ObjectCOMP,OP):
	pass


class blendSOP(OP,SOP):
	pass


class blobtrackTOP(TOP,OP):
	pass


class blurTOP(TOP,OP):
	pass


class Bodies():
	pass


class Body():
	index:any
	owner:any
	rotate:any
	translate:any
	angularVelocity:any
	linearVelocity:any
	pass


class boneCOMP(COMP,ObjectCOMP,OP):
	pass


class bonegroupSOP(OP,SOP):
	pass


class booleanSOP(OP,SOP):
	pass


class Bounds():
	pass


class boxSOP(OP,SOP):
	pass


class bridgeSOP(OP,SOP):
	pass


class buttonCOMP(COMP,PanelCOMP,OP):
	pass


class cacheselectTOP(TOP,OP):
	pass


class cacheSOP(OP,SOP):
	pass


class cacheTOP(TOP,OP):
	pass


class Camera():
	dir:any
	pivot:any
	position:any
	pass


class camerablendCOMP(COMP,ObjectCOMP,OP):
	pass


class cameraCOMP(COMP,ObjectCOMP,OP):
	pass


class capSOP(OP,SOP):
	pass


class captureregionSOP(OP,SOP):
	pass


class captureSOP(OP,SOP):
	pass


class carveSOP(OP,SOP):
	pass


class Cell():
	valid:any
	row:any
	col:any
	owner:any
	val:any
	pass


class Channel():
	valid:any
	index:any
	name:any
	owner:any
	exports:any
	vals:any
	pass


class channelmixTOP(TOP,OP):
	pass


class CHOP(OP):
	numChans:any
	numSamples:any
	start:any
	end:any
	rate:any
	isTimeSlice:any
	export:any
	exportChanges:any
	isCHOP:any
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


class clipblenderCHOP(CHOP,OP):
	clipA:any
	clipB:any
	currentClip:any
	currentFrame:any
	currentTime:any
	endBlendTime:any
	isBlending:any
	isQueued:any
	isTriggerWaiting:any
	lastClipA:any
	lastClipB:any
	nextClip:any
	startBlendTime:any
	triggerClip:any
	pass


class clipCHOP(CHOP,OP):
	pass


class clipDAT(DAT,OP):
	pass


class clipSOP(OP,SOP):
	pass


class clockCHOP(CHOP,OP):
	timecode:any
	pass


class Color():
	r:any
	g:any
	b:any
	a:any
	pass


class Colors():
	pass


class COMP(OP):
	extensions:any
	extensionsReady:any
	internalOPs:any
	internalPars:any
	clones:any
	componentCloneImmune:any
	vfs:any
	dirty:any
	externalTimeStamp:any
	currentChild:any
	selectedChildren:any
	cpuCookTime:any
	childrenCPUCookTime:any
	childrenCPUCookAbsFrame:any
	gpuMemory:any
	pickable:any
	utility:any
	isCOMP:any
	isPrivate:any
	isPrivacyActive:any
	isPrivacyLicensed:any
	privacyFirmCode:any
	privacyProductCode:any
	privacyDeveloperName:any
	privacyDeveloperEmail:any
	inputCOMPs:any
	inputCOMPConnectors:any
	outputCOMPs:any
	outputCOMPConnectors:any
	pass


class compositeCHOP(CHOP,OP):
	chanIndex:any
	pass


class compositeTOP(TOP,OP):
	pass


class Connector():
	index:any
	isInput:any
	isOutput:any
	inOP:any
	outOP:any
	owner:any
	connections:any
	description:any
	pass


class constantCHOP(CHOP,OP):
	pass


class constantMAT(OP,MAT):
	pass


class constantTOP(TOP,OP):
	pass


class containerCOMP(COMP,PanelCOMP,OP):
	pass


class convertDAT(DAT,OP):
	pass


class convertSOP(OP,SOP):
	pass


class convolveTOP(TOP,OP):
	pass


class copyCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	copyIndex:any
	pass


class copySOP(OP,SOP):
	copyIndex:any
	copyTotal:any
	inputPoint:any
	pass


class cornerpinTOP(TOP,OP):
	pass


class countCHOP(CHOP,OP):
	pass


class cplusplusCHOP(CHOP,OP):
	pass


class cplusplusSOP(OP,SOP):
	pass


class cplusplusTOP(TOP,OP):
	pass


class creepSOP(OP,SOP):
	pass


class cropTOP(TOP,OP):
	pass


class crossCHOP(CHOP,OP):
	pass


class crossTOP(TOP,OP):
	pass


class cubemapTOP(TOP,OP):
	pass


class CUDAMemory():
	ptr:any
	size:any
	shape:any
	pass


class CUDAMemoryShape():
	width:any
	height:any
	numComps:any
	dataType:any
	pass


class curveclaySOP(OP,SOP):
	pass


class curvesectSOP(OP,SOP):
	pass


class cycleCHOP(CHOP,OP):
	pass


class DAT(OP):
	export:any
	module:any
	numRows:any
	numCols:any
	text:any
	editingFile:any
	isTable:any
	isText:any
	isEditable:any
	isDAT:any
	locals:any
	jsonObject:any
	pass


class datexecuteDAT(DAT,OP):
	pass


class dattoCHOP(CHOP,OP):
	inputCell:any
	inputCol:any
	inputRow:any
	inputTable:any
	pass


class dattoSOP(OP,SOP):
	pass


class debug():
	style:any
	pass


class deformSOP(OP,SOP):
	pass


class delayCHOP(CHOP,OP):
	chanIndex:any
	pass


class deleteCHOP(CHOP,OP):
	pass


class deleteSOP(OP,SOP):
	inputPoint:any
	inputPrim:any
	pass


class Dependency():
	val:any
	peekVal:any
	callbacks:any
	ops:any
	listAttributes:any
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


class dmxinCHOP(CHOP,OP):
	timecode:any
	pass


class dmxoutCHOP(CHOP,OP):
	pass


class Dongle():
	serialNumber:any
	pass


class DongleList():
	pass


class edgeTOP(TOP,OP):
	pass


class embossTOP(TOP,OP):
	pass


class envelopeCHOP(CHOP,OP):
	chanIndex:any
	pass


class environmentlightCOMP(COMP,ObjectCOMP,OP):
	pass


class errorDAT(DAT,OP):
	pass


class etherdreamCHOP(CHOP,OP):
	pass


class etherdreamDAT(DAT,OP):
	pass


class evaluateDAT(DAT,OP):
	exprCell:any
	exprCol:any
	exprRow:any
	exprTable:any
	inputCell:any
	inputCol:any
	inputRow:any
	inputTable:any
	pass


class eventCHOP(CHOP,OP):
	pass


class examineDAT(DAT,OP):
	pass


class executeDAT(DAT,OP):
	pass


class expressionCHOP(CHOP,OP):
	chanIndex:any
	inputVal:any
	sampleIndex:any
	pass


class extendCHOP(CHOP,OP):
	pass


class extrudeSOP(OP,SOP):
	pass


class facetSOP(OP,SOP):
	pass


class fanCHOP(CHOP,OP):
	pass


class feedbackCHOP(CHOP,OP):
	pass


class feedbackTOP(TOP,OP):
	pass


class fieldCOMP(COMP,PanelCOMP,OP):
	pass


class fifoDAT(DAT,OP):
	pass


class fileinCHOP(CHOP,OP):
	chanIndex:any
	curVal:any
	sampleIndex:any
	pass


class fileinDAT(DAT,OP):
	pass


class FileInfo():
	pass


class fileinSOP(OP,SOP):
	pass


class fileoutCHOP(CHOP,OP):
	pass


class fileoutDAT(DAT,OP):
	writeCount:any
	pass


class filletSOP(OP,SOP):
	pass


class filterCHOP(CHOP,OP):
	chanIndex:any
	pass


class fitSOP(OP,SOP):
	pass


class fitTOP(TOP,OP):
	pass


class flipTOP(TOP,OP):
	pass


class folderDAT(DAT,OP):
	pass


class fontSOP(OP,SOP):
	pass


class forceSOP(OP,SOP):
	pass


class fractalSOP(OP,SOP):
	pass


class functionCHOP(CHOP,OP):
	pass


class geometryCOMP(COMP,ObjectCOMP,OP):
	pass


class gestureCHOP(CHOP,OP):
	pass


class glslMAT(OP,MAT):
	compileResult:any
	pass


class glslmultiTOP(TOP,OP):
	compileResult:any
	pass


class glslTOP(TOP,OP):
	compileResult:any
	pass


class gridSOP(OP,SOP):
	pass


class Group():
	default:any
	name:any
	owner:any
	pass


class groupSOP(OP,SOP):
	inputPoint:any
	inputPrim:any
	pass


class handleCHOP(CHOP,OP):
	pass


class handleCOMP(COMP,ObjectCOMP,OP):
	pass


class heliosdacCHOP(CHOP,OP):
	pass


class hogCHOP(CHOP,OP):
	pass


class hokuyoCHOP(CHOP,OP):
	pass


class holdCHOP(CHOP,OP):
	pass


class holeSOP(OP,SOP):
	pass


class hsvadjustTOP(TOP,OP):
	pass


class hsvtorgbTOP(TOP,OP):
	pass


class inCHOP(CHOP,OP):
	pass


class inDAT(DAT,OP):
	pass


class indicesDAT(DAT,OP):
	pass


class infoCHOP(CHOP,OP):
	pass


class infoDAT(DAT,OP):
	pass


class inMAT(OP,MAT):
	pass


class InputPoint():
	color:any
	normP:any
	normal:any
	sopCenter:any
	pass


class insertDAT(DAT,OP):
	subRow:any
	subCol:any
	fillName:any
	pass


class insideTOP(TOP,OP):
	pass


class inSOP(OP,SOP):
	pass


class interpolateCHOP(CHOP,OP):
	pass


class inTOP(TOP,OP):
	pass


class inversecurveCHOP(CHOP,OP):
	pass


class inversecurveSOP(OP,SOP):
	pass


class inversekinCHOP(CHOP,OP):
	pass


class isosurfaceSOP(OP,SOP):
	curPos:any
	pass


class joinCHOP(CHOP,OP):
	pass


class joinSOP(OP,SOP):
	pass


class jointSOP(OP,SOP):
	pass


class joystickCHOP(CHOP,OP):
	pass


class keyboardinCHOP(CHOP,OP):
	pass


class keyboardinDAT(DAT,OP):
	pass


class keyframeCHOP(CHOP,OP):
	pass


class kinectCHOP(CHOP,OP):
	pass


class kinectSOP(OP,SOP):
	pass


class kinectTOP(TOP,OP):
	pass


class lagCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class latticeSOP(OP,SOP):
	pass


class layoutTOP(TOP,OP):
	pass


class leapmotionCHOP(CHOP,OP):
	pass


class leapmotionTOP(TOP,OP):
	pass


class leuzerod4CHOP(CHOP,OP):
	pass


class levelTOP(TOP,OP):
	pass


class lfoCHOP(CHOP,OP):
	chanIndex:any
	pass


class License():
	index:any
	isEnabled:any
	isRemotelyDisabled:any
	key:any
	remoteDisableDate:any
	status:any
	statusMessage:any
	systemCode:any
	type:any
	updateExpiryDate:any
	version:any
	pass


class Licenses():
	disablePro:any
	dongles:any
	machine:any
	systemCode:any
	isPro:any
	isNonCommercial:any
	type:any
	pass


class lightCOMP(COMP,ObjectCOMP,OP):
	pass


class limitCHOP(CHOP,OP):
	chanIndex:any
	pass


class limitSOP(OP,SOP):
	pass


class lineSOP(OP,SOP):
	pass


class linethickSOP(OP,SOP):
	pass


class ListAttribute():
	bgColor:any
	bottomBorderInColor:any
	bottomBorderOutColor:any
	colStretch:any
	colWidth:any
	draggable:any
	editable:any
	focus:any
	fontFile:any
	fontBold:any
	fontFace:any
	fontItalic:any
	fontSizeX:any
	fontSizeY:any
	sizeInPoints:any
	help:any
	leftBorderInColor:any
	leftBorderOutColor:any
	radio:any
	rightBorderInColor:any
	rightBorderOutColor:any
	rollover:any
	rowHeight:any
	rowIndent:any
	rowStretch:any
	select:any
	text:any
	textColor:any
	textJustify:any
	textOffsetX:any
	textOffsetY:any
	top:any
	topBorderInColor:any
	topBorderOutColor:any
	wordWrap:any
	pass


class ListAttributes():
	pass


class listCOMP(COMP,PanelCOMP,OP):
	attribs:any
	colAttribs:any
	rowAttribs:any
	cellAttribs:any
	displayAttribs:any
	focusCol:any
	focusRow:any
	radioCol:any
	radioRow:any
	rolloverCol:any
	rolloverRow:any
	selectCol:any
	selectRow:any
	selectionBorderColor:any
	selectionColor:any
	selections:any
	dragRow:any
	dragCol:any
	pass


class lodSOP(OP,SOP):
	pass


class logicCHOP(CHOP,OP):
	pass


class lookupCHOP(CHOP,OP):
	pass


class lookupTOP(TOP,OP):
	pass


class lsystemSOP(OP,SOP):
	pass


class ltcinCHOP(CHOP,OP):
	timecode:any
	pass


class ltcoutCHOP(CHOP,OP):
	timecode:any
	pass


class lumablurTOP(TOP,OP):
	pass


class lumalevelTOP(TOP,OP):
	pass


class magnetSOP(OP,SOP):
	pass


class MAT(OP):
	isMAT:any
	pass


class materialSOP(OP,SOP):
	pass


class mathCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class mathTOP(TOP,OP):
	pass


class Matrix():
	vals:any
	rows:any
	cols:any
	pass


class matteTOP(TOP,OP):
	pass


class mergeCHOP(CHOP,OP):
	pass


class mergeDAT(DAT,OP):
	pass


class mergeSOP(OP,SOP):
	pass


class Mesh(Prim):
	closedU:any
	closedV:any
	numRows:any
	numCols:any
	pass


class metaballSOP(OP,SOP):
	pass


class midieventDAT(DAT,OP):
	pass


class midiinCHOP(CHOP,OP):
	pass


class midiinDAT(DAT,OP):
	pass


class midiinmapCHOP(CHOP,OP):
	pass


class midioutCHOP(CHOP,OP):
	pass


class mirrorTOP(TOP,OP):
	pass


class MOD():
	pass


class modelSOP(OP,SOP):
	pass


class Monitor():
	index:any
	isPrimary:any
	isAffinity:any
	width:any
	height:any
	left:any
	right:any
	top:any
	bottom:any
	displayName:any
	description:any
	dpiScale:any
	scaledWidth:any
	scaledHeight:any
	scaledLeft:any
	scaledRight:any
	scaledTop:any
	scaledBottom:any
	serialNumber:any
	refreshRate:any
	pass


class Monitors():
	primary:any
	width:any
	height:any
	left:any
	right:any
	top:any
	bottom:any
	pass


class monitorsDAT(DAT,OP):
	pass


class monochromeTOP(TOP,OP):
	pass


class mouseinCHOP(CHOP,OP):
	pass


class mouseoutCHOP(CHOP,OP):
	pass


class moviefileinTOP(TOP,OP):
	fileHeight:any
	fileWidth:any
	hasAudio:any
	hasDecodeErrors:any
	index:any
	indexFraction:any
	isFullyPreRead:any
	isInvalid:any
	isLastFrame:any
	isLoopFrame:any
	isOddField:any
	isOpen:any
	isOpening:any
	isFileOpening:any
	isPreloading:any
	lastIndexUploaded:any
	numHeaders:any
	numImages:any
	numSeconds:any
	rate:any
	sourceChannels:any
	start:any
	trueIndex:any
	trueNumImages:any
	timecode:any
	pass


class moviefileoutTOP(TOP,OP):
	writeCount:any
	curSeqIndex:any
	fileSuffix:any
	pass


class mqttclientDAT(DAT,OP):
	isConnected:any
	pass


class multiplyTOP(TOP,OP):
	pass


class multitouchinDAT(DAT,OP):
	pass


class natnetinCHOP(CHOP,OP):
	pass


class ndiinTOP(TOP,OP):
	pass


class ndioutTOP(TOP,OP):
	pass


class NetworkEditor(Pane):
	showBackdropCHOPs:any
	showBackdropGeometry:any
	showBackdropTOPs:any
	showColorPalette:any
	showDataLinks:any
	showList:any
	showNetworkOverview:any
	showParameters:any
	straightLinks:any
	x:any
	y:any
	zoom:any
	pass


class noiseCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class noiseSOP(OP,SOP):
	pass


class noiseTOP(TOP,OP):
	pass


class normalmapTOP(TOP,OP):
	pass


class nullCHOP(CHOP,OP):
	pass


class nullCOMP(COMP,ObjectCOMP,OP):
	pass


class nullDAT(DAT,OP):
	pass


class nullMAT(OP,MAT):
	pass


class nullSOP(OP,SOP):
	pass


class nullTOP(TOP,OP):
	pass


class objectCHOP(CHOP,OP):
	pass


class ObjectCOMP(COMP,OP):
	localTransform:any
	worldTransform:any
	pass


class objectmergeSOP(OP,SOP):
	pass


class oculusaudioCHOP(CHOP,OP):
	pass


class oculusriftCHOP(CHOP,OP):
	pass


class oculusriftTOP(TOP,OP):
	pass


class OP():
	valid:any
	id:any
	name:any
	path:any
	digits:any
	base:any
	passive:any
	curPar:any
	time:any
	ext:any
	mod:any
	pages:any
	parGroup:any
	par:any
	builtinPars:any
	customParGroups:any
	customPars:any
	customPages:any
	customTuplets:any
	replicator:any
	storage:any
	tags:any
	children:any
	numChildren:any
	numChildrenRecursive:any
	op:any
	parent:any
	iop:any
	ipar:any
	currentPage:any
	activeViewer:any
	allowCooking:any
	bypass:any
	cloneImmune:any
	current:any
	display:any
	expose:any
	lock:any
	selected:any
	python:any
	render:any
	showCustomOnly:any
	showDocked:any
	viewer:any
	color:any
	comment:any
	nodeHeight:any
	nodeWidth:any
	nodeX:any
	nodeY:any
	nodeCenterX:any
	nodeCenterY:any
	dock:any
	docked:any
	inputs:any
	outputs:any
	inputConnectors:any
	outputConnectors:any
	cookFrame:any
	cookTime:any
	cpuCookTime:any
	cookAbsFrame:any
	cookStartTime:any
	cookEndTime:any
	cookedThisFrame:any
	cookedPreviousFrame:any
	childrenCookTime:any
	childrenCPUCookTime:any
	childrenCookAbsFrame:any
	childrenCPUCookAbsFrame:any
	gpuCookTime:any
	childrenGPUCookTime:any
	childrenGPUCookAbsFrame:any
	totalCooks:any
	cpuMemory:any
	gpuMemory:any
	type:any
	subType:any
	OPType:any
	label:any
	icon:any
	family:any
	isFilter:any
	minInputs:any
	maxInputs:any
	isMultiInputs:any
	visibleLevel:any
	isBase:any
	isCHOP:any
	isCOMP:any
	isDAT:any
	isMAT:any
	isObject:any
	isPanel:any
	isSOP:any
	isTOP:any
	licenseType:any
	pass


class opencolorioTOP(TOP,OP):
	pass


class openvrCHOP(CHOP,OP):
	pass


class openvrSOP(OP,SOP):
	pass


class openvrTOP(TOP,OP):
	pass


class opexecuteDAT(DAT,OP):
	pass


class opfindDAT(DAT,OP):
	pass


class Options():
	pass


class opviewerCOMP(COMP,PanelCOMP,OP):
	pass


class opviewerTOP(TOP,OP):
	pass


class oscinCHOP(CHOP,OP):
	pass


class oscinDAT(DAT,OP):
	pass


class oscoutCHOP(CHOP,OP):
	pass


class oscoutDAT(DAT,OP):
	pass


class outCHOP(CHOP,OP):
	pass


class outDAT(DAT,OP):
	pass


class outMAT(OP,MAT):
	pass


class outsideTOP(TOP,OP):
	pass


class outSOP(OP,SOP):
	pass


class outTOP(TOP,OP):
	pass


class overrideCHOP(CHOP,OP):
	pass


class overTOP(TOP,OP):
	pass


class packTOP(TOP,OP):
	pass


class Page():
	name:any
	owner:any
	parGroups:any
	parTuplets:any
	pars:any
	index:any
	isCustom:any
	pass


class Pane():
	owner:any
	id:any
	link:any
	enable:any
	maximize:any
	name:any
	ratio:any
	bottomLeft:any
	topRight:any
	type:any
	pass


class Panel():
	owner:any
	pass


class panelCHOP(CHOP,OP):
	pass


class PanelCOMP(COMP,OP):
	panel:any
	panelRoot:any
	panelChildren:any
	x:any
	y:any
	width:any
	height:any
	marginX:any
	marginY:any
	marginWidth:any
	marginHeight:any
	pass


class panelexecuteDAT(DAT,OP):
	pass


class PanelValue():
	name:any
	owner:any
	val:any
	valid:any
	pass


class Panes():
	current:any
	pass


class Par():
	valid:any
	val:any
	expr:any
	enableExpr:any
	exportOP:any
	exportSource:any
	bindExpr:any
	bindMaster:any
	bindReferences:any
	bindRange:any
	hidden:any
	index:any
	vecIndex:any
	name:any
	label:any
	subLabel:any
	startSection:any
	displayOnly:any
	readOnly:any
	help:any
	tuplet:any
	tupletName:any
	parGroup:any
	min:any
	max:any
	clampMin:any
	clampMax:any
	default:any
	defaultExpr:any
	normMin:any
	normMax:any
	normVal:any
	enable:any
	order:any
	page:any
	password:any
	mode:any
	prevMode:any
	menuNames:any
	menuLabels:any
	menuIndex:any
	menuSource:any
	collapser:any
	collapsable:any
	sequence:any
	owner:any
	styleCloneImmune:any
	lastScriptChange:any
	isDefault:any
	isCustom:any
	isPulse:any
	isMomentary:any
	isMenu:any
	isNumber:any
	isFloat:any
	isInt:any
	isOP:any
	isPython:any
	isString:any
	isToggle:any
	style:any
	pass


class parameterCHOP(CHOP,OP):
	pass


class parameterCOMP(COMP,PanelCOMP,OP):
	minWidth:any
	pass


class parameterexecuteDAT(DAT,OP):
	pass


class ParCollection():
	owner:any
	pass


class ParGroup():
	bindExpr:any
	bindMaster:any
	bindRange:any
	bindReferences:any
	clampMax:any
	clampMin:any
	collapsable:any
	collapser:any
	default:any
	defaultExpr:any
	enable:any
	enableExpr:any
	exportOP:any
	exportSource:any
	expr:any
	help:any
	isDefault:any
	isCustom:any
	isFloat:any
	isInt:any
	isMenu:any
	isMomentary:any
	isNumber:any
	isOP:any
	isPulse:any
	isPython:any
	isString:any
	isToggle:any
	label:any
	max:any
	menuIndex:any
	menuLabels:any
	menuNames:any
	menuSource:any
	min:any
	mode:any
	name:any
	normMax:any
	normMin:any
	normVal:any
	order:any
	owner:any
	page:any
	password:any
	prevMode:any
	readOnly:any
	displayOnly:any
	sequence:any
	startSection:any
	style:any
	subLabel:any
	val:any
	valid:any
	index:any
	pass


class ParGroupCollection():
	owner:any
	pass


class ParGroupPulse():
	pass


class ParGroupUnit():
	unit:any
	pass


class particleSOP(OP,SOP):
	pass


class patternCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class pbrMAT(OP,MAT):
	pass


class Peer():
	owner:any
	port:any
	address:any
	hostname:any
	pass


class performCHOP(CHOP,OP):
	pass


class performDAT(DAT,OP):
	pass


class phongMAT(OP,MAT):
	pass


class photoshopinTOP(TOP,OP):
	isConnected:any
	isReceivingUpdates:any
	pass


class pipeinCHOP(CHOP,OP):
	pass


class pipeoutCHOP(CHOP,OP):
	pass


class Point():
	index:any
	owner:any
	P:any
	x:any
	y:any
	z:any
	normP:any
	pass


class Points():
	owner:any
	pass


class pointSOP(OP,SOP):
	inputColor:any
	inputColor2:any
	inputNormal:any
	inputNormal2:any
	inputPoint:any
	inputPoint2:any
	inputTexture:any
	inputTexture2:any
	pass


class pointspriteMAT(OP,MAT):
	pass


class Poly(Prim):
	closed:any
	pass


class polyloftSOP(OP,SOP):
	pass


class polypatchSOP(OP,SOP):
	pass


class polyreduceSOP(OP,SOP):
	pass


class polysplineSOP(OP,SOP):
	pass


class polystitchSOP(OP,SOP):
	pass


class posistagenetCHOP(CHOP,OP):
	pass


class Position():
	x:any
	y:any
	z:any
	pass


class Preferences():
	defaults:any
	pass


class prefiltermapTOP(TOP,OP):
	pass


class Prim():
	center:any
	index:any
	normal:any
	owner:any
	weight:any
	direction:any
	min:any
	max:any
	size:any
	pass


class primitiveSOP(OP,SOP):
	inputColor:any
	inputPrim:any
	pass


class Prims():
	owner:any
	pass


class ProductEntry():
	licenseType:any
	updateDate:any
	version:any
	pass


class profileSOP(OP,SOP):
	pass


class Project():
	folder:any
	name:any
	saveVersion:any
	saveBuild:any
	saveTime:any
	saveOsName:any
	saveOsVersion:any
	saveOSName:any
	saveOSVersion:any
	paths:any
	cookRate:any
	realTime:any
	isPrivate:any
	isPrivateKey:any
	cacheParameters:any
	externalToxModifiedInProject:any
	externalToxModifiedOnDisk:any
	windowOnTop:any
	windowStartMode:any
	windowDraw:any
	windowStartCustomWidth:any
	windowStartCustomHeight:any
	windowStartCustomX:any
	windowStartCustomY:any
	performOnStart:any
	performWindowPath:any
	resetAudioOnDeviceChange:any
	pass


class projectionTOP(TOP,OP):
	pass


class projectSOP(OP,SOP):
	pass


class pulseCHOP(CHOP,OP):
	chanIndex:any
	pass


class Quaternion():
	x:any
	y:any
	z:any
	w:any
	pass


class railsSOP(OP,SOP):
	pass


class rampTOP(TOP,OP):
	pass


class raySOP(OP,SOP):
	pass


class realsenseCHOP(CHOP,OP):
	pass


class realsenseTOP(TOP,OP):
	pass


class recordCHOP(CHOP,OP):
	pass


class rectangleSOP(OP,SOP):
	pass


class rectangleTOP(TOP,OP):
	pass


class refineSOP(OP,SOP):
	pass


class remapTOP(TOP,OP):
	pass


class renameCHOP(CHOP,OP):
	pass


class renderpassTOP(TOP,OP):
	pass


class renderpickCHOP(CHOP,OP):
	pickedSOP:any
	pass


class renderselectTOP(TOP,OP):
	pass


class renderTOP(TOP,OP):
	pass


class reorderCHOP(CHOP,OP):
	pass


class reorderDAT(DAT,OP):
	pass


class reorderTOP(TOP,OP):
	pass


class replaceCHOP(CHOP,OP):
	pass


class replicatorCOMP(COMP,OP):
	curItem:any
	pass


class resampleCHOP(CHOP,OP):
	pass


class resampleSOP(OP,SOP):
	pass


class resolutionTOP(TOP,OP):
	pass


class revolveSOP(OP,SOP):
	pass


class rgbkeyTOP(TOP,OP):
	pass


class rgbtohsvTOP(TOP,OP):
	pass


class Run():
	active:any
	group:any
	isCell:any
	isDAT:any
	isString:any
	path:any
	remainingFrames:any
	remainingMilliseconds:any
	source:any
	pass


class Runs():
	pass


class scalabledisplayTOP(TOP,OP):
	cameraTransform:any
	projection:any
	pass


class scanCHOP(CHOP,OP):
	pass


class screengrabTOP(TOP,OP):
	pass


class screenTOP(TOP,OP):
	pass


class scriptCHOP(CHOP,OP):
	timeSliceDefault:any
	pass


class scriptDAT(DAT,OP):
	pass


class scriptSOP(OP,SOP):
	pass


class scurveCHOP(CHOP,OP):
	chanIndex:any
	pass


class Segment():
	beginFrames:any
	beginSamples:any
	beginSeconds:any
	custom:any
	cycle:any
	cycleEndAlertFrames:any
	cycleEndAlertSamples:any
	cycleEndAlertSeconds:any
	cycleLimit:any
	delayFrames:any
	delaySamples:any
	delaySeconds:any
	lengthFrames:any
	lengthSamples:any
	lengthSeconds:any
	maxCycles:any
	owner:any
	row:any
	speed:any
	index:any
	pass


class selectCHOP(CHOP,OP):
	pass


class selectCOMP(COMP,PanelCOMP,OP):
	pass


class selectDAT(DAT,OP):
	inputCell:any
	inputCol:any
	inputRow:any
	inputTable:any
	pass


class selectMAT(OP,MAT):
	pass


class selectSOP(OP,SOP):
	pass


class selectTOP(TOP,OP):
	pass


class Sequence():
	owner:any
	numBlocks:any
	maxBlocks:any
	blocks:any
	pass


class sequenceblendSOP(OP,SOP):
	pass


class sequencerCHOP(CHOP,OP):
	pass


class serialCHOP(CHOP,OP):
	pass


class serialDAT(DAT,OP):
	pass


class sharedmeminCHOP(CHOP,OP):
	pass


class sharedmeminCOMP(COMP,ObjectCOMP,OP):
	pass


class sharedmeminTOP(TOP,OP):
	pass


class sharedmemoutCHOP(CHOP,OP):
	pass


class sharedmemoutCOMP(COMP,ObjectCOMP,OP):
	pass


class sharedmemoutTOP(TOP,OP):
	pass


class shiftCHOP(CHOP,OP):
	chanIndex:any
	pass


class shuffleCHOP(CHOP,OP):
	pass


class skinSOP(OP,SOP):
	pass


class sliderCOMP(COMP,PanelCOMP,OP):
	pass


class slopeCHOP(CHOP,OP):
	pass


class slopeTOP(TOP,OP):
	pass


class SOP(OP):
	compare:any
	template:any
	points:any
	prims:any
	numPoints:any
	numVertices:any
	numPrims:any
	pointAttribs:any
	primAttribs:any
	vertexAttribs:any
	pointGroups:any
	primGroups:any
	center:any
	min:any
	max:any
	size:any
	isSOP:any
	pass


class soptoCHOP(CHOP,OP):
	pass


class soptoDAT(DAT,OP):
	pass


class sortCHOP(CHOP,OP):
	pass


class sortDAT(DAT,OP):
	pass


class sortSOP(OP,SOP):
	pass


class speedCHOP(CHOP,OP):
	chanIndex:any
	pass


class sphereSOP(OP,SOP):
	pass


class spliceCHOP(CHOP,OP):
	pass


class springCHOP(CHOP,OP):
	chanIndex:any
	pass


class springSOP(OP,SOP):
	pass


class spriteSOP(OP,SOP):
	pass


class ssaoTOP(TOP,OP):
	pass


class stitchSOP(OP,SOP):
	pass


class stretchCHOP(CHOP,OP):
	chanIndex:any
	pass


class subdivideSOP(OP,SOP):
	pass


class substanceselectTOP(TOP,OP):
	pass


class substanceTOP(TOP,OP):
	pass


class substituteDAT(DAT,OP):
	inputCell:any
	inputCol:any
	inputRow:any
	inputTable:any
	pass


class subtractTOP(TOP,OP):
	pass


class superquadSOP(OP,SOP):
	pass


class surfsectSOP(OP,SOP):
	pass


class svgTOP(TOP,OP):
	pass


class sweepSOP(OP,SOP):
	inputVertex:any
	pass


class switchCHOP(CHOP,OP):
	pass


class switchDAT(DAT,OP):
	pass


class switchMAT(OP,MAT):
	pass


class switchSOP(OP,SOP):
	pass


class switchTOP(TOP,OP):
	pass


class syncinCHOP(CHOP,OP):
	timecode:any
	pass


class syncoutCHOP(CHOP,OP):
	pass


class syphonspoutinTOP(TOP,OP):
	pass


class syphonspoutoutTOP(TOP,OP):
	pass


class SysInfo():
	numCPUs:any
	ram:any
	numMonitors:any
	xres:any
	yres:any
	tfs:any
	MIDIInputs:any
	MIDIOutputs:any
	pass


class tableCOMP(COMP,PanelCOMP,OP):
	pass


class tableDAT(DAT,OP):
	subRow:any
	subCol:any
	fillName:any
	pass


class tabletCHOP(CHOP,OP):
	pass


class tcpipDAT(DAT,OP):
	pass


class td():
	me:any
	absTime:any
	app:any
	ext:any
	families:any
	licenses:any
	mod:any
	monitors:any
	op:any
	parent:any
	iop:any
	ipar:any
	project:any
	root:any
	runs:any
	sysinfo:any
	ui:any
	pass


class tdu():
	fileTypes:any
	Matrix:any
	Position:any
	Vector:any
	Quaternion:any
	Color:any
	Dependency:any
	FileInfo:any
	ArcBall:any
	Camera:any
	debug:any
	pass


class textDAT(DAT,OP):
	pass


class TextLine():
	glyph:any
	fontIndex:any
	text:any
	origin:any
	lineWidth:any
	pass


class Textport():
	pass


class textSOP(OP,SOP):
	numLines:any
	ascender:any
	descender:any
	capHeight:any
	xHeight:any
	lineGap:any
	numGlyphs:any
	pass


class textTOP(TOP,OP):
	curText:any
	cursorEnd:any
	cursorStart:any
	fontDescender:any
	selectedText:any
	textHeight:any
	textWidth:any
	numLines:any
	ascender:any
	descender:any
	capHeight:any
	xHeight:any
	lineGap:any
	pass


class texture3dTOP(TOP,OP):
	pass


class textureSOP(OP,SOP):
	pass


class thresholdTOP(TOP,OP):
	pass


class tileTOP(TOP,OP):
	pass


class tdu.Timecode():
	countdown:any
	dropFrame:any
	fps:any
	frame:any
	hour:any
	minute:any
	second:any
	negative:any
	smpte:any
	text:any
	totalFrames:any
	totalSeconds:any
	pass


class timeCOMP(COMP,OP):
	frame:any
	seconds:any
	rate:any
	play:any
	timecode:any
	start:any
	end:any
	rangeStart:any
	rangeEnd:any
	loop:any
	independent:any
	tempo:any
	signature1:any
	signature2:any
	pass


class timelineCHOP(CHOP,OP):
	timecode:any
	pass


class timemachineTOP(TOP,OP):
	pass


class timerCHOP(CHOP,OP):
	beginFrame:any
	beginSample:any
	beginSeconds:any
	cumulativeFrames:any
	cumulativeSample:any
	cumulativeSamples:any
	cumulativeSeconds:any
	cumulativeTimecode:any
	masterFrames:any
	masterFrame:any
	masterSamples:any
	masterSample:any
	masterSeconds:any
	masterFraction:any
	masterTimecode:any
	cycle:any
	fraction:any
	playingFrames:any
	playingSample:any
	playingSamples:any
	playingSeconds:any
	playingTimecode:any
	runningFraction:any
	runningFrames:any
	runningFrame:any
	runningSamples:any
	runningSample:any
	runningSeconds:any
	runningTimecode:any
	runningLengthFrames:any
	runningLengthSamples:any
	runningLengthSeconds:any
	runningLengthTimecode:any
	segment:any
	segments:any
	timecode:any
	pass


class timesliceCHOP(CHOP,OP):
	pass


class TOP(OP):
	width:any
	height:any
	aspect:any
	aspectWidth:any
	aspectHeight:any
	depth:any
	gpuMemory:any
	curPass:any
	isTOP:any
	pass


class toptoCHOP(CHOP,OP):
	pass


class torusSOP(OP,SOP):
	pass


class touchinCHOP(CHOP,OP):
	pass


class touchinDAT(DAT,OP):
	pass


class touchinTOP(TOP,OP):
	pass


class touchoutCHOP(CHOP,OP):
	pass


class touchoutDAT(DAT,OP):
	pass


class touchoutTOP(TOP,OP):
	pass


class traceSOP(OP,SOP):
	pass


class trailCHOP(CHOP,OP):
	pass


class trailSOP(OP,SOP):
	pass


class transformCHOP(CHOP,OP):
	pass


class transformSOP(OP,SOP):
	pass


class transformTOP(TOP,OP):
	pass


class transposeDAT(DAT,OP):
	pass


class triggerCHOP(CHOP,OP):
	chanIndex:any
	pass


class trimCHOP(CHOP,OP):
	pass


class trimSOP(OP,SOP):
	pass


class tristripSOP(OP,SOP):
	pass


class tubeSOP(OP,SOP):
	pass


class tuioinDAT(DAT,OP):
	pass


class twistSOP(OP,SOP):
	pass


class udpinDAT(DAT,OP):
	pass


class udpoutDAT(DAT,OP):
	pass


class udtinDAT(DAT,OP):
	pass


class udtoutDAT(DAT,OP):
	pass


class UI():
	clipboard:any
	colors:any
	dpiBiCubicFilter:any
	masterVolume:any
	options:any
	panes:any
	performMode:any
	preferences:any
	redrawMainWindow:any
	rolloverOp:any
	rolloverPar:any
	rolloverPanel:any
	lastChopChannelSelected:any
	showPaletteBrowser:any
	status:any
	undo:any
	windowWidth:any
	windowHeight:any
	windowX:any
	windowY:any
	pass


class underTOP(TOP,OP):
	pass


class Undo():
	globalState:any
	redoStack:any
	state:any
	undoStack:any
	pass


class Vector():
	x:any
	y:any
	z:any
	pass


class Vertex():
	index:any
	owner:any
	point:any
	prim:any
	pass


class vertexSOP(OP,SOP):
	inputColor:any
	inputColor2:any
	inputNormal:any
	inputNormal2:any
	inputTexture:any
	inputTexture2:any
	inputVertex:any
	inputVertex2:any
	pass


class VFS():
	owner:any
	pass


class VFSFile():
	name:any
	size:any
	date:any
	virtualPath:any
	originalFilePath:any
	owner:any
	byteArray:any
	pass


class videodeviceinTOP(TOP,OP):
	isConnected:any
	inputSignalFormat:any
	timecode:any
	pass


class videodeviceoutTOP(TOP,OP):
	pass


class videostreaminTOP(TOP,OP):
	connectionsFailed:any
	connectionsLost:any
	frameTime:any
	isConnected:any
	isConnecting:any
	isOddField:any
	videoHeight:any
	videoWidth:any
	pass


class videostreamoutTOP(TOP,OP):
	streamURL:any
	pass


class viosoTOP(TOP,OP):
	pass


class warpCHOP(CHOP,OP):
	pass


class waveCHOP(CHOP,OP):
	chanIndex:any
	sampleIndex:any
	pass


class webDAT(DAT,OP):
	downloadCurrent:any
	downloadFraction:any
	downloadTotal:any
	queryContentEncoding:any
	queryContentLength:any
	queryContentType:any
	queryContentTypeCharset:any
	pass


class webrenderTOP(TOP,OP):
	loaded:any
	pass


class websocketDAT(DAT,OP):
	pass


class windowCOMP(COMP,OP):
	scalingMonitorIndex:any
	isBorders:any
	isFill:any
	isOpen:any
	width:any
	height:any
	x:any
	y:any
	contentX:any
	contentY:any
	contentWidth:any
	contentHeight:any
	pass


class wireframeMAT(OP,MAT):
	pass


class wireframeSOP(OP,SOP):
	pass


class xmlDAT(DAT,OP):
	pass


class zedCHOP(CHOP,OP):
	pass


class zedSOP(OP,SOP):
	pass


class zedTOP(TOP,OP):
	pass



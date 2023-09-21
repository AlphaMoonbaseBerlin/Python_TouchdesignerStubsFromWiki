class actorCOMP():
	"""actorCOMP"""
	kinstate : Par
	"""Menu : The kinematic state defines the Actor COMPs ability to move from external forces. If an object is dynamic, then it is moveable in the simulation, but if it static then it is not."""
	shape : Par
	"""Menu : The type of collision shape to make from the selected SOPs. Collision shapes can be viewed using a guide in the Actor COMP's viewer"""
	linvelx : Par
	"""The initial linear velocity of the actor in m/s. This parameter can also be used to modify an actor's linear velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters."""
	linvely : Par
	"""The initial linear velocity of the actor in m/s. This parameter can also be used to modify an actor's linear velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters."""
	linvelz : Par
	"""The initial linear velocity of the actor in m/s. This parameter can also be used to modify an actor's linear velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters."""
	angvelx : Par
	"""The initial angular velocity of the actor in degrees per second in m/s. This parameter can also be used to modify the actor's angular velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters."""
	angvely : Par
	"""The initial angular velocity of the actor in degrees per second in m/s. This parameter can also be used to modify the actor's angular velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters."""
	angvelz : Par
	"""The initial angular velocity of the actor in degrees per second in m/s. This parameter can also be used to modify the actor's angular velocity during a simulation. Additionally, it is used in conjunction with the "Cue Velocity" and "Cue Velocity Pulse" parameters."""
	gravityx : Par
	"""Actor's local gravity in m/s^2. Will only be applied if the actor is not using the Bullet Solver COMP's global gravity ie. the "Use Global Gravity" parameter above is turned off."""
	gravityy : Par
	"""Actor's local gravity in m/s^2. Will only be applied if the actor is not using the Bullet Solver COMP's global gravity ie. the "Use Global Gravity" parameter above is turned off."""
	gravityz : Par
	"""Actor's local gravity in m/s^2. Will only be applied if the actor is not using the Bullet Solver COMP's global gravity ie. the "Use Global Gravity" parameter above is turned off."""
	comx : Par
	"""Specifies the center of mass of the collision shape. The center of mass is the point around which the body will rotate. Center of mass can be viewed using a guide in the Actor COMP's viewer. It is shown as a red axis."""
	comy : Par
	"""Specifies the center of mass of the collision shape. The center of mass is the point around which the body will rotate. Center of mass can be viewed using a guide in the Actor COMP's viewer. It is shown as a red axis."""
	comz : Par
	"""Specifies the center of mass of the collision shape. The center of mass is the point around which the body will rotate. Center of mass can be viewed using a guide in the Actor COMP's viewer. It is shown as a red axis."""
	flextype : Par
	"""Menu : The type of dynamic Flex actor."""
	emitsizex : Par
	"""The size of the 2D emission grid. The size represents the number of particles on each side of the emission grid. For example, a 2x5 emission size will emit a grid 2 particles wide and 5 particles high."""
	emitsizey : Par
	"""The size of the 2D emission grid. The size represents the number of particles on each side of the emission grid. For example, a 2x5 emission size will emit a grid 2 particles wide and 5 particles high."""
	par : parameter.actorCOMP
	"""Parameters of parameter.actorCOMP"""
	pass


class ambientlightCOMP():
	"""ambientlightCOMP"""
	cr : Par
	"""You can modify the color of the light three ways: <span class="tipTextCOMP">Color List</span>, <span class="tipTextCOMP">Hue</span>, <span class="tipTextCOMP">Saturation</span>, and <span class="tipTextCOMP">Value</span>, or <span class="tipTextCOMP">Red</span>, <span class="tipTextCOMP">Green</span>, and <span class="tipTextCOMP">Blue</span>. To choose one, click on the appropriate box and the color editing fields below change accordingly."""
	cg : Par
	"""You can modify the color of the light three ways: <span class="tipTextCOMP">Color List</span>, <span class="tipTextCOMP">Hue</span>, <span class="tipTextCOMP">Saturation</span>, and <span class="tipTextCOMP">Value</span>, or <span class="tipTextCOMP">Red</span>, <span class="tipTextCOMP">Green</span>, and <span class="tipTextCOMP">Blue</span>. To choose one, click on the appropriate box and the color editing fields below change accordingly."""
	cb : Par
	"""You can modify the color of the light three ways: <span class="tipTextCOMP">Color List</span>, <span class="tipTextCOMP">Hue</span>, <span class="tipTextCOMP">Saturation</span>, and <span class="tipTextCOMP">Value</span>, or <span class="tipTextCOMP">Red</span>, <span class="tipTextCOMP">Green</span>, and <span class="tipTextCOMP">Blue</span>. To choose one, click on the appropriate box and the color editing fields below change accordingly."""
	par : parameter.ambientlightCOMP
	"""Parameters of parameter.ambientlightCOMP"""
	pass


class animationCOMP():
	"""animationCOMP"""
	playmode : Par
	"""Menu : Specifies the method used to playback the animation or allows the output the entire animation curve."""
	inputindexunit : Par
	"""Menu : When <span class="tipTextCOMP">Play Mode</span> is set to '''Use Input Index''' use this menu to choose the units for the index input channel. For example, choose between setting the index with frames or seconds. The Units X option sets the index to use the key information directly from the key DAT table inside the Animation COMP, disregarding any custom settings found in the attributes DAT table."""
	cyclic : Par
	"""Menu : Adapts the range of the animation for cyclic or non-cyclic input indices. When using a cyclic input index the lookup value for index 0.0 and 1.0 result in the same value. To avoid this, set Cyclic Range to Yes and the lookup will cycle smoothly."""
	rangetype : Par
	"""Menu : Set the working range for the Animation COMP."""
	tleft : Par
	"""Menu : Determines the output of the channels when past the 'End' position. Does not affect Play Mode = Output Full Range, to manipulate the [[Extend Conditions]] of that mode adjust the Extend parameters of the [[Keyframe CHOP]] inside the Animation COMP."""
	tright : Par
	"""Menu : Determines the output of the channels when before the 'Start' position. Does not affect Play Mode = Output Full Range, to manipulate the [[Extend Conditions]] of that mode adjust the Extend parameters of the [[Keyframe CHOP]] inside the Animation COMP."""
	par : parameter.animationCOMP
	"""Parameters of parameter.animationCOMP"""
	pass


class annotateCOMP():
	"""annotateCOMP"""
	Mode : Par
	"""Menu : Switch between Comment, Network Box, and Annotate Modes"""
	Titlealign : Par
	"""Menu : Alignment of title text"""
	Mode : Par
	"""Menu : Switch between Comment, Network Box, and Annotate modes. See also [[Network_Utilities:_Comments,_Network_Boxes,_Annotates]]."""
	Backcolorr : Par
	"""Background color"""
	Backcolorg : Par
	"""Background color"""
	Backcolorb : Par
	"""Background color"""
	Opvieweroversize : Par
	"""Menu : Use the Size/Aspect Override to control viewer's size in the background."""
	Opviewersizew : Par
	"""Diplay viewer as-if it were being displayed at this resolution. This is particularly useful for zooming into operators that don't have a built-in resolution, like CHOPs, SOPs, and DATs."""
	Opviewersizeh : Par
	"""Diplay viewer as-if it were being displayed at this resolution. This is particularly useful for zooming into operators that don't have a built-in resolution, like CHOPs, SOPs, and DATs."""
	Opvieweroffsetx : Par
	"""Offsets the displayed area within the viewer. Combined with OP Viewer Zoom, this lets you display a specific area of a viewer, such as a CHOP channel or table cell."""
	Opvieweroffsety : Par
	"""Offsets the displayed area within the viewer. Combined with OP Viewer Zoom, this lets you display a specific area of a viewer, such as a CHOP channel or table cell."""
	layerzone : Par
	"""Menu : Where this annotateCOMP is layered with regards to other items in the network."""
	par : parameter.annotateCOMP
	"""Parameters of parameter.annotateCOMP"""
	pass


class baseCOMP():
	"""baseCOMP"""
	par : parameter.baseCOMP
	"""Parameters of parameter.baseCOMP"""
	pass


class blendCOMP():
	"""blendCOMP"""
	parenttype : Par
	"""Menu : Method in which parent transforms (i.e. Translate, Rotate, Scale) are combined to produce a unique blended transform."""
	par : parameter.blendCOMP
	"""Parameters of parameter.blendCOMP"""
	pass


class boneCOMP():
	"""boneCOMP"""
	restanglesx : Par
	"""Defines the relative weighting of rotations about Rx, Ry, Rz, the bone's x,y,z axis for the Inverse Kinematics solver."""
	restanglesy : Par
	"""Defines the relative weighting of rotations about Rx, Ry, Rz, the bone's x,y,z axis for the Inverse Kinematics solver."""
	restanglesz : Par
	"""Defines the relative weighting of rotations about Rx, Ry, Rz, the bone's x,y,z axis for the Inverse Kinematics solver."""
	xrange : Par
	"""Float : Specifies the maximum and minimum rotation angles."""
	yrange : Par
	"""Float : Specifies the maximum and minimum rotation angles."""
	crcenterx : Par
	"""Position of the center of the region."""
	crcentery : Par
	"""Position of the center of the region."""
	crcenterz : Par
	"""Position of the center of the region."""
	crtopcapx : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	crtopcapy : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	crtopcapz : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	crbotcapx : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	crbotcapy : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	crbotcapz : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	par : parameter.boneCOMP
	"""Parameters of parameter.boneCOMP"""
	pass


class bulletsolverCOMP():
	"""bulletsolverCOMP"""
	gravityx : Par
	"""Gravity applied to all actors in the simulation in m/s^2. Gravity is applied to actors irrespective of their mass."""
	gravityy : Par
	"""Gravity applied to all actors in the simulation in m/s^2. Gravity is applied to actors irrespective of their mass."""
	gravityz : Par
	"""Gravity applied to all actors in the simulation in m/s^2. Gravity is applied to actors irrespective of their mass."""
	dimension : Par
	"""dropmenu : The dimension of the simulation. The options in this menu can also be recreated using the linear/angular multiplier parameters."""
	linmultx : Par
	"""A multiplier for the linear velocities of the actors in the simulation. For example, if linmult is (0, 1, 1) then the actors can move linearly at normal speed on the Y and Z axes but cannot move in the X direction. These values are multiplied internally by the values from dimension. For example, if the dimension is 2D and linmult is (0, 1, 1) then the only direction the actors can move is along the Y axis because 2D is constraining on the Z and this parameter is constraining on the Y."""
	linmulty : Par
	"""A multiplier for the linear velocities of the actors in the simulation. For example, if linmult is (0, 1, 1) then the actors can move linearly at normal speed on the Y and Z axes but cannot move in the X direction. These values are multiplied internally by the values from dimension. For example, if the dimension is 2D and linmult is (0, 1, 1) then the only direction the actors can move is along the Y axis because 2D is constraining on the Z and this parameter is constraining on the Y."""
	linmultz : Par
	"""A multiplier for the linear velocities of the actors in the simulation. For example, if linmult is (0, 1, 1) then the actors can move linearly at normal speed on the Y and Z axes but cannot move in the X direction. These values are multiplied internally by the values from dimension. For example, if the dimension is 2D and linmult is (0, 1, 1) then the only direction the actors can move is along the Y axis because 2D is constraining on the Z and this parameter is constraining on the Y."""
	angmultx : Par
	"""A multiplier for the angular velocities of the actors in the simulation. For example, if angmult is (1, 0, 0) then the actors can only rotate on the X axes. These values are multiplied internally by the values from dimension. So, if dimension is 2D and angmult is (1, 0, 0) then the actor will not be able to rotate in any direction because 2D constrains rotation only to the Z axis, and this parameter is constraining it only to the X axis."""
	angmulty : Par
	"""A multiplier for the angular velocities of the actors in the simulation. For example, if angmult is (1, 0, 0) then the actors can only rotate on the X axes. These values are multiplied internally by the values from dimension. So, if dimension is 2D and angmult is (1, 0, 0) then the actor will not be able to rotate in any direction because 2D constrains rotation only to the Z axis, and this parameter is constraining it only to the X axis."""
	angmultz : Par
	"""A multiplier for the angular velocities of the actors in the simulation. For example, if angmult is (1, 0, 0) then the actors can only rotate on the X axes. These values are multiplied internally by the values from dimension. So, if dimension is 2D and angmult is (1, 0, 0) then the actor will not be able to rotate in any direction because 2D constrains rotation only to the Z axis, and this parameter is constraining it only to the X axis."""
	par : parameter.bulletsolverCOMP
	"""Parameters of parameter.bulletsolverCOMP"""
	pass


class buttonCOMP():
	"""buttonCOMP"""
	buttontype : Par
	"""Menu : This menu determines the button's state behavior."""
	par : parameter.buttonCOMP
	"""Parameters of parameter.buttonCOMP"""
	pass


class camerablendCOMP():
	"""camerablendCOMP"""
	parenttype : Par
	"""Menu : Method in which parent transforms (i.e. Translate, Rotate, Scale) are combined to produce a unique blended transform."""
	projection : Par
	"""Menu : A pop-up menu lets you choose from <span class="tipTextCOMP">Perspective</span> and <span class="tipTextCOMP">Orthographic</span> projection types. A third option <span class="tipTextCOMP">Perpective to Ortho Blend</span> enables the <span class="tipTextCOMP">Projection Blend</span> parameter below which can be used to blend between perspectives."""
	viewanglemethod : Par
	"""Menu : """
	winx : Par
	"""These parameters define the center of the window during the rendering process. The window parameter takes the view and expands it to fit the camera's field of vision. It is important to note that this action is independent of perspective. In other words, it acts as though you are panning the camera without actually moving the camera."""
	winy : Par
	"""These parameters define the center of the window during the rendering process. The window parameter takes the view and expands it to fit the camera's field of vision. It is important to note that this action is independent of perspective. In other words, it acts as though you are panning the camera without actually moving the camera."""
	bgcolorr : Par
	"""Sets the background color and alpha of the camera's view."""
	bgcolorg : Par
	"""Sets the background color and alpha of the camera's view."""
	bgcolorb : Par
	"""Sets the background color and alpha of the camera's view."""
	bgcolora : Par
	"""Sets the background color and alpha of the camera's view."""
	fog : Par
	"""Menu : This menu determines the type of fog rendered in the viewport: <blockquote><span class="tipTextCOMP">'''Linear'''</span> fog uses the following equation: </blockquote>	
			
[[Image:Objects14.gif]]			
			
<blockquote><span class="tipTextCOMP">'''Exponential'''</span> fog uses the following equation:</blockquote>			
			
[[Image:Objects18.gif]]			
			
<blockquote><span class="tipTextCOMP">'''Squared Exponential'''</span> fog uses the following equation: </blockquote>			
			
[[Image:Objects20.gif]]			
			
<blockquote>Regardless of the fog mode, f is clamped to the range [0,1] after it is computed. Then, if GL is in RGBA color mode, the fragment's color Cr is replaced by:</blockquote>			
			
[[Image:Objects19.gif]]"""
	fogcolorr : Par
	"""The color of the fog."""
	fogcolorg : Par
	"""The color of the fog."""
	fogcolorb : Par
	"""The color of the fog."""
	par : parameter.camerablendCOMP
	"""Parameters of parameter.camerablendCOMP"""
	pass


class cameraCOMP():
	"""cameraCOMP"""
	projection : Par
	"""Menu : A pop-up menu lets you choose from Perspective and Orthographic projection types. A third option Perpective to Ortho Blend enables the Projection Blend parameter below which can be used to blend between perspectives. A 4th option Custom Projection Matrix allows you to specify a custom 4x4 projection matrix using a tdu.Matrix, CHOP or a DAT."""
	viewanglemethod : Par
	"""Menu : This menu determines which method is used to define the camera's angle of view."""
	winrollpivot : Par
	"""Menu : """
	winx : Par
	"""These parameters define the center of the window during the rendering process. The window parameter takes the view and expands it to fit the camera's field of vision. It is important to note that this action is independent of perspective. In other words, it acts as though you are panning the camera without actually moving the camera. The units for this parameter are normalized. That is a Window X of -0.5 will move the previous center of the image to the left edge of the render."""
	winy : Par
	"""These parameters define the center of the window during the rendering process. The window parameter takes the view and expands it to fit the camera's field of vision. It is important to note that this action is independent of perspective. In other words, it acts as though you are panning the camera without actually moving the camera. The units for this parameter are normalized. That is a Window X of -0.5 will move the previous center of the image to the left edge of the render."""
	quadreprojpts1 : Par
	"""Specifies 4 point indices in the SOP referenced by Quad Reproject SOP that make up the quad that determines the region to be reprojected. The indices should be listed in bottom left, bottom right, top left, top right order, as viewed from the camera. The SOP that is referenced should be in the COMP that is being rendered, so the world transform that will be applied to is can be taken into account."""
	quadreprojpts2 : Par
	"""Specifies 4 point indices in the SOP referenced by Quad Reproject SOP that make up the quad that determines the region to be reprojected. The indices should be listed in bottom left, bottom right, top left, top right order, as viewed from the camera. The SOP that is referenced should be in the COMP that is being rendered, so the world transform that will be applied to is can be taken into account."""
	quadreprojpts3 : Par
	"""Specifies 4 point indices in the SOP referenced by Quad Reproject SOP that make up the quad that determines the region to be reprojected. The indices should be listed in bottom left, bottom right, top left, top right order, as viewed from the camera. The SOP that is referenced should be in the COMP that is being rendered, so the world transform that will be applied to is can be taken into account."""
	quadreprojpts4 : Par
	"""Specifies 4 point indices in the SOP referenced by Quad Reproject SOP that make up the quad that determines the region to be reprojected. The indices should be listed in bottom left, bottom right, top left, top right order, as viewed from the camera. The SOP that is referenced should be in the COMP that is being rendered, so the world transform that will be applied to is can be taken into account."""
	bgcolorr : Par
	"""Sets the background color and alpha of the camera's view."""
	bgcolorg : Par
	"""Sets the background color and alpha of the camera's view."""
	bgcolorb : Par
	"""Sets the background color and alpha of the camera's view."""
	bgcolora : Par
	"""Sets the background color and alpha of the camera's view."""
	fog : Par
	"""Menu : This menu determines the type of fog rendered in the viewport: '''Linear''' fog uses the following equation:	
			
[[Image:Objects14.gif]]			
			
'''Exponential''' fog uses the following equation:			
			
[[Image:Objects18.gif]]			
			
'''Squared Exponential''' fog uses the following equation:			
			
[[Image:Objects20.gif]]"""
	fogcolorr : Par
	"""The color of the fog."""
	fogcolorg : Par
	"""The color of the fog."""
	fogcolorb : Par
	"""The color of the fog."""
	par : parameter.cameraCOMP
	"""Parameters of parameter.cameraCOMP"""
	pass


class NotSet():
	"""NotSet"""
	par : parameter.NotSet
	"""Parameters of parameter.NotSet"""
	pass


class constraintCOMP():
	"""constraintCOMP"""
	type : Par
	"""dropmenu : The type of constraint to create: point to point, hinge, or slider."""
	pivot1x : Par
	"""The pivot point for the constraint."""
	pivot1y : Par
	"""The pivot point for the constraint."""
	pivot1z : Par
	"""The pivot point for the constraint."""
	axis1x : Par
	"""The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1."""
	axis1y : Par
	"""The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1."""
	axis1z : Par
	"""The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1."""
	sliderrot1x : Par
	"""The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis."""
	sliderrot1y : Par
	"""The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis."""
	sliderrot1z : Par
	"""The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis."""
	pivot2x : Par
	"""The pivot point for the constraint."""
	pivot2y : Par
	"""The pivot point for the constraint."""
	pivot2z : Par
	"""The pivot point for the constraint."""
	axis2x : Par
	"""The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1."""
	axis2y : Par
	"""The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1."""
	axis2z : Par
	"""The axis around which to create the hinge. Each value is typically a number between 0 and 1. For example, to spin around the Z axis set to 0, 0, 1."""
	sliderrot2x : Par
	"""The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis."""
	sliderrot2y : Par
	"""The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis."""
	sliderrot2z : Par
	"""The rotation of the slider constraint axis. By default the slider constraint is applied on the X axis."""
	par : parameter.constraintCOMP
	"""Parameters of parameter.constraintCOMP"""
	pass


class containerCOMP():
	"""containerCOMP"""
	par : parameter.containerCOMP
	"""Parameters of parameter.containerCOMP"""
	pass


class engineCOMP():
	"""engineCOMP"""
	clock : Par
	"""Menu : Specify the temporal connection to the TouchEngine instance."""
	par : parameter.engineCOMP
	"""Parameters of parameter.engineCOMP"""
	pass


class environmentlightCOMP():
	"""environmentlightCOMP"""
	cr : Par
	"""You can modify the color of the light three ways: Color List, Hue, Saturation, and Value, or Red, Green, and Blue. To choose one, click on the appropriate box and the color editing fields below change accordingly."""
	cg : Par
	"""You can modify the color of the light three ways: Color List, Hue, Saturation, and Value, or Red, Green, and Blue. To choose one, click on the appropriate box and the color editing fields below change accordingly."""
	cb : Par
	"""You can modify the color of the light three ways: Color List, Hue, Saturation, and Value, or Red, Green, and Blue. To choose one, click on the appropriate box and the color editing fields below change accordingly."""
	envlightmaptype2d : Par
	"""Menu : Select the type of environment map to use (only equirectangular available for now)."""
	envlightmaprotatex : Par
	"""Rotate the texture specified by the Environment Map parameter above."""
	envlightmaprotatey : Par
	"""Rotate the texture specified by the Environment Map parameter above."""
	envlightmaprotatez : Par
	"""Rotate the texture specified by the Environment Map parameter above."""
	envlightmapprefilter : Par
	"""Menu : Controls how the environment map is pre-filtered. A pre-filtered environment map is expensive to create, but results in much better rendering quality."""
	par : parameter.environmentlightCOMP
	"""Parameters of parameter.environmentlightCOMP"""
	pass


class fbxCOMP():
	"""fbxCOMP"""
	importmethod : Par
	"""Menu : Determines what to do when clicking the 'Import' button below."""
	sampleratemode : Par
	"""dropmenu : Select between using the 'File FPS' embedded in the FBX file or setting a 'Custom' sample rate."""
	playmode : Par
	"""dropmenu : A menu to specify the method used to play the animation."""
	cuepointunit : Par
	"""nolabel shortvalues dropmenu : Select what type of unit to specify the Cue Point with."""
	indexunit : Par
	"""nolabel shortvalues dropmenu : """
	tstartunit : Par
	"""nolabel shortvalues dropmenu : Specifies a unit type for Trim Start. Changing this will convert the previous unit to the selected unit."""
	tendunit : Par
	"""nolabel shortvalues dropmenu : Specifies a unit type for Trim End. Changing this will convert the previous unit to the selected unit."""
	textendleft : Par
	"""dropmenu : Determines how the animation behaves before the start of the animation (or Trim Start position if it is used)."""
	textendright : Par
	"""dropmenu : Determines how the animation behaves after the end of the animation (or Trim End position if it is used)."""
	par : parameter.fbxCOMP
	"""Parameters of parameter.fbxCOMP"""
	pass


class fieldCOMP():
	"""fieldCOMP"""
	fieldtype : Par
	""" : Specify what kind of data can be input into the field."""
	par : parameter.fieldCOMP
	"""Parameters of parameter.fieldCOMP"""
	pass


class forceCOMP():
	"""forceCOMP"""
	forcex : Par
	"""The linear force in Newtons that will be applied."""
	forcey : Par
	"""The linear force in Newtons that will be applied."""
	forcez : Par
	"""The linear force in Newtons that will be applied."""
	relposx : Par
	"""The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque."""
	relposy : Par
	"""The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque."""
	relposz : Par
	"""The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque."""
	torquex : Par
	"""The rotational force in Newtons that will be applied."""
	torquey : Par
	"""The rotational force in Newtons that will be applied."""
	torquez : Par
	"""The rotational force in Newtons that will be applied."""
	par : parameter.forceCOMP
	"""Parameters of parameter.forceCOMP"""
	pass


class geotextCOMP():
	"""geotextCOMP"""
	mode : Par
	"""Menu : Controls where text is generated from. Either from the 'Text' parameter, or a table DAT provided via the 'Specification DAT' parameter."""
	font : Par
	"""StrMenu : Select the font to be used from the dropdown menu. Available fonts are those that have been registered with the operating system. There may be a delay when selecting fonts that have not been used before as the system creates the necessary intermediate files required for rendering."""
	fontcolorr : Par
	"""The color for the font."""
	fontcolorg : Par
	"""The color for the font."""
	fontcolorb : Par
	"""The color for the font."""
	fontcolorg : Par
	"""The color for the font."""
	fontcolorb : Par
	"""The color for the font."""
	layoutsizew : Par
	"""Text is aligned and word-wrapped within a virtual layout box. This box is what is transformed by the various transform parameters, and then the text is aligned and laid out within that. The width and height units are the same units as the font size."""
	layoutsizeh : Par
	"""Text is aligned and word-wrapped within a virtual layout box. This box is what is transformed by the various transform parameters, and then the text is aligned and laid out within that. The width and height units are the same units as the font size."""
	textpaddingl : Par
	""""""
	textpaddingr : Par
	""""""
	textpaddingb : Par
	""""""
	textpaddingt : Par
	""""""
	alignx : Par
	"""Menu : Controls the horizontal alignment of the text."""
	aligny : Par
	"""Menu : Controls the vertical alignment of the text."""
	alignymode : Par
	"""Menu : Controls how the alignment is calculated for vertical alignment."""
	textpaddingl : Par
	"""Extra padding to add to the sides of the layout box, pushing the text inwards for alignment."""
	textpaddingr : Par
	"""Extra padding to add to the sides of the layout box, pushing the text inwards for alignment."""
	textpaddingb : Par
	"""Extra padding to add to the sides of the layout box, pushing the text inwards for alignment."""
	textpaddingt : Par
	"""Extra padding to add to the sides of the layout box, pushing the text inwards for alignment."""
	par : parameter.geotextCOMP
	"""Parameters of parameter.geotextCOMP"""
	pass


class geometryCOMP():
	"""geometryCOMP"""
	par : parameter.geometryCOMP
	"""Parameters of parameter.geometryCOMP"""
	pass


class glslCOMP():
	"""glslCOMP"""
	top0 : Par
	"""TOP : This is the TOP that will be referenced by the above sampler name above it.
				
'''Exposed by the + Button, texture sampling parameters''':				
				
Refer to the [[Texture Sampling Parameters]] article for more information on the parameters exposed by pressing the + button. The ''parameter'' prefix for each of the parameters is ''top[digit]''."""
	top0extendu : Par
	"""Menu : """
	top0extendv : Par
	"""Menu : """
	top0extendw : Par
	"""Menu : """
	top0filter : Par
	"""Menu : """
	top0anisotropy : Par
	"""Menu : """
	value0x : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	value0y : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	value0z : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	value0w : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	par : parameter.glslCOMP
	"""Parameters of parameter.glslCOMP"""
	pass


class handleCOMP():
	"""handleCOMP"""
	tx : Par
	"""Displacement tx,ty,tz relative to the origin of the bone where the handle is anchored."""
	ty : Par
	"""Displacement tx,ty,tz relative to the origin of the bone where the handle is anchored."""
	tz : Par
	"""Displacement tx,ty,tz relative to the origin of the bone where the handle is anchored."""
	lrxmin : Par
	"""Set the minimum and maximum rotation range in X axis."""
	lrxmax : Par
	"""Set the minimum and maximum rotation range in X axis."""
	lrymin : Par
	"""Set the minimum and maximum rotation range in Y axis."""
	lrymax : Par
	"""Set the minimum and maximum rotation range in Y axis."""
	lrzmin : Par
	"""Set the minimum and maximum rotation range in Z axis."""
	lrzmax : Par
	"""Set the minimum and maximum rotation range in Z axis."""
	par : parameter.handleCOMP
	"""Parameters of parameter.handleCOMP"""
	pass


class impulseforceCOMP():
	"""impulseforceCOMP"""
	forcex : Par
	"""The linear force in Newtons to be applied when the node is pulsed."""
	forcey : Par
	"""The linear force in Newtons to be applied when the node is pulsed."""
	forcez : Par
	"""The linear force in Newtons to be applied when the node is pulsed."""
	relposx : Par
	"""The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque."""
	relposy : Par
	"""The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque."""
	relposz : Par
	"""The position at which to apply the linear force, relative to the center of the body (Note: the physical center of the object, not the center of mass). Having a nonzero relative position will also cause the body to rotate due to added torque."""
	torquex : Par
	"""The rotational force in Newtons that will be applied."""
	torquey : Par
	"""The rotational force in Newtons that will be applied."""
	torquez : Par
	"""The rotational force in Newtons that will be applied."""
	par : parameter.impulseforceCOMP
	"""Parameters of parameter.impulseforceCOMP"""
	pass


class lightCOMP():
	"""lightCOMP"""
	cr : Par
	"""You can modify the color of a light here by adjusting the red, green, and blue parameters.  Alternatively, clicking on the color swatch will open a dialog with HSV and/or RGB sliders allowing interactive color picking with a preview of the selected color."""
	cg : Par
	"""You can modify the color of a light here by adjusting the red, green, and blue parameters.  Alternatively, clicking on the color swatch will open a dialog with HSV and/or RGB sliders allowing interactive color picking with a preview of the selected color."""
	cb : Par
	"""You can modify the color of a light here by adjusting the red, green, and blue parameters.  Alternatively, clicking on the color swatch will open a dialog with HSV and/or RGB sliders allowing interactive color picking with a preview of the selected color."""
	lighttype : Par
	"""Menu : Specifies the type of light."""
	projmaptype : Par
	"""Menu : """
	projmap : Par
	"""TOP : The path to a [[TOP]] used for the light's projector map."""
	projmapextendu : Par
	"""Menu : Sets the extend conditions for the Projector Map texture."""
	projmapextendv : Par
	"""Menu : Sets the extend conditions for the Projector Map texture."""
	projmapextendw : Par
	"""Menu : Sets the extend conditions for the Projector Map texture."""
	projmapfilter : Par
	"""Menu : """
	projmapanisotropy : Par
	"""Menu : """
	projmapmode : Par
	"""Menu : Specify how the projection map is applied"""
	frontfacelit : Par
	"""Menu : Controls how the polygon's normal is used to light the front face of the polygon. For more information refer to the [[Two-Sided Lighting]] article."""
	backfacelit : Par
	"""Menu : Controls how the polygon's normal is used to light the back face of the polygon. For more information refer to the [[Two-Sided Lighting]] article."""
	shadowtype : Par
	"""Menu : Sets the type of shadows cast by the light."""
	lightsize1 : Par
	"""Controls the size of the source light when using Soft or Custom shadows."""
	lightsize2 : Par
	"""Controls the size of the source light when using Soft or Custom shadows."""
	shadowresolution1 : Par
	"""The resolution of the shadow's texture map used for the calculation."""
	shadowresolution2 : Par
	"""The resolution of the shadow's texture map used for the calculation."""
	projection : Par
	"""Menu : A pop-up menu lets you choose the projection type."""
	viewanglemethod : Par
	"""Menu : This menu determines which method is used to define the camera's angle of view."""
	bgcolorr : Par
	"""Set the background color of the view when using the light as a camera."""
	bgcolorg : Par
	"""Set the background color of the view when using the light as a camera."""
	bgcolorb : Par
	"""Set the background color of the view when using the light as a camera."""
	bgcolora : Par
	"""Set the background color of the view when using the light as a camera."""
	par : parameter.lightCOMP
	"""Parameters of parameter.lightCOMP"""
	pass


class listCOMP():
	"""listCOMP"""
	par : parameter.listCOMP
	"""Parameters of parameter.listCOMP"""
	pass


class flexsolverCOMP():
	"""flexsolverCOMP"""
	gravityx : Par
	"""Gravity applied to all actors in the simulation in m/s^2. Gravity is applied to actors irrespective of their mass."""
	gravityy : Par
	"""Gravity applied to all actors in the simulation in m/s^2. Gravity is applied to actors irrespective of their mass."""
	gravityz : Par
	"""Gravity applied to all actors in the simulation in m/s^2. Gravity is applied to actors irrespective of their mass."""
	boundmode : Par
	"""Menu : """
	planer0x : Par
	"""Rotate the default plane. Default plane is a +Z XY plane (same as Grid SOP)."""
	planer0y : Par
	"""Rotate the default plane. Default plane is a +Z XY plane (same as Grid SOP)."""
	planer0z : Par
	"""Rotate the default plane. Default plane is a +Z XY plane (same as Grid SOP)."""
	planet0x : Par
	"""Translate the default plane. Default plane is a +Z XY plane (same as Grid SOP)."""
	planet0y : Par
	"""Translate the default plane. Default plane is a +Z XY plane (same as Grid SOP)."""
	planet0z : Par
	"""Translate the default plane. Default plane is a +Z XY plane (same as Grid SOP)."""
	par : parameter.flexsolverCOMP
	"""Parameters of parameter.flexsolverCOMP"""
	pass


class flowEmitterCOMP():
	"""flowEmitterCOMP"""
	mode : Par
	"""dropmenu : Select Emitter or Collider mode."""
	type : Par
	"""dropmenu : Select the shape type used for the emitter."""
	sizex : Par
	"""Controls the dimensions of the emitter when using Box or Shape TOP types."""
	sizey : Par
	"""Controls the dimensions of the emitter when using Box or Shape TOP types."""
	sizez : Par
	"""Controls the dimensions of the emitter when using Box or Shape TOP types."""
	centerofmassx : Par
	"""Specifies the center of mass of the emitter."""
	centerofmassy : Par
	"""Specifies the center of mass of the emitter."""
	centerofmassz : Par
	"""Specifies the center of mass of the emitter."""
	linearvelx : Par
	"""Target linear velocity of the fuel added to the system."""
	linearvely : Par
	"""Target linear velocity of the fuel added to the system."""
	linearvelz : Par
	"""Target linear velocity of the fuel added to the system."""
	angularvelx : Par
	"""Target angular velocity of the fuel added to the system. Think of this as 'rotational velocity."""
	angularvely : Par
	"""Target angular velocity of the fuel added to the system. Think of this as 'rotational velocity."""
	angularvelz : Par
	"""Target angular velocity of the fuel added to the system. Think of this as 'rotational velocity."""
	velcorratex : Par
	"""Rate at which the the system gets to the target velocity. Each simulation block has its own velocity level, the emitter tries to change any blocks it overlaps with to match its emitter value. The correction rate is how strongly it tries to change the value to this target value, for example if 0 the emiitter won't do anything, when a small value like 0-1 the emitter will gently influence the simulation, when a high value like 10-100 it will force the value."""
	velcorratey : Par
	"""Rate at which the the system gets to the target velocity. Each simulation block has its own velocity level, the emitter tries to change any blocks it overlaps with to match its emitter value. The correction rate is how strongly it tries to change the value to this target value, for example if 0 the emiitter won't do anything, when a small value like 0-1 the emitter will gently influence the simulation, when a high value like 10-100 it will force the value."""
	velcorratez : Par
	"""Rate at which the the system gets to the target velocity. Each simulation block has its own velocity level, the emitter tries to change any blocks it overlaps with to match its emitter value. The correction rate is how strongly it tries to change the value to this target value, for example if 0 the emiitter won't do anything, when a small value like 0-1 the emitter will gently influence the simulation, when a high value like 10-100 it will force the value."""
	colorr : Par
	"""The base color of the combustion."""
	colorg : Par
	"""The base color of the combustion."""
	colorb : Par
	"""The base color of the combustion."""
	colora : Par
	"""The base color of the combustion."""
	par : parameter.flowEmitterCOMP
	"""Parameters of parameter.flowEmitterCOMP"""
	pass


class opviewerCOMP():
	"""opviewerCOMP"""
	opcenterx : Par
	"""Lets you pan across the target operator's viewer when the Scale is > 1. Center adjusts what part of the target operator's viewer is in the middle of the OP Viewer."""
	opcentery : Par
	"""Lets you pan across the target operator's viewer when the Scale is > 1. Center adjusts what part of the target operator's viewer is in the middle of the OP Viewer."""
	opcenterunit : Par
	"""Menu : Center can be expressed in panel units or fraction of width, or display points."""
	par : parameter.opviewerCOMP
	"""Parameters of parameter.opviewerCOMP"""
	pass


class Pallette:depthProjection Ext():
	"""Pallette:depthProjection Ext"""
	Depthtype : Par
	"""Menu : Determines what kind of depth is stored in the source depth image i.e. whether the point cloud is projected in rays from a single camera point, or from the image plane."""
	Fromrange1 : Par
	"""Used for scaling the point cloud depth. This parameter defines the range of depths in the source image. Depths outside this range are extrapolated."""
	Fromrange2 : Par
	"""Used for scaling the point cloud depth. This parameter defines the range of depths in the source image. Depths outside this range are extrapolated."""
	Torange1 : Par
	"""Determines the output range for the depth values. The range of input values is mapped linearly to the output range and values outside of the range are extrapolated."""
	Torange2 : Par
	"""Determines the output range for the depth values. The range of input values is mapped linearly to the output range and values outside of the range are extrapolated."""
	Viewanglemethod : Par
	"""Menu : Determines how the field of view is defined for the projection."""
	Focallengths1 : Par
	"""The normalized focal length values when using the Focal Length view angle method."""
	Focallengths2 : Par
	"""The normalized focal length values when using the Focal Length view angle method."""
	Center1 : Par
	"""The position of the camera relative to the image plane in normalized values i.e. (0.5, 0.5) assumes the camera point is directly in the center of the image plane."""
	Center2 : Par
	"""The position of the camera relative to the image plane in normalized values i.e. (0.5, 0.5) assumes the camera point is directly in the center of the image plane."""
	par : parameter.Pallette:depthProjection Ext
	"""Parameters of parameter.Pallette:depthProjection Ext"""
	pass


class parameterCOMP():
	"""parameterCOMP"""
	combinescopes : Par
	"""Menu : Specify the how to combine the scope parameters below to make the parameter selection."""
	par : parameter.parameterCOMP
	"""Parameters of parameter.parameterCOMP"""
	pass


class replicatorCOMP():
	"""replicatorCOMP"""
	method : Par
	"""Menu : Choose between using a Template DAT Table where each row will create a replicant or using the Number of Replicants parameter below to set how many replications to make."""
	namefromtable : Par
	"""Menu : How the node names will be generated."""
	layout : Par
	"""Menu : How to lay out the new nodes - all in one place (Off), horizontally, vertically, or in a grid."""
	layoutorigin1 : Par
	"""Where to lay out the new nodes, giving the XY location of the top-left node's bottom-left corner."""
	layoutorigin2 : Par
	"""Where to lay out the new nodes, giving the XY location of the top-left node's bottom-left corner."""
	par : parameter.replicatorCOMP
	"""Parameters of parameter.replicatorCOMP"""
	pass


class selectCOMP():
	"""selectCOMP"""
	par : parameter.selectCOMP
	"""Parameters of parameter.selectCOMP"""
	pass


class sharedmeminCOMP():
	"""sharedmeminCOMP"""
	par : parameter.sharedmeminCOMP
	"""Parameters of parameter.sharedmeminCOMP"""
	pass


class sharedmemoutCOMP():
	"""sharedmemoutCOMP"""
	par : parameter.sharedmemoutCOMP
	"""Parameters of parameter.sharedmemoutCOMP"""
	pass


class sliderCOMP():
	"""sliderCOMP"""
	slidertype : Par
	"""Menu : Sets the type of slider."""
	par : parameter.sliderCOMP
	"""Parameters of parameter.sliderCOMP"""
	pass


class tableCOMP():
	"""tableCOMP"""
	tablealign : Par
	"""Menu : Specifies the order in which cells are arranged:"""
	fontsizeunit : Par
	"""Menu : Lets you choose the unit of the specified font size."""
	infoformat : Par
	"""Menu : Determines how the state information in a connected [[Info DAT]] is displayed."""
	tableoffsetx : Par
	"""Offset the Table. This is not offsetting the Table COMP itself but the Table as it is drawn. So when selecting to Crop the Children, the Table will be potentially cut off at the borders of the Table COMP."""
	tableoffsety : Par
	"""Offset the Table. This is not offsetting the Table COMP itself but the Table as it is drawn. So when selecting to Crop the Children, the Table will be potentially cut off at the borders of the Table COMP."""
	par : parameter.tableCOMP
	"""Parameters of parameter.tableCOMP"""
	pass


class textCOMP():
	"""textCOMP"""
	mode : Par
	"""Menu : Controls whether the contents are taken from the Text parameter or from a Specification DAT/CHOP."""
	type : Par
	"""Menu : The Type parameter controls how the value is interpreted and as well as what formatting and editing options are available."""
	formatting : Par
	"""Menu : This parameter controls how the source text is is formatted and displayed inside the panel. The options available will change depending on the selected mode. For example, in Float mode there are options for scientific notation or percentage, while in Integer mode there are options to treat the source value as a time code."""
	thousandsseparator : Par
	"""Menu : Used in Float and Integer mode to add a separator between thousands to make it easier to read large numbers. For example 1,000,000"""
	editmode : Par
	"""Menu : Controls whether the text can be editing directly in the viewer."""
	readingdirection : Par
	"""Menu : Use this parameter to control whether the text is displayed from left-to-right (LTR) or from right-to-left (RTL). Bidirectional layout is also supported when LTR characters are detected when using RTL mode."""
	dragdropmode : Par
	"""Menu : This parameter controls what happens when a user drags something onto an active panel."""
	dragdropmode : Par
	"""Menu : This parameter controls what happens when a user drags something onto an active panel."""
	font : Par
	"""Menu : Select the font to be used from the dropdown menu. Available fonts are those that have been registered with the operating system. There may be a delay when selecting fonts that have not been used before as the system creates the necessary intermediate files required for rendering."""
	typeface : Par
	"""Menu : """
	scaletofit : Par
	"""Menu : Automatically adjust the font size to fit inside the panel."""
	fontsizeunits : Par
	"""Menu : Determines how the font size is interpretted. The default is resolution-independent panel units."""
	fontcolorr : Par
	"""The default color of the text. Additional colors can be applied to separate parts of the text using formatting codes."""
	fontcolorg : Par
	"""The default color of the text. Additional colors can be applied to separate parts of the text using formatting codes."""
	fontcolorb : Par
	"""The default color of the text. Additional colors can be applied to separate parts of the text using formatting codes."""
	selectcolorr : Par
	"""The color of the selection bar when Custom Select Color is enabled."""
	selectcolorg : Par
	"""The color of the selection bar when Custom Select Color is enabled."""
	selectcolorb : Par
	"""The color of the selection bar when Custom Select Color is enabled."""
	textoffsetx : Par
	"""An offset applied to the text position after any other alignment operations. Positive values move the text up and to the right."""
	textoffsety : Par
	"""An offset applied to the text position after any other alignment operations. Positive values move the text up and to the right."""
	textoffsetunits : Par
	"""Menu : Determine the units used by the Text Offset parameter."""
	textpaddingunits : Par
	"""Menu : The units used by the text padding."""
	textpaddingl : Par
	""""""
	textpaddingr : Par
	""""""
	textpaddingb : Par
	""""""
	textpaddingt : Par
	""""""
	textpaddingunits : Par
	"""Menu : The units used by the text padding."""
	alignx : Par
	"""Menu : Determines how the text is positioned horizontally in the panel. For example, with left alignment, the text will be positioned against the left side of the panel plus any defined padding."""
	alignxmode : Par
	"""Menu : Determines how the text is measured for calculating the alignment. Only font metrics are available when using Multiline or Specification DAT mode."""
	aligny : Par
	"""Menu : Determines how the text is positioned vertically inside the panel."""
	alignymode : Par
	"""Menu : Determines how the text is measured when doing the vertical alignment."""
	textpaddingl : Par
	"""Set the amount of space between the edges of the panel and the text. Whether the padding has an effect on the position of the text depends on the current alignment mode and whether word wrapping is used. For example, if the text is left aligned, the text will be positioned away from the left edge based on the left padding. But the text may extend any distance from the right edge depending on the length of the text. However, if word wrap is enabled in multiline mode, then the text will be wrapped at a distance from the right edge based on the padding."""
	textpaddingr : Par
	"""Set the amount of space between the edges of the panel and the text. Whether the padding has an effect on the position of the text depends on the current alignment mode and whether word wrapping is used. For example, if the text is left aligned, the text will be positioned away from the left edge based on the left padding. But the text may extend any distance from the right edge depending on the length of the text. However, if word wrap is enabled in multiline mode, then the text will be wrapped at a distance from the right edge based on the padding."""
	textpaddingb : Par
	"""Set the amount of space between the edges of the panel and the text. Whether the padding has an effect on the position of the text depends on the current alignment mode and whether word wrapping is used. For example, if the text is left aligned, the text will be positioned away from the left edge based on the left padding. But the text may extend any distance from the right edge depending on the length of the text. However, if word wrap is enabled in multiline mode, then the text will be wrapped at a distance from the right edge based on the padding."""
	textpaddingt : Par
	"""Set the amount of space between the edges of the panel and the text. Whether the padding has an effect on the position of the text depends on the current alignment mode and whether word wrapping is used. For example, if the text is left aligned, the text will be positioned away from the left edge based on the left padding. But the text may extend any distance from the right edge depending on the length of the text. However, if word wrap is enabled in multiline mode, then the text will be wrapped at a distance from the right edge based on the padding."""
	par : parameter.textCOMP
	"""Parameters of parameter.textCOMP"""
	pass


class timeCOMP():
	"""timeCOMP"""
	rangelimit : Par
	"""Menu : This menu controls how the playback loops:"""
	signature1 : Par
	"""Specifies the time signature. The first number is the number of beats per measure and the second number indicates the type of note that constitutes one beat. See [http://en.wikipedia.org/wiki/Time_signature Time Signature - Wikipedia] for additional information."""
	signature2 : Par
	"""Specifies the time signature. The first number is the number of beats per measure and the second number indicates the type of note that constitutes one beat. See [http://en.wikipedia.org/wiki/Time_signature Time Signature - Wikipedia] for additional information."""
	par : parameter.timeCOMP
	"""Parameters of parameter.timeCOMP"""
	pass


class usdCOMP():
	"""usdCOMP"""
	sampleratemode : Par
	"""dropmenu : A menu to choose between the file FPS or custom sample rate."""
	playmode : Par
	"""dropmenu : A menu to specify the method used to play the animation."""
	cuepointunit : Par
	"""nolabel shortvalues dropmenu : Specifies a unit type for Cue Point. Changing this will convert the previous unit to the selected unit."""
	indexunit : Par
	"""nolabel shortvalues dropmenu : Specifies a unit type for Index. Changing this will convert the previous unit to the selected unit."""
	tstartunit : Par
	"""nolabel shortvalues dropmenu : Specifies a unit type for Trim Start. Changing this will convert the previous unit to the selected unit."""
	tendunit : Par
	"""nolabel shortvalues dropmenu : Specifies a unit type for Trim End. Changing this will convert the previous unit to the selected unit."""
	textendleft : Par
	"""dropmenu : Determines how USD COMP handles animation positions that lie before the Trim Start position. For example, if Trim Start is set to 1, and the animation current index is -10, the Extend Left menu determines how the animation position is calculated."""
	textendright : Par
	"""dropmenu : Determines how USD COMP handles animation positions that lie after the Trim End position. For example, if Trim End is set to 20, and the animation current index is 25, the Extend Right menu determines how the animation position is calculated."""
	par : parameter.usdCOMP
	"""Parameters of parameter.usdCOMP"""
	pass


class widgetCOMP():
	"""widgetCOMP"""
	par : parameter.widgetCOMP
	"""Parameters of parameter.widgetCOMP"""
	pass


class windowCOMP():
	"""windowCOMP"""
	justifyoffsetto : Par
	"""Menu : All the positioning parameters below are done relative to the location you specify here. Your window can span more than the specified 'area', it's just used as the reference for positioning."""
	justifyh : Par
	"""Menu : Aligns the window horizontally with the monitor or bounds of all monitors."""
	justifyv : Par
	"""Menu : Aligns the window vertically with the monitor or bounds of all monitors."""
	winoffsetx : Par
	"""Horizontal offset applied to window after justifying."""
	winoffsety : Par
	"""Horizontal offset applied to window after justifying."""
	dpiscaling : Par
	"""Menu : Options for managing DPI scaling on high DPI monitors. To inspect a monitor's DPI scaling setting, you can use the [[Monitors DAT]] and refer to the <code>dpi_scale</code> column."""
	size : Par
	"""Menu : Determines how the size of the window is determined."""
	cursorvisible : Par
	"""Menu : Controls whether or not the cursor remains visible when over this window."""
	vsyncmode : Par
	"""Menu : Controls how the window is updated with regards to V-Sync. Enabled means it will update in sync with the monitors refresh which avoids tearing and lost frames. Disabled means it can update at any point during the refresh which can result in tearing or lost frames. FPS is Half Monitor Rate should be used when doing things such as running a 30fps file on a 60Hz display. This makes each update be shown for exactly 2 refreshes which keeps motion looking smooth."""
	par : parameter.windowCOMP
	"""Parameters of parameter.windowCOMP"""
	pass


class kinectazureTOP():
	"""kinectazureTOP"""
	fps5 : Par
	"""Controls the frame rate of both the color and depth cameras. Some higher camera resolutions are not supported when running at 30FPS. Lower framerates can produce brighter color images in low light conditions."""
	fps15 : Par
	"""Controls the frame rate of both the color and depth cameras. Some higher camera resolutions are not supported when running at 30FPS. Lower framerates can produce brighter color images in low light conditions."""
	fps30 : Par
	"""Controls the frame rate of both the color and depth cameras. Some higher camera resolutions are not supported when running at 30FPS. Lower framerates can produce brighter color images in low light conditions."""
	colorres : Par
	"""Menu : The resolution of images captured by the color camera. Different resolutions may have different aspect ratios. Note: 4096 x 3072 is not supported at 30 FPS."""
	depthmode : Par
	"""Menu : The depth mode controls which of the Kinect's two depth cameras (Wide or Narrow FOV) are used to produce the depth image and whether any 'binning' is used to process the data. In 'binned' modes, 2x2 blocks of pixels are combined to produce a filter, lower resolution image. Note: Body tracking is not supported when using the Passive IR depth mode."""
	proccessingmode : Par
	"""Menu : Determines how the body tracking model is processed. The default mode runs mostly on the GPU (supports Nvidia, AMD and Intel), but this can also be switched to a CPU mode when a compatible GPU is not available."""
	orientation : Par
	"""Menu : Used to indicate when the camera is mounted in a non-upright position. This can help improve body-tracking results."""
	image : Par
	"""Menu : A list of available image types to capture from the device and display in this TOP. All image types have a second version that is mapped (aligned) to the image space of the other camera so that color and depth image data can be matched. The resolution of the image is controlled by the Color Resolution or Depth Mode parameters depending on the type of image selected. Use a [[Kinect Azure Select TOP]] to access additional image types from the same camera."""
	powerfreq : Par
	"""Menu : Select the frequency of the power supply for use in the cameras noise cancellation system."""
	syncmode : Par
	"""Menu : When using more than one Kinect Azure camera, this setting can be used to determine which unit is the master and which are subordinates."""
	par : parameter.kinectazureTOP
	"""Parameters of parameter.kinectazureTOP"""
	pass


class leapmotionTOP():
	"""leapmotionTOP"""
	api : Par
	"""Menu : Select between Leap Motion V2 or V4/V5 SDKs for tracking. V5 offers the fastest and most stable tracking, V2 offers some legacy features like gestures."""
	hmd : Par
	"""Menu : Switches the device to '''H'''ead '''M'''ounted '''D'''isplay mode."""
	par : parameter.leapmotionTOP
	"""Parameters of parameter.leapmotionTOP"""
	pass


class mosysTOP():
	"""mosysTOP"""
	par : parameter.mosysTOP
	"""Parameters of parameter.mosysTOP"""
	pass


class moviefileinTOP():
	"""moviefileinTOP"""
	playmode : Par
	"""Menu : Specifies the method used to play the movie, there are 3 options."""
	cuepointunit : Par
	"""Menu : Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage)."""
	cuebehavior : Par
	"""Menu : Customize the Cue parameter's behavior."""
	indexunit : Par
	"""Menu : Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage)."""
	loopcrossfadeunit : Par
	"""Menu : Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage)."""
	audioloop : Par
	"""Menu : This menu helps you determine how to treat the audio as the end of a movie approaches. This is needed because of all the cases of playing a movie, like when driving with an index, the TOP will not know if you intend to loop it or not."""
	imageindexing : Par
	"""Menu : Determines how an image sequence is ordered."""
	deinterlace : Par
	"""Menu : For movies that are stored as fields, where each image is made of two images interleaved together. A 30-frame per second movie would contain 60 fields per second. For each image, the even scanlines of the first field are interleaved with the odd scanlines of the second field. The Movie File In TOP has several ways of dealing with this:"""
	precedence : Par
	"""Menu : Where fields are extracted one field at a time, this will extract the Even field first by default, otehrwise it will extract the odd field first. The video industry has not standardized on one or the other."""
	multalpha : Par
	"""Menu : Premultiplies the image."""
	loadingerrorimage : Par
	"""Menu : When the file can not be loaded for some reason, select what to display instead."""
	tstartunit : Par
	"""Menu : Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage)."""
	tendunit : Par
	"""Menu : Select the units for this parameter from Index, Frames, Seconds, and Fraction (percentage)."""
	textendleft : Par
	"""Menu : Determines how the Movie File In TOP handles movie positions that lie before the Trim Start position. For example, if Trim Start is set to 1, and the movie's current index is -10, the Extend Left menu determines how the movie position is calculated."""
	textendright : Par
	"""Menu : Determines how the Movie File In TOP handles movie positions that lie after the Trim End position. For example, if Trim End is set to 20, and the movie's current index is 25, the Extend Right menu determines how the movie position is calculated."""
	frametimeoutstrat : Par
	"""Menu : When on, if the Disk Read Timeout is reached TouchDesigner will use the latest available frame in place of the skipped frame."""
	par : parameter.moviefileinTOP
	"""Parameters of parameter.moviefileinTOP"""
	pass


class flowTOP():
	"""flowTOP"""
	simpositionx : Par
	"""The position of the simulation volume's center, in the world. The simulation cannot extend outside of the volume."""
	simpositiony : Par
	"""The position of the simulation volume's center, in the world. The simulation cannot extend outside of the volume."""
	simpositionz : Par
	"""The position of the simulation volume's center, in the world. The simulation cannot extend outside of the volume."""
	simsizex : Par
	"""The size of the simulation volume in the world. The simulation cannot extend outside of the volume. Also controls the size of simulation blocks, so the total number of blocks in the volume stays the same. Smaller size blocks will require more blocks for the same size simulation. This increases accuracy but makes the simulation more taxing on the GPU as there are more blocks to calculate."""
	simsizey : Par
	"""The size of the simulation volume in the world. The simulation cannot extend outside of the volume. Also controls the size of simulation blocks, so the total number of blocks in the volume stays the same. Smaller size blocks will require more blocks for the same size simulation. This increases accuracy but makes the simulation more taxing on the GPU as there are more blocks to calculate."""
	simsizez : Par
	"""The size of the simulation volume in the world. The simulation cannot extend outside of the volume. Also controls the size of simulation blocks, so the total number of blocks in the volume stays the same. Smaller size blocks will require more blocks for the same size simulation. This increases accuracy but makes the simulation more taxing on the GPU as there are more blocks to calculate."""
	gravityx : Par
	"""Gravity direction for use with Buoyancy parameter, where amount controls strength of buoyancy force."""
	gravityy : Par
	"""Gravity direction for use with Buoyancy parameter, where amount controls strength of buoyancy force."""
	gravityz : Par
	"""Gravity direction for use with Buoyancy parameter, where amount controls strength of buoyancy force."""
	par : parameter.flowTOP
	"""Parameters of parameter.flowTOP"""
	pass


class nvidiaupscalerTOP():
	"""nvidiaupscalerTOP"""
	gpu : Par
	"""Menu : Select the GPU device to run the AI models on. The GPU must be a Nvidia RTX compatible card."""
	mode : Par
	"""Menu : Choose the mode (Upscale or Super-Resolution) and factor by which the resolution will increase."""
	par : parameter.nvidiaupscalerTOP
	"""Parameters of parameter.nvidiaupscalerTOP"""
	pass


class photoshopinTOP():
	"""photoshopinTOP"""
	imageformat : Par
	"""Menu : Determines what format the Photoshop stream is transferred with."""
	updatemode : Par
	"""Menu : Determines how the image is updated."""
	par : parameter.photoshopinTOP
	"""Parameters of parameter.photoshopinTOP"""
	pass


class syphonspoutinTOP():
	"""syphonspoutinTOP"""
	par : parameter.syphonspoutinTOP
	"""Parameters of parameter.syphonspoutinTOP"""
	pass


class syphonspoutoutTOP():
	"""syphonspoutoutTOP"""
	par : parameter.syphonspoutoutTOP
	"""Parameters of parameter.syphonspoutoutTOP"""
	pass


class videodeviceoutTOP():
	"""videodeviceoutTOP"""
	library : Par
	"""Menu : Select the driver library to use."""
	device : Par
	"""StrMenu : A menu of available video devices to output to. Set the Library parameter above prior to selecting your device."""
	outputpixelformat : Par
	"""Menu : Set the pixel format of the output when possible (depends what type of device is used).	Data may be converted to YUV colorspace depending on what the device and settings require."""
	outputcolorspace : Par
	"""Menu : Set the color space of the data sent out, for supported devices."""
	referencesource : Par
	"""Menu : On AJA devices what input to use as a reference source input."""
	audiobitdepth : Par
	"""Menu : Describes the number of bits of information used for each sample."""
	transfermode : Par
	"""Menu : Controls how the image data is transfered between the GPU and the output card."""
	par : parameter.videodeviceoutTOP
	"""Parameters of parameter.videodeviceoutTOP"""
	pass


class videostreamoutTOP():
	"""videostreamoutTOP"""
	mode : Par
	"""Menu : Selects if the mode works as an RTSP server, sends RTMP to a receiever such as a distribution service like YouTube or Twitch, or sends to an SRT destination."""
	videocodec : Par
	"""Menu : """
	profile : Par
	"""Menu : The H.264 profile to use to encode the frames. Some decoders can only support H.264 encoder at certain profiles."""
	quality : Par
	"""Menu : The quality level of the encoding."""
	bitratemode : Par
	"""Menu : Chooses between constant (CBR) and variable (VBR) bit rate modes. Mode streaming services prefer a constant bit rate mode."""
	audiobitrate : Par
	"""Menu : Set the bit rate used for encoding audio."""
	includesilentaudio : Par
	"""Menu : """
	par : parameter.videostreamoutTOP
	"""Parameters of parameter.videostreamoutTOP"""
	pass


class abletonlinkCHOP():
	"""abletonlinkCHOP"""
	signature1 : Par
	"""Specifies the time signature. The first number is the number of beats per measure and the second number indicates the type of note that constitutes one beat. See [http://en.wikipedia.org/wiki/Time_signature Time Signature - Wikipedia] for additional information."""
	signature2 : Par
	"""Specifies the time signature. The first number is the number of beats per measure and the second number indicates the type of note that constitutes one beat. See [http://en.wikipedia.org/wiki/Time_signature Time Signature - Wikipedia] for additional information."""
	par : parameter.abletonlinkCHOP
	"""Parameters of parameter.abletonlinkCHOP"""
	pass


class analyzeCHOP():
	"""analyzeCHOP"""
	function : Par
	"""Menu : This menu determines the function applied to the channel."""
	par : parameter.analyzeCHOP
	"""Parameters of parameter.analyzeCHOP"""
	pass


class angleCHOP():
	"""angleCHOP"""
	inunit : Par
	"""Menu : Units of incoming channels:"""
	inorder : Par
	"""Menu : The order that rotation angles are assumed to be applied in (Euler angles as they are called). Applicable when converting to and from Quaternions or Vectors."""
	outunit : Par
	"""Menu : Units of outgoing channels:"""
	outorder : Par
	"""Menu : The order that rotation angles are assumed to be applied in (Euler angles as they are called). Applicable when converting to and from Quaternions or Vectors."""
	par : parameter.angleCHOP
	"""Parameters of parameter.angleCHOP"""
	pass


class attributeCHOP():
	"""attributeCHOP"""
	slerp : Par
	"""Menu : The function to perform on the attributes:"""
	rord : Par
	"""Menu : Sets the rotation order of the rotation triplet."""
	par : parameter.attributeCHOP
	"""Parameters of parameter.attributeCHOP"""
	pass


class audiobandeqCHOP():
	"""audiobandeqCHOP"""
	par : parameter.audiobandeqCHOP
	"""Parameters of parameter.audiobandeqCHOP"""
	pass


class audiobinauralCHOP():
	"""audiobinauralCHOP"""
	inputformat : Par
	"""Menu : Select the input format to convert from. The input CHOP is required to have the correct number of channels (eg. 6 for 5.1 Surround)."""
	par : parameter.audiobinauralCHOP
	"""Parameters of parameter.audiobinauralCHOP"""
	pass


class audiodeviceinCHOP():
	"""audiodeviceinCHOP"""
	driver : Par
	"""Menu : Select between default DirectSound/CoreAudio, ASIO, or native device supported drivers."""
	format : Par
	"""Menu : When Driver is set to DirectSound, this set mono, stereo, or multi-channel. Also determines how many channels are created 1(mono) or 2(stereo left and stereo right), or when set to multi-channel set the number of channels active on the Input 1 and Input 2 parameter pages."""
	par : parameter.audiodeviceinCHOP
	"""Parameters of parameter.audiodeviceinCHOP"""
	pass


class audiodeviceoutCHOP():
	"""audiodeviceoutCHOP"""
	driver : Par
	"""Menu : Select between default DirectSound/CoreAudio or ASIO drivers."""
	par : parameter.audiodeviceoutCHOP
	"""Parameters of parameter.audiodeviceoutCHOP"""
	pass


class audiodynamicsCHOP():
	"""audiodynamicsCHOP"""
	compressiontype : Par
	"""Menu : Determines which compression method to use."""
	chanlinkingcomp : Par
	"""Menu : As various channels come into the CHOP, they can either be compressed by an equal amount, or individually.  If they are compressed equally, all of the channels will be evaluated for the highest peak value, and this value will be used to determine the compression amount.	
If they are compressed separately, each channel will be evaluated and compressed by different amounts."""
	chanlinkinglim : Par
	"""Menu : Same as compressor."""
	par : parameter.audiodynamicsCHOP
	"""Parameters of parameter.audiodynamicsCHOP"""
	pass


class audiofileinCHOP():
	"""audiofileinCHOP"""
	playmode : Par
	"""Menu : Specifies the method used to playback the audio, there are 3 options."""
	repeat : Par
	"""Menu : Repeats the audio stream when the end is reached."""
	par : parameter.audiofileinCHOP
	"""Parameters of parameter.audiofileinCHOP"""
	pass


class audiofileoutCHOP():
	"""audiofileoutCHOP"""
	filetype : Par
	"""Menu : Select the file type (container) of the output file."""
	codec : Par
	"""Menu : Select the compression codec for the WAV file type."""
	bitrate : Par
	"""Menu : Selects the bit rate for the MP3 file type."""
	par : parameter.audiofileoutCHOP
	"""Parameters of parameter.audiofileoutCHOP"""
	pass


class audiofilterCHOP():
	"""audiofilterCHOP"""
	filter : Par
	"""Menu : The filter type:"""
	units : Par
	"""Menu : The filter cutoff frequency can be expressed in Hz (menu set to Frequency) or power-of-10 (menu set to Logarithmic). It enables one of the next 2 Filter Cutoff parameters."""
	par : parameter.audiofilterCHOP
	"""Parameters of parameter.audiofilterCHOP"""
	pass


class audiomovieCHOP():
	"""audiomovieCHOP"""
	par : parameter.audiomovieCHOP
	"""Parameters of parameter.audiomovieCHOP"""
	pass


class audiondiCHOP():
	"""audiondiCHOP"""
	par : parameter.audiondiCHOP
	"""Parameters of parameter.audiondiCHOP"""
	pass


class audiooscillatorCHOP():
	"""audiooscillatorCHOP"""
	wavetype : Par
	"""Menu : The shape of the waveform to repeat, unless overridden by the Playback Source:"""
	resetcondition : Par
	"""Menu : This menu determines how the Reset input triggers a reset of the channel(s)."""
	par : parameter.audiooscillatorCHOP
	"""Parameters of parameter.audiooscillatorCHOP"""
	pass


class audioparaeqCHOP():
	"""audioparaeqCHOP"""
	units : Par
	"""Menu : How frequency is expressed:"""
	par : parameter.audioparaeqCHOP
	"""Parameters of parameter.audioparaeqCHOP"""
	pass


class audioplayCHOP():
	"""audioplayCHOP"""
	mode : Par
	"""Menu : Determines how the audio is triggered when using the first input to trigger."""
	par : parameter.audioplayCHOP
	"""Parameters of parameter.audioplayCHOP"""
	pass


class audiorenderCHOP():
	"""audiorenderCHOP"""
	outputformat : Par
	"""Menu : The output format of the audio: Binaural, Stereo, Quadraphonic Surround, 5.1 Surround, 7.1 Surround, Custom Setup, or Ambisonics (AmbiX). Ambisonics is a format for encoding three-dimensional 360 degree audio. The Ambisonics format used in the Audio Render CHOP is the 3rd order SN3D format consisting of 16 encoded channels (WXYZ, RSTUV, KLMNOPQ) that define the sphere of sound. Custom Setup requires use of the Mapping Table."""
	par : parameter.audiorenderCHOP
	"""Parameters of parameter.audiorenderCHOP"""
	pass


class audiospectrumCHOP():
	"""audiospectrumCHOP"""
	mode : Par
	"""Menu : Select which mode to use, modes described below."""
	fftsize : Par
	"""Menu : Converting to frequency needs a power-of-2 number of samples, like 512, 1024, 2048. (FFT means Fast [http://en.wikipedia.org/wiki/Joseph_Fourier Fourier] Transform.) The more samples, the more accurate the spectrum but the more it doesn't represent the most recent sound. Whatever the size, the CHOP uses the most recent samples. Knowing that audio at 44100 samples per second with a timeline frame rate of 60 frames per second gives 735 samples per frame, if the CHOP cooks 1 frame later and the FFT size is 1024, then it will re-use 1024-735 = 289 samples, which is good as there's a little overlap. However if it cooks 2 frames later, it will miss using 446 frames since it will have advanced 735*2=1470 samples and it will only use 1024 of them."""
	outputmenu : Par
	"""Menu : The method how output length will be determined."""
	par : parameter.audiospectrumCHOP
	"""Parameters of parameter.audiospectrumCHOP"""
	pass


class audiostreaminCHOP():
	"""audiostreaminCHOP"""
	srctype : Par
	"""Menu : Select the source type: either from a server URL, or a WebRTC peer."""
	syncoffsetunit : Par
	"""Menu : Specify which units to use for the Audio Sync Offset parameter."""
	par : parameter.audiostreaminCHOP
	"""Parameters of parameter.audiostreaminCHOP"""
	pass


class audiostreamoutCHOP():
	"""audiostreamoutCHOP"""
	mode : Par
	"""Menu : Select the stream out mode: either [[RTSP]] or [[WebRTC]]."""
	par : parameter.audiostreamoutCHOP
	"""Parameters of parameter.audiostreamoutCHOP"""
	pass


class audiovstCHOP():
	"""audiovstCHOP"""
	signature1 : Par
	"""The time signature of the playhead. Not all plugins support changing of the time signature via the playhead."""
	signature2 : Par
	"""The time signature of the playhead. Not all plugins support changing of the time signature via the playhead."""
	par : parameter.audiovstCHOP
	"""Parameters of parameter.audiovstCHOP"""
	pass


class audiowebrenderCHOP():
	"""audiowebrenderCHOP"""
	par : parameter.audiowebrenderCHOP
	"""Parameters of parameter.audiowebrenderCHOP"""
	pass


class beatCHOP():
	"""beatCHOP"""
	playmode : Par
	"""Menu : Specifies the method used to playback the output."""
	resetcondition : Par
	"""Menu : This menu determines how the Reset input triggers a reset of the channel(s)."""
	par : parameter.beatCHOP
	"""Parameters of parameter.beatCHOP"""
	pass


class bindCHOP():
	"""bindCHOP"""
	match : Par
	"""Menu : Match channels between inputs by name or index."""
	par : parameter.bindCHOP
	"""Parameters of parameter.bindCHOP"""
	pass


class blacktraxCHOP():
	"""blacktraxCHOP"""
	protocol : Par
	"""Menu : The network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	outputformat : Par
	"""Menu : Specifies the format for the CHOP channels (ie. how many beacons to add). "From Mapping Table" adds one beacon to the CHOP for every row in the mapping table. "From Max Beacons" adds the number specified in the "Max Beacons" parameter."""
	par : parameter.blacktraxCHOP
	"""Parameters of parameter.blacktraxCHOP"""
	pass


class blendCHOP():
	"""blendCHOP"""
	method : Par
	"""Menu : The blend method:"""
	par : parameter.blendCHOP
	"""Parameters of parameter.blendCHOP"""
	pass


class blobtrackCHOP():
	"""blobtrackCHOP"""
	searchmode : Par
	"""Int : Controls how searching for blobs is done across all the points."""
	areaofinterest : Par
	"""Menu : Limits the area in which blobs are tracked. Points outside the area of interest are ignored."""
	centerx : Par
	"""The center of the area of interest."""
	centery : Par
	"""The center of the area of interest."""
	sizew : Par
	"""The size of the area of interest."""
	sizeh : Par
	"""The size of the area of interest."""
	predicttype : Par
	"""Menu : With prediction enabled, blobs from the last frame have their new position predicted before being matched to the current frame."""
	par : parameter.blobtrackCHOP
	"""Parameters of parameter.blobtrackCHOP"""
	pass


class bodytrackCHOP():
	"""bodytrackCHOP"""
	gpu : Par
	"""Menu : The GPU to run the body tracking models on. An Nvidia RTX or newer card is required."""
	par : parameter.bodytrackCHOP
	"""Parameters of parameter.bodytrackCHOP"""
	pass


class bulletsolverCHOP():
	"""bulletsolverCHOP"""
	xformspace : Par
	"""dropmenu : The space in which to output the transformation values. That is, the transform values (translation/rotation) will be outputted relative to the selected space."""
	par : parameter.bulletsolverCHOP
	"""Parameters of parameter.bulletsolverCHOP"""
	pass


class clipblenderCHOP():
	"""clipblenderCHOP"""
	targetx : Par
	"""This parameter works in conjunction with the root transform channels as defined on the Channels page of the clpblender CHOP as well as the [[Clip CHOP]] parameter called Position Type. When Position Type is set to "Blend To Target" it will blend the root transform channels for the current clip to the new position defined in this parameter."""
	targety : Par
	"""This parameter works in conjunction with the root transform channels as defined on the Channels page of the clpblender CHOP as well as the [[Clip CHOP]] parameter called Position Type. When Position Type is set to "Blend To Target" it will blend the root transform channels for the current clip to the new position defined in this parameter."""
	targetz : Par
	"""This parameter works in conjunction with the root transform channels as defined on the Channels page of the clpblender CHOP as well as the [[Clip CHOP]] parameter called Position Type. When Position Type is set to "Blend To Target" it will blend the root transform channels for the current clip to the new position defined in this parameter."""
	tx : Par
	""""""
	ty : Par
	""""""
	tz : Par
	""""""
	rx : Par
	""""""
	ry : Par
	""""""
	rz : Par
	""""""
	par : parameter.clipblenderCHOP
	"""Parameters of parameter.clipblenderCHOP"""
	pass


class clipCHOP():
	"""clipCHOP"""
	rord : Par
	"""Menu : """
	transtion : Par
	"""Menu : """
	abspos : Par
	"""Menu : """
	rottype : Par
	"""Menu : """
	par : parameter.clipCHOP
	"""Parameters of parameter.clipCHOP"""
	pass


class clockCHOP():
	"""clockCHOP"""
	output : Par
	"""Menu : Fractions or Units affects the channel data that is output from the Clock CHOP. Fraction gives convenient 0-1 ramps and Units give integers, like 0-23 for the hours of a day. For example, use Fractions and the day, hour and minute channels to drive a wall clock."""
	hourformat : Par
	"""Menu : 12 hour or 24 hour - Causes the hour channel to cycle through 12 or 24 hours. Also affects the AM/PM channel."""
	startref : Par
	"""Menu : The date/time that corresponds to year 0, day 1, hour 0, minute 0. It can be relative to Jan 1, 2000 or to the time that the TouchDesigner process started."""
	latitude1 : Par
	"""Enter a latitude (hours/min north/south) of your location. (defaults to Toronto, Canada). Fractional hours are permitted. For example:  43.6532 hours and 0 minutes, is identical to 43 hours and 39 minutes. The parameter latitude1 is hours, latitude2 is minutes."""
	latitude2 : Par
	"""Enter a latitude (hours/min north/south) of your location. (defaults to Toronto, Canada). Fractional hours are permitted. For example:  43.6532 hours and 0 minutes, is identical to 43 hours and 39 minutes. The parameter latitude1 is hours, latitude2 is minutes."""
	northsouth : Par
	"""Menu : Set if the Latitude value above is in the north or south hemisphere."""
	longitude1 : Par
	"""Enter a longitude (hours/min east/west) of your location. Fractional hours are permitted. The parameter longitude1 is hours, longitude2 is minutes."""
	longitude2 : Par
	"""Enter a longitude (hours/min east/west) of your location. Fractional hours are permitted. The parameter longitude1 is hours, longitude2 is minutes."""
	eastwest : Par
	"""Menu : Set if the Longitude value above is in the east or west hemisphere."""
	par : parameter.clockCHOP
	"""Parameters of parameter.clockCHOP"""
	pass


class compositeCHOP():
	"""compositeCHOP"""
	match : Par
	"""Menu : Matches channels in the base input with ones in the layer input by either index or name."""
	relative : Par
	"""Menu : Sets the meaning of the next four parameters - either Absolute values, Relative to the Start/End of the channel, or Relative to the Current Frame. The layer and base are never shifted."""
	risefunc : Par
	"""Menu : How to interpolate from one CHOP to another. It is the shape of the segment between the Start and Peak indices."""
	fallfunc : Par
	"""Menu : How to interpolate from one CHOP to another. It is the shape of the segment between the Release and End."""
	par : parameter.compositeCHOP
	"""Parameters of parameter.compositeCHOP"""
	pass


class constantCHOP():
	"""constantCHOP"""
	startunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	endunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	left : Par
	"""Menu : The left extend conditions (before range)."""
	right : Par
	"""Menu : The right extend conditions (after range)."""
	par : parameter.constantCHOP
	"""Parameters of parameter.constantCHOP"""
	pass


class copyCHOP():
	"""copyCHOP"""
	method : Par
	"""Menu : Select which copy method to use from the menu options below."""
	output : Par
	"""Menu : Select which output method to use from the menu options below."""
	remainder : Par
	"""Menu : See Remainder parameter below.."""
	par : parameter.copyCHOP
	"""Parameters of parameter.copyCHOP"""
	pass


class countCHOP():
	"""countCHOP"""
	triggeron : Par
	"""Menu : Determines whether a trigger occurs on an increasing slope or decreasing slope when passing the trigger threshold. A release will occur on the opposite slope."""
	output : Par
	"""Menu : Select limit options such as loop and/or clamp from the menu. The value will remain in the range from Min to Max."""
	offtoon : Par
	"""Menu : The operation to perform when a trigger event (off to on) occurs."""
	on : Par
	"""Menu : The operation to perform while the input remains triggered (on)."""
	ontooff : Par
	"""Menu : The operation to perform when a release event (on to off) occurs."""
	off : Par
	"""Menu : The operation to perform while the input is not triggered (off).	
			
'''Note''': The scripts are run relative to the parent node of this CHOP, as if the script is in the node above this CHOP."""
	resetcondition : Par
	"""Menu : This menu determines how the Reset input triggers a reset of the channel(s)."""
	par : parameter.countCHOP
	"""Parameters of parameter.countCHOP"""
	pass


class cplusplusCHOP():
	"""cplusplusCHOP"""
	par : parameter.cplusplusCHOP
	"""Parameters of parameter.cplusplusCHOP"""
	pass


class crossCHOP():
	"""crossCHOP"""
	par : parameter.crossCHOP
	"""Parameters of parameter.crossCHOP"""
	pass


class cycleCHOP():
	"""cycleCHOP"""
	blendmethod : Par
	"""Menu : How to blend between cycles:"""
	blendfunc : Par
	"""Menu : The shape of the blending function:"""
	par : parameter.cycleCHOP
	"""Parameters of parameter.cycleCHOP"""
	pass


class dattoCHOP():
	"""dattoCHOP"""
	extractrows : Par
	"""Menu : This parameter allows you to pick different ways of specifying the rows selected."""
	extractcols : Par
	"""Menu : This parameter allows you to pick different ways of specifying the columns selected."""
	output : Par
	"""Menu : Specify the form of the channels output."""
	firstrow : Par
	"""Menu : Specifies whether the first row is ignored, names, or values."""
	firstcolumn : Par
	"""Menu : Specifies whether the first columnn is ignored, names, or values."""
	par : parameter.dattoCHOP
	"""Parameters of parameter.dattoCHOP"""
	pass


class delayCHOP():
	"""delayCHOP"""
	par : parameter.delayCHOP
	"""Parameters of parameter.delayCHOP"""
	pass


class deleteCHOP():
	"""deleteCHOP"""
	discard : Par
	"""Menu : Determines whether the scoped channels should be deleted or retained:"""
	select : Par
	"""Menu : How to select channels - <span class="tipTextCHOP">By Name</span>, or By <span class="tipTextCHOP">Numeric</span> index."""
	chanvalue : Par
	"""Menu : Chooses the type of value range selection:"""
	selrange1 : Par
	"""The lower and upper values of the range used for Range Selection."""
	selrange2 : Par
	"""The lower and upper values of the range used for Range Selection."""
	compchans : Par
	"""Menu : How to select channels used to compare against criteria - By <span class="tipTextCHOP">Name</span>, by <span class="tipTextCHOP">Numeric</span> index, by using the <span class="tipTextCHOP">First Channel</span>, or by using the <span class="tipTextCHOP">Last Channel</span>."""
	compmulti : Par
	"""Menu : If there is more that one compare channel, this determines how to treat the values in the compare channels before checking against the criteria:"""
	condition : Par
	"""Menu : Choose the criteria for the samples to be compare against:"""
	par : parameter.deleteCHOP
	"""Parameters of parameter.deleteCHOP"""
	pass


class dmxinCHOP():
	"""dmxinCHOP"""
	interface : Par
	"""Menu : Select the type of interface to connect to the device with."""
	kinetversion : Par
	"""Menu : Set the version of the KiNET protocol to use."""
	format : Par
	"""Menu : Select between receiving Packet Per Sample (Timesliced), Packet Per Channel (Latest) or Packet Per Channel (All). When selecting Packet Per Channel (Latest), any messages outside the last cook are being discarded while the option Packet Per Channel (All) will append channels that would get otherwise skipped by dropped frames."""
	par : parameter.dmxinCHOP
	"""Parameters of parameter.dmxinCHOP"""
	pass


class dmxoutCHOP():
	"""dmxoutCHOP"""
	interface : Par
	"""Menu : Select the type of interface to connect to the device with."""
	kinetversion : Par
	"""Menu : Set the version of the KiNET protocol to use."""
	format : Par
	"""Menu : Select between sending Packet Per Sample or Packet Per Channel."""
	device : Par
	"""StrMenu : Select a DMX device from the menu."""
	serialport : Par
	"""StrMenu : When the Interface parameter is set to Generic Serial this parameter lets you select which Serial (COM) port to use."""
	localaddress : Par
	"""StrMenu : When the sending machine is equipped with multiple network adapters, this parameter can be used to choose which adapter to send the data from by specifying its IP address here."""
	par : parameter.dmxoutCHOP
	"""Parameters of parameter.dmxoutCHOP"""
	pass


class envelopeCHOP():
	"""envelopeCHOP"""
	method : Par
	"""Menu : The two methods of calculating the envelope:"""
	bounds : Par
	"""Menu : """
	interp : Par
	"""Menu : """
	par : parameter.envelopeCHOP
	"""Parameters of parameter.envelopeCHOP"""
	pass


class etherdreamCHOP():
	"""etherdreamCHOP"""
	par : parameter.etherdreamCHOP
	"""Parameters of parameter.etherdreamCHOP"""
	pass


class eventCHOP():
	"""eventCHOP"""
	resetcondition : Par
	"""Menu : Determines the reset behavior of using the 2nd Input Reset Trigger. This parameter is only active if there is an input connected to the CHOP's 2nd input."""
	par : parameter.eventCHOP
	"""Parameters of parameter.eventCHOP"""
	pass


class expressionCHOP():
	"""expressionCHOP"""
	par : parameter.expressionCHOP
	"""Parameters of parameter.expressionCHOP"""
	pass


class extendCHOP():
	"""extendCHOP"""
	left : Par
	"""Menu : The extend condition before the CHOP interval. They are:"""
	right : Par
	"""Menu : Extend condition after the interval. Same options as Extend Left."""
	par : parameter.extendCHOP
	"""Parameters of parameter.extendCHOP"""
	pass


class facetrackCHOP():
	"""facetrackCHOP"""
	gpu : Par
	"""Menu : The GPU to run the face tracking models on. An Nvidia RTX or newer card is required."""
	landmarks : Par
	"""Menu : """
	par : parameter.facetrackCHOP
	"""Parameters of parameter.facetrackCHOP"""
	pass


class fanCHOP():
	"""fanCHOP"""
	fanop : Par
	"""Menu : Selects either Fan In or Fan Out."""
	range : Par
	"""Menu : Determines how to handle input values that are outside the index range (0 to N-1)."""
	alloff : Par
	"""Menu : For a Fan In operation, when all input channels are off, set the output to -1 or 0."""
	par : parameter.fanCHOP
	"""Parameters of parameter.fanCHOP"""
	pass


class feedbackCHOP():
	"""feedbackCHOP"""
	output : Par
	"""Menu : Choose what to output from this menu."""
	par : parameter.feedbackCHOP
	"""Parameters of parameter.feedbackCHOP"""
	pass


class fileinCHOP():
	"""fileinCHOP"""
	nameoption : Par
	"""Menu : Use this menu to control the names of the loaded channels."""
	rateoption : Par
	"""Menu : Use this menu to adjust the sample rate of the loaded channels."""
	left : Par
	"""Menu : The left extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.fileinCHOP
	"""Parameters of parameter.fileinCHOP"""
	pass


class fileoutCHOP():
	"""fileoutCHOP"""
	par : parameter.fileoutCHOP
	"""Parameters of parameter.fileoutCHOP"""
	pass


class filterCHOP():
	"""filterCHOP"""
	type : Par
	"""Menu : There are seven types of filters:"""
	par : parameter.filterCHOP
	"""Parameters of parameter.filterCHOP"""
	pass


class freedCHOP():
	"""freedCHOP"""
	protocol : Par
	"""Menu : The network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	localaddress : Par
	"""StrMenu : Specify an IP address to receive on, useful when the system has mulitple NICs (Network Interface Card) and you want to select which one to use."""
	par : parameter.freedCHOP
	"""Parameters of parameter.freedCHOP"""
	pass


class freedoutCHOP():
	"""freedoutCHOP"""
	protocol : Par
	"""Menu : Selects the network protocol to use. Refer to the Network Protocols article for more information."""
	par : parameter.freedoutCHOP
	"""Parameters of parameter.freedoutCHOP"""
	pass


class functionCHOP():
	"""functionCHOP"""
	func : Par
	"""Menu : Which math function to apply to the channels. All of the functions are unary functions except for the binary functions 'arctan (Input1/Input2)' and 'Input1 ^ Input2'. In the cases of power functions, a negative base is inverted first to avoid imaginary numbers, and the result is negated."""
	angunit : Par
	"""Menu : For trigonometric functions, the angles can be measured in Degrees, Radians, or Cycles (0 to 1)."""
	match : Par
	"""Menu : How to pair channels together from the two inputs for the binary functions, by name or by channel index."""
	error : Par
	"""Menu : How to correct samples with math errors:"""
	par : parameter.functionCHOP
	"""Parameters of parameter.functionCHOP"""
	pass


class gestureCHOP():
	"""gestureCHOP"""
	playmode : Par
	"""Menu : Controls the gesture playback."""
	resetcondition : Par
	"""Menu : This menu determines how the Reset input (the third input) triggers a reset of the channel(s)."""
	par : parameter.gestureCHOP
	"""Parameters of parameter.gestureCHOP"""
	pass


class handleCHOP():
	"""handleCHOP"""
	par : parameter.handleCHOP
	"""Parameters of parameter.handleCHOP"""
	pass


class heliosdacCHOP():
	"""heliosdacCHOP"""
	par : parameter.heliosdacCHOP
	"""Parameters of parameter.heliosdacCHOP"""
	pass


class hogCHOP():
	"""hogCHOP"""
	par : parameter.hogCHOP
	"""Parameters of parameter.hogCHOP"""
	pass


class hokuyoCHOP():
	"""hokuyoCHOP"""
	interface : Par
	"""Menu : Select the device interface."""
	output : Par
	"""Menu : Outputs the scan data in either Polar or Cartesian coordinates."""
	par : parameter.hokuyoCHOP
	"""Parameters of parameter.hokuyoCHOP"""
	pass


class holdCHOP():
	"""holdCHOP"""
	sample : Par
	"""Menu : Defines when to sample the input channels. The parameters are as follows."""
	par : parameter.holdCHOP
	"""Parameters of parameter.holdCHOP"""
	pass


class inCHOP():
	"""inCHOP"""
	par : parameter.inCHOP
	"""Parameters of parameter.inCHOP"""
	pass


class infoCHOP():
	"""infoCHOP"""
	values : Par
	"""Menu : Select channel with values inside or outside the range specified in <span class="tipTextCHOP">Range</span>."""
	range1 : Par
	"""Set the bounds for selecting channels by value."""
	range2 : Par
	"""Set the bounds for selecting channels by value."""
	par : parameter.infoCHOP
	"""Parameters of parameter.infoCHOP"""
	pass


class interpolateCHOP():
	"""interpolateCHOP"""
	blendfunc : Par
	"""Menu : The shape of the interpolation curve:"""
	overlap : Par
	"""Menu : If an input is not a single frame, and if there are overlaps in the input CHOPs, an option is used to resolve the conflict."""
	match : Par
	"""Menu : Specify how to match the channels of each input."""
	par : parameter.interpolateCHOP
	"""Parameters of parameter.interpolateCHOP"""
	pass


class inversecurveCHOP():
	"""inversecurveCHOP"""
	span1 : Par
	""""""
	span2 : Par
	""""""
	interpolation : Par
	"""Menu : The type of guide curve to create with the guide components."""
	upvectorx : Par
	"""Control bone twist with this parameter."""
	upvectory : Par
	"""Control bone twist with this parameter."""
	upvectorz : Par
	"""Control bone twist with this parameter."""
	par : parameter.inversecurveCHOP
	"""Parameters of parameter.inversecurveCHOP"""
	pass


class inversekinCHOP():
	"""inversekinCHOP"""
	solvertype : Par
	"""Menu : This parameter defines the method used to determine the motion of the Bone object when it, its ancestor, or its children are moved."""
	par : parameter.inversekinCHOP
	"""Parameters of parameter.inversekinCHOP"""
	pass


class joinCHOP():
	"""joinCHOP"""
	blendmethod : Par
	"""Menu : The blend method to produce a seamless sequence:"""
	blendfunc : Par
	"""Menu : The blend interpolation shape to use. See Shape in the [[Cycle CHOP]]."""
	match : Par
	"""Menu : Match channels between inputs by index or by name."""
	par : parameter.joinCHOP
	"""Parameters of parameter.joinCHOP"""
	pass


class joystickCHOP():
	"""joystickCHOP"""
	axisrange : Par
	"""Menu : Select between and axis range of 0 to 1 or -1 to 1."""
	left : Par
	"""Menu : The left extend conditions (before range)."""
	right : Par
	"""Menu : The right extend conditions (after range)."""
	par : parameter.joystickCHOP
	"""Parameters of parameter.joystickCHOP"""
	pass


class keyboardinCHOP():
	"""keyboardinCHOP"""
	active : Par
	"""Menu : While '''On''', the keyboard inputs will be monitored and the CHOP will cook every frame. When set to '''Off''' it will not cook and the current keyboard values will not be output. '''While Playing''' will capture keyboard events only when the [[Timeline]] is playing forward."""
	modifiers : Par
	"""Menu : If it is set to Ctrl, the keys will only go On if you are also pressing the Ctrl key. This works similarly for Alt and Shift modifiers. If it set to Ignore, it doesn't matter if the Ctrl/Alt/Shift key is down or not."""
	channelnames : Par
	"""Menu : Channel names are generated automatically using one of these criteria."""
	left : Par
	"""Menu : The left extend conditions (before range)."""
	right : Par
	"""Menu : The right extend conditions (after range)."""
	par : parameter.keyboardinCHOP
	"""Parameters of parameter.keyboardinCHOP"""
	pass


class keyframeCHOP():
	"""keyframeCHOP"""
	left : Par
	"""Menu : The left extend conditions (before range)."""
	right : Par
	"""Menu : The right extend conditions (after range)."""
	par : parameter.keyframeCHOP
	"""Parameters of parameter.keyframeCHOP"""
	pass


class kinectazureCHOP():
	"""kinectazureCHOP"""
	par : parameter.kinectazureCHOP
	"""Parameters of parameter.kinectazureCHOP"""
	pass


class kinectCHOP():
	"""kinectCHOP"""
	hwversion : Par
	"""Menu : Choose between Kinect v1 or Kinect v2 sensors."""
	skeleton : Par
	"""Menu : Selects options for skeletal tracking."""
	par : parameter.kinectCHOP
	"""Parameters of parameter.kinectCHOP"""
	pass


class lagCHOP():
	"""lagCHOP"""
	lagmethod : Par
	"""Menu : The method by which lag is applied to the channels."""
	lag1 : Par
	"""Applies a lag to a channel. The first value is for lagging up, and the second is for lagging down. It is approximately the time that the output follows 90% of a change to the input."""
	lag2 : Par
	"""Applies a lag to a channel. The first value is for lagging up, and the second is for lagging down. It is approximately the time that the output follows 90% of a change to the input."""
	overshoot1 : Par
	"""Applies overshoot to a channel. The first value is for overshoot while moving up, and the second is for overshoot while moving down."""
	overshoot2 : Par
	"""Applies overshoot to a channel. The first value is for overshoot while moving up, and the second is for overshoot while moving down."""
	slope1 : Par
	"""The first value limits the slope when it is rising, and the second value limits the slope when it is decreasing."""
	slope2 : Par
	"""The first value limits the slope when it is rising, and the second value limits the slope when it is decreasing."""
	accel1 : Par
	"""The first value limits the acceleration when it is rising, and the second value limits the acceleration when it is decreasing."""
	accel2 : Par
	"""The first value limits the acceleration when it is rising, and the second value limits the acceleration when it is decreasing."""
	par : parameter.lagCHOP
	"""Parameters of parameter.lagCHOP"""
	pass


class laserCHOP():
	"""laserCHOP"""
	source : Par
	"""Menu : Select the source operator type for the laser image."""
	updatemethod : Par
	"""Menu : Control how the Laser CHOP pulls data from its source.
    
In most cases you will want to keep this at the default setting "When All Points Drawn". 

There is a specific usage case that requires the "Every Frame" update method. Background is that the Laser CHOP might have to draw the input values over multiple frames. For example given a source with 200 sampling values. After applying all blanking and step sizes at a certain sample rate, the Laser might need more than one frame to draw the full image. The effect will be visible by the Laser image flickering. With the default setting, the Laser will grab a new set of samples from its input once it has completed drawing all previous values. With the "Every Frame" update method, the Laser will grab the updated values for the remaining samples after each frame."""
	par : parameter.laserCHOP
	"""Parameters of parameter.laserCHOP"""
	pass


class laserdeviceCHOP():
	"""laserdeviceCHOP"""
	type : Par
	"""Menu : Specify the type of laser device."""
	queueunits : Par
	"""Menu : The units of queue time."""
	par : parameter.laserdeviceCHOP
	"""Parameters of parameter.laserdeviceCHOP"""
	pass


class leapmotionCHOP():
	"""leapmotionCHOP"""
	api : Par
	"""Menu : Select between Leap Motion V2 or V4/V5 SDKs for tracking. V5 offers the fastest and most stable tracking, V2 offers some legacy features like gestures."""
	hmd : Par
	"""Menu : Switches the device to '''H'''ead '''M'''ounted '''D'''isplay mode."""
	par : parameter.leapmotionCHOP
	"""Parameters of parameter.leapmotionCHOP"""
	pass


class leuzerod4CHOP():
	"""leuzerod4CHOP"""
	rod4porotocol : Par
	"""Menu : Selects which protocol to use. This must match the protocol the scanner was set to use in the RODplussoft setup utility for the device. You may still get some sort of data if the wrong protocol is selected, but the data will be random and incorrect."""
	inputcoordinate : Par
	"""Menu : Available when using ROD4plus ASCII-Remote protocol, specifies whether to use Polar or Cartesian input coordinates. This must match the coordinate the scanner was set to use in the RODplussoft setup utility for the device."""
	outputmode : Par
	"""Menu : Select Raw Data or Blob Tracking mode for output channels. The parameters below are only available in Blob Tracking mode."""
	areaofinterest : Par
	"""Menu : Limits the area in which blobs are tracked."""
	lowerleft1 : Par
	"""Specifies the lower left corner of the bounding box used when Area of Interest parameter is set to Bounding Box."""
	lowerleft2 : Par
	"""Specifies the lower left corner of the bounding box used when Area of Interest parameter is set to Bounding Box."""
	upperright1 : Par
	"""Specifies the upper right corner of the bounding box used when Area of Interest parameter is set to Bounding Box."""
	upperright2 : Par
	"""Specifies the upper right corner of the bounding box used when Area of Interest parameter is set to Bounding Box."""
	par : parameter.leuzerod4CHOP
	"""Parameters of parameter.leuzerod4CHOP"""
	pass


class lfoCHOP():
	"""lfoCHOP"""
	wavetype : Par
	"""Menu : The shape of the waveform to repeat, unless overridden by the Source Wave:"""
	resetcondition : Par
	"""Menu : This menu determines how the Reset input triggers resetting the channel(s)."""
	par : parameter.lfoCHOP
	"""Parameters of parameter.lfoCHOP"""
	pass


class limitCHOP():
	"""limitCHOP"""
	type : Par
	"""Menu : Select limit options such as loop, clamp, or zigzag from the menu. The value will remain in the range from Min to less than Max."""
	quantvalue : Par
	"""Menu : Selects the quantization method to use:"""
	quantindex : Par
	"""Menu : Selects whether to quantize the index relative to the sample 0, or the start index of the CHOP."""
	par : parameter.limitCHOP
	"""Parameters of parameter.limitCHOP"""
	pass


class logicCHOP():
	"""logicCHOP"""
	convert : Par
	"""Menu : This menu determines the method to convert inputs to binary:"""
	preop : Par
	"""Menu : Once converted by the Convert Input stage, Channel Pre OP defines a unary operation on each input sample:"""
	chanop : Par
	"""Menu : Takes the first input and combines its channels, then the second input and combines its channels, and so on."""
	chopop : Par
	"""Menu : Combine CHOPs combines the first channels of each CHOP, the second channels of each CHOP, etc.. Channels between inputs can be combined by number or name. Combining (Logic) Operations are:"""
	match : Par
	"""Menu : Channels are matched between inputs by Channel Name or Channel Number."""
	align : Par
	"""Menu : Inputs that don't start at the same frame can be aligned. Se the section, Align Options."""
	boundmin : Par
	"""Set lower and upper bounds for when Convert Input is set to '''Off When Outside Bounds'''."""
	boundmax : Par
	"""Set lower and upper bounds for when Convert Input is set to '''Off When Outside Bounds'''."""
	par : parameter.logicCHOP
	"""Parameters of parameter.logicCHOP"""
	pass


class lookupCHOP():
	"""lookupCHOP"""
	index1 : Par
	"""The Index Range maps the index channel's values to the lookup table's start and end and defaults to 0 and 1. The first parameter represents the start of the lookup table. When the index channel has this value, it will index the start of the lookup table. The second parameter represents the end of the lookup table and behaves in the same way."""
	index2 : Par
	"""The Index Range maps the index channel's values to the lookup table's start and end and defaults to 0 and 1. The first parameter represents the start of the lookup table. When the index channel has this value, it will index the start of the lookup table. The second parameter represents the end of the lookup table and behaves in the same way."""
	cyclic : Par
	"""Menu : Adapts the range of the Lookup Table (2nd input) for cyclic or non-cyclic input indices. When using a cyclic input index (1st input), the lookup value for index 0.0 and 1.0 result in the same value. To avoid this, set Cyclic Range to Yes and the lookup will cycle smoothly."""
	chanmatch : Par
	"""Menu : Determines how index channels are mapped to lookup Channel tables."""
	match : Par
	"""Menu : Determines how index channels are matched with a lookup channel in 'One Lookup Table Channel' mode."""
	par : parameter.lookupCHOP
	"""Parameters of parameter.lookupCHOP"""
	pass


class ltcinCHOP():
	"""ltcinCHOP"""
	par : parameter.ltcinCHOP
	"""Parameters of parameter.ltcinCHOP"""
	pass


class ltcoutCHOP():
	"""ltcoutCHOP"""
	playmode : Par
	"""Menu : Specifies the method used to output LTC, there are 2 options."""
	par : parameter.ltcoutCHOP
	"""Parameters of parameter.ltcoutCHOP"""
	pass


class mathCHOP():
	"""mathCHOP"""
	preop : Par
	"""Menu : Unary operations can be performed on individual channels. A menu of unary operations (as described above) that are performed on each channel as it comes in to the Math CHOP include:"""
	chanop : Par
	"""Menu : A choice of operations is performed between the channels of an input CHOP, for each input. The Nth sample of one channel is combined with the Nth sample of other channels:"""
	chopop : Par
	"""Menu : A menu of operations that is performed between the input CHOPs, combining several CHOPs into one."""
	postop : Par
	"""Menu : A menu (same as Channel Pre OP) is performed as the finale stage upon the channels resulting from the above operations."""
	match : Par
	"""Menu : Match channels between inputs by name or index."""
	align : Par
	"""Menu : This menu handles cases where multiple input CHOPs have different start or end times. All channels output from a CHOP share the same start/end interval, so the inputs must be treated with the Align Options:"""
	integer : Par
	"""Menu : The resulting values can be converted to integer."""
	fromrange1 : Par
	"""Another way to multiply/add. Converts from one low-high range to another range."""
	fromrange2 : Par
	"""Another way to multiply/add. Converts from one low-high range to another range."""
	torange1 : Par
	"""Another way to multiply/add. Converts from one low-high range to another range."""
	torange2 : Par
	"""Another way to multiply/add. Converts from one low-high range to another range."""
	par : parameter.mathCHOP
	"""Parameters of parameter.mathCHOP"""
	pass


class mergeCHOP():
	"""mergeCHOP"""
	align : Par
	"""Menu : This menu handles cases where multiple input CHOPs have different start or end times. All channels output from a CHOP share the same start/end interval, so the inputs must be treated with the Align Options:"""
	duplicate : Par
	"""Menu : When channels of the input CHOPs have the same name, this menu determines what to do."""
	par : parameter.mergeCHOP
	"""Parameters of parameter.mergeCHOP"""
	pass


class midiinCHOP():
	"""midiinCHOP"""
	source : Par
	"""Menu : Get MIDI input from a device or a file."""
	recordtype : Par
	"""Menu : Determine what to record."""
	notemeth : Par
	"""Menu : Describes how multiple notes are handled. (As one channel, or individual)."""
	velocity : Par
	"""Menu : Describes how multiple velocity events are recorded. (Separate channels or combined in one channel as separate samples)."""
	notenorm : Par
	"""Menu : Note values can be normalized for convenience:"""
	controltype : Par
	"""Menu : There are 128 different controllers available. By choosing By Index Only, you can specify any number of controllers in the Control Index parameter. Otherwise, you can select a controller from the list from this menu. Some controllers have multiple instances, such as Sound Controllers 1-10. Selecting a controller with multiple instances allows you to use the Control Index parameter to select which instances you want. Any invalid control indices will be ignored."""
	format : Par
	"""Menu : Some controllers can be paired together to form 14 bit controllers, rather than the normal 7 bit controllers (controller indices 0-31, 98 and 100). Selecting 14 bit Controllers interprets a pair as one 14 bit controller. Otherwise, they are interpreted as separate 7 bit Controllers."""
	norm : Par
	"""Menu : Controller values can be normalized for convenience:"""
	startunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	endunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	left : Par
	"""Menu : The left extend conditions (before range)."""
	right : Par
	"""Menu : The right extend conditions (after range)."""
	par : parameter.midiinCHOP
	"""Parameters of parameter.midiinCHOP"""
	pass


class midiinmapCHOP():
	"""midiinmapCHOP"""
	left : Par
	"""Menu : """
	right : Par
	"""Menu : """
	par : parameter.midiinmapCHOP
	"""Parameters of parameter.midiinmapCHOP"""
	pass


class midioutCHOP():
	"""midioutCHOP"""
	destination : Par
	"""Menu : Where the MIDI events are sent to. MIDI Mapper is the default destination."""
	autonoteoff : Par
	"""Menu : A MIDI 'All Note Off' event can be sent upon the start and/or end of the output."""
	notenorm : Par
	"""Menu : Values in the range 0-1 are mapped to MIDI value 0-127."""
	controlformat : Par
	"""Menu : Sends 7 or 14 bit controller events."""
	controlnorm : Par
	"""Menu : Maps channel values from different ranges to 0-127."""
	par : parameter.midioutCHOP
	"""Parameters of parameter.midioutCHOP"""
	pass


class mosysCHOP():
	"""mosysCHOP"""
	protocol : Par
	"""Menu : The network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	par : parameter.mosysCHOP
	"""Parameters of parameter.mosysCHOP"""
	pass


class mouseinCHOP():
	"""mouseinCHOP"""
	active : Par
	"""Menu : While '''On''', the mouse movement will be output from and the CHOP will cook every frame. When set to '''Off''' it will not cook and the current mouse X or Y values will not be output. '''While Playing''' will capture mouse events only when the [[Timeline]] is playing forward."""
	output : Par
	"""Menu : Controls the range of the mouse Position X and Position Y."""
	left : Par
	"""Menu : The left extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.mouseinCHOP
	"""Parameters of parameter.mouseinCHOP"""
	pass


class mouseoutCHOP():
	"""mouseoutCHOP"""
	par : parameter.mouseoutCHOP
	"""Parameters of parameter.mouseoutCHOP"""
	pass


class natnetinCHOP():
	"""natnetinCHOP"""
	connectiontype : Par
	"""Menu : Set this to the connection mode the server is set to."""
	par : parameter.natnetinCHOP
	"""Parameters of parameter.natnetinCHOP"""
	pass


class ncamCHOP():
	"""ncamCHOP"""
	protocol : Par
	"""Menu : """
	cameraview : Par
	"""Menu : Select how the camera's orientation and position are outputted."""
	cameraproj : Par
	"""Menu : Select how the camera's projection settings are outputted."""
	cameraprops : Par
	"""Menu : Controls the output of additional camera properties like zoom and focus. These properties can either be normalized (0 to 1) or in their native physical units."""
	timecode : Par
	"""Menu : Select whether the embedded timecode is presented as a single counter or in separate hour, minute, second and frame channels."""
	par : parameter.ncamCHOP
	"""Parameters of parameter.ncamCHOP"""
	pass


class noiseCHOP():
	"""noiseCHOP"""
	type : Par
	"""Menu : The noise function used to generate noise. The functions available are:"""
	xord : Par
	"""Menu : Changing the Transform Order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as T * R * S * Position"""
	rord : Par
	"""Menu : As with transform order (above), changing the order in which the rotations take place will alter the final position and orientation. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows R = Rz * Ry * Rx"""
	tx : Par
	"""XYZ translation values."""
	ty : Par
	"""XYZ translation values."""
	tz : Par
	"""XYZ translation values."""
	rx : Par
	"""XYZ rotation, in degrees."""
	ry : Par
	"""XYZ rotation, in degrees."""
	rz : Par
	"""XYZ rotation, in degrees."""
	sx : Par
	"""XYZ scale to shrink or enlarge the transform."""
	sy : Par
	"""XYZ scale to shrink or enlarge the transform."""
	sz : Par
	"""XYZ scale to shrink or enlarge the transform."""
	px : Par
	"""XYZ pivot to apply the above operations around."""
	py : Par
	"""XYZ pivot to apply the above operations around."""
	pz : Par
	"""XYZ pivot to apply the above operations around."""
	constraint : Par
	"""Menu : Constraint and its parameters allows the noise curve to start and/or end at selected values. The mean value may also be enforced. '''Note:''' This only works when Time Slice is Off because time slicing has no pre-determined start/end."""
	left : Par
	"""Menu : The left extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.noiseCHOP
	"""Parameters of parameter.noiseCHOP"""
	pass


class nullCHOP():
	"""nullCHOP"""
	cooktype : Par
	"""Menu : This controls how nodes downstream from the Null CHOP are triggered for recooking when the Null CHOP output changes. See also: [[Cook]]"""
	par : parameter.nullCHOP
	"""Parameters of parameter.nullCHOP"""
	pass


class oakdeviceCHOP():
	"""oakdeviceCHOP"""
	outtimercount : Par
	"""Menu : """
	outrunningcount : Par
	"""Menu : Outputs the "wall-clock" time since Start occurred, no matter if the device's <code>Play</code> parameter was turned off or not. Will stop counting when the <code>Done</code> state has been reached."""
	par : parameter.oakdeviceCHOP
	"""Parameters of parameter.oakdeviceCHOP"""
	pass


class oakselectCHOP():
	"""oakselectCHOP"""
	outputformat : Par
	"""Menu : The default option "Items As Separate Channels" enables time-slicing while "Items as Separate Samples" does not. If the stream is one which automatically fills in the CHOP, then "Items as Separate Samples" is a useful way to make the CHOP output '''Max Items''' samples consistently."""
	par : parameter.oakselectCHOP
	"""Parameters of parameter.oakselectCHOP"""
	pass


class objectCHOP():
	"""objectCHOP"""
	compute : Par
	"""Menu : Specify the information to output from the objects as described in the parameters below. Except for 'measurements', these match the standard transform formats as described by the [[Transform CHOP]]."""
	xord : Par
	"""Menu : The transform order to use for Rotation, Scale, Transform, Bearing, or Single Bearing Angle <span class="tipTextCHOP">Compute</span> modes."""
	rord : Par
	"""Menu : The rotation order to use for Rotation, Scale, Transform, Bearing, or Single Bearing Angle <span class="tipTextCHOP">Compute</span> modes."""
	bearingref : Par
	"""Menu : Bearing requires a direction to use as a reference base."""
	bearingx : Par
	"""An arbitrary base direction for the bearing calculation."""
	bearingy : Par
	"""An arbitrary base direction for the bearing calculation."""
	bearingz : Par
	"""An arbitrary base direction for the bearing calculation."""
	nameformat : Par
	"""Menu : Sets how the created channels are named."""
	outputrange : Par
	"""Menu : The start and end time of the desired interval of the object path."""
	left : Par
	"""Menu : The extend condition before the CHOP interval. They are:"""
	right : Par
	"""Menu : Extend condition after the interval. Same options as Extend Left."""
	par : parameter.objectCHOP
	"""Parameters of parameter.objectCHOP"""
	pass


class oculusaudioCHOP():
	"""oculusaudioCHOP"""
	bandhint : Par
	"""Menu : If the audio source content is known, this parameter can be set to improve overall sound quality."""
	attenuation : Par
	"""Menu : Select attentuation calculation between the audio source and listener (head)."""
	roomsizex : Par
	"""Sets the size of the box room."""
	roomsizey : Par
	"""Sets the size of the box room."""
	roomsizez : Par
	"""Sets the size of the box room."""
	par : parameter.oculusaudioCHOP
	"""Parameters of parameter.oculusaudioCHOP"""
	pass


class oculusriftCHOP():
	"""oculusriftCHOP"""
	output : Par
	"""Menu : Switches between three different output modes."""
	par : parameter.oculusriftCHOP
	"""Parameters of parameter.oculusriftCHOP"""
	pass


class openvrCHOP():
	"""openvrCHOP"""
	output : Par
	"""Menu : Controls what kind of category of data will be output from this node."""
	skeletonrange : Par
	"""Menu : Controls the range of motion of the skeleton values."""
	par : parameter.openvrCHOP
	"""Parameters of parameter.openvrCHOP"""
	pass


class oscinCHOP():
	"""oscinCHOP"""
	protocol : Par
	"""Menu : The network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	par : parameter.oscinCHOP
	"""Parameters of parameter.oscinCHOP"""
	pass


class oscoutCHOP():
	"""oscoutCHOP"""
	protocol : Par
	"""Menu : Selects the network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	numericformat : Par
	"""Menu : Choose the data format to send data between 32-bit integer, 32-bit float, or 64-bit double."""
	format : Par
	"""Menu : Specify how to format the outgoing messages."""
	par : parameter.oscoutCHOP
	"""Parameters of parameter.oscoutCHOP"""
	pass


class outCHOP():
	"""outCHOP"""
	par : parameter.outCHOP
	"""Parameters of parameter.outCHOP"""
	pass


class overrideCHOP():
	"""overrideCHOP"""
	match : Par
	"""Menu : Monitors the channels in each input and matches them according to this menu."""
	par : parameter.overrideCHOP
	"""Parameters of parameter.overrideCHOP"""
	pass


class panelCHOP():
	"""panelCHOP"""
	par : parameter.panelCHOP
	"""Parameters of parameter.panelCHOP"""
	pass


class pangolinCHOP():
	"""pangolinCHOP"""
	source : Par
	"""Menu : Select the source operator."""
	ratemode : Par
	"""Menu : Select the mode for calculating the rate of the image in Beyond. Note: this is not the rate of the CHOP."""
	par : parameter.pangolinCHOP
	"""Parameters of parameter.pangolinCHOP"""
	pass


class parameterCHOP():
	"""parameterCHOP"""
	nameformat : Par
	""" : Channels can be named suitably for multi-exporting. See [[CHOP_Export]]."""
	par : parameter.parameterCHOP
	"""Parameters of parameter.parameterCHOP"""
	pass


class patternCHOP():
	"""patternCHOP"""
	wavetype : Par
	"""Menu : The shape of one cycle of the pattern."""
	taper1 : Par
	"""Two parameters to multiply by a line from <code>taper1</code> at the start to <code>taper2</code> at the end. The default of (<code>1 1</code>) has no effect."""
	taper2 : Par
	"""Two parameters to multiply by a line from <code>taper1</code> at the start to <code>taper2</code> at the end. The default of (<code>1 1</code>) has no effect."""
	fromrange1 : Par
	"""A value at each From Range will become its corresponding To Range value."""
	fromrange2 : Par
	"""A value at each From Range will become its corresponding To Range value."""
	torange1 : Par
	"""A value at each From Range will become its corresponding To Range value."""
	torange2 : Par
	"""A value at each From Range will become its corresponding To Range value."""
	integer : Par
	"""Menu : A round-off menu to convert all numbers to integers."""
	combine : Par
	"""Menu : If an input CHOP is attached, it adopts the length and sample rate of the input CHOP, and"""
	left : Par
	"""Menu : The left right extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.patternCHOP
	"""Parameters of parameter.patternCHOP"""
	pass


class performCHOP():
	"""performCHOP"""
	par : parameter.performCHOP
	"""Parameters of parameter.performCHOP"""
	pass


class phaserCHOP():
	"""phaserCHOP"""
	outputformat : Par
	"""Menu : Specifies the format of the output."""
	par : parameter.phaserCHOP
	"""Parameters of parameter.phaserCHOP"""
	pass


class pipeinCHOP():
	"""pipeinCHOP"""
	mode : Par
	"""Menu : Set operation as server or client."""
	echo : Par
	"""Menu : Print all incoming commands (not channel data) to the Console which can be opened from the Dialogs menu. A good way to test a connection is to put "<code>echo X</code>" commands in the incoming stream."""
	par : parameter.pipeinCHOP
	"""Parameters of parameter.pipeinCHOP"""
	pass


class pipeoutCHOP():
	"""pipeoutCHOP"""
	mode : Par
	"""Menu : Set operation as server or client."""
	sample : Par
	"""Menu : In single sample mode, this parameter determines which sample to send; the sample at frame 1 or the current sample."""
	par : parameter.pipeoutCHOP
	"""Parameters of parameter.pipeoutCHOP"""
	pass


class posistagenetCHOP():
	"""posistagenetCHOP"""
	par : parameter.posistagenetCHOP
	"""Parameters of parameter.posistagenetCHOP"""
	pass


class pulseCHOP():
	"""pulseCHOP"""
	interp : Par
	"""Menu : You can interpolate the values between pulses using the following function curves:"""
	widthunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	limit : Par
	"""Menu : Enable the Minimum and Maximum clamping values below with this menu."""
	startunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	endunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	left : Par
	"""Menu : The left extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.pulseCHOP
	"""Parameters of parameter.pulseCHOP"""
	pass


class realsenseCHOP():
	"""realsenseCHOP"""
	par : parameter.realsenseCHOP
	"""Parameters of parameter.realsenseCHOP"""
	pass


class recordCHOP():
	"""recordCHOP"""
	record : Par
	"""Menu : When and how much to record:"""
	sample : Par
	"""Menu : Determines whether record should sample the time slice or the current frame. You would generally want to use Current Time Slice, for audio, as all frames will be evaluated.	
			
If the interval is set to be the Current Frame, it will always cook (only look at) the current frame (things downstream still cook regardless of this setting however). Thus, it should generally not be used for audio, but rather fro things like device input, because it interpolates the values between the captured frames."""
	interp : Par
	"""Menu : Determines how to compute missed input samples using interpolation. Using Hold Previous Value does just that; Linear and Cubic interpolation will create a mathematical blend of values in a linear (straight line between values in time), or cubic (smooth round-off curve between beginning and ending values)."""
	output : Par
	"""Menu : Determines the frame range that gets output from the CHOP."""
	segment1 : Par
	"""The data gets recorded in a fixed-range interval and the most recent data gets recorded at the end of the interval and the remaining samples get shifted toward the start of the interval. This is useful for making snakes."""
	segment2 : Par
	"""The data gets recorded in a fixed-range interval and the most recent data gets recorded at the end of the interval and the remaining samples get shifted toward the start of the interval. This is useful for making snakes."""
	resetcondition : Par
	"""Menu : Enabled when a CHOP is connected to the Record CHOP's 3rd input (ie. Input 2). Determines what condition is required to trigger a reset using this input."""
	par : parameter.recordCHOP
	"""Parameters of parameter.recordCHOP"""
	pass


class renameCHOP():
	"""renameCHOP"""
	par : parameter.renameCHOP
	"""Parameters of parameter.renameCHOP"""
	pass


class renderpickCHOP():
	"""renderpickCHOP"""
	strategy : Par
	"""Menu : Decides when to update values based on pick interactions."""
	responsetime : Par
	"""Menu : Determines when the values are updated."""
	pickingby : Par
	"""Menu : Determines how the pick location is set."""
	position : Par
	"""Menu : Returns the position of the point picked on the geometry. Channels ''tx, ty, tz''."""
	normal : Par
	"""Menu : Returns the normals of the point picked on the geometry. Channels ''nx, ny, nz''."""
	par : parameter.renderpickCHOP
	"""Parameters of parameter.renderpickCHOP"""
	pass


class renderstreaminCHOP():
	"""renderstreaminCHOP"""
	par : parameter.renderstreaminCHOP
	"""Parameters of parameter.renderstreaminCHOP"""
	pass


class reorderCHOP():
	"""reorderCHOP"""
	method : Par
	"""Menu : There are three different reordering methods. You can enter a Numeric Pattern, a Character Pattern, or use an optional second input CHOP as an order reference."""
	orderref : Par
	"""Menu : Only enabled if a second input is present. Specifies the format of that input."""
	rempos : Par
	"""Menu : Channels that do not match are called "remaining" and can also be ordered: they can be placed at the At Beginning or At Ending (in reference to the position of the matched channels)."""
	remorder : Par
	"""Menu : The channels that did not match can have the Same as Input order, or can be sorted AlphaNumerically."""
	par : parameter.reorderCHOP
	"""Parameters of parameter.reorderCHOP"""
	pass


class replaceCHOP():
	"""replaceCHOP"""
	length : Par
	"""Menu : Determines the start/end range of the output."""
	par : parameter.replaceCHOP
	"""Parameters of parameter.replaceCHOP"""
	pass


class resampleCHOP():
	"""resampleCHOP"""
	method : Par
	"""Menu : The resample method to apply to the channels:"""
	relative : Par
	"""Menu : Determines how the Start/End parameters are interpreted."""
	interp : Par
	"""Menu : The interpolation method to use when resampling:"""
	par : parameter.resampleCHOP
	"""Parameters of parameter.resampleCHOP"""
	pass


class scurveCHOP():
	"""scurveCHOP"""
	type : Par
	"""Menu : What Curve Type to Generate."""
	fromrange1 : Par
	"""Specify the low and high range of the input index."""
	fromrange2 : Par
	"""Specify the low and high range of the input index."""
	torange1 : Par
	"""Specify the low and high range of the curve."""
	torange2 : Par
	"""Specify the low and high range of the curve."""
	left : Par
	"""Menu : The left extend condition (before range)."""
	right : Par
	"""Menu : The right extend conditions (after range)."""
	par : parameter.scurveCHOP
	"""Parameters of parameter.scurveCHOP"""
	pass


class scanCHOP():
	"""scanCHOP"""
	source : Par
	""" : Choose the source node family."""
	interleave : Par
	""" : Controls the order in which rows are output to minimize flicker."""
	par : parameter.scanCHOP
	"""Parameters of parameter.scanCHOP"""
	pass


class scriptCHOP():
	"""scriptCHOP"""
	par : parameter.scriptCHOP
	"""Parameters of parameter.scriptCHOP"""
	pass


class selectCHOP():
	"""selectCHOP"""
	align : Par
	"""Menu : This menu handles cases where multiple input CHOPs have different start or end times. All channels output from a CHOP share the same start/end interval, so the inputs must be treated with the Align Options:"""
	par : parameter.selectCHOP
	"""Parameters of parameter.selectCHOP"""
	pass


class sequencerCHOP():
	"""sequencerCHOP"""
	par : parameter.sequencerCHOP
	"""Parameters of parameter.sequencerCHOP"""
	pass


class serialCHOP():
	"""serialCHOP"""
	state : Par
	"""Menu : The type of input transition to monitor."""
	port : Par
	"""StrMenu : Selects the COM port that the serial connection will use."""
	baudmenu : Par
	"""Pulse : Use this menu to select from some commonly used baud rates."""
	databits : Par
	"""Menu : This parameter sets the number of data bits sent in each. Data bits are transmitted "backwards". Backwards refers to the order of transmission, which is from least significant bit (LSB) to most significant bit (MSB). To interpret the data bits, you must read from right to left."""
	parity : Par
	"""Menu : This parameter can be set to none, even, or odd. The optional parity bit follows the data bits and is included as a simple means of error checking. Parity bits work by specifying ahead of time whether the parity of the transmission is to be even or odd. If the parity is set to be odd, the transmitter will then set the parity bit in such a way as to make an odd number of 1's among the data bits and the parity bit."""
	stopbits : Par
	"""Menu : The last part of transmission packet consists of 1 or 2 Stop bits. The connection will now wait for the next Start bit."""
	par : parameter.serialCHOP
	"""Parameters of parameter.serialCHOP"""
	pass


class sharedmeminCHOP():
	"""sharedmeminCHOP"""
	memtype : Par
	"""Menu : Reads from a Local or a Global memory location."""
	par : parameter.sharedmeminCHOP
	"""Parameters of parameter.sharedmeminCHOP"""
	pass


class sharedmemoutCHOP():
	"""sharedmemoutCHOP"""
	memtype : Par
	"""Menu : Writes to a Local or a Global memory location."""
	par : parameter.sharedmemoutCHOP
	"""Parameters of parameter.sharedmemoutCHOP"""
	pass


class shiftCHOP():
	"""shiftCHOP"""
	reference : Par
	"""Menu : The start or the end of the channels can be used as the reference position. The channels are shifted by altering the reference position."""
	relative : Par
	"""Menu : Determines how the Start and End parameters are to be interpreted:"""
	par : parameter.shiftCHOP
	"""Parameters of parameter.shiftCHOP"""
	pass


class shuffleCHOP():
	"""shuffleCHOP"""
	method : Par
	"""Menu : Chooses the operation "shuffle" performs:"""
	par : parameter.shuffleCHOP
	"""Parameters of parameter.shuffleCHOP"""
	pass


class slopeCHOP():
	"""slopeCHOP"""
	type : Par
	"""Menu : The type of slope to calculate."""
	method : Par
	"""Menu : The sample pairs used to calculate the slope."""
	par : parameter.slopeCHOP
	"""Parameters of parameter.slopeCHOP"""
	pass


class soptoCHOP():
	"""soptoCHOP"""
	par : parameter.soptoCHOP
	"""Parameters of parameter.soptoCHOP"""
	pass


class sortCHOP():
	"""sortCHOP"""
	method : Par
	"""Menu : There are three different sorting methods. CHOP samples can be reordered by increasing values, decreasing values or in random order."""
	select : Par
	"""Menu : Specify if the channels to be sorted will be specified by index or name."""
	par : parameter.sortCHOP
	"""Parameters of parameter.sortCHOP"""
	pass


class speedCHOP():
	"""speedCHOP"""
	order : Par
	"""Menu : Determines the order of the integral to use. If the input is a velocity, a First Order integral will return the position. If the input is an acceleration, a Second Order integral will return the position, and a First Order integral will return the velocity."""
	limittype : Par
	"""Menu : Select limit options such as loop, clamp, or zigzag from the menu. The value will remain in the range from Min to less than Max."""
	resetcondition : Par
	"""Menu : This menu determines how the Reset input triggers a reset of the channel(s)."""
	par : parameter.speedCHOP
	"""Parameters of parameter.speedCHOP"""
	pass


class spliceCHOP():
	"""spliceCHOP"""
	direction : Par
	"""Menu : Specify which direction the Start and Trim parameters below work."""
	trimmethod : Par
	"""Menu : Gives options for how to set the trim length."""
	insertmethod : Par
	"""Menu : Handles how the 2nd input is spliced into the channel."""
	insertinterp : Par
	"""Menu : Choose interpolation method for stretched insert channel."""
	match : Par
	"""Menu : Match channels between inputs by name or number."""
	unmatchedinterp : Par
	"""Menu : Choose interpolation method for any channels that are unmatched using "Match Channels"."""
	par : parameter.spliceCHOP
	"""Parameters of parameter.spliceCHOP"""
	pass


class springCHOP():
	"""springCHOP"""
	method : Par
	"""Menu : Determines whether the input channel(s) represents a position or a force."""
	par : parameter.springCHOP
	"""Parameters of parameter.springCHOP"""
	pass


class stretchCHOP():
	"""stretchCHOP"""
	interp : Par
	"""Menu : The interpolation method to use when resampling."""
	relative : Par
	"""Menu : Determines how Start/End parameters are interpreted:"""
	par : parameter.stretchCHOP
	"""Parameters of parameter.stretchCHOP"""
	pass


class stypeCHOP():
	"""stypeCHOP"""
	protocol : Par
	"""Menu : The network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	par : parameter.stypeCHOP
	"""Parameters of parameter.stypeCHOP"""
	pass


class stypeoutCHOP():
	"""stypeoutCHOP"""
	protocol : Par
	"""Menu : Selects the network protocol to use. Refer to the Network Protocols article for more information."""
	packetnumber : Par
	"""Menu : Determine how the packet number field is generated. The packet number generally increments by 1 each frame and loops from 255 to 0."""
	par : parameter.stypeoutCHOP
	"""Parameters of parameter.stypeoutCHOP"""
	pass


class switchCHOP():
	"""switchCHOP"""
	par : parameter.switchCHOP
	"""Parameters of parameter.switchCHOP"""
	pass


class syncinCHOP():
	"""syncinCHOP"""
	par : parameter.syncinCHOP
	"""Parameters of parameter.syncinCHOP"""
	pass


class syncoutCHOP():
	"""syncoutCHOP"""
	localportmode : Par
	"""Menu : Choose between automatically or manually selecting local port to use."""
	par : parameter.syncoutCHOP
	"""Parameters of parameter.syncoutCHOP"""
	pass


class tabletCHOP():
	"""tabletCHOP"""
	active : Par
	"""Menu : While '''On''', the pen movement will be output from and the CHOP will cook every frame. When set to '''Off''' it will not cook and the values will not be updated. '''While Playing''' will capture pen events only when the [[Timeline]] is playing forward."""
	left : Par
	"""Menu : The left extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.tabletCHOP
	"""Parameters of parameter.tabletCHOP"""
	pass


class timesliceCHOP():
	"""timesliceCHOP"""
	method : Par
	"""Menu : How to sample the input CHOP to create the output time slice. If the input CHOP is not time sliced and lies outside the current time slice region, its extend regions will be sampled."""
	par : parameter.timesliceCHOP
	"""Parameters of parameter.timesliceCHOP"""
	pass


class timecodeCHOP():
	"""timecodeCHOP"""
	mode : Par
	"""Menu : The source used for generating the timecode"""
	dropframe : Par
	"""Menu : Specify how to calculate [https://en.wikipedia.org/wiki/SMPTE_timecode#Drop-frame_timecode drop-frames]. Drop frames are used when the FPS is fractional. FPS cannot increment a fractional amount per frame so FPS is rounded to the next whole number and the accumulation of error is accommodated for by adding drop frames."""
	indexunit : Par
	"""Menu : The index value units."""
	par : parameter.timecodeCHOP
	"""Parameters of parameter.timecodeCHOP"""
	pass


class timelineCHOP():
	"""timelineCHOP"""
	par : parameter.timelineCHOP
	"""Parameters of parameter.timelineCHOP"""
	pass


class timerCHOP():
	"""timerCHOP"""
	timecontrol : Par
	"""Menu : '''Sequential''' (timeline-independent) or '''Locked to Timeline'''. In Locked to Timeline, non-deterministic features are disabled. '''External CHOP Channel''' lets you drive the master time (<code>.masterSeconds</code> etc) using a CHOP channel defined by the parameters on the External page."""
	lengthtype : Par
	"""Menu : Describes how the length is defined."""
	lengthunits : Par
	"""Menu : Choose between using Samples, Frames, or Seconds as the units for this parameter."""
	delayunits : Par
	"""Menu : Choose between using Samples, Frames, or Seconds as the units for this parameter."""
	cueunits : Par
	"""Menu : Choose between using Samples, Frames, Seconds, Fraction(0-1) as the units for this parameter."""
	notifyunits : Par
	"""Menu : Choose between using Samples, Frames, or Seconds as the units for this parameter."""
	ondone : Par
	"""Menu : Determines which action to take when the timer gets to the end, ie "is done" or finished. Note there is also a onDone callback that can be used for customizing behavior."""
	segmethod : Par
	"""Menu : If the Segment Method is '''Serial Timers''', the timers will be played back-to-back. If the Segment Method is '''Parallel Timers''', the timers can be played at the same time, and a set of channels will be output for each timer."""
	segunits : Par
	"""Menu : For the columns <code>delay</code>, <code>begin</code>, <code>length</code> and <code>cycleendalert</code>, you specify whether it’s seconds, frames or samples with this menu."""
	segsendtime : Par
	"""Menu : Describes how the end time is calculated."""
	interpolation : Par
	"""Menu : By default, custom channels step to their new value at the begin of the segment. This menu lets you interpolate to the new value linearly, or any combination of ease-in and ease-out."""
	substartunits : Par
	"""Menu : Choose between using Samples, Frames, or Seconds as the units for this parameter."""
	subendunits : Par
	"""Menu : Choose between using Samples, Frames, or Seconds as the units for this parameter."""
	subendaction : Par
	"""Menu : Controls the behavior once the sub range end point is reached: Loop at End, or Pause at End."""
	outtimercount : Par
	"""Menu : Outputs the elapsed Seconds channel as <code>timer_seconds</code>, Frames outputs channel as <code>timer_frames</code>, or Samples outputs channel as <code>timer_samples</code>. Because this is elapsed time, <code>timer_frames</code> starts at 0, as do the others."""
	outdelaycount : Par
	"""Menu : Outputs the delay count in seconds, frames or samples."""
	outlength : Par
	"""Menu : Outputs channel <code>length</code>, starting with 0 for first segment ending at #segments at end."""
	outcumulativecount : Par
	"""Menu : Outputs <code>cumulative_seconds</code>, <code>cumulative_frames</code> or <code>cumulative_samples</code>. It is a time count that adds up all the Timer Active times for all segments since Start: it is affected by "Speed", and counts up only while <code>timer_active</code> (Play) is on.   See the python member <code>.cumulativeSeconds</code>."""
	outplayingcount : Par
	"""Menu : Outputs <code>playing_seconds</code>, <code>playing_frames</code> or <code>playing_samples</code>. It is a time count that adds up all the Timer Active times for all segments since Start: it is not affected by "Speed", and counts up only while <code>timer_active</code> and <code>play</code> is on.  See the python member <code>.playingSeconds</code>."""
	outrunningcount : Par
	"""Menu : Outputs the "wall-clock" time since Start occurred, no matter what are the delays, speeds, cycles or pre-mature clicking of Go To Segment End, etc. It stops counting when Done has been reached. <code>running_seconds</code>, <code>running_frames</code>, or <code>running_samples</code>. When CHOP is set to Parallel Timers, this will output a channel per segment plus one global running time channel.   See the python member <code>.runningSeconds</code>."""
	outmastercount : Par
	"""Menu : Outputs <code>master_seconds</code>, <code>master_frames</code> or <code>master_samples</code>. It is a time count that adds up all the Timer Active times for all segments since Start: it is affected by "Speed", and counts up only while <code>timer_active</code> and <code>play</code> is on. It also includes any delay times.   See the python member <code>.masterSeconds</code>."""
	extunits : Par
	"""Menu : Choose between using Samples, Frames, or Seconds as the units for this parameter."""
	par : parameter.timerCHOP
	"""Parameters of parameter.timerCHOP"""
	pass


class toptoCHOP():
	"""toptoCHOP"""
	downloadtype : Par
	"""Menu : Gives the option for a delayed data download from the GPU, which is much faster and does not stall the render."""
	activechannel : Par
	"""Menu : When enabled, only pixels that have a non-zero value in the selected active channel will be added to the CHOP channel."""
	rgbaunit : Par
	"""Menu : Scales the output to lie in the range 0-1, 0-255 or 0-65535."""
	crop : Par
	"""Menu : Specifies what to extract from the image."""
	uvunits : Par
	"""Menu : Specifies the units for the following 4 parameters. The parameters can use the local variables <code>$NR</code> and <code>$NC</code> for the number of rows and columns."""
	interp : Par
	"""Menu : Determines the interpolation method when UV sampling with an input CHOP."""
	imageleft : Par
	"""Menu : The image extend conditions when sampling the image with U less than 0."""
	imageright : Par
	"""Menu : The image extend conditions for U greater than 1."""
	imagebottom : Par
	"""Menu : The image extend conditions for V less than 0."""
	imagetop : Par
	"""Menu : The image extend conditions for V greater than 1.	
			
The extend conditions are:"""
	defcolorr : Par
	"""The color to use when outside the bounds of the image, and the Default Color extend condition is set."""
	defcolorg : Par
	"""The color to use when outside the bounds of the image, and the Default Color extend condition is set."""
	defcolorb : Par
	"""The color to use when outside the bounds of the image, and the Default Color extend condition is set."""
	defcolora : Par
	"""The color to use when outside the bounds of the image, and the Default Color extend condition is set."""
	startunit : Par
	"""Menu : Select the units to use for this parameter, Samples, Frames, or Seconds."""
	left : Par
	"""Menu : The left extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.toptoCHOP
	"""Parameters of parameter.toptoCHOP"""
	pass


class touchinCHOP():
	"""touchinCHOP"""
	protocol : Par
	"""Menu : Selects which network protocol to use to transfer data. Different protocol's have methods of connecting and using the address parameter. For more information refer to the [[Network Protocols]] article."""
	syncports : Par
	"""Menu : This parameter lets you send the the data in a single global pipe if required. This can be important if various data streams must be sent in frame sync."""
	par : parameter.touchinCHOP
	"""Parameters of parameter.touchinCHOP"""
	pass


class touchoutCHOP():
	"""touchoutCHOP"""
	protocol : Par
	"""Menu : Selects which network protocol to use to transfer data. Different protocol's have methods of connecting and using the address parameter. For more information refer to the [[Network Protocols]] article."""
	syncports : Par
	"""Menu : This parameter lets you send the the data in a single global pipe if required. This can be important if various data streams must be sent in frame sync."""
	par : parameter.touchoutCHOP
	"""Parameters of parameter.touchoutCHOP"""
	pass


class trailCHOP():
	"""trailCHOP"""
	capture : Par
	"""Menu : Determines when to capture values."""
	par : parameter.trailCHOP
	"""Parameters of parameter.trailCHOP"""
	pass


class transformCHOP():
	"""transformCHOP"""
	inxord : Par
	"""Menu : Changing the Transform order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as T * R * S * Position"""
	inrord : Par
	"""Menu : As with transform order (above), changing the order in which the rotations take place will alter the final position and orientation. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows R = Rz * Ry * Rx"""
	input0preop : Par
	"""Menu : Operation(s) to apply on the transforms on Input 0, before they are combined with other transforms."""
	input1preop : Par
	"""Menu : Operation(s) to apply on the transforms on Input 1, before they are combined with other transforms."""
	inputoperation : Par
	"""Menu : The operation that should be applied between transforms coming from Input 0 and Input 1. Refer to the main description of this node for an explanation of how multiple samples and/or transform sets are combined between the two inputs."""
	xord : Par
	"""Menu : See description from earlier Transform Order parameter."""
	rord : Par
	"""Menu : See description from earlier Rotate Order parameter."""
	tx : Par
	"""XYZ translation values."""
	ty : Par
	"""XYZ translation values."""
	tz : Par
	"""XYZ translation values."""
	rx : Par
	"""XYZ rotation, in degrees."""
	ry : Par
	"""XYZ rotation, in degrees."""
	rz : Par
	"""XYZ rotation, in degrees."""
	sx : Par
	"""XYZ scale to shrink or enlarge the transform."""
	sy : Par
	"""XYZ scale to shrink or enlarge the transform."""
	sz : Par
	"""XYZ scale to shrink or enlarge the transform."""
	px : Par
	"""XYZ pivot to apply the above operations around."""
	py : Par
	"""XYZ pivot to apply the above operations around."""
	pz : Par
	"""XYZ pivot to apply the above operations around."""
	preop : Par
	"""Menu : Operation(s) to apply on the transforms generated by the above parameters, before it is combined with other transforms."""
	multiplyorder : Par
	"""Menu : Controls how the input transform(s) are combined with the transform specified on this page. The below two descriptions use a multiply "vector on the right" convention (column vectors)."""
	postop : Par
	"""Menu : Optionally applied one last operation to the final generated transform before it is output."""
	output : Par
	"""Menu : Specify the format the transform will be output in."""
	unmatchedchans : Par
	"""Menu : Controls how channels that don't match the naming convention for the various transform format are treated."""
	outxord : Par
	"""Menu : See description from earlier Transform Order parameter."""
	outrord : Par
	"""Menu : See description from earlier Rotate Order parameter."""
	hintx : Par
	"""Specify approximate starting values for the rotation channels produced."""
	hinty : Par
	"""Specify approximate starting values for the rotation channels produced."""
	hintz : Par
	"""Specify approximate starting values for the rotation channels produced."""
	par : parameter.transformCHOP
	"""Parameters of parameter.transformCHOP"""
	pass


class transformxyzCHOP():
	"""transformxyzCHOP"""
	input0type : Par
	"""Menu : Choose if the input 0 values should be treated as a position or a vectors. Vectors will not have the translation portion of the transform applied to them, and can be normalized before and/or after the transformation is applied."""
	inxord : Par
	"""Menu : Changing the Transform order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block. In matrix math terms, if we use the 'multiply vector on the right' (column vector) convention, a transform order of Scale, Rotate, Translate would be written as T * R * S * Position"""
	inrord : Par
	"""Menu : As with transform order (above), changing the order in which the rotations take place will alter the final position and orientation. A Rotation order of Rx Ry Rz would create the final rotation matrix as follows R = Rz * Ry * Rx"""
	input1preop : Par
	"""Menu : Operation(s) to apply on the transforms on Input 1, before they are combined with other transforms."""
	xord : Par
	"""Menu : See description from earlier Transform Order parameter."""
	rord : Par
	"""Menu : See description from earlier Rotate Order parameter."""
	tx : Par
	"""XYZ translation values."""
	ty : Par
	"""XYZ translation values."""
	tz : Par
	"""XYZ translation values."""
	rx : Par
	"""XYZ rotation, in degrees."""
	ry : Par
	"""XYZ rotation, in degrees."""
	rz : Par
	"""XYZ rotation, in degrees."""
	sx : Par
	"""XYZ scale to shrink or enlarge the transform."""
	sy : Par
	"""XYZ scale to shrink or enlarge the transform."""
	sz : Par
	"""XYZ scale to shrink or enlarge the transform."""
	px : Par
	"""XYZ pivot to apply the above operations around."""
	py : Par
	"""XYZ pivot to apply the above operations around."""
	pz : Par
	"""XYZ pivot to apply the above operations around."""
	multiplyorder : Par
	"""Menu : Controls how the input transform(s) are combined with the transform specified on this page. The below two descriptions use a multiply "vector on the right" convention (column vectors)."""
	unmatchedchans : Par
	"""Menu : Controls how channels that don't match the naming convention for the various transform format are treated."""
	par : parameter.transformxyzCHOP
	"""Parameters of parameter.transformxyzCHOP"""
	pass


class triggerCHOP():
	"""triggerCHOP"""
	triggeron : Par
	"""Menu : Determines whether a trigger occurs on an increasing slope or decreasing slope when passing the trigger threshold. A release will occur on the opposite slope."""
	ashape : Par
	"""Menu : The shape of the attack ramp."""
	dshape : Par
	"""Menu : The shape of the decay ramp."""
	rshape : Par
	"""Menu : The shape of the release ramp."""
	remainder : Par
	"""Menu : See Remainder Options. What to do with remaining samples at end of the interval:"""
	par : parameter.triggerCHOP
	"""Parameters of parameter.triggerCHOP"""
	pass


class trimCHOP():
	"""trimCHOP"""
	relative : Par
	"""Menu : Determines whether the Start/End parameters are expressed as absolute numbers (relative to time 0) or numbers that are relative to the start and end of the input channels."""
	discard : Par
	"""Menu : Which part of the channel to discard:"""
	par : parameter.trimCHOP
	"""Parameters of parameter.trimCHOP"""
	pass


class warpCHOP():
	"""warpCHOP"""
	method : Par
	"""Menu : The warping method to use: <span class="tipTextCHOP">Rate</span> or <span class="tipTextCHOP">Index Control</span>."""
	par : parameter.warpCHOP
	"""Parameters of parameter.warpCHOP"""
	pass


class waveCHOP():
	"""waveCHOP"""
	wavetype : Par
	"""Menu : There is a choice of waveforms shapes:"""
	left : Par
	"""Menu : The left extend conditions (before/after range)."""
	right : Par
	"""Menu : The right extend conditions (before/after range)."""
	par : parameter.waveCHOP
	"""Parameters of parameter.waveCHOP"""
	pass


class wrnchaiCHOP():
	"""wrnchaiCHOP"""
	gpu : Par
	"""Menu : A menu of available GPU(s) to run wrnchAI on. Selecting 'Default' uses the same GPU TouchDesigner is currently running on."""
	par : parameter.wrnchaiCHOP
	"""Parameters of parameter.wrnchaiCHOP"""
	pass


class zedCHOP():
	"""zedCHOP"""
	referenceframe : Par
	""" : Selects the reference frame for plane position."""
	par : parameter.zedCHOP
	"""Parameters of parameter.zedCHOP"""
	pass


class alignSOP():
	"""alignSOP"""
	align : Par
	"""Menu : Can optionally align subgroups of ''n'' primitives or every ''n''th primitive in a cyclical manner."""
	leftuv1 : Par
	"""Pivot Location for each "left" primitive."""
	leftuv2 : Par
	"""Pivot Location for each "left" primitive."""
	rightuv1 : Par
	"""Pivot location for each "right" primitive."""
	rightuv2 : Par
	"""Pivot location for each "right" primitive."""
	rightuvend1 : Par
	"""If an auxiliary input is used, this location specifies an end point for the alignment. Left primitives are then distributed uniformly between the <code>Right UV</code> and the <code>Right UV End</code>."""
	rightuvend2 : Par
	"""If an auxiliary input is used, this location specifies an end point for the alignment. Left primitives are then distributed uniformly between the <code>Right UV</code> and the <code>Right UV End</code>."""
	xord : Par
	"""Menu : Sets the overall transform and rotation order for the transformations. The transform and rotation order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values."""
	rord : Par
	"""Menu : Sets the overall transform and rotation order for the transformations. The transform and rotation order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values."""
	tx : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of translation about the local <code>xyz</code> axes."""
	ty : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of translation about the local <code>xyz</code> axes."""
	tz : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of translation about the local <code>xyz</code> axes."""
	rx : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of rotation about the local <code>xyz</code> axes."""
	ry : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of rotation about the local <code>xyz</code> axes."""
	rz : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of rotation about the local <code>xyz</code> axes."""
	sx : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of scaling about the local <code>xyz</code> axes."""
	sy : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of scaling about the local <code>xyz</code> axes."""
	sz : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of scaling about the local <code>xyz</code> axes."""
	px : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of translation / rotation / scaling about the local <code>xyz</code> axes"""
	py : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of translation / rotation / scaling about the local <code>xyz</code> axes"""
	pz : Par
	"""Allows you to perform a post-alignment transformation. Specify the amount of translation / rotation / scaling about the local <code>xyz</code> axes"""
	par : parameter.alignSOP
	"""Parameters of parameter.alignSOP"""
	pass


class armSOP():
	"""armSOP"""
	capttype : Par
	"""Menu : You can use either '''Ellipses''' or '''Capture Regions''' as deformation geometry. Ellipses are for use with the Skeleton SOP. Capture Regions are for use with the Capture SOP."""
	axis : Par
	"""Menu : Position the model along the +X or -X axis."""
	shoulder1tx : Par
	"""The X, Z position of the first shoulder circle, as well as its overall scale."""
	shoulder1ty : Par
	"""The X, Z position of the first shoulder circle, as well as its overall scale."""
	shoulder1tz : Par
	"""The X, Z position of the first shoulder circle, as well as its overall scale."""
	shoulder2tx : Par
	"""The X, Z position of the second shoulder circle, as well as its overall scale."""
	shoulder2ty : Par
	"""The X, Z position of the second shoulder circle, as well as its overall scale."""
	shoulder2tz : Par
	"""The X, Z position of the second shoulder circle, as well as its overall scale."""
	shoulder3tx : Par
	"""The X, Z position of the third shoulder circle, as well as its overall scale."""
	shoulder3ty : Par
	"""The X, Z position of the third shoulder circle, as well as its overall scale."""
	shoulder3tz : Par
	"""The X, Z position of the third shoulder circle, as well as its overall scale."""
	shoulder4tx : Par
	"""The X, Z position of the fourth shoulder circle, as well as its overall scale."""
	shoulder4ty : Par
	"""The X, Z position of the fourth shoulder circle, as well as its overall scale."""
	shoulder4tz : Par
	"""The X, Z position of the fourth shoulder circle, as well as its overall scale."""
	shoulder5tx : Par
	"""The X, Z position of the fifth shoulder circle, as well as its overall scale."""
	shoulder5ty : Par
	"""The X, Z position of the fifth shoulder circle, as well as its overall scale."""
	shoulder5tz : Par
	"""The X, Z position of the fifth shoulder circle, as well as its overall scale."""
	elbow1tx : Par
	"""The X, Z position of the first elbow circle, as well as its overall scale."""
	elbow1ty : Par
	"""The X, Z position of the first elbow circle, as well as its overall scale."""
	elbow1tz : Par
	"""The X, Z position of the first elbow circle, as well as its overall scale."""
	elbow2tx : Par
	"""The X, Z position of the second elbow circle, as well as its overall scale."""
	elbow2ty : Par
	"""The X, Z position of the second elbow circle, as well as its overall scale."""
	elbow2tz : Par
	"""The X, Z position of the second elbow circle, as well as its overall scale."""
	elbow3tx : Par
	"""The X, Z position of the third elbow circle, as well as its overall scale."""
	elbow3ty : Par
	"""The X, Z position of the third elbow circle, as well as its overall scale."""
	elbow3tz : Par
	"""The X, Z position of the third elbow circle, as well as its overall scale."""
	elbow4tx : Par
	"""The X, Z position of the fourth elbow circle, as well as its overall scale."""
	elbow4ty : Par
	"""The X, Z position of the fourth elbow circle, as well as its overall scale."""
	elbow4tz : Par
	"""The X, Z position of the fourth elbow circle, as well as its overall scale."""
	elbow5tx : Par
	"""The X, Z position of the fifth elbow circle, as well as its overall scale."""
	elbow5ty : Par
	"""The X, Z position of the fifth elbow circle, as well as its overall scale."""
	elbow5tz : Par
	"""The X, Z position of the fifth elbow circle, as well as its overall scale."""
	wrist1tx : Par
	"""The X, Z position of the first wrist circle, as well as its overall scale."""
	wrist1ty : Par
	"""The X, Z position of the first wrist circle, as well as its overall scale."""
	wrist1tz : Par
	"""The X, Z position of the first wrist circle, as well as its overall scale."""
	wrist2tx : Par
	"""The X, Z position of the second wrist circle, as well as its overall scale."""
	wrist2ty : Par
	"""The X, Z position of the second wrist circle, as well as its overall scale."""
	wrist2tz : Par
	"""The X, Z position of the second wrist circle, as well as its overall scale."""
	wrist3tx : Par
	"""The X, Z position of the third wrist circle, as well as its overall scale."""
	wrist3ty : Par
	"""The X, Z position of the third wrist circle, as well as its overall scale."""
	wrist3tz : Par
	"""The X, Z position of the third wrist circle, as well as its overall scale."""
	wrist4tx : Par
	"""The X, Z position of the fourth wrist circle, as well as its overall scale."""
	wrist4ty : Par
	"""The X, Z position of the fourth wrist circle, as well as its overall scale."""
	wrist4tz : Par
	"""The X, Z position of the fourth wrist circle, as well as its overall scale."""
	wrist5tx : Par
	"""The X, Z position of the fifth wrist circle, as well as its overall scale."""
	wrist5ty : Par
	"""The X, Z position of the fifth wrist circle, as well as its overall scale."""
	wrist5tz : Par
	"""The X, Z position of the fifth wrist circle, as well as its overall scale."""
	tx : Par
	"""End Affector Translation. For a full explanation of transforms, see the [[Transform SOP]]."""
	ty : Par
	"""End Affector Translation. For a full explanation of transforms, see the [[Transform SOP]]."""
	tz : Par
	"""End Affector Translation. For a full explanation of transforms, see the [[Transform SOP]]."""
	rx : Par
	"""End Affector Rotation. For a full explanation of transforms, see the [[Transform SOP]]."""
	ry : Par
	"""End Affector Rotation. For a full explanation of transforms, see the [[Transform SOP]]."""
	rz : Par
	"""End Affector Rotation. For a full explanation of transforms, see the [[Transform SOP]]."""
	sx : Par
	"""End Affector Scale. For a full explanation of transforms, see the [[Transform SOP]]."""
	sy : Par
	"""End Affector Scale. For a full explanation of transforms, see the [[Transform SOP]]."""
	sz : Par
	"""End Affector Scale. For a full explanation of transforms, see the [[Transform SOP]]."""
	par : parameter.armSOP
	"""Parameters of parameter.armSOP"""
	pass


class basisSOP():
	"""basisSOP"""
	uparmtype : Par
	"""Menu : Select the method of parameterization in u from the options below."""
	urange1 : Par
	"""Range specifies the domain interval to be shifted. All the knots captured in this range are shifted by the same amount as far as the closest neighbouring knot on either side."""
	urange2 : Par
	"""Range specifies the domain interval to be shifted. All the knots captured in this range are shifted by the same amount as far as the closest neighbouring knot on either side."""
	vparmtype : Par
	"""Menu : Select the method of parameterization in v from the options below."""
	vrange1 : Par
	"""Range specifies the domain interval to be shifted. All the knots captured in this range are shifted by the same amount as far as the closest neighbouring knot on either side."""
	vrange2 : Par
	"""Range specifies the domain interval to be shifted. All the knots captured in this range are shifted by the same amount as far as the closest neighbouring knot on either side."""
	par : parameter.basisSOP
	"""Parameters of parameter.basisSOP"""
	pass


class blendSOP():
	"""blendSOP"""
	par : parameter.blendSOP
	"""Parameters of parameter.blendSOP"""
	pass


class booleanSOP():
	"""booleanSOP"""
	booleanop : Par
	"""Menu : Some of the operations below produce guide geometry to give you visual feedback on the results of the operation being performed. The appearance of the geometry is context sensitive - if you are performing an intersect operation, or either of the edge operations the guide will be both inputs; if you are doing A minus B then the guide will be B and if B minus A then the guide will be A. If you are doing union then there will be no guide geometry.	
		
If the guide geometry is too distracting, you can disable it by entering the Viewport options dialog and clicking on the Guide geometry button so that it no longer appears indented. This procedure is global and will disable the guide geometry of other SOPs as well.

The Boolean SOP will automatically orient polygons so they face the same way. This may not be enough in some cases because Boolean results in some unshared edges where the intersection cut took place. If the shading is still not good enough, you are best to follow Boolean with a Facet SOP. In it, Consolidate Points, Orient Polygons and finally Cusp.		
		
If you have really strange shaped polygons, you can first triangulate one or both of the inputs with the Divide SOP."""
	par : parameter.booleanSOP
	"""Parameters of parameter.booleanSOP"""
	pass


class bridgeSOP():
	"""bridgeSOP"""
	bridge : Par
	"""Menu : Allows bridging of subgroups of N primitives or patterns of primitives."""
	frenet : Par
	"""Specifies the type of normal to use for computing direction:"""
	frenet : Par
	"""Menu : Specifies the type of normal to use for computing direction:"""
	rotatet1 : Par
	"""The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents."""
	rotatet2 : Par
	"""The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents."""
	rotatet3 : Par
	"""The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents."""
	scalet1 : Par
	"""The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents."""
	scalet2 : Par
	"""The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents."""
	scalet3 : Par
	"""The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents."""
	scalec1 : Par
	"""Further scaling of the curvature.	
			
'''Note:''' If the resulting skin bulges too greatly, you can achieve a smooth resulting transition between surfaces by disabling the <span class="tipTextSOP">Preserve Tangent</span> &amp; <span class="tipTextSOP">Preserve Curvature Magnitude</span> parameters, and manually tweaking the Tangent Scales and the Curvature Scales. In general, avoid tweaking the Rotations of the Tangents unless you wish to deform the resulting surface.			
			
If the bridge bulges on one side but not the other, try increasing the <span class="tipTextSOP">Min. Number of Cross sections</span> in the bridge."""
	scalec2 : Par
	"""Further scaling of the curvature.	
			
'''Note:''' If the resulting skin bulges too greatly, you can achieve a smooth resulting transition between surfaces by disabling the <span class="tipTextSOP">Preserve Tangent</span> &amp; <span class="tipTextSOP">Preserve Curvature Magnitude</span> parameters, and manually tweaking the Tangent Scales and the Curvature Scales. In general, avoid tweaking the Rotations of the Tangents unless you wish to deform the resulting surface.			
			
If the bridge bulges on one side but not the other, try increasing the <span class="tipTextSOP">Min. Number of Cross sections</span> in the bridge."""
	scalec3 : Par
	"""Further scaling of the curvature.	
			
'''Note:''' If the resulting skin bulges too greatly, you can achieve a smooth resulting transition between surfaces by disabling the <span class="tipTextSOP">Preserve Tangent</span> &amp; <span class="tipTextSOP">Preserve Curvature Magnitude</span> parameters, and manually tweaking the Tangent Scales and the Curvature Scales. In general, avoid tweaking the Rotations of the Tangents unless you wish to deform the resulting surface.			
			
If the bridge bulges on one side but not the other, try increasing the <span class="tipTextSOP">Min. Number of Cross sections</span> in the bridge."""
	par : parameter.bridgeSOP
	"""Parameters of parameter.bridgeSOP"""
	pass


class cacheSOP():
	"""cacheSOP"""
	par : parameter.cacheSOP
	"""Parameters of parameter.cacheSOP"""
	pass


class captureregionSOP():
	"""captureregionSOP"""
	orient : Par
	"""Menu : Defines the direction axis of the region. Use Z axis when the region is inside a bone object.	
			
[[Image:TouchGeometry46.gif]]"""
	tx : Par
	"""Position of the center of the region."""
	ty : Par
	"""Position of the center of the region."""
	tz : Par
	"""Position of the center of the region."""
	tcapx : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	tcapy : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	tcapz : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	bcapx : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	bcapy : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	bcapz : Par
	"""The X, Y, Z radii of the top/bottom hemisphere."""
	weight1 : Par
	"""Defines the weight of a point exactly on the centre line and edge of the region respectively. Point weights in-between are blended."""
	weight2 : Par
	"""Defines the weight of a point exactly on the centre line and edge of the region respectively. Point weights in-between are blended."""
	colorr : Par
	"""The Capture Region SOP<uses region colors for helpful feedback.	
			
By default the region inherits the color of its containing object (via an expression)."""
	colorg : Par
	"""The Capture Region SOP<uses region colors for helpful feedback.	
			
By default the region inherits the color of its containing object (via an expression)."""
	colorb : Par
	"""The Capture Region SOP<uses region colors for helpful feedback.	
			
By default the region inherits the color of its containing object (via an expression)."""
	par : parameter.captureregionSOP
	"""Parameters of parameter.captureregionSOP"""
	pass


class captureSOP():
	"""captureSOP"""
	weightfrom : Par
	"""Menu : Use this menu to specify where to get the weight from."""
	color : Par
	"""Menu : This option colors each point by capture region (using point attributes) according to its capture weight. The points inherit their colors from the Capture Region(s) in which they lie. For example, if a point falls within a blue capture region and also a yellow capture region, the point will be colored green (more blue near if the blue weighting dominates, and more yellow if the yellow weight dominates). In addition, the points become darker as the weighting gets lighter. For example, near the edge of a blue region, a caught point will appear dark blue. Near the centre, it will appear bright blue. If a point is not caught by any region, it is colored bright red."""
	par : parameter.captureSOP
	"""Parameters of parameter.captureSOP"""
	pass


class choptoSOP():
	"""choptoSOP"""
	startposx : Par
	"""Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes."""
	startposy : Par
	"""Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes."""
	startposz : Par
	"""Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes."""
	endposx : Par
	"""Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes."""
	endposy : Par
	"""Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes."""
	endposz : Par
	"""Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes."""
	method : Par
	""" : The sample data fetch method:"""
	mapping : Par
	"""Menu : Determines how the CHOP samples are mapped to the geometry points."""
	par : parameter.choptoSOP
	"""Parameters of parameter.choptoSOP"""
	pass


class circleSOP():
	"""circleSOP"""
	type : Par
	"""Menu : For information on the different types, see the [http://www.derivativeinc.com/Tools/Touch000/Manual/Guides/GeoTypesGuide/GeometryTypes.pdf Geometry Types Guide]. Depending on the primitive type chosen, some SOP options may not apply."""
	orient : Par
	"""Menu : The plane on which the circle lies."""
	radx : Par
	"""The Radius of the Circle in the X and Y directions."""
	rady : Par
	"""The Radius of the Circle in the X and Y directions."""
	tx : Par
	"""The Center of the Circle in X, Y and Z."""
	ty : Par
	"""The Center of the Circle in X, Y and Z."""
	tz : Par
	"""The Center of the Circle in X, Y and Z."""
	arc : Par
	"""Menu : Determines how the circle should be drawn. Applies to polygons and imperfect splines only."""
	angle : Par
	"""Float : The beginning and ending angles of the arc. An arc will start at the beginning angle, and proceed towards the ending angle. If beginning=0 and end=360 it will be a full circle. As a reference:	
		
<div><center>[[Image:TouchGeometry222.gif]]</center></div>		
		
'''Note:''' The total angle can exceed 360, making multiple wraps of the circle."""
	texture : Par
	"""Menu : Option to include texture cooordinates or not."""
	par : parameter.circleSOP
	"""Parameters of parameter.circleSOP"""
	pass


class claySOP():
	"""claySOP"""
	par : parameter.claySOP
	"""Parameters of parameter.claySOP"""
	pass


class clipSOP():
	"""clipSOP"""
	clipop : Par
	"""Menu : Options controlling what part of the clip to keep:"""
	dirx : Par
	"""The default values of <code>0 1 0</code> creates a Normal vector straight up in Y, which is perpendicular to the XZ plane, which becomes the clipping plane. <code>1 0 0</code> points the normal in positive X, giving a clipping plane in YZ. The plane may be positioned at an angle by using values typed in (<code>1 1 0</code> gives a 45 angle plane) or interactively by using the direction vector jack."""
	diry : Par
	"""The default values of <code>0 1 0</code> creates a Normal vector straight up in Y, which is perpendicular to the XZ plane, which becomes the clipping plane. <code>1 0 0</code> points the normal in positive X, giving a clipping plane in YZ. The plane may be positioned at an angle by using values typed in (<code>1 1 0</code> gives a 45 angle plane) or interactively by using the direction vector jack."""
	dirz : Par
	"""The default values of <code>0 1 0</code> creates a Normal vector straight up in Y, which is perpendicular to the XZ plane, which becomes the clipping plane. <code>1 0 0</code> points the normal in positive X, giving a clipping plane in YZ. The plane may be positioned at an angle by using values typed in (<code>1 1 0</code> gives a 45 angle plane) or interactively by using the direction vector jack."""
	par : parameter.clipSOP
	"""Parameters of parameter.clipSOP"""
	pass


class convertSOP():
	"""convertSOP"""
	fromtype : Par
	"""Menu : Determines which geometry by type will be converted. The default is All Types:"""
	totype : Par
	"""Menu : Determines what the above From Type geometry will be converted to. Conversion to Polygons is the default:	
		
		
'''Notes''':		
Not all geometry can be converted to specific types. For example, a triangulated polygon surface to a single NURBS surface, or a Mesh sphere into a primitive sphere. Also, certain conversions will preserve shapes. For example, converting a Bzier curve to a NURBS curve or a polygonal mesh to a NURBS Surface.		
		
'''Circle Notes''': Converting to primitive circles is available for action users who are used to working with polygon circles so that you can convert them to primitive circles for the TouchDesigner Skeleton, Arm, and Limb SOPs.		
		
'''Trimmed Surface Notes''': If the primitive to be converted is a curve (NURBS or Bezier) and is flat, a trimmed surface will be generated such that the visible piece coincides with the curve. If the curve is not flat, it will be converted to a non-trimmed surface. The advantage of the trimmed solution is that it yields a very clean surface and handles concave curves perfectly."""
	surftype : Par
	"""Menu : This option is used to select how the points of the created surface are connected."""
	par : parameter.convertSOP
	"""Parameters of parameter.convertSOP"""
	pass


class copySOP():
	"""copySOP"""
	xord : Par
	"""Menu : Sets the overall transform order for the transformations. The <span class="tipTextSOP">Transform Order</span> determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu."""
	rord : Par
	"""Menu : Sets the order of the rotations within the overall transform order."""
	tx : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	ty : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	tz : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	rx : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	ry : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	rz : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	sx : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	sy : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	sz : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	px : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	py : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	pz : Par
	"""These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference."""
	upvectorx : Par
	"""When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat object passes through the Y axis of the target object."""
	upvectory : Par
	"""When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat object passes through the Y axis of the target object."""
	upvectorz : Par
	"""When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat object passes through the Y axis of the target object."""
	setpt : Par
	"""StrMenu : Copy the attributes to the source geometry's points."""
	setprim : Par
	"""StrMenu : Copy the attributes to the source geometry's primitives."""
	setvtx : Par
	"""StrMenu : Copy the attributes to the source geometry's vertices."""
	mulpt : Par
	"""StrMenu : Multiply the attributes with the source geometry's point attributes."""
	mulprim : Par
	"""StrMenu : Multiply the attributes with the source geometry's primitive attributes."""
	mulvtx : Par
	"""StrMenu : Multiply the attributes with the source geometry's vertex attributes."""
	addpt : Par
	"""StrMenu : Add the attributes to the source geometry's point attributes."""
	addprim : Par
	"""StrMenu : Add the attributes to the source geometry's primitive attributes."""
	addvtx : Par
	"""StrMenu : Add the attributes to the source geometry's vertex attributes."""
	subpt : Par
	"""StrMenu : Subtract the attributes from the source geometry's point attributes."""
	subprim : Par
	"""StrMenu : Subtract the attributes from the source geometry's primitive attributes."""
	subvtx : Par
	"""StrMenu : Subtract the attributes from the source geometry's vertex attributes."""
	par : parameter.copySOP
	"""Parameters of parameter.copySOP"""
	pass


class cplusplusSOP():
	"""cplusplusSOP"""
	par : parameter.cplusplusSOP
	"""Parameters of parameter.cplusplusSOP"""
	pass


class creepSOP():
	"""creepSOP"""
	resetmethod : Par
	"""Menu : The Source Input is Translated, Rotated and Scaled so as to complete the given options listed below."""
	tx : Par
	"""Translate the Source Input Creep geometry on the surface of the Path Input."""
	ty : Par
	"""Translate the Source Input Creep geometry on the surface of the Path Input."""
	tz : Par
	"""Translate the Source Input Creep geometry on the surface of the Path Input."""
	rx : Par
	"""Rotate the Source Input creep geometry on the surface of the Path Input."""
	ry : Par
	"""Rotate the Source Input creep geometry on the surface of the Path Input."""
	rz : Par
	"""Rotate the Source Input creep geometry on the surface of the Path Input."""
	sx : Par
	"""Scale the Source Input creep geometry on the surface of the Path Input."""
	sy : Par
	"""Scale the Source Input creep geometry on the surface of the Path Input."""
	sz : Par
	"""Scale the Source Input creep geometry on the surface of the Path Input."""
	par : parameter.creepSOP
	"""Parameters of parameter.creepSOP"""
	pass


class curveclaySOP():
	"""curveclaySOP"""
	projop : Par
	"""Menu : Choice of several projection axes:"""
	projdir1 : Par
	"""Specify the direction vector of the projection."""
	projdir2 : Par
	"""Specify the direction vector of the projection."""
	projdir3 : Par
	"""Specify the direction vector of the projection."""
	deformop : Par
	"""Menu : Choice of several projection axes:"""
	deformdir1 : Par
	"""Specify the direction vector of the displacement."""
	deformdir2 : Par
	"""Specify the direction vector of the displacement."""
	deformdir3 : Par
	"""Specify the direction vector of the displacement."""
	par : parameter.curveclaySOP
	"""Parameters of parameter.curveclaySOP"""
	pass


class dattoSOP():
	"""dattoSOP"""
	merge : Par
	"""Menu : Specify whether to merge point data or primitive data. This parameter is only enabled when there is an input connected to the SOP."""
	build : Par
	"""Menu : Specifies how to build geometry."""
	connect : Par
	"""Menu : Connectivity of polygons."""
	prtype : Par
	"""Menu : When creating a particle system, specify to render the particles as lines or point sprites."""
	par : parameter.dattoSOP
	"""Parameters of parameter.dattoSOP"""
	pass


class extrudeSOP():
	"""extrudeSOP"""
	dofuse : Par
	"""Menu : This should almost always be turned on when cross-sections are used. It consolidates points of polygons that would otherwise cross or overlap when the bevel takes place."""
	fronttype : Par
	"""Menu : Control how the front face of the extrusion should be built. You may wish to have a "No Output" because some faces are never actually seen when doing animation and, therefore, would only take up additional overhead if left on."""
	backtype : Par
	"""Menu : This value controls whether or not the back of the extruded object will have a face or not. The options are the same as the Front Face options above."""
	sidetype : Par
	"""Menu : Controls how the cross-section(s) will be extruded. If the input cross-section is a Bzier or NURBS curve, the surface will be constructed with a patch of the same geometry type."""
	par : parameter.extrudeSOP
	"""Parameters of parameter.extrudeSOP"""
	pass


class facetrackSOP():
	"""facetrackSOP"""
	par : parameter.facetrackSOP
	"""Parameters of parameter.facetrackSOP"""
	pass


class facetSOP():
	"""facetSOP"""
	cons : Par
	"""Menu : Consolidate eliminates the redundancy of having many points that are close to each other, by merging them together to form a fewer set of common points. Consolidate is useful for cleaning up an edge that may appear between adjacent polygons that have been merged."""
	par : parameter.facetSOP
	"""Parameters of parameter.facetSOP"""
	pass


class fileinSOP():
	"""fileinSOP"""
	par : parameter.fileinSOP
	"""Parameters of parameter.fileinSOP"""
	pass


class fitSOP():
	"""fitSOP"""
	method : Par
	"""Menu : Specifies one of two fitting styles: approximation or interpolation. Each style has a number of parameters that are accessible from the respective folder. For more information see the Approximation and Interpolation pages below."""
	type : Par
	"""Menu : The output of the Fit SOP is a NURBS or Bzier primitive. All input faces are fitted to Spline curves, and all input surfaces are fitted to spline surfaces. The resulting shapes are identical whether created as NURBS or as Bzier primitives."""
	surftype : Par
	"""Menu : This option is used to select the type of surface, when using a Mesh Primitive Type."""
	scope : Par
	"""Menu : Scope establishes the interpolation method."""
	dataparmu : Par
	"""Menu : Specifies the parameterization of the data in the U direction (the only direction if the input is a curve). The data parameterization can be uniform, chord length, or centripetal.	
			
: Uniform Uniform parameterization uses equally spaced parameter values. It works best when the geometry is very regular. When the data is unevenly spaced, this approach can produce very unintuitive shapes, and is not recommended.			
: Chord Length Chord length computes the parameterization of the data based on the relative distances between successive data points. It is the most commonly used approach because is tends to produce the most accurate results.			
: Centripetal Centripetal parameterization is similar to chord length, but yields better results when the data has very sharp corners."""
	dataparmv : Par
	"""Menu : V data parameterization is identical to U data parameterization, but it affects the V direction when the input is a surface. It is not used when the input is a face."""
	closeu : Par
	"""Menu : This menu determines whether the fitted curve should be closed, or whether the fitted surface should be wrapped in the U parametric direction. The options are to open (Off), close (On), or inherit the closure type from the input primitive."""
	closev : Par
	"""Menu : This menu determines whether the fitted surface should be wrapped in the V parametric direction. The options are to open (Off), close (On), or inherit the closure type from the input primitive. V Wrap is ignored when the input is a face."""
	par : parameter.fitSOP
	"""Parameters of parameter.fitSOP"""
	pass


class fontSOP():
	"""fontSOP"""
	type : Par
	""" : Select from the following types. For information on the different types, see the Geometry Types section. Bzier Curves and Polygons provide the most efficient use of memory, because they use polygons for letters containing straight segments, and Bzier curves for all others.	
		
'''Note:''' Due to an Open GL bug, holes in Bzier fonts may shade incorrectly."""
	tx : Par
	"""Translates the geometry in x, y and z."""
	ty : Par
	"""Translates the geometry in x, y and z."""
	tz : Par
	"""Translates the geometry in x, y and z."""
	sx : Par
	"""Scales the text in the X and Y axis."""
	sy : Par
	"""Scales the text in the X and Y axis."""
	kernx : Par
	"""Letter spacing in the X direction. Line spacing in the Y direction if there are multiple lines. If you need manual character-by-character, you can do it in Model mode."""
	kerny : Par
	"""Letter spacing in the X direction. Line spacing in the Y direction if there are multiple lines. If you need manual character-by-character, you can do it in Model mode."""
	texture : Par
	""" : This adds uv coordinates to the geometry created by the Font SOP."""
	par : parameter.fontSOP
	"""Parameters of parameter.fontSOP"""
	pass


class fractalSOP():
	"""fractalSOP"""
	dirx : Par
	"""The direction of the Fractalisation. The default values of <code>0, 0, 1</code> make the fractal deviations point in the Z direction. Can be overridden by: Use Vertex Normals."""
	diry : Par
	"""The direction of the Fractalisation. The default values of <code>0, 0, 1</code> make the fractal deviations point in the Z direction. Can be overridden by: Use Vertex Normals."""
	dirz : Par
	"""The direction of the Fractalisation. The default values of <code>0, 0, 1</code> make the fractal deviations point in the Z direction. Can be overridden by: Use Vertex Normals."""
	par : parameter.fractalSOP
	"""Parameters of parameter.fractalSOP"""
	pass


class gridSOP():
	"""gridSOP"""
	type : Par
	"""Menu : Select from the following types. For information on the different types, see the Geometry Types section. Depending on the primitive type chosen, some SOP options may not apply."""
	surftype : Par
	"""Menu : (Results only viewable for polygons and meshes)."""
	orient : Par
	"""Menu : Specifies on which plane the Grid is built."""
	sizex : Par
	"""The X and Y scale of the grid."""
	sizey : Par
	"""The X and Y scale of the grid."""
	tx : Par
	"""Center of grid in X, Y, and Z."""
	ty : Par
	"""Center of grid in X, Y, and Z."""
	tz : Par
	"""Center of grid in X, Y, and Z."""
	texture : Par
	"""Menu : This adds uv coordinates to the geometry created by the Grid SOP."""
	par : parameter.gridSOP
	"""Parameters of parameter.gridSOP"""
	pass


class holeSOP():
	"""holeSOP"""
	par : parameter.holeSOP
	"""Parameters of parameter.holeSOP"""
	pass


class inSOP():
	"""inSOP"""
	par : parameter.inSOP
	"""Parameters of parameter.inSOP"""
	pass


class isosurfaceSOP():
	"""isosurfaceSOP"""
	minx : Par
	"""Determines the minimum clipping plane boundary for display of iso surface."""
	miny : Par
	"""Determines the minimum clipping plane boundary for display of iso surface."""
	minz : Par
	"""Determines the minimum clipping plane boundary for display of iso surface."""
	maxx : Par
	"""Determines maximum clipping plane boundary for display of iso surfaces."""
	maxy : Par
	"""Determines maximum clipping plane boundary for display of iso surfaces."""
	maxz : Par
	"""Determines maximum clipping plane boundary for display of iso surfaces."""
	divsx : Par
	"""The density, or resolution of the iso surface polygons in X, Y and Z."""
	divsy : Par
	"""The density, or resolution of the iso surface polygons in X, Y and Z."""
	divsz : Par
	"""The density, or resolution of the iso surface polygons in X, Y and Z."""
	par : parameter.isosurfaceSOP
	"""Parameters of parameter.isosurfaceSOP"""
	pass


class joinSOP():
	"""joinSOP"""
	dir : Par
	"""Menu : This menu determines the parametric direction of the joining operation, which can be in U or in V, and is meaningful only when the inputs are surfaces. The U direction is associated with columns; the V direction refers to rows. For example, joining two surfaces in U will generate a surface with more columns than either input. The number of rows might be higher too, but only if the two inputs have a different number of rows or a different V basis."""
	joinop : Par
	"""Menu : Can optionally join subgroups of n primitives or every nth primitive in a cyclical manner.	
		
'''For Example'''; assume there are six primitives numbered for 0 - 5, and N = 2. Then, 		
		
# Groups will generate 0-1 2-3 4-5		
# Skipping will generate 0-2-6 and 1-3-5."""
	par : parameter.joinSOP
	"""Parameters of parameter.joinSOP"""
	pass


class jointSOP():
	"""jointSOP"""
	lrscale1 : Par
	"""These parameters control the shape of the smooth path, varying the shape of the implied curve from the left or right. If the Orient Circles option is on, the sign of the scale has no effect. For a discussion of the relative terms right and left, see [[Align SOP]]."""
	lrscale2 : Par
	"""These parameters control the shape of the smooth path, varying the shape of the implied curve from the left or right. If the Orient Circles option is on, the sign of the scale has no effect. For a discussion of the relative terms right and left, see [[Align SOP]]."""
	lroffset1 : Par
	"""These parameters allow you to override the distance between circles, thereby affecting the shape of the joint."""
	lroffset2 : Par
	"""These parameters allow you to override the distance between circles, thereby affecting the shape of the joint."""
	par : parameter.jointSOP
	"""Parameters of parameter.jointSOP"""
	pass


class kinectSOP():
	"""kinectSOP"""
	hwversion : Par
	"""Menu : Only Kinect v1 sensors supported at this time."""
	skeleton : Par
	"""Menu : Only used for Kinect 1 devices. Specify whether to track full skeleton or seated skeleton."""
	par : parameter.kinectSOP
	"""Parameters of parameter.kinectSOP"""
	pass


class latticeSOP():
	"""latticeSOP"""
	deformtype : Par
	"""Menu : Choose if deformation should be done using a regularly spaced lattice or an arbitary point cloud."""
	divsx : Par
	"""Must be set to match the number of divisions in the lattice grid object(s)."""
	divsy : Par
	"""Must be set to match the number of divisions in the lattice grid object(s)."""
	divsz : Par
	"""Must be set to match the number of divisions in the lattice grid object(s)."""
	kernel : Par
	"""StrMenu : Deformation by specifying a Kernal Function and Points makes it easier to deform arbitrary clouds of points, as this makes the topology of the lattice behave more like a metaball rather than as a fixed lattice. ''Kernel Function'' determines which meta kernel to use to determine the influence of a point. For more information on kernel types check here: [[Metaball#Metaball_Model_Types|Metaball Model Types]]"""
	par : parameter.latticeSOP
	"""Parameters of parameter.latticeSOP"""
	pass


class lineSOP():
	"""lineSOP"""
	pax : Par
	"""These X,Y, and Z values set the position of the beginning of the line."""
	pay : Par
	"""These X,Y, and Z values set the position of the beginning of the line."""
	paz : Par
	"""These X,Y, and Z values set the position of the beginning of the line."""
	pbx : Par
	"""These X,Y, and Z values set the position of the end of the line."""
	pby : Par
	"""These X,Y, and Z values set the position of the end of the line."""
	pbz : Par
	"""These X,Y, and Z values set the position of the end of the line."""
	texture : Par
	"""Menu : Texture adds (0,1) coordinates to the vertices when set to Unit. Creates a rectangle without uv attributes when set to Off."""
	par : parameter.lineSOP
	"""Parameters of parameter.lineSOP"""
	pass


class linethickSOP():
	"""linethickSOP"""
	startwidth1 : Par
	"""Controls the width of the surface created at the start of the line. Startwidth1 adjusts the width on the inside of the curve, Startwidth2 adjusts the width on the outside of the curve."""
	startwidth2 : Par
	"""Controls the width of the surface created at the start of the line. Startwidth1 adjusts the width on the inside of the curve, Startwidth2 adjusts the width on the outside of the curve."""
	endwidth1 : Par
	"""Controls the width of the surface created at the end of the line. Endwidth1 adjusts the width on the inside of the curve, Endwidth2 adjusts the width on the outside of the curve."""
	endwidth2 : Par
	"""Controls the width of the surface created at the end of the line. Endwidth1 adjusts the width on the inside of the curve, Endwidth2 adjusts the width on the outside of the curve."""
	domain1 : Par
	"""Fraction of the input curve that is used to create the new surface geometry. Domain1 sets position on the curve for Startwidth, Domain2 sets position on the curve for Endwidth."""
	domain2 : Par
	"""Fraction of the input curve that is used to create the new surface geometry. Domain1 sets position on the curve for Startwidth, Domain2 sets position on the curve for Endwidth."""
	shape : Par
	"""Menu : This menu selects the type of interpolation used between Startwidth and Endwidth."""
	par : parameter.linethickSOP
	"""Parameters of parameter.linethickSOP"""
	pass


class lsystemSOP():
	"""lsystemSOP"""
	type : Par
	"""Menu : Provides two options for output geometry:"""
	incu : Par
	"""Defines the default color U, V index increments when the turtle symbols ` or # are used."""
	incv : Par
	"""Defines the default color U, V index increments when the turtle symbols ` or # are used."""
	par : parameter.lsystemSOP
	"""Parameters of parameter.lsystemSOP"""
	pass


class magnetSOP():
	"""magnetSOP"""
	xord : Par
	"""Menu : Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu."""
	rord : Par
	"""Menu : Sets the order of the rotations within the overall transform order."""
	tx : Par
	"""These three fields move the Source geometry in the three axes. The Translates of the metaball only affect the position of the area of influence. The influence itself is provided by an imaginary magnet within the Magnet SOP itself, and the attitude of this influence is determined by the Translates of the Magnet SOP.	
			
'''Note:''' If the '''Translate''' values of the Magnet SOP are all zero, the magnet will have no deforming influence. The weight of the [[Metaball SOP]] scales the influence of the Magnet SOP's Translates."""
	ty : Par
	"""These three fields move the Source geometry in the three axes. The Translates of the metaball only affect the position of the area of influence. The influence itself is provided by an imaginary magnet within the Magnet SOP itself, and the attitude of this influence is determined by the Translates of the Magnet SOP.	
			
'''Note:''' If the '''Translate''' values of the Magnet SOP are all zero, the magnet will have no deforming influence. The weight of the [[Metaball SOP]] scales the influence of the Magnet SOP's Translates."""
	tz : Par
	"""These three fields move the Source geometry in the three axes. The Translates of the metaball only affect the position of the area of influence. The influence itself is provided by an imaginary magnet within the Magnet SOP itself, and the attitude of this influence is determined by the Translates of the Magnet SOP.	
			
'''Note:''' If the '''Translate''' values of the Magnet SOP are all zero, the magnet will have no deforming influence. The weight of the [[Metaball SOP]] scales the influence of the Magnet SOP's Translates."""
	rx : Par
	"""These three fields rotate the Source geometry in the three axes."""
	ry : Par
	"""These three fields rotate the Source geometry in the three axes."""
	rz : Par
	"""These three fields rotate the Source geometry in the three axes."""
	sx : Par
	"""These three fields scale the input geometry in the three axes."""
	sy : Par
	"""These three fields scale the input geometry in the three axes."""
	sz : Par
	"""These three fields scale the input geometry in the three axes."""
	px : Par
	"""The pivot point for the transformations. Not the same as the pivot point in the pivot channels."""
	py : Par
	"""The pivot point for the transformations. Not the same as the pivot point in the pivot channels."""
	pz : Par
	"""The pivot point for the transformations. Not the same as the pivot point in the pivot channels."""
	par : parameter.magnetSOP
	"""Parameters of parameter.magnetSOP"""
	pass


class mergeSOP():
	"""mergeSOP"""
	par : parameter.mergeSOP
	"""Parameters of parameter.mergeSOP"""
	pass


class metaballSOP():
	"""metaballSOP"""
	radx : Par
	"""Controls the radius of the metaball field."""
	rady : Par
	"""Controls the radius of the metaball field."""
	radz : Par
	"""Controls the radius of the metaball field."""
	tx : Par
	"""Metaball center in X, Y and Z."""
	ty : Par
	"""Metaball center in X, Y and Z."""
	tz : Par
	"""Metaball center in X, Y and Z."""
	par : parameter.metaballSOP
	"""Parameters of parameter.metaballSOP"""
	pass


class modelSOP():
	"""modelSOP"""
	par : parameter.modelSOP
	"""Parameters of parameter.modelSOP"""
	pass


class noiseSOP():
	"""noiseSOP"""
	attribute : Par
	"""Menu : This menu sets which attribute of the geometry the Noise SOP acts on."""
	type : Par
	"""Menu : The noise function used to generate noise. The functions available are:"""
	xord : Par
	"""Menu : The menu attached to this parameter allows you to specify the order in which the transforms will take place. Changing the Transform order will change where things go much the same way as going a block and turning east gets you to a different place than turning east and then going a block."""
	rord : Par
	"""Menu : The rotational matrix presented when you click on this option allows you to set the transform order for the rotations. As with transform order (above), changing the order in which the rotations take place will alter the final position."""
	tx : Par
	"""Translate the sampling plane through the noise space."""
	ty : Par
	"""Translate the sampling plane through the noise space."""
	tz : Par
	"""Translate the sampling plane through the noise space."""
	rx : Par
	"""Rotate the sampling plane in the noise space."""
	ry : Par
	"""Rotate the sampling plane in the noise space."""
	rz : Par
	"""Rotate the sampling plane in the noise space."""
	sx : Par
	"""Scale the sampling plane."""
	sy : Par
	"""Scale the sampling plane."""
	sz : Par
	"""Scale the sampling plane."""
	px : Par
	"""Control the pivot for the transform of the sampling plane."""
	py : Par
	"""Control the pivot for the transform of the sampling plane."""
	pz : Par
	"""Control the pivot for the transform of the sampling plane."""
	par : parameter.noiseSOP
	"""Parameters of parameter.noiseSOP"""
	pass


class nullSOP():
	"""nullSOP"""
	par : parameter.nullSOP
	"""Parameters of parameter.nullSOP"""
	pass


class oculusriftSOP():
	"""oculusriftSOP"""
	model : Par
	"""Menu : Select which controller model to load."""
	par : parameter.oculusriftSOP
	"""Parameters of parameter.oculusriftSOP"""
	pass


class NotSet():
	"""NotSet"""
	par : parameter.NotSet
	"""Parameters of parameter.NotSet"""
	pass


class particleSOP():
	"""particleSOP"""
	prtype : Par
	"""Menu : Selects how the particles are rendered."""
	behave : Par
	"""Menu : Select between emitting particles from the geometry's points or deforming the original geometry using the Particle SOP's behavior."""
	ptreuse : Par
	"""Menu : Decide how the internal memory for points is reused when a point needs to be created or when a point dies."""
	attractmode : Par
	"""Menu : Select which mode of attraction to use for Surface Attractors."""
	externalx : Par
	"""Forces of gravity acting on the particles. When drag is zero, the particles can accelerate with no limit on their speed."""
	externaly : Par
	"""Forces of gravity acting on the particles. When drag is zero, the particles can accelerate with no limit on their speed."""
	externalz : Par
	"""Forces of gravity acting on the particles. When drag is zero, the particles can accelerate with no limit on their speed."""
	windx : Par
	"""Wind forces acting on the particles. Similar to <span class="tipTextSOP">External Force</span>. Using <span class="tipTextSOP">Wind</span> (and no other forces, such as <span class="tipTextSOP">Turbulence</span>), the particles will not exceed the wind velocity.	
			
====Discussion - Wind vs External Force====			
			
The application of <span class="tipTextSOP">External Force</span> directly affects a particles' acceleration, the rate of which is determined by the mass (F = Mass  Acceleration). <span class="tipTextSOP">Wind</span> is an additional force, but one that is velocity sensitive. If a particle is already travelling at wind velocity, then it shouldn't receive any extra force from it. This implies a maximum velocity when using <span class="tipTextSOP">Wind</span> on its own.			
			
An increase in mass impedes acceleration for a given constant force. <span class="tipTextSOP">Drag</span> is a force opposing the direction of motion which is velocity sensitive, i.e. the larger the velocity, the greater the effect of drag. Its useful for limiting the velocity of particles."""
	windy : Par
	"""Wind forces acting on the particles. Similar to <span class="tipTextSOP">External Force</span>. Using <span class="tipTextSOP">Wind</span> (and no other forces, such as <span class="tipTextSOP">Turbulence</span>), the particles will not exceed the wind velocity.	
			
====Discussion - Wind vs External Force====			
			
The application of <span class="tipTextSOP">External Force</span> directly affects a particles' acceleration, the rate of which is determined by the mass (F = Mass  Acceleration). <span class="tipTextSOP">Wind</span> is an additional force, but one that is velocity sensitive. If a particle is already travelling at wind velocity, then it shouldn't receive any extra force from it. This implies a maximum velocity when using <span class="tipTextSOP">Wind</span> on its own.			
			
An increase in mass impedes acceleration for a given constant force. <span class="tipTextSOP">Drag</span> is a force opposing the direction of motion which is velocity sensitive, i.e. the larger the velocity, the greater the effect of drag. Its useful for limiting the velocity of particles."""
	windz : Par
	"""Wind forces acting on the particles. Similar to <span class="tipTextSOP">External Force</span>. Using <span class="tipTextSOP">Wind</span> (and no other forces, such as <span class="tipTextSOP">Turbulence</span>), the particles will not exceed the wind velocity.	
			
====Discussion - Wind vs External Force====			
			
The application of <span class="tipTextSOP">External Force</span> directly affects a particles' acceleration, the rate of which is determined by the mass (F = Mass  Acceleration). <span class="tipTextSOP">Wind</span> is an additional force, but one that is velocity sensitive. If a particle is already travelling at wind velocity, then it shouldn't receive any extra force from it. This implies a maximum velocity when using <span class="tipTextSOP">Wind</span> on its own.			
			
An increase in mass impedes acceleration for a given constant force. <span class="tipTextSOP">Drag</span> is a force opposing the direction of motion which is velocity sensitive, i.e. the larger the velocity, the greater the effect of drag. Its useful for limiting the velocity of particles."""
	turbx : Par
	"""The amplitude of turbulent (chaotic) forces along each axis. Use positive values, if any."""
	turby : Par
	"""The amplitude of turbulent (chaotic) forces along each axis. Use positive values, if any."""
	turbz : Par
	"""The amplitude of turbulent (chaotic) forces along each axis. Use positive values, if any."""
	limitposx : Par
	"""The particles will die or bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are <code>1000</code> units away, which is very large. Reduce the values to about one to see the effect."""
	limitposy : Par
	"""The particles will die or bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are <code>1000</code> units away, which is very large. Reduce the values to about one to see the effect."""
	limitposz : Par
	"""The particles will die or bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are <code>1000</code> units away, which is very large. Reduce the values to about one to see the effect."""
	limitnegx : Par
	"""The particles will die or bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are <code>1000</code> units away, which is very large. Reduce the values to about one to see the effect."""
	limitnegy : Par
	"""The particles will die or bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are <code>1000</code> units away, which is very large. Reduce the values to about one to see the effect."""
	limitnegz : Par
	"""The particles will die or bounce off the limit planes when it reaches them. The six limit plane fields define a bounding cube. The default settings are <code>1000</code> units away, which is very large. Reduce the values to about one to see the effect."""
	hit : Par
	"""Menu : Control over what happens when a particle hits either the six collision planes or the collide object. The options are:"""
	splittype : Par
	"""Menu : Select if the particle will split and under what conditions."""
	splitmin : Par
	"""When a particle splits, it splits into a number of other particles. The number of particles is randomly set between this range."""
	splitmax : Par
	"""When a particle splits, it splits into a number of other particles. The number of particles is randomly set between this range."""
	splitvelx : Par
	"""Each split particle is given this base velocity."""
	splitvely : Par
	"""Each split particle is given this base velocity."""
	splitvelz : Par
	"""Each split particle is given this base velocity."""
	splitvarx : Par
	"""This is a random amount that is added to the split velocity. When creating fireworks, the variance is large while the velocity is low. When rendering raindrops splashing, the split velocity is large in Y, and the variance in X and Z causes the particles to bounce up - but randomly - in the XZ plane."""
	splitvary : Par
	"""This is a random amount that is added to the split velocity. When creating fireworks, the variance is large while the velocity is low. When rendering raindrops splashing, the split velocity is large in Y, and the variance in X and Z causes the particles to bounce up - but randomly - in the XZ plane."""
	splitvarz : Par
	"""This is a random amount that is added to the split velocity. When creating fireworks, the variance is large while the velocity is low. When rendering raindrops splashing, the split velocity is large in Y, and the variance in X and Z causes the particles to bounce up - but randomly - in the XZ plane."""
	par : parameter.particleSOP
	"""Parameters of parameter.particleSOP"""
	pass


class pointSOP():
	"""pointSOP"""
	tx : Par
	"""Expressions to translate the XYZ coordinates of a given point can be entered here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.x</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.y</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.z</syntaxhighlight>.	
			
Simply entering <syntaxhighlight lang=python inline>me.inputPoint.x</syntaxhighlight> into the Position X field means that the X coordinate of each point that comes in is passed straight through with no modification.			
			
Changing this entry to <syntaxhighlight lang=python inline>me.inputPoint.x+5</syntaxhighlight> means that the X coordinate of each point that comes in will be displaced by 5 units. This expression can be expanded to produce many useful effects. Transformations can also be effected in the Y and Z fields."""
	ty : Par
	"""Expressions to translate the XYZ coordinates of a given point can be entered here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.x</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.y</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.z</syntaxhighlight>.	
			
Simply entering <syntaxhighlight lang=python inline>me.inputPoint.x</syntaxhighlight> into the Position X field means that the X coordinate of each point that comes in is passed straight through with no modification.			
			
Changing this entry to <syntaxhighlight lang=python inline>me.inputPoint.x+5</syntaxhighlight> means that the X coordinate of each point that comes in will be displaced by 5 units. This expression can be expanded to produce many useful effects. Transformations can also be effected in the Y and Z fields."""
	tz : Par
	"""Expressions to translate the XYZ coordinates of a given point can be entered here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.x</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.y</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.z</syntaxhighlight>.	
			
Simply entering <syntaxhighlight lang=python inline>me.inputPoint.x</syntaxhighlight> into the Position X field means that the X coordinate of each point that comes in is passed straight through with no modification.			
			
Changing this entry to <syntaxhighlight lang=python inline>me.inputPoint.x+5</syntaxhighlight> means that the X coordinate of each point that comes in will be displaced by 5 units. This expression can be expanded to produce many useful effects. Transformations can also be effected in the Y and Z fields."""
	doweight : Par
	"""Menu : Select between keeping the weight or adding a new weight."""
	doclr : Par
	"""Menu : Select between keeping the color, adding new color, or using no color."""
	diffr : Par
	"""If you select 'Add Color' from the menu above, Cd color attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputColor[0]</syntaxhighlight> for red, <syntaxhighlight lang=python inline>me.inputColor[1]</syntaxhighlight> for green, <syntaxhighlight lang=python inline>me.inputColor[2]</syntaxhighlight> for blue, and <syntaxhighlight lang=python inline>me.inputColor[3]</syntaxhighlight> for alpha.
If you select 'No Color' from the menu above, the Cd color attribute will be removed from the SOP."""
	diffg : Par
	"""If you select 'Add Color' from the menu above, Cd color attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputColor[0]</syntaxhighlight> for red, <syntaxhighlight lang=python inline>me.inputColor[1]</syntaxhighlight> for green, <syntaxhighlight lang=python inline>me.inputColor[2]</syntaxhighlight> for blue, and <syntaxhighlight lang=python inline>me.inputColor[3]</syntaxhighlight> for alpha.
If you select 'No Color' from the menu above, the Cd color attribute will be removed from the SOP."""
	diffb : Par
	"""If you select 'Add Color' from the menu above, Cd color attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputColor[0]</syntaxhighlight> for red, <syntaxhighlight lang=python inline>me.inputColor[1]</syntaxhighlight> for green, <syntaxhighlight lang=python inline>me.inputColor[2]</syntaxhighlight> for blue, and <syntaxhighlight lang=python inline>me.inputColor[3]</syntaxhighlight> for alpha.
If you select 'No Color' from the menu above, the Cd color attribute will be removed from the SOP."""
	donml : Par
	"""Menu : Select between keeping the normals, adding new normals, or using no normals."""
	nx : Par
	"""If you select 'Add Normal' from the menu above, N normal attributes will be added/modified in the SOP. Enter expressions to change a given point normal here. Point normals are directional vectors used by other SOPs, such as Turbulence, Facet and Copy. See [[Attributes]] article for detailed information. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputNormal[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputNormal[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputNormal[2]</syntaxhighlight>.
If you select 'No Normal' from the menu above, the N normal attribute will be removed from the SOP."""
	ny : Par
	"""If you select 'Add Normal' from the menu above, N normal attributes will be added/modified in the SOP. Enter expressions to change a given point normal here. Point normals are directional vectors used by other SOPs, such as Turbulence, Facet and Copy. See [[Attributes]] article for detailed information. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputNormal[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputNormal[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputNormal[2]</syntaxhighlight>.
If you select 'No Normal' from the menu above, the N normal attribute will be removed from the SOP."""
	nz : Par
	"""If you select 'Add Normal' from the menu above, N normal attributes will be added/modified in the SOP. Enter expressions to change a given point normal here. Point normals are directional vectors used by other SOPs, such as Turbulence, Facet and Copy. See [[Attributes]] article for detailed information. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputNormal[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputNormal[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputNormal[2]</syntaxhighlight>.
If you select 'No Normal' from the menu above, the N normal attribute will be removed from the SOP."""
	douvw : Par
	"""Menu : Select between keeping the texture coordinates, adding new texture coordinates, or using no texture coordinates."""
	mapu : Par
	"""If you select 'Add Texture' from the menu above, uv texture coordinate attributes will be added/modified in the SOP. Enter expressions here to control the values of the texture coordinates here. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputTexture[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputTexture[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputTexture[2]</syntaxhighlight>.
If you select 'No Texture' from the menu above, the uv texture coordinate attribute will be removed from the SOP."""
	mapv : Par
	"""If you select 'Add Texture' from the menu above, uv texture coordinate attributes will be added/modified in the SOP. Enter expressions here to control the values of the texture coordinates here. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputTexture[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputTexture[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputTexture[2]</syntaxhighlight>.
If you select 'No Texture' from the menu above, the uv texture coordinate attribute will be removed from the SOP."""
	mapw : Par
	"""If you select 'Add Texture' from the menu above, uv texture coordinate attributes will be added/modified in the SOP. Enter expressions here to control the values of the texture coordinates here. The attributes to modify are: <syntaxhighlight lang=python inline>me.inputTexture[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputTexture[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputTexture[2]</syntaxhighlight>.
If you select 'No Texture' from the menu above, the uv texture coordinate attribute will be removed from the SOP."""
	dowidth : Par
	"""Menu : Select between keeping the width attribute or adding a new width. This Width (width) attribute is used exclusively with [[Line MAT]] to control line width when the material is rendered."""
	dopscale : Par
	"""Menu : Select between keeping the scale attribute, adding new scale, or using no scale. This scale (pscale) attribute is used with the [[Particle SOP]] and acts as a multiplier for the size of particles. The value of this attribute is multiplied by the size specified in the [[Particle SOP]]'s render attributes to scale each particle. This attribute is used by the [[Point Sprite MAT]] when rendering point sprites."""
	custom1type : Par
	"""Menu : The type of attribute created can be selected from this menu."""
	custom1val1 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	custom1val2 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	custom1val3 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	custom1val4 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	domass : Par
	"""Menu : Retains, adds, or removes mass and drag attributes for points."""
	dospringk : Par
	"""Menu : Retains, adds, or removes spring constant attributes for points. The Spring Constant is a well known physical property affecting each point."""
	dovel : Par
	"""Menu : Retains, adds, or removes the velocity of points. Defines the magnitude of the particle's velocity in the X, Y and Z directions."""
	vx : Par
	"""If you select 'Add Velocity' from the menu above, v velocity attributes will be added/modified in the SOP. Enter expressions to change a given point velocity here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.v[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.v[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.v[2]</syntaxhighlight>. If you select 'No Velocity' from the menu above, the v velocity attribute will be removed from the SOP."""
	vy : Par
	"""If you select 'Add Velocity' from the menu above, v velocity attributes will be added/modified in the SOP. Enter expressions to change a given point velocity here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.v[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.v[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.v[2]</syntaxhighlight>. If you select 'No Velocity' from the menu above, the v velocity attribute will be removed from the SOP."""
	vz : Par
	"""If you select 'Add Velocity' from the menu above, v velocity attributes will be added/modified in the SOP. Enter expressions to change a given point velocity here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.v[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.v[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.v[2]</syntaxhighlight>. If you select 'No Velocity' from the menu above, the v velocity attribute will be removed from the SOP."""
	doup : Par
	"""Menu : Creates/Removes the "up" attribute for points. This attribute defines an up vector which is used to fully define the space around a point (for particle instancing or copying geometry). The up vector can be used in conjunction with the copy template's normals to control the orientation of the copies in the [[Copy SOP]]."""
	upx : Par
	"""If you select 'Add Up Vector' from the menu above, up attributes will be added/modified in the SOP. Enter expressions to change a given point up vector here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.up[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.up[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.up[2]</syntaxhighlight>. If you select 'No Up Vector' from the menu above, the up attribute will be removed from the SOP."""
	upy : Par
	"""If you select 'Add Up Vector' from the menu above, up attributes will be added/modified in the SOP. Enter expressions to change a given point up vector here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.up[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.up[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.up[2]</syntaxhighlight>. If you select 'No Up Vector' from the menu above, the up attribute will be removed from the SOP."""
	upz : Par
	"""If you select 'Add Up Vector' from the menu above, up attributes will be added/modified in the SOP. Enter expressions to change a given point up vector here. The attributes to modify here are: <syntaxhighlight lang=python inline>me.inputPoint.up[0]</syntaxhighlight>, <syntaxhighlight lang=python inline>me.inputPoint.up[1]</syntaxhighlight> and <syntaxhighlight lang=python inline>me.inputPoint.up[2]</syntaxhighlight>. If you select 'No Up Vector' from the menu above, the up attribute will be removed from the SOP."""
	doradius : Par
	"""Menu : Retains, adds, or removes radiusf attributes for points, used to modify the distance roll-off effect. The roll-off is: <code>r /(r+d^2)</code> Where <code>r</code> is radius, and <code>d</code> is distance from attractor point. If no radius is set, no attenuation is performed."""
	doscale : Par
	"""Menu : Retains, adds, or removes scalef attributes for points, a multiplier for total force associated with this attractor point.	
			
Both Radius and Force Scale will default to 1 if not created as point attributes.			
			
'''Radial / Normal / Edge / Directional Force''' - These four parameters introduce a type of force when created and each has a corresponding multiplier associated with it."""
	doradialf : Par
	"""Menu : Retains, adds, or removes radialf attributes for points, the force directed towards the attractor point. Positive multipliers are towards while negative are away."""
	donormalf : Par
	"""Menu : Retains, adds, or removes normalf attributes for points, the force directed along the point normal direction."""
	doedgef : Par
	"""Menu : Retains, adds, or removes edgef attributes for points, which only works on primitive face types. The force is directed in the direction of the edge leading from that point. If multiple vertices reference the same point, then the direction is the edge direction of the last primitive referencing the point.	
			
If the face open, then the end point has an edge direction equal to that of the preceding point in that primitive.			
			
'''Note:''' When edge forces are added using the Point SOP, the force directions are computed in the Point SOP itself. Thus, any following transformations do not effect these. If you wish for the edge directions to be transformed as well, all transformations must be done before the Point SOP. Only the edge forces function like this."""
	dodirf : Par
	"""Menu : Retains, adds, or removes dirf attributes for points, an arbitrary directional force still affected by the distance roll-off function."""
	dirfx : Par
	"""If you select 'Add Dir. F' from the menu above, dirf attribute will be added/modified in the SOP. Enter expressions here to control the values of the force in the arbitrary direction here. If you select 'No Dir. F' from the menu above, the dirf attribute will be removed from the SOP."""
	dirfy : Par
	"""If you select 'Add Dir. F' from the menu above, dirf attribute will be added/modified in the SOP. Enter expressions here to control the values of the force in the arbitrary direction here. If you select 'No Dir. F' from the menu above, the dirf attribute will be removed from the SOP."""
	dirfz : Par
	"""If you select 'Add Dir. F' from the menu above, dirf attribute will be added/modified in the SOP. Enter expressions here to control the values of the force in the arbitrary direction here. If you select 'No Dir. F' from the menu above, the dirf attribute will be removed from the SOP."""
	par : parameter.pointSOP
	"""Parameters of parameter.pointSOP"""
	pass


class polypatchSOP():
	"""polypatchSOP"""
	basis : Par
	"""Menu : Select spline type: <span class="tipTextSOP">Cardinal</span> or <span class="tipTextSOP">BSpline</span>."""
	connecttype : Par
	"""Menu : This option is used to select how the points of the created surface are connected."""
	closeu : Par
	"""Menu : Settings for wrapping in U direction."""
	closev : Par
	"""Menu : Settings for wrapping in V direction."""
	firstuclampoff : Par
	"""Settings for clamping first end in U."""
	firstuclampon : Par
	"""Settings for clamping first end in U."""
	firstuclampifprim : Par
	"""Settings for clamping first end in U."""
	lastuclampoff : Par
	"""Settings for clamping last end in U."""
	lastuclampon : Par
	"""Settings for clamping last end in U."""
	lastuclampifprim : Par
	"""Settings for clamping last end in U."""
	firstvclampoff : Par
	"""Settings for clamping first end in V."""
	firstvclampon : Par
	"""Settings for clamping first end in V."""
	firstvclampifprim : Par
	"""Settings for clamping first end in V."""
	lastvclampoff : Par
	"""Settings for clamping last end in V."""
	lastvclampon : Par
	"""Settings for clamping last end in V."""
	lastvclampifprim : Par
	"""Settings for clamping last end in V."""
	divisionsx : Par
	"""The number of divisions in the output surface. Use more divisions for a smoother surface."""
	divisionsy : Par
	"""The number of divisions in the output surface. Use more divisions for a smoother surface."""
	par : parameter.polypatchSOP
	"""Parameters of parameter.polypatchSOP"""
	pass


class polyreduceSOP():
	"""polyreduceSOP"""
	method : Par
	"""Menu : Select how to reduce the number of polygons from the following methods."""
	par : parameter.polyreduceSOP
	"""Parameters of parameter.polyreduceSOP"""
	pass


class polysplineSOP():
	"""polysplineSOP"""
	basis : Par
	"""Menu : Spline type to use. There are seven choices:"""
	closure : Par
	"""Menu : Determines if the output spline is open or closed."""
	divide : Par
	"""Menu : Settings for refining the spline by adding extra divisions."""
	par : parameter.polysplineSOP
	"""Parameters of parameter.polysplineSOP"""
	pass


class polystitchSOP():
	"""polystitchSOP"""
	par : parameter.polystitchSOP
	"""Parameters of parameter.polystitchSOP"""
	pass


class profileSOP():
	"""profileSOP"""
	method : Par
	"""Menu : This menu allows you to extract a stand-alone 3D curve as the world or parametric image of the profile. The non-parametric option will yield a curve whose shape and position in space are identical or very similar to those of the chosen profile. The parametric option will produce a planar, XY face whose vertices and type will be identical to those of the profile in 2D; also, if the profile is a spline it will have the same basis as the extracted curve."""
	maptype : Par
	"""Menu : Select how to reposition and scale an existing profile to fit within the specified domain range. It is a good means of bringing an invisible profile into view by setting the mapping range between 0 and 1 in the U and V parametric directions. A profile mapped outside the unit domain becomes invisible but is not removed from the surface. Other ways to change a profile are available through the [[Primitive SOP]]."""
	urange1 : Par
	"""Indicates in percentages what part of the U surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the U parametric direction. The range is not restricted to the 0-1 interval."""
	urange2 : Par
	"""Indicates in percentages what part of the U surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the U parametric direction. The range is not restricted to the 0-1 interval."""
	vrange1 : Par
	"""Indicates in percentages what part of the V surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the V parametric direction. The range is not restricted to the 0-1 interval."""
	vrange2 : Par
	"""Indicates in percentages what part of the V surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the V parametric direction. The range is not restricted to the 0-1 interval."""
	par : parameter.profileSOP
	"""Parameters of parameter.profileSOP"""
	pass


class railsSOP():
	"""railsSOP"""
	cycle : Par
	"""Menu : Select how the cross=section is applied along the rails."""
	vertex1 : Par
	"""The vertices at which the cross-section is connected to the rails."""
	vertex2 : Par
	"""The vertices at which the cross-section is connected to the rails."""
	dirx : Par
	"""The direction vector to use."""
	diry : Par
	"""The direction vector to use."""
	dirz : Par
	"""The direction vector to use."""
	par : parameter.railsSOP
	"""Parameters of parameter.railsSOP"""
	pass


class rasterSOP():
	"""rasterSOP"""
	direction : Par
	"""Menu : Determines the direction of rasterization. Depending on the image horizontal or vertical might work better."""
	downloadtype : Par
	"""Menu : Gives the option for a delayed data download from the GPU, which is much faster and does not stall the render."""
	par : parameter.rasterSOP
	"""Parameters of parameter.rasterSOP"""
	pass


class raySOP():
	"""raySOP"""
	method : Par
	"""Menu : Select the method of projection for the Ray SOP."""
	normal : Par
	"""Menu : If selected, updates each point in the source geometry with the normal at the collision surface it intersects with. If the point doesn't intersect at the collision surface, a normal of (0,0,0) is used."""
	par : parameter.raySOP
	"""Parameters of parameter.raySOP"""
	pass


class rectangleSOP():
	"""rectangleSOP"""
	orient : Par
	"""Menu : Picks the major plane the rectangle's y-axis orients itself with. Set it to <span class="Heading4">camera</span> if it is to point towards a camera."""
	cameraaspectx : Par
	"""Specify the aspect ratio of the camera with this parameter and the Restangle SOP's aspect ratio will match. This makes it easy to apply a texture on the rectangle which matches the camera's viewport without any further adjustments."""
	cameraaspecty : Par
	"""Specify the aspect ratio of the camera with this parameter and the Restangle SOP's aspect ratio will match. This makes it easy to apply a texture on the rectangle which matches the camera's viewport without any further adjustments."""
	sizex : Par
	"""Adjusts the size of the rectangle in X and Y. If the size of the rectangle is being chosen from a Camera, or from a connected input SOP, then this parameter behaves as a scale. Otherwise it will set the size of the rectangle for all other modes."""
	sizey : Par
	"""Adjusts the size of the rectangle in X and Y. If the size of the rectangle is being chosen from a Camera, or from a connected input SOP, then this parameter behaves as a scale. Otherwise it will set the size of the rectangle for all other modes."""
	tx : Par
	"""These X, Y, and Z Values determine where the center of the Rectangle is located. If the position of the rectangle is being chosen from a Camera, or from a connected input SOP, then this parameter behaves as an offset. Otherwise it will set the center of the rectangle for all other modes."""
	ty : Par
	"""These X, Y, and Z Values determine where the center of the Rectangle is located. If the position of the rectangle is being chosen from a Camera, or from a connected input SOP, then this parameter behaves as an offset. Otherwise it will set the center of the rectangle for all other modes."""
	tz : Par
	"""These X, Y, and Z Values determine where the center of the Rectangle is located. If the position of the rectangle is being chosen from a Camera, or from a connected input SOP, then this parameter behaves as an offset. Otherwise it will set the center of the rectangle for all other modes."""
	texture : Par
	"""Menu : Texture addes (0,1) coordinates to the vertices when set to <span class="tipTextSOP">Face</span>. Creates a rectangle without uv attributes when set to <span class="tipTextSOP">Off</span>."""
	par : parameter.rectangleSOP
	"""Parameters of parameter.rectangleSOP"""
	pass


class refineSOP():
	"""refineSOP"""
	space : Par
	"""Menu : Specify how to measure along splines / curves."""
	subdivspace : Par
	""" : Subdivide refines a primitive such that the subdivision causes a sharp discontinuity if ever displaced. In essence subdivide is equivalent to refine for polygons and Bziers, since any refinement causes a potential discontinuity. In the case of a NURBS it is equivalent to a maximum refinement (i.e. count = primitive basis order - 1)."""
	par : parameter.refineSOP
	"""Parameters of parameter.refineSOP"""
	pass


class revolveSOP():
	"""revolveSOP"""
	surftype : Par
	"""Menu : This option is used to select the type of surface, when using a Mesh Primitive Type."""
	originx : Par
	"""Coordinates defining the origin of the revolution."""
	originy : Par
	"""Coordinates defining the origin of the revolution."""
	originz : Par
	"""Coordinates defining the origin of the revolution."""
	dirx : Par
	"""X, Y, and Z coordinates of the direction vector defining the direction of the revolve."""
	diry : Par
	"""X, Y, and Z coordinates of the direction vector defining the direction of the revolve."""
	dirz : Par
	"""X, Y, and Z coordinates of the direction vector defining the direction of the revolve."""
	type : Par
	"""Menu : Determines how the revolve should be generated."""
	angle : Par
	"""Float : The start and end angles of the revolve. A revolve will start at the beginning angle, and proceed towards the ending angle. If <span class="tipTextSOP">Beginning</span> = <code>0</code> and <span class="tipTextSOP">End</span> = <code>360</code> it will be fully revolved. Values greater than 360 are also valid."""
	par : parameter.revolveSOP
	"""Parameters of parameter.revolveSOP"""
	pass


class scriptSOP():
	"""scriptSOP"""
	par : parameter.scriptSOP
	"""Parameters of parameter.scriptSOP"""
	pass


class selectSOP():
	"""selectSOP"""
	par : parameter.selectSOP
	"""Parameters of parameter.selectSOP"""
	pass


class sequenceblendSOP():
	"""sequenceblendSOP"""
	par : parameter.sequenceblendSOP
	"""Parameters of parameter.sequenceblendSOP"""
	pass


class skinSOP():
	"""skinSOP"""
	surftype : Par
	"""Menu : (Results only viewable for polygons and meshes)."""
	closev : Par
	"""Menu : This menu (menu: Off, On, If primitive does) setting determines whether the surface should be wrapped in the V parametric direction. The options are to open (Off), close (On), or inherit the closure type from the cross-sections. V Wrap is ignored when doing bilinear skinning."""
	skinops : Par
	"""Menu : Can optionally skin subgroups of n primitives or every nth primitive in a cyclical manner.	
		
'''For example'''; assume there are six primitives numbered for 0 - 5, and <span class="tipTextSOP">N</span> = 2. Then,		
		
* Groups will generate 0-1 2-3 4-5		
* Skipping will generate 0-2-6 and 1-3-5."""
	par : parameter.skinSOP
	"""Parameters of parameter.skinSOP"""
	pass


class sortSOP():
	"""sortSOP"""
	ptsort : Par
	"""Menu : Sort the points in the input geometry, according to the following criteria:"""
	pointproxx : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	pointproxy : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	pointproxz : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	pointdirx : Par
	"""Allows you to specify a unique vector along which points can be sorted."""
	pointdiry : Par
	"""Allows you to specify a unique vector along which points can be sorted."""
	pointdirz : Par
	"""Allows you to specify a unique vector along which points can be sorted."""
	primsort : Par
	"""Menu : Sort the primitives according to the following criteria:"""
	primproxx : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	primproxy : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	primproxz : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	primdirx : Par
	"""Allows you to specify a unique vector along which primitives can be sorted."""
	primdiry : Par
	"""Allows you to specify a unique vector along which primitives can be sorted."""
	primdirz : Par
	"""Allows you to specify a unique vector along which primitives can be sorted."""
	partsort : Par
	"""Menu : Sort the primitives according to the following criteria:"""
	partproxx : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	partproxy : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	partproxz : Par
	"""The X, Y and Z coordinates to reference when sorting by <span class="tipTextSOP">Proximity to Point</span>."""
	partdirx : Par
	"""Allows you to specify a unique vector along which particles can be sorted."""
	partdiry : Par
	"""Allows you to specify a unique vector along which particles can be sorted."""
	partdirz : Par
	"""Allows you to specify a unique vector along which particles can be sorted."""
	par : parameter.sortSOP
	"""Parameters of parameter.sortSOP"""
	pass


class sphereSOP():
	"""sphereSOP"""
	type : Par
	"""Menu : Select from the following types. For information on the different types, see the [[:Category:Geometry|Geometry]] category articles. Depending on the primitive type chosen, some SOP options may not apply."""
	surftype : Par
	"""Menu : This option is used to select the type of surface, when using a <span class="tipTextSOP">Mesh Primitive Type</span>."""
	radx : Par
	"""The radius of the sphere in X, Y and Z."""
	rady : Par
	"""The radius of the sphere in X, Y and Z."""
	radz : Par
	"""The radius of the sphere in X, Y and Z."""
	tx : Par
	"""Offset of sphere center from object center."""
	ty : Par
	"""Offset of sphere center from object center."""
	tz : Par
	"""Offset of sphere center from object center."""
	rx : Par
	"""These three fields rotate the Sphere along the X, Y, and Z axes."""
	ry : Par
	"""These three fields rotate the Sphere along the X, Y, and Z axes."""
	rz : Par
	"""These three fields rotate the Sphere along the X, Y, and Z axes."""
	orient : Par
	"""Menu : Determines axis for sphere. Poles of sphere align with orientation axis."""
	texture : Par
	"""Menu : Adds UV texture coordinates to the sphere."""
	par : parameter.sphereSOP
	"""Parameters of parameter.sphereSOP"""
	pass


class sprinkleSOP():
	"""sprinkleSOP"""
	method : Par
	"""Menu : Describes where points are located."""
	par : parameter.sprinkleSOP
	"""Parameters of parameter.sprinkleSOP"""
	pass


class stitchSOP():
	"""stitchSOP"""
	stitchop : Par
	"""Menu : Stitches sub-groups of n primitives or patterns of primitives."""
	dir : Par
	"""Menu : Allows stitching along either the U or V parametric direction."""
	leftuv1 : Par
	"""Point on each left / right primitive at which to begin / end the stitch."""
	leftuv2 : Par
	"""Point on each left / right primitive at which to begin / end the stitch."""
	rightuv1 : Par
	"""Point on each left / right primitive at which to begin / end the stitch."""
	rightuv2 : Par
	"""Point on each left / right primitive at which to begin / end the stitch."""
	lrwidth1 : Par
	"""The first value represents the width of the left stitch. The second value represents the width of the right stitch."""
	lrwidth2 : Par
	"""The first value represents the width of the left stitch. The second value represents the width of the right stitch."""
	lrscale1 : Par
	"""Use this parameter to control the direction and position of the tangential slopes."""
	lrscale2 : Par
	"""Use this parameter to control the direction and position of the tangential slopes."""
	par : parameter.stitchSOP
	"""Parameters of parameter.stitchSOP"""
	pass


class superquadSOP():
	"""superquadSOP"""
	type : Par
	"""Menu : Select from the following types. For information on the different types, see the [http://www.derivativeinc.com/Tools/Touch000/Manual/Guides/GeoTypesGuide/GeometryTypes.pdf Geometry Types Guide]. Depending on the primitive type chosen, some SOP options may not apply."""
	surftype : Par
	"""Menu : This option is used to select the type of surface, when using a <span class="tipTextSOP">Mesh</span> primitive type."""
	radx : Par
	"""Determines overall radius."""
	rady : Par
	"""Determines overall radius."""
	radz : Par
	"""Determines overall radius."""
	tx : Par
	"""Offset of superquad center from object center."""
	ty : Par
	"""Offset of superquad center from object center."""
	tz : Par
	"""Offset of superquad center from object center."""
	orient : Par
	"""Menu : Determines pole axis for the iso surface."""
	texture : Par
	"""Menu : Adds UV texture coordinates to the sphere."""
	par : parameter.superquadSOP
	"""Parameters of parameter.superquadSOP"""
	pass


class sweepSOP():
	"""sweepSOP"""
	cycle : Par
	"""Menu : Determines the Cycle Type based on these menu options."""
	skin : Par
	"""Menu : Determines the output based on these menu options."""
	par : parameter.sweepSOP
	"""Parameters of parameter.sweepSOP"""
	pass


class textSOP():
	"""textSOP"""
	output : Par
	"""Menu : """
	readingdirection : Par
	"""Menu : Use to set whether the language reads Left to Right or Right to Left."""
	kerning1 : Par
	"""The amount of space to add between letters in X and Y. Kerning is way of adding an arbitrary offset between letters. There already is a default offset associated with each font so the letters are flush against each other. The <span class="tipTextSOP">Kerning</span> parameter this adds to that and allows for a Y offset."""
	kerning2 : Par
	"""The amount of space to add between letters in X and Y. Kerning is way of adding an arbitrary offset between letters. There already is a default offset associated with each font so the letters are flush against each other. The <span class="tipTextSOP">Kerning</span> parameter this adds to that and allows for a Y offset."""
	alignx : Par
	"""Menu : Sets the horizontal alignment."""
	xord : Par
	"""Menu : Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu."""
	rord : Par
	"""Menu : Sets the order of the rotations within the overall transform order."""
	tx : Par
	"""These three fields move the geometry in the three axes."""
	ty : Par
	"""These three fields move the geometry in the three axes."""
	tz : Par
	"""These three fields move the geometry in the three axes."""
	rx : Par
	"""These three fields rotate the geometry in the three axes."""
	ry : Par
	"""These three fields rotate the geometry in the three axes."""
	rz : Par
	"""These three fields rotate the geometry in the three axes."""
	sx : Par
	"""These three fields scale the geometry in the three axes."""
	sy : Par
	"""These three fields scale the geometry in the three axes."""
	sz : Par
	"""These three fields scale the geometry in the three axes."""
	px : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.	
			
For example, during a scaling operation, if the pivot point of an object is located at: <code>-1, -1, 0</code> and you wanted to scale the object by <code>0.5</code> (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left."""
	py : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.	
			
For example, during a scaling operation, if the pivot point of an object is located at: <code>-1, -1, 0</code> and you wanted to scale the object by <code>0.5</code> (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left."""
	pz : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.	
			
For example, during a scaling operation, if the pivot point of an object is located at: <code>-1, -1, 0</code> and you wanted to scale the object by <code>0.5</code> (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left."""
	par : parameter.textSOP
	"""Parameters of parameter.textSOP"""
	pass


class textureSOP():
	"""textureSOP"""
	type : Par
	"""Menu : The <span class="tipTextSOP">Face</span>, <span class="tipTextSOP">Uniform Spline</span>, and <span class="tipTextSOP">Arc-Length Spline</span> texturing methods accept spline curves as well as polygons.	
			
When using one of the spline-based methods, specifying a paste hierarchy in the <span class="tipTextSOP">Group</span> field will propagate the computation of texture coordinates to all of its nodes. Projection methods will typically yield smoother texture continuity between pasted surfaces than any of the spline methods. Sometimes it helps ensuring that pasted features are Chord-length parameterized with the [[Basis SOP]]."""
	axis : Par
	"""Menu : Axis to project along, or projection method from splines. X, Y, or Z axes."""
	coord : Par
	"""Menu : Select to apply texture coordinates to their Natural Location, Point textures, or Vertex textures.	
			
When <span class="tipTextSOP">Natural location</span> is selected, the UV's will be applied to the verticies when using <span class="tipTextSOP">Polar</span>, <span class="tipTextSOP">Cylindrical</span>, <span class="tipTextSOP">Rows and Columns</span>, and <span class="tipTextSOP">Face</span> texture types.  <span class="tipTextSOP">Orthographic</span>, <span class="tipTextSOP">Uniform Spline</span>, <span class="tipTextSOP">Average Spline</span> and <span class="tipTextSOP">Arc Length Spline</span> will always generate point UV's when you choose <span class="tipTextSOP">Natural</span>.			
			
Natural Location will also create vertex uvs when creating new texture layers, if a vertex uv already exists for layer 0.			
			
IIf the primitive is open in both directions like a grid or a surface (so that the ends do not touch), then the advantage of vertex UV's does not apply since there are no matched seams on the single surface to worry about.			
			
Using vertex UVs gives you unique points at the closed seam whereas point UVs are shared at seams and are, by default given a value of 0 for either U or V depending on the closed direction of the surface. If you want to make a closed surface open, simply insert a [[Carve SOP]] in the chain and place a single carve in the surface of the direction that the surface is closed."""
	su : Par
	"""Scales the texture coordinates a specific amount."""
	sv : Par
	"""Scales the texture coordinates a specific amount."""
	sw : Par
	"""Scales the texture coordinates a specific amount."""
	offsetu : Par
	"""Offsets the texture coordinates a specific amount."""
	offsetv : Par
	"""Offsets the texture coordinates a specific amount."""
	offsetw : Par
	"""Offsets the texture coordinates a specific amount."""
	xord : Par
	"""Menu : Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu."""
	rord : Par
	"""Menu : Sets the order of the rotations within the overall transform order."""
	tx : Par
	"""These three fields move the texture coordinates in the three axes."""
	ty : Par
	"""These three fields move the texture coordinates in the three axes."""
	tz : Par
	"""These three fields move the texture coordinates in the three axes."""
	rx : Par
	"""These three fields rotate the texture coordinates in the three axes."""
	ry : Par
	"""These three fields rotate the texture coordinates in the three axes."""
	rz : Par
	"""These three fields rotate the texture coordinates in the three axes."""
	scaletwox : Par
	"""These three fields scale the texture coordinates in the three axes."""
	scaletwoy : Par
	"""These three fields scale the texture coordinates in the three axes."""
	scaletwoz : Par
	"""These three fields scale the texture coordinates in the three axes."""
	px : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which the texture coordinates scale and rotate. Altering the pivot point produces different results depending on the transformation performed.	
			
For example, during a scaling operation, if the pivot point of the texture coordinates is located at: <code>-1, -1, 0</code> and you wanted to scale by <code>0.5</code> (reduce its size by 50%) the texture would scale toward the pivot point and appear to slide down and to the left.			
			
[[Image:TouchGeometry91.gif]]			
			
In the example above, rotations performed on a texture coordinates with different pivot points produce very different results."""
	py : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which the texture coordinates scale and rotate. Altering the pivot point produces different results depending on the transformation performed.	
			
For example, during a scaling operation, if the pivot point of the texture coordinates is located at: <code>-1, -1, 0</code> and you wanted to scale by <code>0.5</code> (reduce its size by 50%) the texture would scale toward the pivot point and appear to slide down and to the left.			
			
[[Image:TouchGeometry91.gif]]			
			
In the example above, rotations performed on a texture coordinates with different pivot points produce very different results."""
	pz : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which the texture coordinates scale and rotate. Altering the pivot point produces different results depending on the transformation performed.	
			
For example, during a scaling operation, if the pivot point of the texture coordinates is located at: <code>-1, -1, 0</code> and you wanted to scale by <code>0.5</code> (reduce its size by 50%) the texture would scale toward the pivot point and appear to slide down and to the left.			
			
[[Image:TouchGeometry91.gif]]			
			
In the example above, rotations performed on a texture coordinates with different pivot points produce very different results."""
	par : parameter.textureSOP
	"""Parameters of parameter.textureSOP"""
	pass


class torusSOP():
	"""torusSOP"""
	type : Par
	"""Menu : Select from the following types. For information on the different types, see the [[:Category:Geometry|Geometry]] category articles."""
	surftype : Par
	"""Menu : This option is used to select the type of surface, when using a <span class="tipTextSOP">Mesh</span> primitive type."""
	orient : Par
	"""Menu : The axis along which the torus is constructed."""
	radx : Par
	"""The first value (radx) defines the radius of the torus, the second value (rady) determines the radius of the inner ring.	
			
[[Image:TouchGeometry256.gif]]"""
	rady : Par
	"""The first value (radx) defines the radius of the torus, the second value (rady) determines the radius of the inner ring.	
			
[[Image:TouchGeometry256.gif]]"""
	tx : Par
	"""Offset of torus center from object origin."""
	ty : Par
	"""Offset of torus center from object origin."""
	tz : Par
	"""Offset of torus center from object origin."""
	angleu : Par
	"""Float : The start and end sweep angles of the torus, if <span class="tipTextSOP">U Wrap</span> is not enabled."""
	anglev : Par
	"""Float : These are the start and end angles of the cross-section circle that is swept to make the torus, if <span class="tipTextSOP">V Wrap</span> is not enabled."""
	par : parameter.torusSOP
	"""Parameters of parameter.torusSOP"""
	pass


class traceSOP():
	"""traceSOP"""
	par : parameter.traceSOP
	"""Parameters of parameter.traceSOP"""
	pass


class trailSOP():
	"""trailSOP"""
	result : Par
	"""Menu : How to construct the trail geometry."""
	surftype : Par
	"""Menu : This option is used to select the type of surface, when using a <span class="tipTextSOP">Mesh Primitive Type</span>."""
	par : parameter.trailSOP
	"""Parameters of parameter.trailSOP"""
	pass


class transformSOP():
	"""transformSOP"""
	xord : Par
	"""Menu : Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu."""
	rord : Par
	"""Menu : Sets the order of the rotations within the overall transform order."""
	tx : Par
	"""These three fields move the Source geometry in the three axes."""
	ty : Par
	"""These three fields move the Source geometry in the three axes."""
	tz : Par
	"""These three fields move the Source geometry in the three axes."""
	rx : Par
	"""These three fields rotate the Source geometry in the three axes."""
	ry : Par
	"""These three fields rotate the Source geometry in the three axes."""
	rz : Par
	"""These three fields rotate the Source geometry in the three axes."""
	sx : Par
	"""These three fields scale the Source geometry in the three axes."""
	sy : Par
	"""These three fields scale the Source geometry in the three axes."""
	sz : Par
	"""These three fields scale the Source geometry in the three axes."""
	px : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.	
			
For example, during a scaling operation, if the pivot point of an object is located at: <code>-1, -1, 0</code> and you wanted to scale the object by <code>0.5</code> (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left.			
			
[[Image:TouchGeometry91.gif]]			
			
In the example above, rotations performed on an object with different pivot points produce very different results."""
	py : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.	
			
For example, during a scaling operation, if the pivot point of an object is located at: <code>-1, -1, 0</code> and you wanted to scale the object by <code>0.5</code> (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left.			
			
[[Image:TouchGeometry91.gif]]			
			
In the example above, rotations performed on an object with different pivot points produce very different results."""
	pz : Par
	"""The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object.	
			
For example, during a scaling operation, if the pivot point of an object is located at: <code>-1, -1, 0</code> and you wanted to scale the object by <code>0.5</code> (reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left.			
			
[[Image:TouchGeometry91.gif]]			
			
In the example above, rotations performed on an object with different pivot points produce very different results."""
	upvectorx : Par
	"""When orienting an object, the <span class="tipTextSOP">Up Vector</span> is used to determine where the positive Y axis points."""
	upvectory : Par
	"""When orienting an object, the <span class="tipTextSOP">Up Vector</span> is used to determine where the positive Y axis points."""
	upvectorz : Par
	"""When orienting an object, the <span class="tipTextSOP">Up Vector</span> is used to determine where the positive Y axis points."""
	posttx : Par
	"""Menu : Sets the center of the geometry after the Transform page has been applied."""
	fromx : Par
	"""Menu : Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above."""
	tox : Par
	"""Menu : When using Reference Input this determines which part of the Reference Input to align the geometry to."""
	postty : Par
	"""Menu : Sets the center of the geometry after the Transform page has been applied."""
	fromy : Par
	"""Menu : Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above."""
	toy : Par
	"""Menu : When using Reference Input this determines which part of the Reference Input to align the geometry to."""
	posttz : Par
	"""Menu : Sets the center of the geometry after the Transform page has been applied."""
	fromz : Par
	"""Menu : Determines which part of the input geometry to align to the Origin or Reference Input as selected in Post Translate parameter above."""
	toz : Par
	"""Menu : When using Reference Input this determines which part of the Reference Input to align the geometry to."""
	postscale : Par
	"""Menu : Sets the scale of the geometry after the Transform page has been applied."""
	postscalex : Par
	"""Menu : Sets the scale of the geometry after the Transform page has been applied to scale."""
	postscaley : Par
	"""Menu : Sets the scale of the geometry after the Transform page has been applied to scale."""
	postscalez : Par
	"""Menu : Sets the scale of the geometry after the Transform page has been applied to scale."""
	par : parameter.transformSOP
	"""Parameters of parameter.transformSOP"""
	pass


class trimSOP():
	"""trimSOP"""
	optype : Par
	"""Menu : The types of trimming operations available."""
	par : parameter.trimSOP
	"""Parameters of parameter.trimSOP"""
	pass


class tristripSOP():
	"""tristripSOP"""
	par : parameter.tristripSOP
	"""Parameters of parameter.tristripSOP"""
	pass


class tubeSOP():
	"""tubeSOP"""
	type : Par
	"""Menu : Select from the following types. For information on the different types, see the [[:Category:Geometry|Geometry]] category articles."""
	surftype : Par
	"""Menu : This option is used to select the type of surface, when using a Mesh Primitive Type."""
	orient : Par
	"""Menu : Primary axis of tube (long axis)."""
	rord : Par
	"""Menu : """
	tx : Par
	"""Location of the tube center from the object origin."""
	ty : Par
	"""Location of the tube center from the object origin."""
	tz : Par
	"""Location of the tube center from the object origin."""
	rx : Par
	""""""
	ry : Par
	""""""
	rz : Par
	""""""
	rad1 : Par
	"""The first field is the radius of the top of the tube and the second field represents the radius of the bottom of the tube."""
	rad2 : Par
	"""The first field is the radius of the top of the tube and the second field represents the radius of the bottom of the tube."""
	texture : Par
	"""Menu : Adds UV texture coordinates to the sphere."""
	par : parameter.tubeSOP
	"""Parameters of parameter.tubeSOP"""
	pass


class vertexSOP():
	"""vertexSOP"""
	doclr : Par
	"""Menu : Select between keeping the color, adding new color, or using no color for vertex color attributes from incoming geometry."""
	diffr : Par
	"""If you select 'Add Color' from the menu above, Cd color vertex attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are: <code>me.inputColor[0]</code> for red, <code>me.inputColor[1]</code> for green, <code>me.inputColor[2]</code> for blue, and <code>me.inputColor[3]</code> for alpha. If you select 'No Color' from the menu above, the Cd color vertex attribute will be removed from the SOP."""
	diffg : Par
	"""If you select 'Add Color' from the menu above, Cd color vertex attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are: <code>me.inputColor[0]</code> for red, <code>me.inputColor[1]</code> for green, <code>me.inputColor[2]</code> for blue, and <code>me.inputColor[3]</code> for alpha. If you select 'No Color' from the menu above, the Cd color vertex attribute will be removed from the SOP."""
	diffb : Par
	"""If you select 'Add Color' from the menu above, Cd color vertex attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are: <code>me.inputColor[0]</code> for red, <code>me.inputColor[1]</code> for green, <code>me.inputColor[2]</code> for blue, and <code>me.inputColor[3]</code> for alpha. If you select 'No Color' from the menu above, the Cd color vertex attribute will be removed from the SOP."""
	douvw : Par
	"""Menu : Select between keeping the texture coordinates, adding new texture coordinates, or using no texture coordinates for the vertex texture attributes from incoming geometry."""
	mapu : Par
	"""If you select 'Add Texture' from the menu above, uv texture coordinate vertex attributes will be added/modified in the SOP. Enter expressions here to control the values of the vertex texture coordinates here. The attributes to modify are: <code>me.inputTexture[0]</code>, <code>me.inputTexture[1]</code> and <code>me.inputTexture[2]</code>. If you select 'No Texture' from the menu above, the uv texture coordinates vertex attribute will be removed from the SOP."""
	mapv : Par
	"""If you select 'Add Texture' from the menu above, uv texture coordinate vertex attributes will be added/modified in the SOP. Enter expressions here to control the values of the vertex texture coordinates here. The attributes to modify are: <code>me.inputTexture[0]</code>, <code>me.inputTexture[1]</code> and <code>me.inputTexture[2]</code>. If you select 'No Texture' from the menu above, the uv texture coordinates vertex attribute will be removed from the SOP."""
	mapw : Par
	"""If you select 'Add Texture' from the menu above, uv texture coordinate vertex attributes will be added/modified in the SOP. Enter expressions here to control the values of the vertex texture coordinates here. The attributes to modify are: <code>me.inputTexture[0]</code>, <code>me.inputTexture[1]</code> and <code>me.inputTexture[2]</code>. If you select 'No Texture' from the menu above, the uv texture coordinates vertex attribute will be removed from the SOP."""
	docrease : Par
	"""Menu : Select between keeping the crease, adding new crease, or using no crease for creaseweight attribute from incoming geometry.	
		
The <code>Crease Weight</code> attribute can be used to set individual edge crease weights for sub-division surfaces (see [[Subdivide SOP]] ). This vertex attribute defines the weight for the edge which goes from that vertex to the next vertex in the polygon. For example, with a triangle (which has vertices 0, 1, 2), the attribute for vertex 1 defines the crease weight for the edge (1, 2). The attribute for vertex 2 defines the crease weight for edge (2, 0). The crease weight should be greater than 0. The larger the value for crease weights, the sharper the edge will be when sub-divided.		
		
Crease attributes can be visualized by passing them into a [[Subdivide SOP]]."""
	custom1type : Par
	"""Menu : The type of attribute created can be selected from this menu."""
	custom1val1 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	custom1val2 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	custom1val3 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	custom1val4 : Par
	"""Set the values of the Custom Attrib using these parameters."""
	par : parameter.vertexSOP
	"""Parameters of parameter.vertexSOP"""
	pass


class wireframeSOP():
	"""wireframeSOP"""
	par : parameter.wireframeSOP
	"""Parameters of parameter.wireframeSOP"""
	pass


class artnetDAT():
	"""artnetDAT"""
	par : parameter.artnetDAT
	"""Parameters of parameter.artnetDAT"""
	pass


class chopexecuteDAT():
	"""chopexecuteDAT"""
	executeloc : Par
	"""Menu : ([[Operator Language|Tscript]] only) Determines the location the script is run from."""
	freq : Par
	"""Menu : Enabled when using the <span class="tipTextDAT">While On</span> or <span class="tipTextDAT">While Off</span> options above.  Determines if the DAT executes <span class="tipTextDAT">For Every Sample</span> or <span class="tipTextDAT">Once Per Frame</span>."""
	par : parameter.chopexecuteDAT
	"""Parameters of parameter.chopexecuteDAT"""
	pass


class choptoDAT():
	"""choptoDAT"""
	output : Par
	"""Menu : Create a row per channel or column per channel."""
	par : parameter.choptoDAT
	"""Parameters of parameter.choptoDAT"""
	pass


class clipDAT():
	"""clipDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.clipDAT
	"""Parameters of parameter.clipDAT"""
	pass


class convertDAT():
	"""convertDAT"""
	how : Par
	"""Menu : Convert text format."""
	par : parameter.convertDAT
	"""Parameters of parameter.convertDAT"""
	pass


class cplusplusDAT():
	"""cplusplusDAT"""
	par : parameter.cplusplusDAT
	"""Parameters of parameter.cplusplusDAT"""
	pass


class datexecuteDAT():
	"""datexecuteDAT"""
	executeloc : Par
	"""Menu : ([[Operator Language|Tscript]] only) Determines the location the script is run from."""
	execute : Par
	"""Menu : Determines if the methods are executed at the start of the frame or end of the frame."""
	par : parameter.datexecuteDAT
	"""Parameters of parameter.datexecuteDAT"""
	pass


class errorDAT():
	"""errorDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.errorDAT
	"""Parameters of parameter.errorDAT"""
	pass


class etherdreamDAT():
	"""etherdreamDAT"""
	par : parameter.etherdreamDAT
	"""Parameters of parameter.etherdreamDAT"""
	pass


class evaluateDAT():
	"""evaluateDAT"""
	output : Par
	"""StrMenu : Determines what format will be used for output from the DAT."""
	outputsize : Par
	"""Menu : If the Output Table Size parameter is Strings, Expressions, or Commands, and there is a second input, you can choose the output table size to be either Input DAT or the Formula DAT.  If the Formula DAT is chosen and its table size is greater than the input data table, then the last cell in each row or column will be used when evaluating the remaining formulas."""
	par : parameter.evaluateDAT
	"""Parameters of parameter.evaluateDAT"""
	pass


class examineDAT():
	"""examineDAT"""
	source : Par
	"""Menu : Specifies what part of the operator to examine."""
	format : Par
	"""Menu : Determines whether the output is raw text or in table format."""
	par : parameter.examineDAT
	"""Parameters of parameter.examineDAT"""
	pass


class executeDAT():
	"""executeDAT"""
	executeloc : Par
	"""Menu : ([[Operator Language|Tscript]] only) Determines the location the script is run from."""
	par : parameter.executeDAT
	"""Parameters of parameter.executeDAT"""
	pass


class fifoDAT():
	"""fifoDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.fifoDAT
	"""Parameters of parameter.fifoDAT"""
	pass


class fileinDAT():
	"""fileinDAT"""
	par : parameter.fileinDAT
	"""Parameters of parameter.fileinDAT"""
	pass


class fileoutDAT():
	"""fileoutDAT"""
	par : parameter.fileoutDAT
	"""Parameters of parameter.fileoutDAT"""
	pass


class folderDAT():
	"""folderDAT"""
	nameformat : Par
	"""Menu : Select whether to include the filename extension or not."""
	dateformat : Par
	"""Menu : The format used to display the item's dates in the table."""
	type : Par
	"""Menu : The types of contents to display."""
	par : parameter.folderDAT
	"""Parameters of parameter.folderDAT"""
	pass


class inDAT():
	"""inDAT"""
	par : parameter.inDAT
	"""Parameters of parameter.inDAT"""
	pass


class indicesDAT():
	"""indicesDAT"""
	par : parameter.indicesDAT
	"""Parameters of parameter.indicesDAT"""
	pass


class infoDAT():
	"""infoDAT"""
	par : parameter.infoDAT
	"""Parameters of parameter.infoDAT"""
	pass


class insertDAT():
	"""insertDAT"""
	insert : Par
	"""Menu : Specify what to insert."""
	at : Par
	"""Menu : Specify where to insert."""
	par : parameter.insertDAT
	"""Parameters of parameter.insertDAT"""
	pass


class jsonDAT():
	"""jsonDAT"""
	output : Par
	"""Menu : Select the output of the JSON DAT."""
	par : parameter.jsonDAT
	"""Parameters of parameter.jsonDAT"""
	pass


class keyboardinDAT():
	"""keyboardinDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.keyboardinDAT
	"""Parameters of parameter.keyboardinDAT"""
	pass


class lookupDAT():
	"""lookupDAT"""
	index : Par
	"""dropmenu : Select how the index values are interpreted: as values/indices contained in a column or contained in a row."""
	valueloction : Par
	"""dropmenu : When 'Row Values' or 'Col Values' is selected in the Index Parameter, this parameter lets you select how the lookup row or column where the index value searches will be specified."""
	par : parameter.lookupDAT
	"""Parameters of parameter.lookupDAT"""
	pass


class mergeDAT():
	"""mergeDAT"""
	how : Par
	"""Menu : Sets how tables are merged together."""
	par : parameter.mergeDAT
	"""Parameters of parameter.mergeDAT"""
	pass


class midieventDAT():
	"""midieventDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.midieventDAT
	"""Parameters of parameter.midieventDAT"""
	pass


class midiinDAT():
	"""midiinDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.midiinDAT
	"""Parameters of parameter.midiinDAT"""
	pass


class monitorsDAT():
	"""monitorsDAT"""
	monitors : Par
	"""Menu : Specify which monitors to report information about."""
	units : Par
	"""Menu : Specify if the numbers are reported in Native Pixel units or DPI Scaled units."""
	par : parameter.monitorsDAT
	"""Parameters of parameter.monitorsDAT"""
	pass


class mqttclientDAT():
	"""mqttclientDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.mqttclientDAT
	"""Parameters of parameter.mqttclientDAT"""
	pass


class multitouchinDAT():
	"""multitouchinDAT"""
	outputtype : Par
	"""Menu : Sets how the output is displayed in the table."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.multitouchinDAT
	"""Parameters of parameter.multitouchinDAT"""
	pass


class ndiDAT():
	"""ndiDAT"""
	par : parameter.ndiDAT
	"""Parameters of parameter.ndiDAT"""
	pass


class nullDAT():
	"""nullDAT"""
	par : parameter.nullDAT
	"""Parameters of parameter.nullDAT"""
	pass


class opexecuteDAT():
	"""opexecuteDAT"""
	executeloc : Par
	"""Menu : ([[Operator Language|Tscript]] only) Determines the location the script is run from."""
	par : parameter.opexecuteDAT
	"""Parameters of parameter.opexecuteDAT"""
	pass


class opfindDAT():
	"""opfindDAT"""
	activecook : Par
	"""Menu : Determines when to cook the DAT."""
	combinefilters : Par
	"""Menu : Combine 'All', 'Any' or 'Custom' of the filters below to get a match. 'Custom' allows for specifying a subselection of filters with 'or' and 'and' keywords."""
	par : parameter.opfindDAT
	"""Parameters of parameter.opfindDAT"""
	pass


class oscinDAT():
	"""oscinDAT"""
	protocol : Par
	"""Menu : Select which protocol to use, refer to the [[Network Protocols]] article for more information."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.oscinDAT
	"""Parameters of parameter.oscinDAT"""
	pass


class oscoutDAT():
	"""oscoutDAT"""
	protocol : Par
	"""Menu : Selects the network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.oscoutDAT
	"""Parameters of parameter.oscoutDAT"""
	pass


class outDAT():
	"""outDAT"""
	par : parameter.outDAT
	"""Parameters of parameter.outDAT"""
	pass


class panelexecuteDAT():
	"""panelexecuteDAT"""
	executeloc : Par
	"""Menu : ([[Operator Language|Tscript]] only) Determines the location the script is run from."""
	par : parameter.panelexecuteDAT
	"""Parameters of parameter.panelexecuteDAT"""
	pass


class parameterDAT():
	"""parameterDAT"""
	par : parameter.parameterDAT
	"""Parameters of parameter.parameterDAT"""
	pass


class parameterexecuteDAT():
	"""parameterexecuteDAT"""
	executeloc : Par
	"""Menu : ([[Operator Language|Tscript]] only) Determines the location the script is run from."""
	par : parameter.parameterexecuteDAT
	"""Parameters of parameter.parameterexecuteDAT"""
	pass


class pargroupexecuteDAT():
	"""pargroupexecuteDAT"""
	callbackmode : Par
	"""Menu : This controls the format of the 'curr' and 'prev' arguments to the callbacks."""
	par : parameter.pargroupexecuteDAT
	"""Parameters of parameter.pargroupexecuteDAT"""
	pass


class performDAT():
	"""performDAT"""
	triggermode : Par
	"""Menu : Offers two options for when to trigger a refresh of the logs."""
	par : parameter.performDAT
	"""Parameters of parameter.performDAT"""
	pass


class renderpickDAT():
	"""renderpickDAT"""
	strategy : Par
	"""Menu : Decides when to update values based on pick interactions."""
	responsetime : Par
	"""Menu : Determines when the values are updated."""
	position : Par
	"""Menu : Returns the position of the point picked on the geometry. Columns ''tx, ty, tz''."""
	normal : Par
	"""Menu : Returns the normals of the point picked on the geometry. Columns ''nx, ny, nz''."""
	par : parameter.renderpickDAT
	"""Parameters of parameter.renderpickDAT"""
	pass


class reorderDAT():
	"""reorderDAT"""
	reorder : Par
	"""Menu : This parameter allows you to reorder either rows or columns."""
	method : Par
	"""Menu : Specify how to reorder the table."""
	par : parameter.reorderDAT
	"""Parameters of parameter.reorderDAT"""
	pass


class scriptDAT():
	"""scriptDAT"""
	par : parameter.scriptDAT
	"""Parameters of parameter.scriptDAT"""
	pass


class selectDAT():
	"""selectDAT"""
	extractrows : Par
	"""Menu : This parameter allows you to pick different ways of specifying the rows selected."""
	extractcols : Par
	"""Menu : This parameter allows you to pick different ways of specifying the columns selected."""
	output : Par
	"""Menu : Determines what format will be used for output from the DAT."""
	par : parameter.selectDAT
	"""Parameters of parameter.selectDAT"""
	pass


class serialDAT():
	"""serialDAT"""
	format : Par
	"""Menu : Interpret the incoming data as binary or ASCII data. If the format is Per Byte, one row is appended for each binary byte received. If the format is Per Line, one row is appended for each null or newline delimited message received."""
	baudrate : Par
	"""Int : The maximum number of bits of information, including "control" bits, that are transmitted per second. Check your input device's default baud rate and set accordingly."""
	databits : Par
	"""Menu : This parameter sets the number of data bits sent in each. Data bits are transmitted "backwards". Backwards refers to the order of transmission, which is from least significant bit (LSB) to most significant bit (MSB). To interpret the data bits, you must read from right to left."""
	parity : Par
	"""Menu : This parameter can be set to none, even, or odd. The optional parity bit follows the data bits and is included as a simple means of error checking. Parity bits work by specifying ahead of time whether the parity of the transmission is to be even or odd. If the parity is set to be odd, the transmitter will then set the parity bit in such a way as to make an odd number of 1's among the data bits and the parity bit."""
	stopbits : Par
	"""Menu : The last part of transmission packet consists of 1 or 2 Stop bits. The connection will now wait for the next Start bit."""
	dtr : Par
	"""Menu : The DTR (data-terminal-ready) flow control. (Windows Only)."""
	rts : Par
	"""Menu : The RTS (request-to-send) flow control. (Windows Only)."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.serialDAT
	"""Parameters of parameter.serialDAT"""
	pass


class socketioDAT():
	"""socketioDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.socketioDAT
	"""Parameters of parameter.socketioDAT"""
	pass


class soptoDAT():
	"""soptoDAT"""
	extract : Par
	"""Menu : Specify whether to pull point data or primitive data."""
	par : parameter.soptoDAT
	"""Parameters of parameter.soptoDAT"""
	pass


class sortDAT():
	"""sortDAT"""
	sortmethod : Par
	"""Menu : Determines how the table will be sorted."""
	order : Par
	"""Menu : Determines the type of sorting."""
	unique : Par
	"""Menu : Remove duplicate rows/column entries in the sorted row/column."""
	par : parameter.sortDAT
	"""Parameters of parameter.sortDAT"""
	pass


class substituteDAT():
	"""substituteDAT"""
	match : Par
	"""Menu : Specify where to match:"""
	extractrows : Par
	"""Menu : This parameter allows you to pick different ways of specifying the rows scoped."""
	extractcols : Par
	"""Menu : This parameter allows you to pick different ways of specifying the columns scoped."""
	par : parameter.substituteDAT
	"""Parameters of parameter.substituteDAT"""
	pass


class switchDAT():
	"""switchDAT"""
	par : parameter.switchDAT
	"""Parameters of parameter.switchDAT"""
	pass


class tableDAT():
	"""tableDAT"""
	defaultreadencoding : Par
	"""Menu : Sets the expected file encoding format, or auto-detects the format.  UTF8, UTF16-LE, UTF16-BE, CP1252"""
	fill : Par
	"""Menu : You can create and fill rows and columns of a table. Fill Type menu gives 5 options: Manual, Set Size, Set Size and Contents, Fill by Column, and Fill by Row. When a Fill option is chosen, you can generate multiple rows/columns with specific headings using space-separated names or an expression, plus expressions to fill the cells."""
	par : parameter.tableDAT
	"""Parameters of parameter.tableDAT"""
	pass


class tcpipDAT():
	"""tcpipDAT"""
	mode : Par
	"""Menu : Specify if this operator is communicating as a '''client''' or a '''server'''."""
	format : Par
	"""Menu : Determines how the incoming data is parsed into the table."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.tcpipDAT
	"""Parameters of parameter.tcpipDAT"""
	pass


class textDAT():
	"""textDAT"""
	par : parameter.textDAT
	"""Parameters of parameter.textDAT"""
	pass


class touchinDAT():
	"""touchinDAT"""
	protocol : Par
	"""Menu : Select which protocol to use, refer to the [[Network Protocols]] article for more information."""
	par : parameter.touchinDAT
	"""Parameters of parameter.touchinDAT"""
	pass


class touchoutDAT():
	"""touchoutDAT"""
	protocol : Par
	"""Menu : Select which protocol to use, refer to the [[Network Protocols]] article for more information."""
	par : parameter.touchoutDAT
	"""Parameters of parameter.touchoutDAT"""
	pass


class transposeDAT():
	"""transposeDAT"""
	par : parameter.transposeDAT
	"""Parameters of parameter.transposeDAT"""
	pass


class tuioinDAT():
	"""tuioinDAT"""
	protocol : Par
	"""Menu : Select which protocol to use, refer to the [[Network Protocols]] article for more information."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.tuioinDAT
	"""Parameters of parameter.tuioinDAT"""
	pass


class udpinDAT():
	"""udpinDAT"""
	protocol : Par
	"""Menu : Select which protocol to use, refer to the [[Network Protocols]] article for more information."""
	format : Par
	"""Menu : Determines how the incoming data is parsed."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.udpinDAT
	"""Parameters of parameter.udpinDAT"""
	pass


class udpoutDAT():
	"""udpoutDAT"""
	protocol : Par
	"""Menu : Selects the network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	format : Par
	"""Menu : Determines how the incoming data is parsed."""
	localportmode : Par
	"""Menu : Choose between automatically or manually selecting local port to use."""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.udpoutDAT
	"""Parameters of parameter.udpoutDAT"""
	pass


class udtinDAT():
	"""udtinDAT"""
	protocol : Par
	""" : Select which protocol to use, refer to the [[Network Protocols]] article for more information."""
	format : Par
	""" : Determines how the incoming data is parsed into the table."""
	executeloc : Par
	""" : Determines the location the script is run from."""
	par : parameter.udtinDAT
	"""Parameters of parameter.udtinDAT"""
	pass


class udtoutDAT():
	"""udtoutDAT"""
	protocol : Par
	""" : Selects the network protocol to use. Refer to the [[Network Protocols]] article for more information."""
	format : Par
	""" : Determines how the incoming data is parsed."""
	executeloc : Par
	""" : Determines the location the script is run from."""
	par : parameter.udtoutDAT
	"""Parameters of parameter.udtoutDAT"""
	pass


class webclientDAT():
	"""webclientDAT"""
	reqmethod : Par
	"""Menu : Selects the [https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods HTTP request method]."""
	authtype : Par
	"""Menu : The type of authentication."""
	par : parameter.webclientDAT
	"""Parameters of parameter.webclientDAT"""
	pass


class webDAT():
	"""webDAT"""
	method : Par
	""" : Currently only POST is implemented, though this will be expanded with other techniques such as GET."""
	par : parameter.webDAT
	"""Parameters of parameter.webDAT"""
	pass


class webserverDAT():
	"""webserverDAT"""
	par : parameter.webserverDAT
	"""Parameters of parameter.webserverDAT"""
	pass


class webrtcDAT():
	"""webrtcDAT"""
	par : parameter.webrtcDAT
	"""Parameters of parameter.webrtcDAT"""
	pass


class websocketDAT():
	"""websocketDAT"""
	executeloc : Par
	"""Menu : Determines the location the script is run from."""
	par : parameter.websocketDAT
	"""Parameters of parameter.websocketDAT"""
	pass


class xmlDAT():
	"""xmlDAT"""
	merge : Par
	"""Menu : Merge and label can be used to combine two inputs of data. The second input must be XML formatted, and not SGML/HTML. These two parameters control where and how the second input is merged."""
	show : Par
	"""Menu : This controls how the selected elements are presented."""
	par : parameter.xmlDAT
	"""Parameters of parameter.xmlDAT"""
	pass


class constantMAT():
	"""constantMAT"""
	colorr : Par
	"""The color of the light reflected from the material."""
	colorg : Par
	"""The color of the light reflected from the material."""
	colorb : Par
	"""The color of the light reflected from the material."""
	colormap : Par
	"""TOP : Provides a TOP texture to use as a color map."""
	colormapextendu : Par
	"""Menu : """
	colormapextendv : Par
	"""Menu : """
	colormapextendw : Par
	"""Menu : """
	colormapfilter : Par
	"""Menu : """
	colormapanisotropy : Par
	"""Menu : """
	colormapcoord : Par
	"""Menu : """
	colormapcoordinterp : Par
	"""Menu : """
	par : parameter.constantMAT
	"""Parameters of parameter.constantMAT"""
	pass


class depthMAT():
	"""depthMAT"""
	par : parameter.depthMAT
	"""Parameters of parameter.depthMAT"""
	pass


class glslMAT():
	"""glslMAT"""
	glslversion : Par
	"""Menu : Pick what version of GLSL to compile the shader with."""
	inprim : Par
	"""Menu : The type of geometry that will be inputed into the Geometry Shader."""
	outprim : Par
	"""Menu : The type of geometry that the Geometry Shader will output."""
	lightingspace : Par
	"""Menu : Allows lighting space switch from the current default World Space to legacy Camera Space which was used for TouchDesigner 088."""
	top0 : Par
	"""TOP : This is the TOP that will be referenced by the above sampler name above it.	
				
'''Exposed by the + Button, texture sampling parameters''':				
				
Refer to the [[Texture Sampling Parameters]] article for more information on the parameters exposed by pressing the + button. The ''parameter'' prefix for each of the parameters is ''top[digit]''."""
	top0extendu : Par
	"""Menu : """
	top0extendv : Par
	"""Menu : """
	top0extendw : Par
	"""Menu : """
	top0filter : Par
	"""Menu : """
	top0anisotropy : Par
	"""Menu : """
	value0x : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	value0y : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	value0z : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	value0w : Par
	"""The value to assign to the uniform. If the uniform is a float the first entry of the four is used, if the uniform is a vec2 the first two entries are used, etc."""
	chopunitype0 : Par
	"""Menu : The type of the uniform. You can send up to 4 channels into the GLSL shader in a single uniform. For a CHOP with a single channel declare your uniform as a float, for one with two channels declare your uniform as a vec2, etc. The data is interleaved in the uniform. I.e., the .x component is the 1st channel, .y is the 2nd channel, etc."""
	choparraytype0 : Par
	"""Menu : GPUs can send array data into a GLSL shader using Uniform Arrays or Texture Buffers. A Uniform Array uses very limited memory to store its data, and can be access like any other regular uniform value (but in an array). Texture Buffers use texture memory and texture fetches to access the data, which allows them to store many more values.		
				
In both cases the index is the 0-based index (an integer) into the array/buffer that you want to get a value for."""
	chanscope0 : Par
	"""StrMenu : You can select which channels from the CHOP will be used to fill the array. Up to the first 4 channels scoped will be used (depending on the type of the uniform array)."""
	par : parameter.glslMAT
	"""Parameters of parameter.glslMAT"""
	pass


class inMAT():
	"""inMAT"""
	par : parameter.inMAT
	"""Parameters of parameter.inMAT"""
	pass


class lineMAT():
	"""lineMAT"""
	depthinterpolationmodel : Par
	"""dropmenu : Depth Interpolation Model depthmodel – a menu to select how the width of line items changes by their distance from the camera."""
	liftdirection : Par
	"""dropmenu : If a line is being drawn on a polygon or its edge (the polygon being in another Geometry COMP + shader), and you need to lift it off the surface to be fully visible, this specifies whether to displace the line points toward the camera or along the line's normal (which can be the direction of the polygon's normal)."""
	linejointtype : Par
	"""dropmenu : A menu to select the joint type where two lines segments meet."""
	linestartcaptype : Par
	"""dropmenu : A menu to Specify the end cap type at the Line start. You can control the size of each end cap type in the Cap page."""
	lineendcaptype : Par
	"""dropmenu : A menu to Specify the end cap type at the Line end."""
	linenearcolorr : Par
	"""Specifies the color value for the Line at the Distance Near plane and any location closer to camera."""
	linenearcolorg : Par
	"""Specifies the color value for the Line at the Distance Near plane and any location closer to camera."""
	linenearcolorb : Par
	"""Specifies the color value for the Line at the Distance Near plane and any location closer to camera."""
	linefarcolorr : Par
	"""Specifies the color value for the Line at the Distance Far plane and beyond (farther from camera)."""
	linefarcolorg : Par
	"""Specifies the color value for the Line at the Distance Far plane and beyond (farther from camera)."""
	linefarcolorb : Par
	"""Specifies the color value for the Line at the Distance Far plane and beyond (farther from camera)."""
	pointtype : Par
	"""dropmenu : A menu to select the Point type."""
	pointnearcolorr : Par
	"""Specifies the color value for the Point at the Distance Near plane and any location closer to camera."""
	pointnearcolorg : Par
	"""Specifies the color value for the Point at the Distance Near plane and any location closer to camera."""
	pointnearcolorb : Par
	"""Specifies the color value for the Point at the Distance Near plane and any location closer to camera."""
	pointfarcolorr : Par
	"""Specifies the color value for the Point at the Distance Far plane and beyond (farther from camera)."""
	pointfarcolorg : Par
	"""Specifies the color value for the Point at the Distance Far plane and beyond (farther from camera)."""
	pointfarcolorb : Par
	"""Specifies the color value for the Point at the Distance Far plane and beyond (farther from camera)."""
	pointliftdirection : Par
	"""dropmenu : A menu to select the the dirction to lift points.  See parameter Lift Direction."""
	attributetype : Par
	"""dropmenu : When drawing a vector at each point, this determines where to get the XYZ of the vector. By default it gets it from an attribute of the SOP, the point normal by default. But when instancing is used, you can get it from an instance attribute from an Instance OP. The vector can be represented in world space or in the reference frame of the Geometry COMP."""
	vectorstartcaptype : Par
	"""dropmenu : A menu to Specify the end cap type at the Vector start. You can control the size of each end cap type in the Cap page."""
	vectorendcaptype : Par
	"""dropmenu : A menu to Specify the end cap type at the Vector end. You can control the size of each end cap type in the Cap page."""
	vectornearcolorr : Par
	"""Specifies the color value for the Vector at the Distance Near plane and any location closer to camera."""
	vectornearcolorg : Par
	"""Specifies the color value for the Vector at the Distance Near plane and any location closer to camera."""
	vectornearcolorb : Par
	"""Specifies the color value for the Vector at the Distance Near plane and any location closer to camera."""
	vectorfarcolor : Par
	"""rgb : Specifies the color value for the Vector at the Distance Far plane and beyond (farther from camera)."""
	par : parameter.lineMAT
	"""Parameters of parameter.lineMAT"""
	pass


class NotSet():
	"""NotSet"""
	srcblend : Par
	"""Menu : This value is multiplied by the color value of the pixel that is being written to the Color-Buffer (also know as the Source Color)."""
	destblend : Par
	"""Menu : This value is multiplied by the color value of the pixel currently in the Color-Buffer (also known as the Destination Color)."""
	srcblenda : Par
	"""Menu : This value is multiplied by the alpha value of the pixel that is being written to the Color-Buffer (also know as the Source Alpha)."""
	destblenda : Par
	"""Menu : This value is multiplied by the alpha value of the pixel currently in the Color-Buffer (also known as the Destination Alpha)."""
	depthfunc : Par
	"""Menu : The depth value of the pixel being drawn is compared to the depth value currently in the depth-buffer using this function. If the test passes then the pixel is drawn to the Frame-Buffer. If the test fails the pixel is discarded and no changes are made to the Frame-Buffer."""
	alphafunc : Par
	"""Menu : This menu works in conjunction with the Alpha Threshold parameter below in determining which pixels to keep based on their alpha value."""
	wireframe : Par
	"""Menu : Enables and disables wire-frame rendering with the option of OpenGL Tesselated or Topology based wireframes."""
	cullface : Par
	"""Menu : Selects which faces to render."""
	par : parameter.NotSet
	"""Parameters of parameter.NotSet"""
	pass


class nullMAT():
	"""nullMAT"""
	par : parameter.nullMAT
	"""Parameters of parameter.nullMAT"""
	pass


class outMAT():
	"""outMAT"""
	par : parameter.outMAT
	"""Parameters of parameter.outMAT"""
	pass


class pbrMAT():
	"""pbrMAT"""
	basecolorr : Par
	"""Base color of the texture, used to calculate diffuse and specular contributions."""
	basecolorg : Par
	"""Base color of the texture, used to calculate diffuse and specular contributions."""
	basecolorb : Par
	"""Base color of the texture, used to calculate diffuse and specular contributions."""
	emitr : Par
	"""This is the color that the material will emit even if there is no light."""
	emitg : Par
	"""This is the color that the material will emit even if there is no light."""
	emitb : Par
	"""This is the color that the material will emit even if there is no light."""
	constantr : Par
	"""Adds to the final color. Where there are point colors, finalcolor += Point Color * Constant Color. This behaves like there is ambient illumination of 1 1 1. It is not affected by textures or transparency."""
	constantg : Par
	"""Adds to the final color. Where there are point colors, finalcolor += Point Color * Constant Color. This behaves like there is ambient illumination of 1 1 1. It is not affected by textures or transparency."""
	constantb : Par
	"""Adds to the final color. Where there are point colors, finalcolor += Point Color * Constant Color. This behaves like there is ambient illumination of 1 1 1. It is not affected by textures or transparency."""
	frontfacelit : Par
	"""Menu : Controls how the polygon's normal is used to light the front face of the polygon. For more information refer to the [[Two-Sided Lighting]] article."""
	backfacelit : Par
	"""Menu : Back Face's</span> <code>backfacelit</code> - Controls how the polygon's normal is used to light the back face of the polygon. For more information refer to the [[Two-Sided Lighting]] article."""
	basecolormap : Par
	"""TOP : Clicking on the arrows to the right of the map field will open the [[Texture Sampling Parameters]] for Color Map.  The other Map parameters below will have their own Texture Sampling Parameters as well."""
	basecolormapextendu : Par
	"""Menu : """
	basecolormapextendv : Par
	"""Menu : """
	basecolormapextendw : Par
	"""Menu : """
	basecolormapfilter : Par
	"""Menu : """
	basecolormapanisotropy : Par
	"""Menu : """
	basecolormapcoord : Par
	"""Menu : """
	basecolormapcoordinterp : Par
	"""Menu : """
	specularlevelmap : Par
	"""TOP : Specifies a specular level map."""
	specularlevelmapextendu : Par
	"""Menu : """
	specularlevelmapextendv : Par
	"""Menu : """
	specularlevelmapextendw : Par
	"""Menu : """
	specularlevelmapfilter : Par
	"""Menu : """
	specularlevelmapanisotropy : Par
	"""Menu : """
	specularlevelmapcoord : Par
	"""Menu : """
	specularlevelmapcoordinterp : Par
	"""Menu : """
	specularlevelmapchannelsource : Par
	"""Menu : """
	metallicmap : Par
	"""TOP : Specifies a metallic texture map. This is equivalent to the Metallic map in Substance Designer."""
	metalnessmapextendu : Par
	"""Menu : """
	metalnessmapextendv : Par
	"""Menu : """
	metalnessmapextendw : Par
	"""Menu : """
	metalnessmapfilter : Par
	"""Menu : """
	metalnessmapanisotropy : Par
	"""Menu : """
	metallicmapcoord : Par
	"""Menu : """
	metallicmapcoordinterp : Par
	"""Menu : """
	metallicmapchannelsource : Par
	"""Menu : """
	roughnessmap : Par
	"""TOP : Specifies a roughness texture map. This is equivalent to the Roughness map in Substance Designer."""
	roughnessmapextendu : Par
	"""Menu : """
	roughnessmapextendv : Par
	"""Menu : """
	roughnessmapextendw : Par
	"""Menu : """
	roughnessmapfilter : Par
	"""Menu : """
	roughnessmapanisotropy : Par
	"""Menu : """
	roughnessmapcoord : Par
	"""Menu : """
	roughnessmapcoordinterp : Par
	"""Menu : """
	roughnessmapchannelsource : Par
	"""Menu : """
	ambientocclusionmap : Par
	"""TOP : Specifies a ambient occlusion texture map. This is equivalent to the Ambient Occlusion map in Substance Designer. Ambient Occlusion affects the contribution from the Environement Light COMP."""
	ambientocclusionmapextendu : Par
	"""Menu : """
	ambientocclusionmapextendv : Par
	"""Menu : """
	ambientocclusionmapextendw : Par
	"""Menu : """
	ambientocclusionmapfilter : Par
	"""Menu : """
	ambientocclusionmapanisotropy : Par
	"""Menu : """
	ambientocclusionmapcoord : Par
	"""Menu : """
	ambientocclusionmapcoordinterp : Par
	"""Menu : """
	ambientocclusionmapchannelsource : Par
	"""Menu : """
	normalmap : Par
	"""TOP : Uses a [[Normal Map TOP|Normal Map]] from TOPs to create a 'bump map' effect. Bump-mapping simulates bumps or wrinkles in a surface to give it a 3D depth effect. Your geometry must have tangent attributes created for this feature to work (T[4]). Create these using the [[Attribute Create SOP]]."""
	normalmapextendu : Par
	"""Menu : """
	normalmapextendv : Par
	"""Menu : """
	normalmapextendw : Par
	"""Menu : """
	normalmapfilter : Par
	"""Menu : """
	normalmapanisotropy : Par
	"""Menu : """
	normalmapcoord : Par
	"""Menu : """
	normalmapcoordinterp : Par
	"""Menu : """
	heightmap : Par
	"""TOP : Specifies a height texture map. This is equivalent to the Height map in Substance Designer. The height map is used in conjunction with the normal map to perform parallax mapping."""
	heightmapextendu : Par
	"""Menu : """
	heightmapextendv : Par
	"""Menu : """
	heightmapextendw : Par
	"""Menu : """
	heightmapfilter : Par
	"""Menu : """
	heightmapanisotropy : Par
	"""Menu : """
	heightmapcoord : Par
	"""Menu : """
	heightmapcoordinterp : Par
	"""Menu : """
	heightmapchannelsource : Par
	"""Menu : """
	emitmap : Par
	"""TOP : Specifies a TOP texture that is multiplied with the Emit color parameter of the material. The object must have texture coordinates. The alpha of this map is ignored."""
	emitmapextendu : Par
	"""Menu : """
	emitmapextendv : Par
	"""Menu : """
	emitmapextendw : Par
	"""Menu : """
	emitmapfilter : Par
	"""Menu : """
	emitmapanisotropy : Par
	"""Menu : """
	emitmapcoord : Par
	"""Menu : """
	emitmapcoordinterp : Par
	"""Menu : """
	alphamap : Par
	"""TOP : This map multiplies the alpha of the object. It uses the red channel of the map, other channels are ignored."""
	alphamapextendu : Par
	"""Menu : """
	alphamapextendv : Par
	"""Menu : """
	alphamapextendw : Par
	"""Menu : """
	alphamapfilter : Par
	"""Menu : """
	alphamapanisotropy : Par
	"""Menu : """
	alphamapcoord : Par
	"""Menu : """
	alphamapcoordinterp : Par
	"""Menu : """
	rim1map : Par
	"""TOP : This map will multiple the calculated rim light color."""
	rim1mapextendu : Par
	"""Menu : """
	rim1mapextendv : Par
	"""Menu : """
	rim1mapextendw : Par
	"""Menu : """
	rim1mapfilter : Par
	"""Menu : """
	rim1mapanisotropy : Par
	"""Menu : """
	rim1mapcoord : Par
	"""Menu : """
	rim1mapcoordinterp : Par
	"""Menu : """
	rim1colorr : Par
	"""The color of the rim light."""
	rim1colorg : Par
	"""The color of the rim light."""
	rim1colorb : Par
	"""The color of the rim light."""
	shadowcolorr : Par
	"""The color that will be used in shadowed areas."""
	shadowcolorg : Par
	"""The color that will be used in shadowed areas."""
	shadowcolorb : Par
	"""The color that will be used in shadowed areas."""
	darknessemitcolorr : Par
	"""The color that is used for areas that are in darkness."""
	darknessemitcolorg : Par
	"""The color that is used for areas that are in darkness."""
	darknessemitcolorb : Par
	"""The color that is used for areas that are in darkness."""
	darknessemitmap : Par
	"""TOP : This map multiplies the <span class="tipTextMAT">Darkness Emit Color</span>. This maps alpha is not used."""
	darknessemitmapextendu : Par
	"""Menu : """
	darknessemitmapextendv : Par
	"""Menu : """
	darknessemitmapextendw : Par
	"""Menu : """
	darknessemitmapfilter : Par
	"""Menu : """
	darknessemitmapanisotropy : Par
	"""Menu : """
	darknessemitmapcoord : Par
	"""Menu : """
	darknessemitmapcoordinterp : Par
	"""Menu : """
	instancetexture : Par
	"""StrMenu : When provider per-instance textures in the [[Geometry COMP]], this parameter selects which map the instance texture will be applied as."""
	colorbuffer1rgb : Par
	"""StrMenu : Allows sending things like normals or emit color to different Render TOP color buffers in a single pass."""
	par : parameter.pbrMAT
	"""Parameters of parameter.pbrMAT"""
	pass


class phongMAT():
	"""phongMAT"""
	diffr : Par
	"""The color of the diffuse light reflected from the material."""
	diffg : Par
	"""The color of the diffuse light reflected from the material."""
	diffb : Par
	"""The color of the diffuse light reflected from the material."""
	ambr : Par
	"""The color of the ambient light reflected from the material."""
	ambg : Par
	"""The color of the ambient light reflected from the material."""
	ambb : Par
	"""The color of the ambient light reflected from the material."""
	specr : Par
	"""The color of the specular light reflected from the material. This changes the color of the highlights on shiney objects."""
	specg : Par
	"""The color of the specular light reflected from the material. This changes the color of the highlights on shiney objects."""
	specb : Par
	"""The color of the specular light reflected from the material. This changes the color of the highlights on shiney objects."""
	emitr : Par
	"""This is the color that the material will emit even if there is no light."""
	emitg : Par
	"""This is the color that the material will emit even if there is no light."""
	emitb : Par
	"""This is the color that the material will emit even if there is no light."""
	constantr : Par
	"""Adds to the final color. Where there are point colors, finalcolor += Point Color * Constant Color. This behaves like there is ambient illumination of 1 1 1. It is not affected by textures or transparency."""
	constantg : Par
	"""Adds to the final color. Where there are point colors, finalcolor += Point Color * Constant Color. This behaves like there is ambient illumination of 1 1 1. It is not affected by textures or transparency."""
	constantb : Par
	"""Adds to the final color. Where there are point colors, finalcolor += Point Color * Constant Color. This behaves like there is ambient illumination of 1 1 1. It is not affected by textures or transparency."""
	colormap : Par
	"""TOP : Specifies a TOP texture that is multiplied by the results of all of the lighting calculations. The alpha of this map is used as a part of calculating the objects alpha.  Clicking on the arrows to the right of the map field will open the [[Texture Sampling Parameters]] for Color Map.  The other Map parameters below will have their own Texture Sampling Parameters as well."""
	colormapextendu : Par
	"""Menu : """
	colormapextendv : Par
	"""Menu : """
	colormapextendw : Par
	"""Menu : """
	colormapfilter : Par
	"""Menu : """
	colormapanisotropy : Par
	"""Menu : """
	colormapcoord : Par
	"""Menu : """
	colormapcoordinterp : Par
	"""Menu : """
	normalmap : Par
	"""TOP : Uses a [[Normal Map TOP|Normal Map]] from TOPs to create a 'bump map' effect. Bump-mapping simulates bumps or wrinkles in a surface to give it a 3D depth effect. '''Your geometry must have tangent attributes created for this feature to work (T[4]). Create these using the [[Attribute Create SOP]].'''"""
	normalmapextendu : Par
	"""Menu : """
	normalmapextendv : Par
	"""Menu : """
	normalmapextendw : Par
	"""Menu : """
	normalmapfilter : Par
	"""Menu : """
	normalmapanisotropy : Par
	"""Menu : """
	normalmapcoord : Par
	"""Menu : """
	normalmapcoordinterp : Par
	"""Menu : """
	heightmap : Par
	"""TOP : Specifies a height texture map. The height map is used in conjunction with the normal map to perform parallax mapping."""
	heightmapextendu : Par
	"""Menu : """
	heightmapextendv : Par
	"""Menu : """
	heightmapextendw : Par
	"""Menu : """
	heightmapfilter : Par
	"""Menu : """
	heightmapanisotropy : Par
	"""Menu : """
	heightmapcoord : Par
	"""Menu : """
	heightmapcoordinterp : Par
	"""Menu : """
	heightmapchannelsource : Par
	"""Menu : """
	diffusemap : Par
	"""TOP : Specifies a TOP that multiples the Diffuse Color. The object must have texture coordinates. The alpha of this map is ignored."""
	diffusemapextendu : Par
	"""Menu : """
	diffusemapextendv : Par
	"""Menu : """
	diffusemapextendw : Par
	"""Menu : """
	diffusemapfilter : Par
	"""Menu : """
	diffusemapanisotropy : Par
	"""Menu : """
	diffusemapcoord : Par
	"""Menu : """
	diffusemapcoordinterp : Par
	"""Menu : """
	specmap : Par
	"""TOP : Specifies a TOP texture that is multiplied with the Specular color parameter of the material. The object must have texture coordinates. The alpha of this map is ignored."""
	specmapextendu : Par
	"""Menu : """
	specmapextendv : Par
	"""Menu : """
	specmapextendw : Par
	"""Menu : """
	specmapfilter : Par
	"""Menu : """
	specmapanisotropy : Par
	"""Menu : """
	specmapcoord : Par
	"""Menu : """
	specmapcoordinterp : Par
	"""Menu : """
	emitmap : Par
	"""TOP : Specifies a TOP texture that is multiplied with the Emit color parameter of the material. The object must have texture coordinates. The alpha of this map is ignored."""
	emitmapextendu : Par
	"""Menu : """
	emitmapextendv : Par
	"""Menu : """
	emitmapextendw : Par
	"""Menu : """
	emitmapfilter : Par
	"""Menu : """
	emitmapanisotropy : Par
	"""Menu : """
	emitmapcoord : Par
	"""Menu : """
	emitmapcoordinterp : Par
	"""Menu : """
	envmap : Par
	"""TOP : Uses a TOP texture to define an environment map for the material. Environment mapping simulates an object reflecting its surroundings. The TOP defined in this parameter is the texture that will be reflected. The Env Map is added to whatever the normal lighting will be, so to make an object purely reflective turn the Diffuse and Specular parameters to 0. This input expects a sphere map. An example of a sphere map can be found [http://debevec.org/Probes/campus_probe.jpg here]. This input will also accept a cube map, created with the [[Cube Map TOP]] or the [[Render TOP]]'s Render Cube Map parameter."""
	envmapextendu : Par
	"""Menu : """
	envmapextendv : Par
	"""Menu : """
	envmapextendw : Par
	"""Menu : """
	envmapfilter : Par
	"""Menu : """
	envmapanisotropy : Par
	"""Menu : """
	envmapcolorr : Par
	"""This color is multiplied with the texture specified by the <span class="tipTextMAT">Environment Map</span> parameter above."""
	envmapcolorg : Par
	"""This color is multiplied with the texture specified by the <span class="tipTextMAT">Environment Map</span> parameter above."""
	envmapcolorb : Par
	"""This color is multiplied with the texture specified by the <span class="tipTextMAT">Environment Map</span> parameter above."""
	envmaprotatex : Par
	"""Rotate the texture specified by the <span class="tipTextMAT">Environment Map</span> parameter above."""
	envmaprotatey : Par
	"""Rotate the texture specified by the <span class="tipTextMAT">Environment Map</span> parameter above."""
	envmaprotatez : Par
	"""Rotate the texture specified by the <span class="tipTextMAT">Environment Map</span> parameter above."""
	envmaptype2d : Par
	"""Menu : Select between using a sphere map or an equirectangular map as the Environment Map type."""
	frontfacelit : Par
	"""Menu : Controls how the polygon's normal is used to light the front face of the polygon. For more information refer to the [[Two-Sided Lighting]] article."""
	backfacelit : Par
	"""Menu : Controls how the polygon's normal is used to light the back face of the polygon. For more information refer to the [[Two-Sided Lighting]] article."""
	alphamap : Par
	"""TOP : This map multiplies the alpha of the object. It uses the red channel of the map, other channels are ignored."""
	alphamapextendu : Par
	"""Menu : """
	alphamapextendv : Par
	"""Menu : """
	alphamapextendw : Par
	"""Menu : """
	alphamapfilter : Par
	"""Menu : """
	alphamapanisotropy : Par
	"""Menu : """
	alphamapcoord : Par
	"""Menu : """
	alphamapcoordinterp : Par
	"""Menu : """
	texture1 : Par
	"""TOP : You can specify up to 4 textures for multi-texturing."""
	texture1mapextendu : Par
	"""Menu : """
	texture1mapextendv : Par
	"""Menu : """
	texture1mapextendw : Par
	"""Menu : """
	texture1mapfilter : Par
	"""Menu : """
	texture1mapanisotropy : Par
	"""Menu : """
	texture1coord : Par
	"""Menu : Specifies which texture coordinate to use for the map."""
	texture1coordinterp : Par
	"""Menu : """
	texture2 : Par
	"""TOP : You can specify up to 4 textures for multi-texturing."""
	texture2mapextendu : Par
	"""Menu : """
	texture2mapextendv : Par
	"""Menu : """
	texture2mapextendw : Par
	"""Menu : """
	texture2mapfilter : Par
	"""Menu : """
	texture2mapanisotropy : Par
	"""Menu : """
	texture2coord : Par
	"""Menu : Specifies which texture coordinate to use for the map."""
	texture2coordinterp : Par
	"""Menu : """
	texture3 : Par
	"""TOP : You can specify up to 4 textures for multi-texturing."""
	texture3mapextendu : Par
	"""Menu : """
	texture3mapextendv : Par
	"""Menu : """
	texture3mapextendw : Par
	"""Menu : """
	texture3mapfilter : Par
	"""Menu : """
	texture3mapanisotropy : Par
	"""Menu : """
	texture3coord : Par
	"""Menu : Specifies which texture coordinate to use for the map."""
	texture3coordinterp : Par
	"""Menu : """
	texture4 : Par
	"""TOP : You can specify up to 4 textures for multi-texturing."""
	texture4mapextendu : Par
	"""Menu : """
	texture4mapextendv : Par
	"""Menu : """
	texture4mapextendw : Par
	"""Menu : """
	texture4mapfilter : Par
	"""Menu : """
	texture4mapanisotropy : Par
	"""Menu : """
	texture4coord : Par
	"""Menu : Specifies which texture coordinate to use for the map."""
	texture4coordnterp : Par
	"""Menu : """
	rim1map : Par
	"""TOP : This map will multiple the calculated rim light color."""
	rim1mapextendu : Par
	"""Menu : """
	rim1mapextendv : Par
	"""Menu : """
	rim1mapextendw : Par
	"""Menu : """
	rim1mapfilter : Par
	"""Menu : """
	rim1mapanisotropy : Par
	"""Menu : """
	rim1mapcoord : Par
	"""Menu : """
	rim1mapcoordinterp : Par
	"""Menu : """
	rim1colorr : Par
	"""The color of the rim light."""
	rim1colorg : Par
	"""The color of the rim light."""
	rim1colorb : Par
	"""The color of the rim light."""
	shadowcolorr : Par
	"""The color that will be used in shadowed areas."""
	shadowcolorg : Par
	"""The color that will be used in shadowed areas."""
	shadowcolorb : Par
	"""The color that will be used in shadowed areas."""
	darknessemitcolorr : Par
	"""The color that is used for areas that are in darkness."""
	darknessemitcolorg : Par
	"""The color that is used for areas that are in darkness."""
	darknessemitcolorb : Par
	"""The color that is used for areas that are in darkness."""
	darknessemitmap : Par
	"""TOP : This map multiplies the <span class="tipTextMAT">Darkness Emit Color</span>. This maps alpha is not used."""
	darknessemitmapextendu : Par
	"""Menu : """
	darknessemitmapextendv : Par
	"""Menu : """
	darknessemitmapextendw : Par
	"""Menu : """
	darknessemitmapfilter : Par
	"""Menu : """
	darknessemitmapanisotropy : Par
	"""Menu : """
	darknessemitmapcoord : Par
	"""Menu : """
	darknessemitmapcoordinterp : Par
	"""Menu : """
	spec2r : Par
	"""Adds a secondary specular highlight color."""
	spec2g : Par
	"""Adds a secondary specular highlight color."""
	spec2b : Par
	"""Adds a secondary specular highlight color."""
	instancetexture : Par
	"""StrMenu : When provider per-instance textures in the [[Geometry COMP]], this parameter selects which map the instance texture will be applied as."""
	colorbuffer1rgb : Par
	"""StrMenu : Allows sending things like normals or diffuse color to different Render TOP color buffers in a single pass."""
	par : parameter.phongMAT
	"""Parameters of parameter.phongMAT"""
	pass


class pointspriteMAT():
	"""pointspriteMAT"""
	colorr : Par
	"""The color of the light reflected from the material."""
	colorg : Par
	"""The color of the light reflected from the material."""
	colorb : Par
	"""The color of the light reflected from the material."""
	colormap : Par
	"""TOP : The color map to apply to the sprites. The Color Map will be multiplied by the color of the sprites. The Color Map parameter can also take 3D / 2D Texture Arrays (from the [[Texture 3D TOP]] for example), and the w texture coordinate will select the correct map from the array.		
				
The final size of the point sprite is controlled by the pscale point attribute (if present) getting multiplied of the result of the next 6 parameters. There are two types of scale this MAT can apply, and they are blended using the Attenuate Point Scale parameter to create one final point scale (which is multiplied by pscale)."""
	colormapextendu : Par
	"""Menu : """
	colormapextendv : Par
	"""Menu : """
	colormapextendw : Par
	"""Menu : """
	colormapfilter : Par
	"""Menu : """
	colormapanisotropy : Par
	"""Menu : """
	par : parameter.pointspriteMAT
	"""Parameters of parameter.pointspriteMAT"""
	pass


class selectMAT():
	"""selectMAT"""
	par : parameter.selectMAT
	"""Parameters of parameter.selectMAT"""
	pass


class switchMAT():
	"""switchMAT"""
	par : parameter.switchMAT
	"""Parameters of parameter.switchMAT"""
	pass


class wireframeMAT():
	"""wireframeMAT"""
	colorr : Par
	"""The color of the light reflected from the material."""
	colorg : Par
	"""The color of the light reflected from the material."""
	colorb : Par
	"""The color of the light reflected from the material."""
	wireframemode : Par
	"""Menu : Controls what wireframes are rendered."""
	par : parameter.wireframeMAT
	"""Parameters of parameter.wireframeMAT"""
	pass



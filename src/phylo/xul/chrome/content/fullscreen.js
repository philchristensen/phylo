function init(){
	activateFullscreen();
	//activateExtensionsManager();
	activateFirebug();
}

function getCornerMeasurements(width, height){
	return {
		'width' 	: 600,
		'height'	: 400,
		'left'		: screen.width - width,
		'top'		: screen.height - height,
	}
}

function activateFullscreen(){
	var uri = 'chrome://phylo/content/phylo.xul';
	var winName = 'fullscreenWindow';
	var width = screen.width - 600;
	var height = screen.height;
	var winFeatures = 'chrome,dependent,top=0,left=0,width=' + width + ',height=' + height + ',menubar=no,titlebar=no,fullscreen=yes';
	return window.open(uri,winName,winFeatures);
}

function activateConsole(){
	var uri = 'chrome://global/content/console.xul';
	var winName = 'jsConsole';
	
	var rect = getCornerMeasurements(600, 400);
	
	var winFeatures = 'chrome,dependent,top=' + rect.top +
									 ',left=' + rect.left +
									 ',width=' + rect.width +
									 ',height=' + rect.height + 
									 ',menubar=no,titlebar=yes,fullscreen=no';
	return window.open(uri,winName,winFeatures);
}

function activateExtensionsManager(){
	var uri = 'chrome://mozapps/content/extensions/extensions.xul?type=extensions';
	var winName = 'extensionsManager';
	
	var rect = getCornerMeasurements(600, 400);
	
	var winFeatures = 'chrome,dependent,top=' + rect.top +
									 ',left=' + rect.left +
									 ',width=' + rect.width +
									 ',height=' + rect.height + 
									 ',menubar=no,titlebar=yes,fullscreen=no';
	return window.open(uri,winName,winFeatures);
}

function activateFirebug(){
	var uri = 'chrome://chromebug/content/chromebug.xul';
	var winName = 'firebug';
	
	var rect = getCornerMeasurements(600, 400);
	
	var winFeatures = 'chrome,dependent,top=' + rect.top +
									 ',left=' + rect.left +
									 ',width=' + rect.width +
									 ',height=' + rect.height + 
									 ',menubar=no,titlebar=yes,fullscreen=no';
	return window.open(uri,winName,winFeatures);
}


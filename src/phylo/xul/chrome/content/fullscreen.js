function init(){
	activateFullscreen();
}

function activateFullscreen(){
	var uri = 'chrome://phylo/content/phylo.xul';
	var winName = 'fullscreenWindow';
	var width = screen.width - 600;
	var height = screen.height;
	var winFeatures = 'chrome,dependent,top=0,left=0,width=' + width + ',height=' + height + ',menubar=no,titlebar=no,fullscreen=yes';
	return window.open(uri,winName,winFeatures);
}



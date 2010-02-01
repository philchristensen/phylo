function activateFullscreen(){
	var uri = 'chrome://phylo/content/phylo.xul';
	var winName = 'fullscreenWindow';
	var winFeatures = 'chrome,dependent,top=0,left=0,width=' + screen.width + ',height=' + screen.height + ',menubar=no,titlebar=no,fullscreen=yes';
	return window.open(uri,winName,winFeatures);
}


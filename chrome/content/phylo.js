function activateFullscreen(){
	var uri = 'chrome://phylo/content/phylo.xul';
	var winName = 'fullscreenWindow';
	var winFeatures = 'chrome,dependent,top=0,left=0,width=' + screen.width + ',height=' + screen.height + ',titlebar=no,fullscreen=yes';
	window.open(uri,winName,winFeatures);
}


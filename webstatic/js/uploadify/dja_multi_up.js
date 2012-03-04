$(document).ready(function() {
	$('#uploadify').uploadify({
		'uploader'  : '/static/js/uploadify/uploadify.swf',
		'script'    : '/upload/',
		'cancelImg' : '/static/js/uploadify/cancel.png',
		'folder'    : '/media/images',
		'auto'      : true,
		'multi'     : true,
		'fileExt'   : '*.jpg;*.bmp;*.png',
		'fileDesc'  : 'jpg',
		'queueID'   : 'file_upload_queue',
		'removeCompleted': false,
	});
});


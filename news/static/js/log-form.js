document.getElementById('but').onclick='';
	$(document).ready(function() {
		$("h1#but").click(function() {
			$("fieldset#box").slideToggle(400);
		});
	});
document.getElementById('but').onclick='';
	$(document).ready(function() {
		$("h1#but").click(function() {
			$("fieldset#box").slideToggle(400);
		});
	});
swal({
   title: "Are you sure?",   
   text: "You will not be able to recover this imaginary file!",  
   type: "warning",   showCancelButton: true,   confirmButtonColor: "#DD6B55",  
   confirmButtonText: "Yes, delete it!",   closeOnConfirm: false }, function(){ 
        swal("Deleted!", "Your imaginary file has been deleted.", "success"); 
});
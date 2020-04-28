//SCROLL TO TOP BUTTON
//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
	scrollFunction()
};

function scrollFunction() {
	if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		mybutton.style.display = "block";
	} else {
		mybutton.style.display = "none";
	}
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}


//EMAIL JS
var myform = $("form#myform");
myform.submit(function (event) {
	event.preventDefault();

	// Change to your service ID, or keep using the default service
	var service_id = "default_service";
	var template_id = "alio_prints";

	myform.find("button").text("Sending...");
	emailjs.sendForm(service_id, template_id, myform[0]).then(
		function () {
			alert("Your message was sent!");
			myform.find("button").text("Send");
		},
		function (err) {
			alert("Send email failed!\r\n Response:\n " + JSON.stringify(err));
			myform.find("button").text("Send");
		}
	);
	return false;
});


//CAROUSEL FOR LARGE SCREENS
$('#myCarousel').carousel({
	interval: 1000
})

$('.carousel .item').each(function () {
	var next = $(this).next();

	if (!next.length) {
		next = $(this).siblings(':first');
	}

	next.children(':first-child').clone().appendTo($(this));

	if (next.next().length > 0) {
		next.next().children(':first-child').clone().appendTo($(this));
	} else {
		$(this).siblings(':first').children(':first-child').clone().appendTo($(this));
	}
});

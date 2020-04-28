//SCROLL TO TOP BUTTON
//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
	scrollFunction();
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

//CAROUSEL FOR LARGE SCREENS
$('#myCarousel').carousel({
	interval: 1000
});

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

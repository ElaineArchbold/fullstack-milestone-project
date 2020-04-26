$(document).ready(function() {
	$('#myCarousel').carousel({
	interval: 2000
	})
    
    $('#myCarousel').on('slid.bs.carousel', function() {
    	//alert("slid");
	});
    
    
});

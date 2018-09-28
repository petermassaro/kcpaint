
function displayAddressFields() {
	var checkBox = document.getElementById('address');
	var fields = document.getElementById('address_optional');

	if (checkBox.checked == false) {
		fields.style.display = 'block';
	} else {
		fields.style.display = 'none';
	}
}


// function toggleNavMenu(){
//     var toggleMenu = document.getElementById('');
// }


// (function($) {
//     "use strict"; // Start of use strict

//     // jQuery for page scrolling feature - requires jQuery Easing plugin
//     $('a.page-scroll').bind('click', function(event) {
//         var $anchor = $(this);
//         $('html, body').stop().animate({
//             scrollTop: ($($anchor.attr('href')).offset().top - 50)
//         }, 1250, 'easeInOutExpo');
//         event.preventDefault();
//     });

//     // Highlight the top nav as scrolling occurs
//     $('body').scrollspy({
//         target: '.navbar-fixed-top',
//         offset: 51
//     });

//     // // Closes the Responsive Menu on Menu Item Click
//     $('.navbar-collapse ul li a').click(function(){ 
//             $('.navbar-toggle:visible').click();
//     });

//     // Offset for Main Navigation
//     $('#mainNav').affix({
//         offset: {
//             top: 100
//         }
//     });

//     $(document).click(function(){
//         $("#dropdown").hide();
//     })

// })(jQuery); // End of use strict




jQuery(document).ready(function($) {
$(function(){
  // assign the slider to a variable
  var slider = $('#slider1').bxSlider({infiniteLoop: false,hideControlOnEnd: true,});
/*
    $('#start').click(function(){
         slider.startShow();
         return false;
    });
     $('#stop').click(function(){
         slider.stopShow();
         return false;
    });
 */
    $('#start').click(function(){
    function func() {
                    slider.goToNextSlide();
                    timer = setTimeout(func, 3000);
                    }
    var timer = setTimeout(func, 3000);

        
    return false;
  });

  $('#stop').click(function(){
    clearTImeout(timer);
    return false;
  });

  // assign a click event to the external thumbnails
  $('.thumbs a').click(function(){
   var thumbIndex = $('.thumbs a').index(this);
    // call the "goToSlide" public function
    slider.goToSlide(thumbIndex);
  
    // remove all active classes
    $('.thumbs a').removeClass('pager-active');
    // assisgn "pager-active" to clicked thumb
    $(this).addClass('pager-active');
    // very important! you must kill the links default behavior
    return false;
  });
  $('.bx-next').click(function(){
            var thumNext = $('.thumbs .pager-active').next();
            $('.thumbs a').removeClass('pager-active');
            thumNext.addClass('pager-active');
            
  });
    $('.bx-prev').click(function(){
            var thumPrev = $('.thumbs .pager-active').prev();
            $('.thumbs a').removeClass('pager-active');
            thumPrev.addClass('pager-active');
            
  });

  // assign "pager-active" class to the first thumb
  $('.thumbs a:first').addClass('pager-active');
          $('.bx-prev, .bx-next').css('opacity','0')
   $('.bx-wrapper,.bx-prev,.bx-next').hover(function(){
             $('.bx-prev, .bx-next').animate({opacity:'1'},100)
            },
            function(){
              $('.bx-prev, .bx-next').animate({opacity:'0'},100)
            });  
            

   
   });
    $('video,audio').mediaelementplayer();
    $('nav a.jsaction').click(function(){
        $('.contwr .curent').animate({opacity:'0',left:'-1200'},'fast').removeClass('curent'); 
        var linkBlock = $(this).attr('rel');
        $('.'+linkBlock).css('left','20px').animate({opacity:'1'},'fast').addClass('curent'); 
        return false;     
    });
    $('.close').click(function(){
       $(this).parents('.hide_my').animate({opacity:'0',left:'-1200'},'fast').removeClass('curent'); 
       return false;
    });
    $('#img').click(function(){
        $('.contwr div[data-type="img"]').show();
        $('.contwr a[data-type="img"]').show();
        $('.contwr div[data-type="video"]').hide();
        $('.contwr a[data-type="video"]').hide();
        return false;
    });
    $('#vid').click(function(){
        $('.contwr div[data-type="video"]').show();
        $('.contwr a[data-type="video"]').show();
        $('.contwr div[data-type="img"]').hide();
        $('.contwr a[data-type="img"]').hide();
        return false;
    });
});
/*===================================
    ScrollBar 
===================================*/
$(window).load(function() {
	mCustomScrollbars();
});

function mCustomScrollbars(){
	/* 
	malihu custom scrollbar function parameters: 
	1) scroll type (values: "vertical" or "horizontal")
	2) scroll easing amount (0 for no easing) 
	3) scroll easing type 
	4) extra bottom scrolling space for vertical scroll type only (minimum value: 1)
	5) scrollbar height/width adjustment (values: "auto" or "fixed")
	6) mouse-wheel support (values: "yes" or "no")
	7) scrolling via buttons support (values: "yes" or "no")
	8) buttons scrolling speed (values: 1-20, 1 being the slowest)
	*/
	$("#mcs3_container").mCustomScrollbar("vertical",500,"easeOutCirc",1.05,"auto","yes","no",0); 
}

/* function to fix the -10000 pixel limit of jquery.animate */
$.fx.prototype.cur = function(){
    if ( this.elem[this.prop] != null && (!this.elem.style || this.elem.style[this.prop] == null) ) {
      return this.elem[ this.prop ];
    }
    var r = parseFloat( jQuery.css( this.elem, this.prop ) );
    return typeof r == 'undefined' ? 0 : r;
}


















$(document).ready(function () {
    if($(".apartments .slider").length){
        $(".apartments .slider").owlCarousel({
            loop: true,
            margin: 10,
            nav: true,
            dots: false,
            responsive: {
                0: {
                    items: 1
                },
                1000: {
                    items: 3
                }
            }
        });
    }
    
    if($(".image-list").length){
        var imgSlider = $(".image-list").owlCarousel({
            loop: false,
            margin: 10,
            nav: true,
            dots: false,
            responsive: {
                0: {
                    items: 1
                },
                1000: {
                    items: 6
                }
            }
        });
        
    }


    $(document).bind("keydown", function(e){
        if (e.keyCode == 37){
            prevSlide()
            imgSlider.trigger('prev.owl.carousel')
        }
        
        if(e.keyCode == 39){
            nextSlide()
            imgSlider.trigger('next.owl.carousel')
        }
    })
    
    
    if($(".image-list").length){
        var targetsrc = $(".main-image img")
        $(".image-list img").on("click", function(){
            var src = $(this).attr('src') 
            targetsrc.attr('src', src)

            $(".image-list .image").removeClass('active');
            $(this).parent('.image').addClass("active");
        })
    }
});


function prevSlide(){
    var src = $(".image-list .image.active img").attr('src');
    var current = $(".image-list .image.active");
    if(current.parent('.owl-item').prev().find('.image').length){
        $(".image-list .image").removeClass('active');
        current.parent('.owl-item').prev().find('.image').addClass("active");
        swapImageSrc(src)
    }
}

function nextSlide(){
    var src = $(".image-list .image.active img").attr('src');
    var current = $(".image-list .image.active");
    if(current.parent('.owl-item').next().find('.image').length){
        $(".image-list .image").removeClass('active');
        current.parent('.owl-item').next().find('.image').addClass("active");
        swapImageSrc(src)
    }
}

function swapImageSrc(src){
    $(".main-image img").attr('src', src)
}
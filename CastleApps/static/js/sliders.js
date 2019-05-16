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
        $(".image-list").owlCarousel({
            loop: true,
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
});
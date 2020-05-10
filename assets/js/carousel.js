$(document).ready(function () {
    setInterval(function () {
        $('.stacks').slick({
            slidesToScroll: 1,
            swipeToSlide: true,
            autoplay: true,
            autoplaySpeed: 2000,
            variableWidth: true,
            prevArrow: $('.prev'),
            nextArrow: $('.next'),
            responsive: [
                {
                    breakpoint: 991,
                    settings: {
                        swipeToSlide: true,
                        arrows: false
                    }
                }
            ]
        });

    }, 100)
});

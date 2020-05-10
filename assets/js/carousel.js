$(document).ready(function () {

    setInterval(function () {
        $('.portfolio.mobile').slick({
            slidesToShow: 3,
            responsive: [
                {
                    breakpoint: 991,
                    settings: {
                        arrows: false,
                        slidesToShow: 1,
                        centerMode: true,
                        centerPadding: '60px',
                    }
                }
            ]
        });
        //when the slick slide initializes we want to set all of our slides to the same height
        $('.portfolio.mobile').on('setPosition', function () {
            jbResizeSlider();
        });

        //we need to maintain a set height when a resize event occurs.
        //Some events will through a resize trigger: $(window).trigger('resize');
        $(window).on('resize', function (e) {
            jbResizeSlider();
        });

        //since multiple events can trigger a slider adjustment, we will control that adjustment here
        function jbResizeSlider() {
            $slickSlider = $('.portfolio');
            $slickSlider.find('.slick-slide').height('auto');

            var slickTrack = $slickSlider.find('.slick-track');
            var slickTrackHeight = $(slickTrack).height();

            $slickSlider.find('.slick-slide').css('height', slickTrackHeight + 'px');
        }


        $('.stacks').slick({
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 2000,
            variableWidth: true,
            prevArrow: $('.prev'),
            nextArrow: $('.next')
        });

    }, 100);
});

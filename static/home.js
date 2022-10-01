//Start Alumin coursel

$(document).ready(function()
{
        if($('.bbb_slider').length)
        {
            var trendsSlider = $('.bbb_slider');
            trendsSlider.owlCarousel(
            {
                loop:false,
                margin:30,
                nav:false,
                dots:false,
                autoplayHoverPause:true,
                autoplay:false,
                responsive:
                {
                    0:{items:1},
                    575:{items:2},
                    991:{items:3}
                }
            });

            trendsSlider.on('click', '.bbb_fav', function (ev)
            {
                $(ev.target).toggleClass('active');
            });

            if($('.bbb_prev').length)
            {
                var prev = $('.bbb_prev');
                prev.on('click', function()
                {
                    trendsSlider.trigger('prev.owl.carousel');
                });
            }

            if($('.bbb_next').length)
            {
                var next = $('.bbb_next');
                next.on('click', function()
                {
                    trendsSlider.trigger('next.owl.carousel');
                });
            }
        }

    });



/* Counter */

function animate(obj, initVal, lastVal, duration) {
    let startTime = null;
 //get the current timestamp and assign it to the currentTime variable
 let currentTime = Date.now();
 //pass the current timestamp to the step function
 const step = (currentTime ) => {
 //if the start time is null, assign the current time to startTime
 if (!startTime) {
    startTime = currentTime ;
 }
 //calculate the value to be used in calculating the number to be displayed
 const progress = Math.min((currentTime - startTime)/ duration, 1);
 //calculate what to be displayed using the value gotten above
 obj.innerHTML = Math.floor(progress * (lastVal - initVal) + initVal);
 //checking to make sure the counter does not exceed the last value (lastVal)
 if (progress < 1) {
    window.requestAnimationFrame(step);
 } else {
       window.cancelAnimationFrame(window.requestAnimationFrame(step));
    }
 };
 //start animating
    window.requestAnimationFrame(step);
 }
 let text1 = document.getElementById('0101');
 let text2 = document.getElementById('0102');
 let text3 = document.getElementById('0103');
 let text4 = document.getElementById('0104');
 let text5 = document.getElementById('0105');
 let text6 = document.getElementById('0106');
 const load = () => {
    animate(text1, 0, 511, 7000);
    animate(text2, 0, 232, 7000);
    animate(text3, 100, 225, 7000);
    animate(text3, 0, 105, 7000);
    animate(text3, 0, 15, 7000);
    animate(text3, 0, 225, 7000);
 }
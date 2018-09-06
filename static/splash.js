$(function(){
   // executes when complete page is fully loaded, including all frames, objects and images
    console.log("Nice to meet you");

    $(".project-shader").mouseenter(function() {
       $(".project-shader").css("opacity", "0.0");
       $(".project-caption").css("opacity", "0.0");
       $(this).css("opacity", "0.5");
       $(this).prev().css("opacity", "1.0");
     });

    $(".project-caption").mouseenter(function() {
       $(".project-shader").css("opacity", "0.0");
       $(".project-caption").css("opacity", "0.0");
       $(this).css("opacity", "1.0");
       $(this).next().css("opacity", "0.5");
    });

    $(".project-shader").mouseleave(function() {
       $(this).css("opacity", "0.0");
       $(this).prev().css("opacity", "0.0");
     });
     
     $(".project-shader").mouseleave(function() {
        $(this).css("opacity", "0.0");
        $(this).next().css("opacity", "0.0");
      });
});

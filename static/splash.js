$(function(){
   // executes when complete page is fully loaded, including all frames, objects and images
    console.log("Nice to meet you");
    // $("#project-row").css("opacity", "0.9");
    // $('.loading').delay(800).css("visibility", "hidden");
    // $('.loading-caption-container').delay(800).css("visibility", "hidden")

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

      //if css opacity 0.5 and css opacity 1.0 then


     //footer hovering stuff
     // $(".name-footer").mouseenter(function() {
     //    var imageCaption = $(this).find('img').attr("alt");
     //    console.log('hovering');
     //    $("#footer-caption").text(imageCaption);
     //    $(".project-gif-footer").css("opacity", "0.3");
     //    $(this).find('img').css("opacity", "1.0");
     //  });
     //
     //  $(".iconbox").mouseleave(function() {
     //    console.log('hovering');
     //    $("#footer-caption").text("More Stuff");
     //    $(".project-gif-footer").css("opacity", "1.0");
     //  });

      //expand image on click
      // $(function() {
		  //   $('.content-image').on('click', function() {
			//     $('.imagepreview').attr('src', $(this).find('img').attr('src'));
			//     $('#imagemodal').modal('show');
      // 		});
      // });





// $("#project-gif-footer").(function() {
//   console.log("hovering works");
//   var imageCaption = $(this).attr("alt");
//   console.log(imageCaption + "1");
//   $( "#footer-caption" ).text( imageCaption );
//   console.log(imageCaption + "2");


// });

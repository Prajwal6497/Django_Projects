// console.log($);
// console.log(jQuery);


// $("button").click(function () {
//     console.log("Button Clicked");
// });

// OR //

// jQuery("button").click(function () {
//     console.log("Button Clicked");
// });

// jQuery.noConflict();
// jQuery(document).ready(function ($) {
//     $("button").click(function () {
//         console.log("Button Clicked");
//     });    
// });

// jQuery.noConflict();
// jQuery(document).ready(function ($) {
//     $("p").click(function (){
//         alert("Element Selector");
//     });
//     $("#btn-id").click(function (){
//         alert("ID Selector");
//     });
//     $(".btn-class").click(function () {
//         alert("Class Selector");
//     });
    
// });

// jQuery.noConflict();
// jQuery(document).ready(function ($) {
//     //Mouse Events
//     $("p").click(function () {
//         console.log("clicked");
//     });   
//     $("p").dblclick(function () {
//         console.log("Double clicked");
//     });
//     $("p").mouseenter(function () {
//         console.log("Mouse Enter");
//     });
//     $("p").mouseleave(function () {
//         console.log("Mouse Leave");
//     }); 

//     // Keyboard Events
//     $("#name").keypress(function () {
//         console.log("Key Pressed");
//     });
//     $("#name").keyup(function () {
//         console.log("Key UP");
//     });
//     $("#name").keydown(function () {
//         console.log("Key Down");
//     });
    
//     // Form Events
//     $("#fname").focus(function () {
//         console.log("Focus Field");
//     });
//     $("#fname").blur(function () {
//         console.log("blur Field");
//     });
//     $("#form-id").submit(function (e) {
//         console.log("Form Submitted");
//         e.preventDefault();
//     });

//     //Window Event
//     $(window).resize(function (){
//         console.log("Window Resized");
//     });

// });


jQuery.noConflict();
jQuery(document).ready(function ($) {
    //Hide 
    $("#btn-hide").click(function (){
        $("#img-id").hide(1000, function (){
            console.log("Image Hide Ho Chuka Hai");
        });
    });

    //Show
    $("#btn-show").click(function (){
        $("#img-id").show(5000, function (){
            console.log("Image Show Ho Chuka Hai");
        });
    });

     //Hide and Show -  Toggle
     $("#btn-toggle").click(function (){
        $("#img-id").toggle(1000, function (){
            console.log("Image Hide/Show Ho Chuka Hai");
        });
    });

     //Fade Out
     $("#btn-fadeout").click(function (){
        $("#img-id").fadeOut(function (){
            console.log("Image Fade Out");
        });
    });

    //Fade In
    $("#btn-fadein").click(function (){
        $("#img-id").fadeIn(function (){
            console.log("Image Fade In");
        });
    });

    //Fade To
    $("#btn-fadeto").click(function (){
        $("#img-id").fadeTo(1000, 0.5, function (){
            console.log("Image Fade To");
        });
    });

    //Fade Toggle
    $("#btn-fadetoggle").click(function (){
        $("#img-id").fadeToggle(function (){
            console.log("Image Fade Toggle");
        });
    });
    
    

    //Slide Up
    $("#btn-slideup").click(function (){
        $("#img-id").slideUp(1000, function (){
            console.log("SLide Up Image");
        });
    });

    //Slide Down
     $("#btn-slidedown").click(function (){
        $("#img-id").slideDown(1000, function (){
            console.log("SLide Down Image");
        });
    });

    //Slide Toggle
    $("#btn-slidetoggle").click(function (){
        $("#img-id").slideToggle(1000, function (){
            console.log("SLide Toggle Image");
        });
    });

    // Animate - Perform a custom animation of a set of CSS Properties
    $("#btn-animate").click(function (){
        $("#zom-id").animate({ left: "+=150" }, 1000, function () {
            console.log("Image Animate Ho Chuka Hai");
        });
    });

    // Get Text Data
    let textdata = $("p").text();
    console.log(textdata);

    // Set Text Data
    $("#btn-settext").click(function (){
        let newTextdata = "This is new text";
        $("p").text(newTextdata);
    });

    // Get HTML
    let htmldata = $("p").html();
    console.log(htmldata);
    // Set Text Data
    $("#btn-setHTML").click(function (){
        let newTextdata = "<b>This is new HTML</b>";
        $("p").html(newTextdata);
    });

    // Get Value
    let inputValue = $("#name").val();
    console.log(inputValue);
    // Set Value
    $("#btn-setValue").click(function (){
        let newValue = "Prajwal";
        $("#name").val(newValue);
    });

    // Get Attribute
   let attrValue1 =  $("link").attr("href");
   console.log(attrValue1);

   // Get Attribute Value
   let attrValue2 =  $("#name").attr("data-sid");
   console.log(attrValue2);

   // Set Attribute Value
   $("#btn-setattribute").click(function () {
    // Get Old Data
    console.log("Old Data", $("#name").attr("data-sid"))
    // Set New Data
    $("#name").attr("data-sid", "20");
    console.log("New data Set");
    // Get New Data
    console.log("New Data", $("#name").attr("data-sid"));
   });

   // Set Image src attribute
   $("#btn-setimage").click(function () {
    $("#img-id").attr("src", "images/img2.jpg");
   });

   //Add CSS Classes
   $("#btn-addcss").click(function() {
    $("p").addClass("myclass");
   });
   //Remove CSS Classes
   $("#btn-removecss").click(function() {
    $("p").removeClass("myclass");
   });
   //ToggleCSS Classes
   $("#btn-togglecss").click(function() {
    $("p").toggleClass("myclass");
   });

   // Get CSS Property Value
   let colvalue = $("#div-id").css("color");
   console.log(colvalue);
   // Set CSS Property Value
   $("#btn-setcss").click(function (){
    console.log("setting");
    $("#div-id").css("font-size", 70);
   });

   //Set Multiple CSS Property
   $("#btn-setmulticss").click(function (){
    console.log("sett multi css");
    $("#div-id").css({"font-size": 120, "background-color": "pink" });
   });

   
});
var canvas = document.getElementById("myCanvas");
var image_input = document.querySelector("#image-input");
var image = document.getElementById("image");
var points_x = document.getElementById('input_list_x');
var points_y = document.getElementById('input_list_y');
var points_list_x = [];
var points_list_y = [];
var ctx = canvas.getContext("2d");
ctx.font = "16px Arial";

if (image){
    canvas.width = image.naturalWidth;
    canvas.height = image.naturalHeight
    var background_image = new Image();
    background_image.src = image.src;
    console.log(background_image.src);
    ctx.drawImage(background_image,0,0);
};



canvas.addEventListener("mousemove", function(e) { 
    var cRect = canvas.getBoundingClientRect();              // Gets the CSS positions along with width/height
    var canvasX = Math.round(e.clientX - cRect.left);        // Subtract the 'left' of the canvas from the X/Y
    var canvasY = Math.round(e.clientY - cRect.top);         // positions to get make (0,0) the top left of the 
    ctx.clearRect(0, 0, canvas.width, canvas.height);        // canvas
    if (background_image){
        ctx.drawImage(background_image,0,0);
    };

    for (let index_number= 0 ; index_number < points_list_x.length; ++index_number){
        drawCoordinates(points_list_x[index_number],points_list_y[index_number]);

    };
    points_x.value = points_list_x;
    points_y.value = points_list_y;
    console.log(points_x.value)
    console.log(points_y.value)
    ctx.fillText("X: "+canvasX+", Y: "+canvasY, 10, 20);
});

canvas.addEventListener("click",function(e){
    var cRect = canvas.getBoundingClientRect();              // Gets the CSS positions along with width/height
    var canvasX = Math.round(e.clientX - cRect.left);        // Subtract the 'left' of the canvas from the X/Y
    var canvasY = Math.round(e.clientY - cRect.top);  
    drawCoordinates(canvasX, canvasY);
    points_list_x.push(canvasX);
    points_list_y.push(canvasY);
});
//
//image_input.addEventListener("change",function(){
//    console.log("change");
//    var background = new Image();
//    console.log(image_input.files[0]);
//    background.src = URL.createObjectURL(image_input.files[0])
//    ctx.drawImage(background,0,0);
//
////    background.src=image_input.files[0].name;
////    console.log(background.src)
////    ctx.drawImage(image_input.value,0,0);
//});


function drawCoordinates(x,y){	
  	var ctx = document.getElementById("myCanvas").getContext("2d");
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, 2 * Math.PI);
    ctx.fill();
};
//console.log(points_list_x);

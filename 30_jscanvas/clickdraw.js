// Team Acranauts: May and Anjini 


//retrieve node in Dom via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
//aka creates the canvas 
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//toggle = switch | button that switches rectangle and circle 
//var toggleMode = function(e) {

    var toggleMode = (e) => {
        console.log("toggling...");
        if(mode == "rect") {
            mode = "circle"
            //console.log("circle");

        }
        else {
            mode = "rect"
            //console.log("rect");

        }
    }
    var rectcirc = document.getElementById("buttonToggle");
    rectcirc.addEventListener("click", toggleMode);

    var drawRect = function(e){
        var mouseX = e.offsetX;
        console.log(mouseX);
        
        var mouseY = e.offsetY;
        console.log(mouseY);
        
        console.log("mouseclick registered at ","HHE", mouseX, mouseY);
        ctx.beginPath();
        ctx.rect(mouseX,mouseY,50,50);
        ctx.stroke();
    }

    var drawCircle = function(e) {
    // var drawCircle = (e) => {
        var mouseX = e.offsetX;
        console.log(mouseX);
        
        var mouseY = e.offsetY;
        console.log(mouseY);

        console.log("mouseclick registered at ", mouseX, mouseY);
        ctx.beginPath();
        ctx.arc(mouseX,mouseY, 25, 0, 2 * Math.PI);
        ctx.stroke();
    }
    //????
    var draw = function(e) {
        //var draw = (e) => {
        console.log("AJAJ")
        if(mode == "rect"){
            console.log("rec")
            c.addEventListener("click",drawCircle);
            drawRect;
        }
        else{
            console.log("circ")
            c.addEventListener("click",drawCircle);
            drawCircle;
        }
    }
    var wipeCanvas = function() {
        //var wipeCanvas = () => {
        ctx.clearRect(0,0,c.width, c.height);
    }
    var cleaning = document.getElementById("buttonClear");
    cleaning.addEventListener("click", wipeCanvas);
    c.addEventListener("click", draw);
    // var bToggler = document. ;
    // bToggler. ;
    // var clearB = ;
    // clearB. ;
    
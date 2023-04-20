// Team Acronauts :: Anjini and May
// SoftDev pd07
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17m
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  // will add a string to the end "thelist"
  var list = document.getElementById("thelist");
  // access "thelist" created in the html file
  var newitem = document.createElement("li");
  //adds a new bullet point to add the string to 
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  //removes an item from "thelist" using the index
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  // items is a varable that contains all the bulletpoints 
  for(var i = 0; i < items.length; i++) {
    //its going to iterate through each index of items
    items[i].classList.add('red');
    //it'll add red if red isn't in the class (for "thelist" from the index.html file)
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      //even add red, odd add blue to class
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
function fib(n) {
    if(n == 0){
        return 0
    }
    else if(n == 1){
        return 1
    }
    else{
      // fib.setAttribute("AHAHA",fib(10))
      return(fib(n-2) + fib(n-1))
    }
}

function print(){
  var ans = document.createElement("li")
  ans.innerHTML = fib(10)
  document.getElementById("thelist").appendChild(ans)
  var ans2 = document.createElement("li")
  ans2.innerHTML = fact(10)
  document.getElementById("thelist").appendChild(ans2)
  var ans3 = document.createElement("li")
  ans3.innerHTML = gcd(10,5)
  document.getElementById("thelist").appendChild(ans3)
}

// FAC

function fact(n) {
  if(n < 2){
      return 1
  }
  else{
      return (n * fact(n-1))
  }
}

// GCD
function gcd(x, y){
  if (x<y){
    var small = x
    var big = y
  }
  else{
    var small = y
    var big = x
  }

  for(var i = small; i>0; i--){
    if (big % i == 0){
      return i
    }
  }
}


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};



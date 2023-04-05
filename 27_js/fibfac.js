// Arcanauts: May and Anjini
// SoftDev pd7
// K27 -- Basic functions in JavaScript
// 2023-04-03t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

function fact(n) {
    if(n < 2){
        return 1
    }
    else{
        return (n * fact(n-1))
    }
}

function fib(n) {
    if(n == 0){
        return 0
    }
    else if(n == 1){
        return 1
    }
    else{
        return(fib(n-2) + fib(n-1))
    }
}

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

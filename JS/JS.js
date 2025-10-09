/*
////Types of outputs in JS
    console.log('Backend works here')// This is a print statement that prints on the console.
    alert('Welcome to the site!!') // This is an alert or basically this popup that appears on screen.

////Variables and Data types in JS
    var name = 'Viscous'; // var is a variable that can be changed later in the code.
    let age = 19; // let is used to make a non global variable.
    const pi = 3.14; // const is a variable that cannot be changed later in the code.
    x=10;//int//this will be treated as a global variable,that is even called out of a function.
    y=20.5;//float
    z="Hello World";//string
    is_true=true;//boolean
    is_false=false;//boolean
    n=null;//null
    u=undefined;//undefined
 
////If else:
    if (age > 18) {
        console.log('You are an adult');
    }
    else if (age === 18) {
        console.log('You are exactly 18');
    }
    else {
        console.log('You are not an adult');
    }
////function:
    function checkAge(age) {
        if (age > 18) {
            console.log('You are an adult');
        }
        else if (age === 18) {
            console.log('You are exactly 18');
        }
        else {
            console.log('You are not an adult');
        }
    }
////class:
    class Person {
        constructor(name, age) {//This is basically self.name in python type
            this.name = name;
            this.age = age;
        }
    
        checkAge() {
            if (this.age > 18) {
                console.log(`${this.name} is an adult`);
            }
            else if (this.age === 18) {
                console.log(`${this.name} is exactly 18`);
            }
            else {
                console.log(`${this.name} is not an adult`);
            }
        }
    }
////Array(List):
    const fruits = ['apple', 'banana', 'orange'];
    console.log(fruits[0]); // apple
    fruits.push('grape');
    console.log(fruits.length); // 4
    fruits.pop();//remove last element
    fruits.pop();
    console.log(fruits); // 2
    fruits.shift(); // remove first element
    console.log(fruits); // 1
////Object(Dictionary):
    const person = {
        name: 'John',
        age: 30,
        isEmployed: true
    };
    console.log(person.name); // John
    console.log(person['age']); // 30
    person.age = 31;
    console.log(person.age); // 31

////Variable Scope:
    function testScope() {
        var x = 1; // function-scoped
        let y = 2; // block-scoped
        const z = 3; // block-scoped
        console.log(x); // 1
        console.log(y); // 2
        console.log(z); // 3
    }
    testScope();
    console.log(x); // ReferenceError: x is not defined
    console.log(y); // ReferenceError: y is not defined
    console.log(z); // ReferenceError: z is not defined 
////for loop:
    for (var i = 0; i < 3; i++) {
        console.log(i); // 0, 1, 2
    }
////while loop:
    var j = 0;
    while (j < 3) {
        console.log(j); // 0, 1, 2
        j++;
    }
////Arrow function:
    const square = (x) => {
        return x * x;
    };
    console.log(square(5)); // 25
    
*/ 
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


////Arrow function:
    const square = (x) => {
        return x * x;
    };
    console.log(square(5)); // 25



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
    //Str are immutable but lists are mutable
    const fruits = ['apple', 'banana', 'orange'];
    console.log(fruits[0]); // apple
    fruits.push('grape');
    console.log(fruits.length); // 4
    fruits.pop();//remove last element
    console.log(fruits); // 2
    fruits.shift(); // remove first element
    console.log(fruits); // 1
    fruits.unshift('mango'); // add element at the beginning
    console.log(fruits); // 3
    console.log(fruits.indexOf('banana')); // 1
    console.log(fruits.slice(0, 2)); // ['mango', 'banana']
    console.log(fruits.join(', ')); // 'mango, banana, orange'
    condole.log(fruits.toString()); // convert array to string
    

////Loop through array:
    const numbers = [1, 2, 3, 4, 5];
    for (let i in numbers) {
        console.log(i);//prints index 0,1,2,3,4 
    }
    
    const numbers = [1, 2, 3, 4, 5];
        for (let i of numbers) {
            console.log(i);//prints values 1,2,3,4,5
        }


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
////for-of loop:
    //iterating over array
    const colors = ['red', 'green', 'blue'];
    for(let color of colors){
        console.log(color);}
    }
////for-in loop:
    //iterating over object
    const car = {make: 'Toyota', model: 'Camry', year: 2020};
    for(let key in car){
        console.log(`${key}: ${car[key]}`);
    }


/////Ternary operator:
    //Prompt runs only in browser environment
    const age = prompt("Please enter your age:");
    let access = (age >= 18) ? 'granted' : 'denied';
    console.log(`Access ${access}`);


/////String methods:
    //Creating a string
    let str = "Hello, World!";
    let str1 = str.toUpperCase(); // Convert to uppercase
    let str2 = str.toLowerCase(); // Convert to lowercase
    let str3 = str.slice(0, 5); // Extract substring
    let str4 = str.replace("World", "JS"); // Replace substring
    let str5 = str.split(", "); // Split string into array
    let str6 = str.charAt(0); // Get character at index 0
    let str7 = str.indexOf("World"); // Find index of substring
    let str8 = str.concat(" Welcome to JavaScript."); // Concatenate strings
    let str9 = str.trim(); // Remove whitespace from both ends
    console.log(str1); // "HELLO, WORLD!"
    console.log(str2); // "hello, world!"
    console.log(str3); // "Hello"
    console.log(str4); // "Hello, JS!"
    console.log(str5); // ["Hello", "World!"]
    console.log(str6); // "H"
    console.log(str7); // 7
    console.log(str8); // "Hello, World! Welcome to JavaScript."
    console.log(str9); // "Hello, World!"
    //Template literals:
    let name = "Alice";
    let greeting = `Hello, ${name}! Welcome to JS.`;//use of template literals
    console.log(greeting); // "Hello, Alice! Welcome to JS."

    //escape characters
    let text = "He said, \"Hello!\"\nWelcome to JS.";
    console.log(text);
    //Output:
    //He said, "Hello!"
    //Welcome to JS.
*/

////
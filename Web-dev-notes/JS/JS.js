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
    letprevess = (age >= 18) ? 'granted' : 'denied';
    console.log(prevess $prevess}`);


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

////Methods:
    //higher order function example:
    //callback function example:
    let arr=[1,2,3,4,5];
    //arr.forEach(val,idx,arr)
    arr.forEach(function sq(element) {
        console.log(element * 2);
    });
    let sq = (a)=> a*a;

////map method://same as forEach but this method return a new arr but forEach changes in existing one:
    let squaredArr = arr.map(sq);
    console.log(squaredArr);//[1,4,9,16,25]

////filter method:
    let evenArr = arr.filter(function isEven(element) {
        return element % 2 === 0;
    });
    console.log(evenArr);//[2,4]
    
////reduce method:
    let arr = [1, 2, 3, 4, 5];
    let max = arr.reduce((prev, curr) => {
        return prev > curr ? prev : curr;
    });
    
    console.log(max);//15

////find method:
    let found = arr.find((element) => {
        return element > 3;
    });
    console.log(found);//4


////console.dir() method:
    console.dir(window);//full window funx object
    console.dir(document);//document object or the dom structure
    console.log(document);//html version of the dom structure
    ////bacially there is a prebuilt window object in JS that represents the browser window.i.e. windows.console.log  is the original console .log is the alias.

////DOM:
    ////how to make dynamic changes to a webpage using DOM methods:
        document.body.style.backgroundColor = "lightblue";//change background color of body

    ////Selection with id:
        let id = document.getElementById("myElement");//gets element with id myElement
        id.innerHTML = "Content changed using DOM!";//change content of element with id myElement
    ////Selection with class name:
        let className = document.getElementsByClassName("myClass");//gets elements with class name myClass
        className[0].innerHTML = "First element with class myClass changed!";//change content of first element with class name myClass
    ////Selection with tag name:
        let tagName = document.getElementsByTagName("p");//gets all paragraph elements
        tagName[0].innerHTML = "First paragraph changed!";//change content of first paragraph element
    ////forgot all these methods and use query selector only

    ////Selection with query selector:
        let queryId = document.querySelector("#myElement");//gets element with id myElement
        queryId.innerHTML = "Content changed using query selector!";//change content of element with id myElement

        let queryClass = document.querySelector(".myClass");//gets first element with class name myClass
        queryClass.innerHTML = "First element with class myClass changed using query selector!";//change content of first element with class name myClass

        let queryTag = document.querySelector("p");//gets first paragraph element
        queryTag.innerHTML = "First paragraph changed using query selector!";//change content of first paragraph element

    ////Selection with query selector all:
        let queryAllId = document.querySelectorAll("#myElement");//gets all elements with id myElement
        queryAllId[0].innerHTML = "Content changed using query selector all!";//change content of element with id myElement

        let queryAllClass = document.querySelectorAll(".myClass");//gets all elements with class name myClass
        queryAllClass[0].innerHTML = "First element with class myClass changed using query selector all!";//change content of first element with class name myClass

        let queryAllTag = document.querySelectorAll("p");//gets all paragraph elements
        queryAllTag[0].innerHTML = "First paragraph changed using query selector all!";//change content of first paragraph element  

////DOM Manipulation:
    ////tagName method://returns tag for the element nodes
        console.log(queryAllId[0].tagName);//prints the tag name of the element with id myElement
        queryAllId[0].tagName = "DIV";//changes the tag name of the element with id myElement to DIV
    ////innerText://returns the text content of the element and its children
        console.log(queryAllClass[0].innerText);//prints the text content of the first element with class name myClass
        queryAllClass[0].innerText = "Changed using innerText";//changes the text content of the first element with class name myClass    
    ////innerHTML://returns the HTML content of the element and its children
        console.log(queryAllTag[0].innerHTML);//prints the HTML content of the first paragraph element
        queryAllTag[0].innerHTML = "<b>Changed using innerHTML</b>";//changes the HTML content of the first paragraph element
    ////textContent://returns the text content of the element and its children, including hidden elements
        console.log(queryAllTag[0].textContent);//prints the text content of the first paragraph element including hidden elements 
        queryAllTag[0].textContent = "Changed using textContent";//changes the text content of the first paragraph element including hidden elements
    ////getAttribute://gets the value of an attribute on the specified element
        let img = document.querySelector("img");//gets the first image element
        console.log(img.getAttribute("src"));//prints the value of the src attribute of the image element    
    ////setAttribute://sets the value of an attribute on the specified element
        img.setAttribute("alt", "Image changed using setAttribute");//sets the value of the alt attribute of the image element
    ////style://returns the style attribute of the element
        console.log(img.style);//prints the style attribute of the image element
        img.style.border = "2px solid black";//sets the border style of the image element

////INSERTING or DELETING ELEMENTS:
    ///node.append()//adds a node to the end of the list of children of a specified parent node.
        let newDiv = document.createElement("div");//creates a new div element
        newDiv.innerHTML = "This is a new div added using append()";//sets the innerHTML of the new div element
        document.body.append(newDiv);//adds the new div element to the end of the body element
    ///node.prepend()//adds a node to the beginning of the list of children of a specified parent node.
        let anotherDiv = document.createElement("div");//creates a new div element
        anotherDiv.innerHTML = "This is another div added using prepend()";//sets the innerHTML of the new div element
        document.body.prepend(anotherDiv);//adds the new div element to the beginning of the body element
    ///node.insertBefore(newNode, referenceNode)//inserts a node before a reference node as a child of a specified parent node.
        let beforeDiv = document.createElement("div");//creates a new div element
        beforeDiv.innerHTML = "This is a div added using insertBefore()";//sets the innerHTML of the new div element
        let referenceNode = document.querySelector("h3");//gets the h3 element as the reference node
        document.body.insertBefore(beforeDiv, referenceNode);//inserts the new div element before the h3 element
    ///node.after(referenceNode)//inserts a node after a reference node as a child of a specified parent node.
        let afterDiv = document.createElement("div");//creates a new div element
        afterDiv.innerHTML = "This is a div added using after()";//sets the innerHTML of the new div element
        referenceNode.after(afterDiv);//inserts the new div element after the h3 element
    ///node.remove()//removes a node from the DOM.
        anotherDiv.remove();//removes the anotherDiv element from the DOM
    ////appendChild()://adds a node to the end of the list of children of a specified parent node.
        let childDiv = document.createElement("div");//creates a new div element
        childDiv.innerHTML = "This is a child div added using appendChild()";//sets the innerHTML of the new div element
        document.body.appendChild(childDiv);//adds the new div element to the end of the body element
    ////removeChild()://removes a node from the DOM.
        document.body.removeChild(childDiv);//removes the childDiv element from the DOM

////EVENTS:
    ////Adding a button
        let button = document.createElement("button");//creates a new button element
        button.innerHTML = "Click Me";//sets the innerHTML of the button element
        document.body.appendChild(button);//adds the button element to the end of the body element
        let button2 = document.createElement("button");//creates a new button element
        button2.innerHTML = "Click Me twice";//sets the innerHTML of the button element
        document.body.appendChild(button2);//adds the button element to the end of the body element
    
    
    ////onclick event:
        button.onclick = () => {
            console.log("Button clicked using onclick event!");//logs a message to the console when the button is clicked
            alert("button clicked using onclick event!");//shows an alert when the button is clicked
        };
    ////dblclick event:
        button2.ondblclick = () => {
            console.log("Button double clicked using ondblclick event!");//logs a message to the console when the button is double clicked
            alert("button double clicked using ondblclick event!");//shows an alert when the button is double clicked
        };

////Dark and Light mode:
    let darkModeButton = document.createElement("button");//creates a new button element
    darkModeButton.innerHTML = "Toggle Dark/Light Mode";//sets the innerHTML of the button element
    document.body.appendChild(darkModeButton);//adds the button element to the end of the body element
    
    let currMode = "light";//initial mode is light mode
    darkModeButton.onclick = () => {
        if(currMode === "light"){
            document.body.style.backgroundColor = "black";//change background color to black
            document.body.style.color = "white";//change text color to white
            currMode = "dark";//update current mode to dark mode
        }
        else{
            document.body.style.backgroundColor = "white";//change background color to white
            document.body.style.color = "black";//change text color to black
            currMode = "light";//update current mode to light mode
        }
    };

////EVENT LISTENERS:
    ////click event listener:
        button.addEventListener("click", () => {
            console.log("Button clicked using addEventListener!");//logs a message to the console when the button is clicked
            alert("button clicked using addEventListener!");//shows an alert when the button is clicked
        });
    

*/
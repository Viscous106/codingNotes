//alert("Hello, World!");//popup in browser

//////// Variable_declaration

/*name1 = "John";
age=7;
a=true;
b=false;
c=9.9;
x=null;
y=undefined;
*/
//console.log(x,typeof x,y,typeof y,a,typeof a,b,typeof b,c,typeof c,name1,typeof name1,age,typeof age);

/////const and let

//const name1 = "John"; // cont and cant be changed like var
//let age = 7; // let can be changed like var

/*x=BigInt(1234567890123456789012345678901234567890); // BigInt for large integers
y=Symbol("description"); // Symbol for unique identifiers
console.log(x,typeof x,y,typeof y);*/

//////dict or object:
/*const person = {
    name: "John",
    age: 30,
    isEmployed: true,
    salary: 50000,
    address: {
        street: "123 Main St",
        city: "New York",
        zip: "10001"
    }
};*/
//console.log(person.isEmployed,person.name, person["name"], person["age"], person.address.city); // Accessing properties using dot notation and bracket notation
//console.log(person,typeof person);

////////Operators:
/*
a=5;
b=3;
a+=1; // Incrementing a by 1
b-=1; // Decrementing b by 1
console.log(a,b); // Output: 6, 2
console.log(a+b,a-b,a*b,a/b,a%b,a**b); // Arithmetic operators
console.log(a==b,a===b,a!=b,a!==b,a<b,a<=b,a>b,a>=b); // Comparison operators
*/
/*
console.log("condition1 &&condition2=",2>1 && 3<4)//and
console.log("condition1 ||condition2=",2>1 || 3>4)//or
console.log("condition1 ? value1 : value2=",2>1 ? "Yes" : "No") // Ternary operator
console.log("5 instanceof Number=",5 instanceof Number) // Instanceof operator*/

///////if ,else if, else:
/*let age=prompt("enter a age:");
if(age>=18){
    console.log('Bravo,you may enjoy this movie.')
}
else if(age<18){
    console.log('sorry sir you have to wait',18-age,'more years')
}
else{
    console.log('invalid input!!')
}
*/
//////ternary operator:
/*age=prompt("enter a age:");
console.log(age>=18 ? 'Bravo,you may enjoy this movie.' : 'sorry sir you are not allowed to watch this movie, you have to wait ' + (18 - age) + ' more years');
*/

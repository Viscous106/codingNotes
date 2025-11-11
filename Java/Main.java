
//import java.util.*;
//import java.util.Arrays;
/*
class javaNotes {
        public static void main(String[] args) {

        ///////////How to print variables:
                int a = 10;
                System.out.println(a);
                String name = "John";
                System.out.println(name);
                System.out.printf("The value of a is %d and name is %s\n", a, name);//formatted print
                System.out.format("The value of a is %d and name is %s\n", a, name);//formatted print

        /////////types of non decimals datatypes

                byte for 1byte [-128 to 127]
                short for 2bytes [-32,768 to 32,767]
                int 4bytes [-2,147,483,648 to 2,147,483,647]
                long 8bytes [-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807]
        
        /////////types of decimal datatypes:
                float 4bytes [1.4E-45 to 3.4028235E38]
                double 8bytes [4.9E-324 to 1.7976931348623157E308]
        /////////boolean and strings datatypes:
                char 2bytes ['a' to 'z' or 'A' to 'Z' or any symbol]
                boolean 1byte [true or false]
                String [collection of characters]
        
        //////////cassting:
                public static void main(String[] args){
                long a =100000L;//L here tells the system that the num is a long
                int b =400000;
                long result =a*b;
                System.out.print(result);


        //////////input int:
                Scanner in = new Scanner(System.in);
                System.out.println("Enter a number:");
                //how to take integer output
                int input1=in.nextInt();
                System.out.print("you have entered "+input1);

        //////////input string:
                Scanner in = new Scanner(System.in);
                System.out.println("Enter a text:");
                //how to take string input
                String input0=in.next();//it takes input till space
                String input1=in.nextLine();//it takes input till end of line
                System.out.print("you have entered "+input1);
                System.out.println(input1.length());//length of string
                System.out.println(input1.toLowerCase());//lowercase
                System.out.println(input1.toUpperCase());//uppercase
                System.out.println(input1.trim());//removes spaces before and after the string
                System.out.println(input1.substring(0,4));//substring from 0 to 3


        /////////1D array:
                
                //Meth 1
                // int[] arr = new int[5];//declaration of array of size 5
                // arr[0]=10;
                // arr[1]=60;
                // arr[2]=30;
                // arr[3]=40;
                // arr[4]=50;                
                
                //Meth 2
                int[] arr = {10, 60, 30, 40, 50};//declaration and initialization of arraay
                System.out.println(arr);//prints the address of the array
                System.out.println(arr[0]);//prints the 0th index value of array
                System.out.println(arr.length);//length of array
                Arrays.sort(arr);
                System.out.println(Arrays.toString(arr));//prints the sorted array

                ////To take arr input use for loop.
                int n=arr.length;///To find length of array
                
        //////////2d array:
                
                //Meth 1
                int[][] arr = new int[3][3];//declaration of 2D array of size 3x3
                arr[0][0]=10;
                arr[0][1]=20;
                arr[0][2]=30;
                arr[1][0]=40;
                arr[1][1]=50;
                arr[1][2]=60;
                arr[2][0]=70;
                arr[2][1]=80;
                arr[2][2]=90;
                 
                //Meth 2
                // int[][] arr = {{10,20,30},{40,50,60},{70,80,90}};//declaration and initialization of 2D array
                System.out.println(Arrays.deepToString(arr));//prints the 2D array


                //final int a = 10; //constant variable
                // a = 20; //error as constant variable cannot be changed
                

                
        ////////operators 
                int a = 10;
                int b = 20;
                System.out.println(a+b);//addition
                System.out.println(a-b);//subtraction
                System.out.println(a*b);//multiplication
                System.out.println(b/a);//division
                //if one is float and one is int then the output will be float
                //if both are int then the output will be int
                System.out.println(b%a);//modulus
                System.out.println(++a);//pre-increment
                System.out.println(a++);//post-increment
                System.out.println(--b);//pre-decrement
                System.out.println(b--);//post-decrement

                //logical operators: &&(and), ||(or), !(not)
                System.out.println((a<b) && (a==10));//true && true = true
                System.out.println((a>b) || (a==10));//false || true = true
                System.out.println(!(a==10));//not true = false

                //comparison operators: ==, !=, >, <, >=, <=
                System.out.println(a==b);//false
                System.out.println(a!=b);//true
                System.out.println(a>b);//false
                System.out.println(a<b);//true
                System.out.println(a>=b);//false
                System.out.println(a<=b);//true


        /////////function maths:
                int a = 10;
                int b = 20;
                System.out.println(Math.max(a,b));//max of a and b
                System.out.println(Math.min(a,b));//min of a and b
                System.out.println(Math.sqrt(16));//square root
                System.out.println(Math.abs(-4));//absolute value
                System.out.println(Math.random());//random value between 0 and 1
                System.out.println((int)(Math.random()*100));//random value between 0 and 100

        /////////if-else:
                Scanner in = new Scanner(System.in);
                int a = in.nextInt();
                if(a>0){
                        System.out.println("a is positive");
                }
                else{
                        System.out.println("a is negative");
                }


        /////////switch-case:
                Scanner in = new Scanner(System.in);
                int a = in.nextInt();
                switch(day){
                        case 1:
                                System.out.println("Monday");
                                break;
                        case 2:
                                System.out.println("Tuesday");
                                break;
                        case 3:
                                System.out.println("Wednesday");
                                break;
                        case 4:
                                System.out.println("Thursday");
                                break;
                        case 5:
                                System.out.println("Friday");
                                break;
                        case 6:
                                System.out.println("Saturday");
                                break;
                        case 7:
                                System.out.println("Sunday");
                                break;
                        default:
                                System.out.println("Invalid day");
                                break;
                
        //////////while loop:
                Scanner in = new Scanner(System.in);
                int n = in.nextInt();
                int i = 1;
                while(i<=n){
                        System.out.println(i);
                        i++;
                }
        
        /////////for loop:
                Scanner in = new Scanner(System.in);
                int n = in.nextInt();
                for(int i=1;i<=n;i++){//(initialization, condition, increment)
                        System.out.println(i);
                }
        
        /////////do-while loop:
                Scanner in = new Scanner(System.in);
                int n = in.nextInt();
                int i = 1;
                do{
                        System.out.println(i);
                        i++;
                }while(i<=n);//if condition is false then also it will execute once
        
        /////////for-each loop:
                int[] arr = {10, 20, 30, 40, 50};
                for(int num:arr){//for each element in array
                        System.out.println(num);
                }

        /////////break and continue:
                Scanner in = new Scanner(System.in);
                int n = in.nextInt();
                for(int i=1;i<=n;i++){
                        if(i==5){
                                break;//breaks the loop when i=5
                        }
                        System.out.println(i);
                }
                for(int i=1;i<=n;i++){
                        if(i==5){
                                continue;//skips the iteration when i=5
                        }
                        System.out.println(i);
                }
        
        ///////////try-catch:
                Scanner in = new Scanner(System.in);
                System.out.println("Enter a number:");
                int a = in.nextInt();
                try{
                        System.out.println("The value of a is "+a);
                        System.out.println("The value of 10/a is "+10/a);
                }
                catch(ArithmeticException e){
                        System.out.println("Cannot divide by zero");
                }
                catch(Exception e){
                        System.out.println("Some error occurred");
                }
                finally{
                        System.out.println("This block is always executed");
                }

        ///////////Methods or functions:
                //method to add two numbers
                public static int add(int a, int b){
                        return a+b;
                }
                public static void main(String[] args){
                        int sum = add(10, 20);
                        System.out.println("The sum is "+sum);
                }

        ///////////function overloading:
        /// if it is int then it will call int add function
        /// if it is double then it will call double add function
                class MathOperation{
                        int add(int a, int b){
                                return a+b;
                        }
                        double add(double a, double b){
                                return a+b;
                        }


        ///////////Types of inheritance:
                //single inheritance: class B extends A
                        class Animal{
                                void info(){
                                System.out.println("Animal makes sound");
                                String color = "brown";
                                System.out.println("Color: " + color);
                        }
                }
                        class Dog extends Animal{
                                void info(){
                                System.out.println("Dog barks");
                                super.info();//calls the parent class function
                                String breed = "Labrador";
                                System.out.println("Breed: " + breed);
                                String color = "black";
                                System.out.println("Color: " + color);//prints the color of dog class
                                System.out.println("Color: " + super.color);//prints the color of animal class
                        }
                }
                Dog d = new Dog();
                d.info();
                Animal a = new Animal();
                a.info();

                //multilevel inheritance: class C extends B, class B extends A
                
                //hierarchical inheritance: class B extends A, class C extends A


                //multiple inheritance is not supported in java
                //but it can be achieved using interfaces
                

        ////////Fizz-Buzz:
                Scanner sc=new Scanner(System.in);
                int a= sc.nextInt();
                if (a%3==0){
                    if(a%5==0){
                        System.out.println("Fizz-Buzz");
                    }
                    else{
                        System.out.print("Fizz");
                    }
                }
                else if(a%5==0){
                    System.out.print("Buzz");
                }
        ////////Arraylist:
                ArrayList<String> fruits = new ArrayList<>();
                fruits.add("Apple");
                fruits.add("Banana");
                fruits.add("Orange");
                System.out.println(fruits);
                fruits.remove("Banana");
                String A = fruits.get(0);
                fruits.add(2,"Mango");//Adds at index 2
                fruits.set(0,"Kiwi");//Updates index 0
                fruits.remove(1);//Removes element at index 1
                System.out.println(fruits);
                System.out.println(A);
                

////////OOPS:
        class Person{
                        //attributes//plane declaration of variable
                        String name;
                        int roll;
                        int age;
                        double cgr;
                        String college;

                        //constructor
                        Person(String name, int age,int roll,double cgr){
                                this.name = name;
                                this.college = "SST";
                                this.roll = roll;
                                this.age = age;
                                this.cgr = cgr;
                        }

                        //function to display person details:
                        void display(){
                                System.out.println("Name: "+name);
                                System.out.println("Age: "+age);
                                System.out.println("Roll: "+roll);
                                System.out.println("CGR: "+cgr);
                                System.out.println("Colledge:"+college);
                        }
                }
                Person p1 = new Person("John", 25,1013,8.9);//object creation
                p1.display();//function call

        //Shallow Copy vs Deep Copy:
                class Student{
                        String name;
                        int roll;
                        Student(String name, int roll){
                                this.name = name;
                                this.roll = roll;
                        }
                }
                Student s1 = new Student("Alice", 101);
                
                //Shallow Copy
                Student s2 = s1;
                s2.name = "Bob";
                System.out.println(s1.name);//prints Bob

                //Deep Copy
                Student s3 = new Student(s1.name, s1.roll);
                s3.name = "Charlie";
                System.out.println(s1.name);//prints Bob
        }
}
*/
        class Vehicle {
                public int numGears;
                public int numTyres;
                public int Topspeed;
                public void startEngine(){
                        System.out.println("Engine Started");
                }        
                public void stopEngine(){
                        System.out.println("Engine Stopped");
                }
                public void info() {
                System.out.println("No of Gears: " + numGears);
                System.out.println("No of Tyres: " + numTyres);
                System.out.println("TopSpeed: " + Topspeed);
                }
        }

        class car extends Vehicle {
                numGears = 6;
                numTyres = 4;
                Topspeed = 300;
                boolean isConvertible;
                void openTrunk(){
                        if(isConvertible){
                                System.out.println("Trunk Opened");
                        }
                }
        }

        class bike extends Vehicle {
                numGears = 6;
                numTyres = 4;
                Topspeed = 300;
                boolean hasHelmetSpace;
                void kickstart(){
                }
        }
public class Main {
        public static void main(String[] args) { 
        car c = new car();
        c.startEngine();
        c.numGears=4;
  }
}
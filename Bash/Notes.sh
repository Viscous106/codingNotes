#! /bin/bash

# ./filePath  use this to run the file 

# Single line comment
: '
    Multi line comment
'

: '
###Print Statement:
    echo "hello world!!"

###Intro to functions:

    fxn(){
        local var="loc.."
        echo $var
    }
    fxn #Calling Fxn 

###Sum of two variable:
    #Concatenation:
        
 
###Types of Data types:
    #String:
        str="KO!!"
        #Concatenation:
            str1="Hi "
            str2="Hello"
            echo "$str1$str2"
    
    #NUMbers:
        num=15
        #Num Operations:
            num1=5
            num2=10
            sum=$((num1 + num2))
            difference=$((num2 - num1))
            product=$((num1 * num2))
            quotient=$((num2 / num1))
            echo "Sum: $sum, Difference: $difference, Product: $product, Quotient: $quotient"   
    #Arrays:
        fruit=("apple","banana")
    #Associative arrays or dictionary:
        declare -A colors
        colors[apple]="red"
        colors[banana]="yellow"
        echo ${colors[apple]}
    #Operators:
        -eq = is ==
        -ne != is !=
        -lt or < is <
        -le is <=
        -gt or > is >
        -ge is >=
        % modulus
        && logical AND
        || logical OR
        -e: Checks if a file exists
        -d: Checks if a directory exists
        -f: Checks if a file is a regular file
        -s: Checks if a file is not empty

###Conditionals:
    #IfElseelif:
        a=9
        if [ $a -eq 9 ]; then # Check if a is equal to 10
            echo "a is 9"  
        elif [ $a -ne 9 ]; then # Check if a is not equal to 10
            echo "a is not 9"
        else
            echo "maths isnt mathing anymore"
        fi
    # Nested if statement
        num=5
        if [ $num -gt 0 ]; then
            if [ $num -lt 10 ]; then
                echo "Number is between 1 and 9"
            fi
        fi
'
###Intro to Loops:
    #For Loop:
        for i in {1..6}; do
            echo "$i"
        done
    #While loop:
        count=1
        while [ $count -ne 5 ]; do
            echo "Count is $count"
            ((count++))
        done


    




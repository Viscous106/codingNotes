

###Types of Data types:
    
        
###Operators:
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
    # Break and continue example
    for i in {1..5}; do
        if [ $i -eq 3 ]; then
            continue
        fi
        echo "Number $i"
        if [ $i -eq 4 ]; then
            break
        fi
    done
    # Nested loops example
    for i in {1..3}; do
        for j in {1..2}; do
            echo "Outer loop $i, Inner loop $j"
        done
    done

###Intro to functions:

    fxn(){
        var="local"
        echo $var
    }
    fxn #Calling Fxn 

    greet() {
        name=$1
        echo "Hello, $name!"
    }
    greet "Alice"
    
    add() {
        sum=$(($1 + $2))
        echo $sum
    }
    result=$(add 5 3)
    echo "The sum is $result"

'
###
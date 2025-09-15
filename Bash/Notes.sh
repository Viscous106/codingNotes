#! /bin/bash

# ./filePath  use this to run the file 

# Single line comment
: '
Multi line comment
'

: '

echo "hello world!!" ##Print Statement

###Conditionals:
a=10
if [ $a -eq 10 ]; then # Check if a is equal to 10
    echo "a is 10"
elif [ $a -ne 10 ]; then # Check if a is not equal to 10
    echo "a is not 10"
else
    echo "maths isnt mathing anymore"
fi
'
#-----------------------------------------------------------------------------------------------------------------------------------
#
#   In this example we will introduce arrays, for loops and functions.
#   The function we will be creating adds seconds to a string, this will be used to find our data start point later.
#   An array holds associated data, which can be of any type and mixed. 
#   We can access data in an array by calling its position, normally called index, in the array. Index always starts from 0.
#   Create a variable and set it equal to a pair of square brackets [] and fill it with numbers or strings(must have parentthesis)
#   To print out data from the array call we use the variablename[i], where i is a number between 0 and the length of your array - 1
#
#-----------------------------------------------------------------------------------------------------------------------------------

myArray = ['1', 5, 'hello', 12345, 8.5, 'how are you']
print myArray[2]

#-----------------------------------------------------------------------------------------------------------------------------------
#
#   If we want to print out every member of the array how can we do that? Any Suggestions?
#   We could print the variable each time with its individual index but on a large array that would be inpracticle.
#   A better way is to use a for loop, this is a fundamental block to almost any code. 
#   Computers are very good at doing the same thing very fast. 
#   We will use the for loop to go though the array and print out each member of the array. 
#
#-----------------------------------------------------------------------------------------------------------------------------------

for i in myArray:
    print i

    

#-----------------------------------------------------------------------------------------------------------------------------------
#
#   A function allows you to make code that is a reusable block, it also allows us to modifiy and change code for a specific function
#   without having to worry about causing issues with the whole programming. 
#   A function could be any usefull block such as printing an array to the screen.
#   To make a function we need to first define it using def then the function name and the variable we will be passing into the function, these are just placeholder names.
#   To use a function we call the function name and place the variable we want the function to act on in the the brackets.
#
#-----------------------------------------------------------------------------------------------------------------------------------

def printArray(x):
    for i in x:
        print i

printArray(myArray)



#-----------------------------------------------------------------------------------------------------------------------------------
#
#   Now we are going to put this together to make our function to make the seconds.
#   How many numbers in a minute, 0 - 59 but we need it in ss format so 00 - 59
#   We will have the string HH:MM: inputed into the function and we want to add every possible second to the time and store the
#   complete 'HH:MM:SS' string which will be used in our final example as a way to find the start of our flight data. 
#   We need four arrays and two for loops, an array from '0' - '5' and '0' - '9' and two blank arrays to put the new time into. 
#   We nest for loops so that for each item in the first array we go throught the whole of the second array. 
#   We can add the i and j values together to make the seconds and then using string concatination we can add the seconds to the 
#   time string we passed in. 
#   This new time can then be stored in the empty array by using the .append(variable) operator to push it to the array.
#
#-----------------------------------------------------------------------------------------------------------------------------------

def addSeconds():
    t = '10:45:'
    s1 = ['0','1','2','3','4','5']
    s2 = ['0','1','2','3','4','5','6','7','8','9']
    launch = []
    for i in s1:
        for j in s2:
            s = i + j
            ntime = t + s
            launch.append(ntime)

    return launch

launch = addSeconds()
print (launch)
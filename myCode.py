#task is to find the Kth occurance of a distinct string in the array

def distinct_string_occurance(array, k):
    #finding the distinct and non-distinct occurance using boolean 
    mydict = {}
    for element in array:
        if element not in mydict:
            mydict[element] = True
        else:
            mydict[element] = False
    

    #finding the kth occurance in this case, 2nd occurance of distinct string
    counter = 0
    for element in array:
        if mydict[element] is True:
            counter += 1
            if counter == k:
                return element
    return element

array = ["a","b","a", "c", "c", "d"]
k = 2
call_function = distinct_string_occurance(array, k)
print(call_function)
def duplicateZeros(arr):
    i = 0
    while (i < len(arr)):
        if arr[i] == 0: # if the current element is a 0
            arr.insert(i, 0) # insert a 0 after the current element
            arr.pop() # pop the element that has fallen off our array
            i += 1 # increment by one so we arn't in a infinite loop
        i += 1

    return arr

def main():
    arr = [1,0,2,3,0,4,5,0]
    print(duplicateZeros(arr))
  
  
# Initalizing main function
if __name__=="__main__":
    main()

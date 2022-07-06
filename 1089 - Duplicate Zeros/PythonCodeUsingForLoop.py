def duplicateZeros(arr):
    flag = False
    for x in range(len(arr) - 1):
        if flag == True: 
            flag = False
            continue
        if arr[x] == 0:
            arr.insert(x,0)
            arr.pop()
            flag = True
            continue

    return arr

def main():
    arr = [1,0,2,3,0,4,5,0]
    print(duplicateZeros(arr))
  
  
# Initalizing main function
if __name__=="__main__":
    main()

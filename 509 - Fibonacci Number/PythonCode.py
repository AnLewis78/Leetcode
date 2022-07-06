
def fib(n):

    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

    
def main():
    n = 4
    print(fib(n))
  
  
# Initalizing main function
if __name__=="__main__":
    main()

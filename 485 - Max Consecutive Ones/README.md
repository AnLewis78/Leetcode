Pre-Planning:

In starting with this problem, we need to look at the definition of Fibonacci's Sequence. The definiton of Fibonacci's Sequence is :

![image](https://assets.leetcode.com/users/images/6552c864-b3c9-408b-a65e-9e2909593918_1657132950.400477.png)

Reference: https://en.wikipedia.org/wiki/Fibonacci_number

---

Python Approach:

- From our pre-planning, we are told that we need to set n0 = 0 and n1 = 1
- Next, we are given the formula that Fibonacci came up with back around the 1200's A.D.
- In applying this we are able to recursively go through Fibonacci's formula, reusing the same if statements to check if n is a 0 or 1, and return us the appropriate sequence for what we initially pass in for n

Python Code:

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

---

Java Approach:

- Using the same method as we looked at with our python code, we are able to rewrite this in Java.
- From our definition we found in our pre-planning, we need to hardcode n0 = 0, and n1 = 1
- Lastly, we can recursively use the formula fibonacci came up with in order to reuse the same if statement and return us the appropriate sequence for what we initially pass in for n

Java Code:

    public class Java {

        public static void main(String[] args){
        
            int n = 4;
            System.out.println(fib(n)); 
        }

        public static int fib(int n){
            if (n == 0 || n == 1)
            {
                return n;
            }
            else
            {
                return fib(n - 1) + fib(n - 2);
            }  
        }
    }

---

Thank You For Reading
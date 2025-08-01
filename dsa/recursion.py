# n=int(input("Enter a number: "))
# x=int(input("Enter another number: "))
# for i in range(n):
#     if x==n:
#         break
#     print(i)
#     n += 1

                              # factoial using recursion

# def fact(n):
#     if n==0:
#         return(1)
#     return(n*fact(n-1))

# print(fact(5))

                                   #recursive stack
# def fact(n):
#     if n==0:
#         return
#     fact(n-1)
#     print(n,end="")

# print(fact(5))  # Output: 12345

                           #fabionacci series using recursion
# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(5))  # Output: 5 (0, 1, 1, 2, 3, 5)

                                    #trifabonacci series using recursion
# def tri(n):
#     if n == 0:
#         return 0
#     if  n==1 or n==2:
#         return 1
#     return tri(n-1) + tri(n-2) + tri(n-3)
# print(tri(5)) 

                                        #power of two using recursion
# def power_of_two(n):
#     #base case
#     if n<=0:
#         return False             #return False for non-positive numbers
#     if n == 1:
#         return True                ## 1 is 2^0, so it's a power of two
#     if n % 2 != 0:
#         return False                      #return False for odd numbers
#     #recursive case
#     return power_of_two(n//2)
# print(power_of_two(-4))  
 
                                       #power of three using recursion
# def power_of_three(n):
#     #base case
#     if n<=0:
#         return False             #return False for non-positive numbers
#     if n == 1:
#         return True                ## 1 is 3^0, so it's a power of three
#     if n % 2 == 0:
#         return False                      #return False for even numbers
#     #recursive case
#     return power_of_three(n//3)
# print(power_of_three(0))  

                          #gcd using recursion
# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# print(gcd(5,15))  

                           #gcd and lcm using recursion
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# def lcm(a, b):
#     return (a * b) // gcd(a, b)
# print("GCD:", gcd(5, 15))  # Output: GCD: 3
# print("LCM:", lcm(5, 15))  # Output: LCM



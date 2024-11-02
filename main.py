from datetime import datetime, timedelta


current = datetime.now()
print(current)
expri = current + timedelta(minutes=0.5)
print(expri)
b=expri
a=int(input("enter the number"))
print(a)
print(expri)
curr= datetime.now()
print(type(curr))
print(type(b))
if curr <= b:
    print("is success")
else:
    print('its expried')

# a=int(input("enter your number:"))
# for i in range(3):
#     print()
#     for j in range(5):
#         print('*',end=" ")

# for i in range(5):
#     print()
#     for j in range(i):
#         print("2",end=" ")

# for i in range(6):
#     print(" "*(6-i),"*"*(i))

# a=int(input("enter the number"))
# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(a))

# a=int(input("enter the number"))
# def fibo(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0

#     else:
#         return fibo (n-1)+fibo (n-2)
# for i in range(1,a+1):
#     print(fibo(i))

# a = int(input("Enter the number: "))

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# # Generate the Fibonacci sequence
# for i in range(1, a + 1):
#     print(fibo(i))






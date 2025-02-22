for i in range (0,101):
    print(i)


for i in range (0,50):
    while(i%2==0):
        print(i)
        i=+1


num = int(input("enter the number:"))
for i in range (0,21):
    print(f"{num}×{i}={num*i}")

num = int(input("enter a number"))
sum_for = 0
for i in range (1 , num+1):
    sum_for += i
  
    print(f"{sum_for}")


num = int(input("Enter a number: "))
factorial = 1
i = num

while i > 0:
    factorial *= i  
    i -= 1  

print(f"{factorial}")



for i in range (1,101):
    while(i%3==0 and i%5==0):
        print(i)
        i=+1






 
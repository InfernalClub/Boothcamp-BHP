print("Exercise 1")
for number in range(101):
    print(number)
#101 won't count itself as it stops when it gets there hence why it's not 100

print("Exercise 2")
for number in range(2, 501, 2):
    print(number)
#it's a convoluted yet fair way to just count even (pares) numbers

print("Exercise 3")
for number in range(1, 101):
    if number % 10 == 0:
        print("baby")
    elif number % 5 == 0:
        print("ice ice")
    else:
        print(number)
#A simple condition interrupts the count and replaces it for a specific word when its condition is meet, nothing too crazy

print("Exercise 4")
total = 0

for number in range(0, 500001, 2):
    total += number
print(total)
#Just a big sum

print("Exercise 5")
for number in range(2024, 0, -3):
    print(number)
#We just went backwards

print("Exercise 6")
startNum = 3
endNum = 10
multiple = 2

for number in range(startNum, endNum + 1):
    if number % multiple == 0:
        print(number)
#so instead of just making the calculations we set values that change while the count continues, also nothing too crazy
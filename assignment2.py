# 33. Find all indexes of 'p'

s1 = "practice is important to perfectly learn python"

indexes = []

for i in range(len(s1)):
    if s1[i] == 'p':
        indexes.append(i)

print(indexes)

# 34. Count strings length > 2 and palindrome

words = ["aba", "hello", "1991", "aa", "madam"]

count = 0

for word in words:
    if len(word) > 2 and word == word[::-1]:
        count += 1

print("Count:", count)

# 35. Unique words length >=4 starting with w/W

s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife"

result = []

for word in s1.split():
    if len(word) >= 4 and word[0] == 'w' or word[0] == 'W':
        if word not in result:
            result.append(word)

print(result)

# 36. Count frequency of each character

s1 = input("Enter string: ")

d = {}

for ch in s1:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)

# 37. Display costliest product

products = {
    'soap':50,
    'oil':200,
    'laptop':60000,
    'phone':25000,
    'mouse':500
}

costliest = max(products, key=products.get)

print("Costliest product is", costliest)

# 38. Remove specified keys from dictionary

d = {
    'name':'Kelly',
    'age':25,
    'salary':8000,
    'city':'New york'
}

keys_to_remove = ['name','salary']

for key in keys_to_remove:
    d.pop(key)

print(d)


# 39. Countdown using while loop
num = int(input("Enter number: "))

while num >= 0:
    if num == 0:
        print("Blast!")
    else:
        print(num)

    num -= 1

# 40. Grade checker program

print("Welcome to the grade checker program!")

while True:

    marks = float(input("Enter your marks (0-100): "))

    if marks >= 90:
        print("Your grade is A+")
    elif marks >= 80:
        print("Your grade is A")
    elif marks >= 70:
        print("Your grade is B")
    elif marks >= 60:
        print("Your grade is C")
    elif marks >= 50:
        print("Your grade is D")
    else:
        print("Your grade is Fail")

    choice = input("Do you want to check another marks?: ")

    if choice == "no":
        print("Thank you")
        break

# 41. FizzBuzz Program

a = int(input("Enter number: "))

if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")

elif a % 3 == 0:
    print("Fizz")

elif a % 5 == 0:
    print("Buzz")

else:
    print(a)
    
# 42. Password Authentication System

password = "python123"

attempt = 0

while attempt < 3:

    user = input("Enter password: ")

    if user == password:
        print("Access granted")
        break

    else:
        attempt += 1

if attempt == 3:
    print("Access denied")



# 43. Simple Coin Toss Game

import random

print("Welcome to the Simple Coin Toss Game!")

while True:

    guess = input("Guess heads or tails: ")

    while guess != "heads" and guess != "tails":
        print("Invalid choice")
        guess = input("Guess heads or tails: ")

    coin = random.choice(["heads","tails"])

    print("Coin shows:", coin)

    if guess == coin:
        print("You guessed it right!")
    else:
        print("Wrong guess!")

    play = input("Do you want to play again? (yes/no): ")

    if play == "no":
        print("Thanks for playing!")
        break
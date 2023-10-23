# Question 1
import random

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        expected = "BuzzWoof"
    elif num % 3 == 0 and num % 7 == 0:
        expected = "FizzWoof"
    elif num % 5 == 0 and num % 3 == 0:
        expected = "FizzBuzz"
    elif num % 3 == 0:
        expected = "Fizz"
    elif num % 5 == 0:
        expected = "Buzz"
    elif num % 7 == 0:
        expected = "Woof"
    else:
        expected = str(num)
    
    if (num % 2 == 1):
        if random.randint(1,5) == 1:
            print("Computer, enter the next number: ", num)
            if not str(num) == expected:
                print("You win!")
                break
        else:
            print("Computer, enter the next number: ", expected)
    
    else:
        user_input = input("Enter the next number: ")
        if not user_input == expected:
            print("You lose!")
            break

# Question 2
random_number = random.randint(0, 100)
print("I'm thinking of a number between 0 and 100. Can you guess what it is?")
guesses = 0
user_input = -10
while user_input != random_number and guesses < 5:
    user_input = int(input("Enter your guess: "))
    guesses += 1
    if user_input > random_number:
        print("Too high!")
    elif user_input < random_number:
        print("Too low!")
    else:
        print("Correct!")
        print("It took you", guesses, "guesses.")
        break

print("The number was", random_number)
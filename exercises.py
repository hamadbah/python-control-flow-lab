def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is Fun!")

print_greeting()

def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ")
    handle_letter = letter.lower()
    vowels = "aeiou"
    if handle_letter in vowels:
        print(f"The letter {handle_letter} is a vowel")
    else:
        print(f"The letter {handle_letter} is a constant")

check_letter()

def check_voting_eligibility():
    age = int(input("Please enter your age: "))
    if age < 0:
        print("Invalid Input. Age can not be negative number")
        return
    
    voting_age = 18

    if age >= voting_age:
        print(f"You are {age} years old. You are eligible to vote.")
    else:
        print(f"You are {age} years old. You are not eligible to vote.")

check_voting_eligibility()

def calculate_dog_years():
    dog_age = int(input("Input a dog's age: "))
    if dog_age < 0:
        print("Invalid input. Age cannot be negative.")
        return
    if dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = (2 * 10) + (dog_age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")

calculate_dog_years()

                  


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

def weather_advice():
    cold = input("Enter if it is cold (Yes/No): ").lower()
    raining = input("Enter if it is raining (Yes/No): ").lower()

    is_cold = (cold == "yes")
    is_raining = (raining == "yes")
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    elif not is_cold and not is_raining:
        print("Wear light clothing.")
    else:
        print("Invalid Choose try again")
        return

weather_advice()

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    day = int(input("Enter the day of the month: "))

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    season = ""

    if (month == "Dec" and day >= 21) or (month in ["Jan", "Feb"]) or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or (month in ["Apr", "May"]) or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or (month in ["Jul", "Aug"]) or (month == "Sep" and day <= 21):
        season = "Summer"
    elif (month == "Sep" and day >= 22) or (month in ["Oct", "nov"]) or (month == "Dec" and day <= 20):
        season = "Fall"
    else:
        print("Choose a valid day and month") 
        return
    
    print(f"The season of {day} {month} is {season}.")

determine_season()
    
def guess_number():
    target = 42
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == target:
            print("Congratulations, you guessed correctly!")
            return
        elif guess < target and attempt != max_attempts:
            print("Your guess is too low.")
        elif guess > target and attempt != max_attempts:
            print("Your guess is too high.")
        else:
            print("Sorry, you failed to guess the number in five attempts.")

guess_number()
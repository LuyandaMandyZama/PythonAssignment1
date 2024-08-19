#name = input("What is your name?")

#print(f"Hello, {name}!")


#try:
       #age = int(input("How old are you?"))
       #if age < 0:
          # print("Your age cannot be a negative value")
#except ValueError:
    #print("Please enter a whole number")


#location =input("Where are you located?")

#print("Where is your location:")
#location = input()

name = input("What is your name?")

try:
       age = int(input("How old are you?"))
       if age < 0:
          print("Your age cannot be a negative value")
except ValueError:
    print("Please enter a whole number")


location = input("Where are you located?")

print(f"Hello, {name}! You are {age} years old and live in {location}. Welcome! it is nice to meet you.")

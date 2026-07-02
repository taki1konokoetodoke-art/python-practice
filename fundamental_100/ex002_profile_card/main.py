name = input("Enter your name: ")
age = input("Enter your age: ")
food = input("Enter your favorite food: ")

float_age = float(age)
print(f"Hello, my name is {name}.")

if float_age < 20:
    print(f"I am {age} years old, and I am a teenager.")
else:
    print(f"I am {age} years old, and I am an adult.")
    
print(f"My favorite food is {food}.") 
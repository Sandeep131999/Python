try:
    age = int(input("How old are you?"))
except ValueError:
    print("enter a correct input its must be a numeric")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")


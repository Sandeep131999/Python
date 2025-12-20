def canBuyAlcohol (age):
    if type (age) !=int:
        return
    if age>= 18:
        return True

print(canBuyAlcohol(19))

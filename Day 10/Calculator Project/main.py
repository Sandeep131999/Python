import art
def add(n1, n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiplication (n1,n2):
    return n1 * n2

def division (n1,n2):
    return n1/n2

print(art.logo)
n1= float(input("type a first number \n"))
continueFlag = True
while continueFlag:
    operators = {
        "+" : add,
        "-" : subtract,
        "*" : multiplication,
        "/" : division
    }
    for key in operators:
        print (key)
    operator = input("Choose your operator \n")
    n2 = float(input ("type your second number \n "))
    output = operators[operator](n1,n2)
    print(f" {n1} {operator} {n2} = {output} ")
    cont= input("do you want to continue type 'yes' or type 'no' to exit ").lower()
    if cont ==  "no":
        continueFlag = False
    else:
        n1 = output
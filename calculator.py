import math


class Calculator:
    def __init__(x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation


print("welcome to calculaor")
while true:
    print("[1] add")
    print("[2] subtract")
    print("[3] multiply")
    print("[4] modulo")

    operation = int(input("option: "))
    x = int(input("number 1: "))
    y = int(input("number 2: "))


Calculator(x, y, operation)

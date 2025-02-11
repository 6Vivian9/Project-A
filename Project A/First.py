import math

#LEARNING OOP

class piCalc:
    def __init__(self):
        self.dec = 0
    
    def getdec(self):
        self.dec = int(input("Enter the number of decimal places: "))

    def calculate(self):
        print(f"{math.pi:.{self.dec}f}")


if __name__ == "__main__":
    pi = piCalc()
    pi.getdec()
    pi.calculate()
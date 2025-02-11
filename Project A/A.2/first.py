import math

class Nth_Digit:
    def __init__(self):
        self.dec = 0
        
    def calculatepi(self):
        self.pi_len = f"{math.pi:.17f}"
        self.pi_len = len(self.pi_len)

    def inputdigit(self):
        self.dec = int(input("Enter a Number: "))

    def findmatchdigit(self):
        for i in range(self.pi_len):
            formatted_pi = f"{math.pi:.{i+1}f}"
            last_decimal = formatted_pi[-1]
            if last_decimal == str(self.dec):
                print(f"Match found at {i+1}th decimal place")
                break
            
if __name__ == "__main__":
    obj = Nth_Digit()
    obj.inputdigit()
    obj.calculatepi()
    obj.findmatchdigit()
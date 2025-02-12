import string

class prime:
    def __init__(self):
        self.pnum = 0
        self.plist = []
        self.primenumbers = []

    def loop(self):
        for i in range(len(self.plist)):
            if self.plist[i] <= 1:
                continue
            is_prime = True
            for j in range(2, int(self.plist[i]**0.5) + 1):
                if self.plist[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(self.plist[i])

    def getinput(self):
        self.pnum = input("Enter List of Numbers: ")
        self.plist = [int(digit) for digit in self.pnum]
        self.primenumbers = [0] * len(self.plist)

    def main(self):
        prim.getinput()
        prim.loop()

if __name__ == "__main__":
    prim = prime()
    prim.main()
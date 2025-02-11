class fibo:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = 0

    def calculatefibo(self):
        for i in range(self.c):
            if self.a >= self.b:
                self.b = self.a + self.b
                print(self.a)
            else:
                self.a = self.a + self.b
                print(self.b)

    def inputnumber(self):
        self.c = int(input("Enter a Number: "))

    def main(self):
        obj.inputnumber()
        obj.calculatefibo()

if __name__ == "__main__":
    obj = fibo()
    obj.main()
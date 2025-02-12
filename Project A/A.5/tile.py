class tile:
    def __init__(self):
        self.w = 0
        self.h = 0
        self.c = 0
        self.a = 0

    def solve(self):
        self.a = (self.w * self.h)
        print(f"The total cost to cover a {self.w} x {self.h} is ",self.a * self.c)

    def input(self):
        self.w = int(input("Enter Width: "))
        self.h = int(input("Enter Height: "))
        self.c = float(input("Enter Per Unit Cost: "))
        tile.solve()

if __name__ == "__main__":
    tile = tile()
    tile.input()

    
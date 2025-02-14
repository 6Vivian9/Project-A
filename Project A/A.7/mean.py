class mean:
    def __init__(self):
        self.a_list = [4,2,3,5,6,1]
    def find_largest(self):
        for i in range(0, len(self.a_list)):
            if self.a_list[i] > self.a_list[i-1]:
                self.temp = self.a_list[i]
        print(self.temp)

    def reverse_list(self):
        a = -1
        self.temp = [0] * len(self.a_list)
        for i in range(0, len(self.a_list)):
            self.temp[i] = self.a_list[a]
            a = a-1
        print(self.temp)


    def main(self):
        mean.reverse_list()
        


if __name__ == "__main__":
    mean = mean()
    mean.main()
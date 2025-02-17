import random

class slot:
    def __init__(self):
        self.balance = float(10)
        self.bronze = float(2)
        self.silver = float(3.5)
        self.gold = float(5)


    def deposit(self):
        self.balance = float(input("How much would you like to Deposit?"))
        slot.ui()

    def ui(self):
        while True:
            choice = int(input(f"What would you like to do?\n[1] Spin\n[2] Deposit\n[3] Cash out\nCurrent Balance: ${self.balance}\n: "))
            if choice == 1:
                self.spin()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.cashout()
                break
            else:
                print("Invalid Option")

    def cashout(self):
        print("Thanks for playing!")

    def spin(self):
        self.multiplyer = 0.0
        self.bet = float(input(f"How much do you want to bet?\nCurrent Balance: ${self.balance}\n"))
        if self.bet > self.balance:
            print("Not enough Balance!\n\n\n")
            slot.spin()
            return
        
        self.slot_dict = {
            "1": " Gold ",
            "2": "Silver",
            "3": "Bronze",
            "4": "Silver",
            "5": "Bronze",
            "6": "Bronze"
        }

        for i in range (0, 3):           
            self.c1 = random.randint(1, 6)
            self.c2 = random.randint(1, 6)
            self.c3 = random.randint(1, 6)
            if i == 1:
                self.determine()

            print(f"{self.slot_dict[str(self.c1)]} {self.slot_dict[str(self.c2)]} {self.slot_dict[str(self.c3)]}")
        
        if self.multiplyer == 0:
            self.balance = self.balance - self.bet
            print(f"Oh no You Lose! Current balance: {self.balance}\n\n\n")
            slot.ui()
        else:
            self.balance = (self.bet * self.multiplyer)
            print(f"You Win! Current Balance: {self.balance}\n\n\n")
            slot.ui()

    def determine(self):
        if self.slot_dict[str(self.c1)] == "Bronze" and self.slot_dict[str(self.c2)] == "Bronze" and self.slot_dict[str(self.c3)] == "Bronze":
            self.multiplyer = self.bronze
        elif self.slot_dict[str(self.c1)] == "Silver" and self.slot_dict[str(self.c2)] == "Silver" and self.slot_dict[str(self.c3)] == "Silver":
            self.multiplyer = self.silver
        elif self.slot_dict[str(self.c1)] == "Gold" and self.slot_dict[str(self.c2)] == "Gold" and self.slot_dict[str(self.c3)] == "Gold":
            self.multiplyer = self.gold
        else:
            self.multiplyer = 0

    def main(self):
        self.ui()

if __name__ == "__main__":
    slot = slot()
    slot.main()
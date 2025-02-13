class mortgage:
    def __init__(self):
        self.loan = float(input("How much is the loan: "))
        self.rate = float(input("How much is the yearly rate: ")) / 100
        self.year = int(input("How many years?: "))
        mortgage.solve(self)

    def solve(self):
        monthly_rate = self.rate / 12
        num_payments = self.year * 12
        monthly_payment =  (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1) * self.loan 
        annual_payment = monthly_payment * 12
        print(f"The annual payment is: {annual_payment:.2f}")

    #GIVEN UP CANT UNDERSTAND MORTGAGE TOO YOUNG


if __name__ == "__main__":
    mortgage = mortgage()
    mortgage.solve()
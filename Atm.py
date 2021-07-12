class Atm:
    def __init__(self,atm_card_number,pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
    def CashWithDrawl(self):
        print("CashWithDrawl")
    def BalanceEnquiry(Self):
        print("BalanceEquiry")
audi = Atm("6470246","8994402")
audi.CashWithDrawl()
audi.BalanceEnquiry()
    

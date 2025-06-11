from customerclass import *



class Account:
    def __init__(self,customer,number):
        self.customer = customer
        self.number = number

    def addmoney(self,amount):
        self.customer.acc +=amount
        return self.customer.acc


    def withdrewmoney(self,amount):
        self.customer.acc -= amount
        return self.customer.acc
    def benifits(self,rate):
        return self.customer.acc*rate
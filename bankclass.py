from accountclass import *



customer1=Customer("ahmed","<24545445>",1000)
account1=Account(customer1,1001)
customer2=Customer('ali',"<3256412>",50000)
account2=Account(customer2,1002)
customer3=Customer('heba',"<56454>",10000)
account3=Account(customer2,1003)


print(f"{account1.customer.name} balance after deposit {account1.addmoney(500)}")
print(f"{account1.customer.name} balance after withdrew {account1.withdrewmoney(500)}")
print(f"{account1.customer.name} balance after deposit {account1.customer.acc+account1.benifits(.1)}")


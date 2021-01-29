from prettytable import  PrettyTable
money=eval(input("enter money:"))
month=eval(input("enter month:"))
print("interest rate=5.75% per year")
x = PrettyTable(["Month", "Money", "Earn", ])
earn=0
for i in range(0,month+1):
    x.add_row([i,format(money,"5.2f"),format(earn,"5.2f")])
    money = money * (1 + 0.0575 / 12)
    earn=earn+money*0.0575/12
print(x)
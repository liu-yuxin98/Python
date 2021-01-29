from chapter7 import Loan as L
def main():
    # enter yearly interest rate
    annualInterestRate=eval(input("enter yearly interest rate, eg. 7.25:"))
    #enter number of years
    numberOfYears=eval(input("enter number of years as an integer:"))
    #enter loan amount
    loanAmount=eval(input("enter loan amount,eg. 1000.97"))
    #enter a borrower
    borrower=input("enter a borrower's name:")
    #create a loan object
    loan1=L.Loan(annualInterestRate,numberOfYears,loanAmount,borrower)
    #dispaly loan date, monthly payment, total payment
    print("the loan is for",loan1.getBorrower())
    print("the monthly payment:",format(loan1.getMonthlyPayment(),".2f"))
    print("the total payment is:",format(loan1.getTotalPayment(),".2f"))

main()

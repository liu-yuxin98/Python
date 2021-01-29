import math
class Loan:
    def __init__(self,annualInterestRate=2.5,numberOfYears=1,loanAmount=1000,borrower=""):
        self.__annualInterestRate=annualInterestRate
        self.__numberOfYears=numberOfYears
        self.__loanAmount=loanAmount
        self.__borrower=borrower
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def getNumberOfYears(self):
        return self.__numberOfYears
    def getLoanAmount(self):
        return self.__loanAmount
    def getBorrower(self):
        return self.__borrower
    def setAnnualInterestRate(self,annualIR):
        self.__annualInterestRate=annualIR
    def setLoanAmount(self,loanA):
        self.__loanAmount=loanA
    def setNumberOfYears(self,numberY):
        self.__numberOfYears=numberY
    def setBorrower(self,b):
        self.__borrower=b
    def getMonthlyPayment(self):
        totalPayment=math.pow(1+(self.__annualInterestRate/100),self.getNumberOfYears())\
                     *self.__loanAmount
        monthlypayment=totalPayment/(self.__numberOfYears*12)
        return monthlypayment

    def getTotalPayment(self):
        return math.pow(1+(self.__annualInterestRate/100),self.getNumberOfYears())\
                     *self.__loanAmount

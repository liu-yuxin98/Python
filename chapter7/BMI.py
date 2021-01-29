import math
class BMI:
    def __init__(self,name="",age=1,weight=0,height=50):
        self.__name=name
        self.__age=age
        self.__weight=weight
        self.__height=height
    def getBMI(self):
        k_p_p=0.45359237
        m_p_i=0.0254
        bmi=self.__weight*k_p_p/\
            math.pow((self.__height*m_p_i),2)
        bmi=round(bmi*100)/100
        return bmi
    def getStatus(self):
        bmi=self.getBMI()
        if bmi<18.5:
            return "Underweight"
        elif bmi<25:
            return "Normal"
        else:
            return "Obsese"
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height
    def getResult(self):
        print(self.__name,end=" ")
        print("is",self.__age,"years old")
        print("height is",self.__height,"weight is",self.__weight)
        print("BMI is",self.getBMI())
        print(self.getStatus())

'''
#test
b1=BMI("james",18,145,70)
b1.getResult()
'''

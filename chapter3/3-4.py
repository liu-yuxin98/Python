
totalAmount=eval(input("enter a number"))
totalAmount*=100
Dollar=totalAmount//100
Quarter=(totalAmount%100)//25
Dim=((totalAmount%100)-25*Quarter)//10
Cent5=(((totalAmount%100)-25*Quarter)-10*Dim)//5
Cent=(((totalAmount%100)-25*Quarter)-10*Dim)-5*Cent5
print("{} dollar,{} quarter,{} dim,{}Cent5,{} cent".format\
          (Dollar, Quarter, Dim,Cent5,Cent ))
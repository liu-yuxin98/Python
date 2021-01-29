# -*- coding: utf-8 -*-
# 2020-02-01
# author Liu,Yuxin
import random
cardList=[ x for x in range(53)]
print(cardList)
kind=['梅花','方片','红桃','黑桃']
rank=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
random.shuffle(cardList)
for i in range(5):
    kind2=kind[cardList[i]//13]
    rank2=rank[cardList[i]%13]
    print(kind2," ",rank2)


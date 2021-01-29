class TV:
    def __init__(self):
        self.chanel=0 #default channel
        self.volumn=0
        self.on=False
    def setChannel(self,channel):
        self.chanel=channel
    def setVolumn(self,volumn):
        self.volumn=volumn
    def turnon(self):
        self.on=True
    def turnoff(self):
        self.on=False
    def channelup(self):
        self.chanel+=1
    def channeldown(self):
        self.chanel-=1
    def volumnup(self):
        self.volumn+=1
    def volumndown(self):
        self.volumn-=1

t1=TV()
t1.setVolumn(12)
t1.volumnup()
print(t1.volumn)


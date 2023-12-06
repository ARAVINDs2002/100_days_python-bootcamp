class Robot:
    def __init__(self,name,color,age):
        self.name=name
        self.color=color
        self.age=age
    def sayhi(self):
        print("hi i am a robot and name is"+self.name)
        print("hi i am a robot and color is"+self.color)
        print("hi i am a robot and age is"+str(self.age))
r1=Robot("robo1","whiteish_grey",12) 
r2=Robot("robo2","whiteish_blue",130) 
r1.sayhi()    
r2.sayhi()    
        
        
        
        
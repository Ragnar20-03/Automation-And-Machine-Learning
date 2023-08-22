

class Demo :
    value = 0 

    def __init__(self , A , B ):
        self.No1 = A 
        self.No2 = B

    def fun(self):
        print("inside Fun")
        print("Self : " , self)
        print("No1 is : " , self.No1)
        print("No2 is : " , self.No2)
        print("Value  : " , self.value)

    def gun(self):
        print("inside gun")
        print("Self : " , self)
        print("No1 is : " , self.No1)
        print("No2 is : " , self.No2)
        print("Value  : " , self.value)
    


def main() : 
    obj1 = Demo(11 , 21 )
    obj2 = Demo(31 , 51 )

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()

if __name__== "__main__":
    main()
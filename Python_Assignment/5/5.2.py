class Circle : 

    def __init__(self ):
        self.r = 0.0
        self.py = 3.14
        self.area = 0
    
    def Accept(self , radius):
        self.r = radius 
    
    def CalculateArea(self):
        self.area =  2 * self.r * self.py * self.py

    def Display(self):
        print("Area is : " , self.area)



def main():
    obj1 = Circle()
    No = int(input("Enter radius\n"))
    obj1.Accept(No)
    obj1.CalculateArea()
    obj1.Display()

if __name__ == "__main__":
    main()
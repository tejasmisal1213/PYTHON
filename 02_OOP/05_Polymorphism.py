print(5 + 5)
print("Tejas" + "Misal")

# complex num Addition

class Complex:
    def __init__(self, real,img):
        self.real = real
        self.img = img

    def showNo(self):
        print(self.real,"T +", self.img,"S")

    def __add__(self,num2):
        newReal = self.real  + n2.real 
        newImg = self.img + n2.img
        return Complex(newReal , newImg)


n1= Complex(10,10)
n1.showNo()

n2= Complex(2,3)
n2.showNo()

n3 = n1 + n2
n3.showNo()


    

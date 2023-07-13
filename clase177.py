from tkinter import*
root=Tk()
root.geometry("500x500")
root.config(bg="lightblue")



class clase:
    def __init__(self,fruit_name,quantity):
        self.fruit= fruit_name
        self.quantity=int(quantity)
        self.var1 = 200
        
    def b(self):
        var2=self.quantity*self.var1
        print(var2)
        if (self.fruit=="Manzana"):
            var3=self.quantity*52
        elif(self.fruit=="Naranja"):
            var3=self.quantity*60
        elif(self.fruit=="Mango"):
            var3=self.quantity*60
            
        print(self.fruit +"  " +  str(self.quantity) +"  " +  str(var3))
        
    def getCost(self):
            self.b()
        
        
def c():
    fruit = "Manzana"
    quantity = 200
    obj1=clase(fruit,quantity)
    obj1.getCost()
    
button_1=Button(root,text="calcular cosas",command=c)
button_1.place(relx=0.5,rely=0.5,anchor=CENTER)

    

root.mainloop()
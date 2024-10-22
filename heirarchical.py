class Parent1:
    def func_1(self):
        print("This function is defined inside the parent class.")

class Child_1(Parent1):
    def func_2(self):
        print("This function is defined inside the child 1.")

class Child_2(Parent1):
    def func_3(self):
        print("This function is defined inside the child 2.")

object1 = Child_1()
object2 = Child_2()

object1.func_1()  
object1.func_2()  

object2.func_1()  
object2.func_3()    

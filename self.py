#python Program
#Rishikesh 

 
class PrepInsta:
    def __init__(self,name):
        self.name=name 
        #print(‘You are in Parent class’)
    def display(self):
        print(self.name)
        print(‘U are in Display Function ‘)
ob1=PrepInsta(‘rishikesh’) ##object 
ob1.display()

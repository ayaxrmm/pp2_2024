'''Define a class which has at least two methods: getString: 
to get a string from console input printString: to print 
the string in upper case.

'''
class myClass:
    def __init__(self) :
        self.inputstr = ""
    def getstring(self) :
        self.inputstr = input("enter: ")
    def printstring(self) :
        print(self.inputstr.upper())
myClass = myClass()
myClass.getstring()
myClass.printstring()


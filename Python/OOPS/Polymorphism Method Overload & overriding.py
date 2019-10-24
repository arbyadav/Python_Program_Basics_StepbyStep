class pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class Myeditors :

    def execute(self):
        print("Spell Check")
        print("Conversation Check")
        print("Compiling")
        print("Running")

class laptop:
    
    def code(self,ide):
        ide.execute()
        
p1=Myeditors()
l1=laptop()
l1.code(p1)



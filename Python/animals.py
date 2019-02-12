class Dog:
    def __init__(self, name):
        self.name = name


    def bark(self):
        print("Woof!")


    def eat(self,food):
        if food == "bacon":
            print("The bacon kind!")
        else:
            print("NOOOOOOOOOOOOOOOOOOOO")
    # 
    # def learn_name(self, name):
    #     self.name = name


    def hear(self, string):
        if self.name in string:
            self.bark()

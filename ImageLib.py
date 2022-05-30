




class JORzTemplate():
    # Define a class object attribute, it will be the same for any instance of the class
    pi = 3.142

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, parameter1):
        # Create attributes and set initial values
        self.parameter1 = parameter1

    # Methods
    def run(self, numberz):
        print(self.parameter1, numberz * JORzTemplate.pi)

    @staticmethod
    def jorz_static_method():
        print("Yoo Hoo")


message = "Cad é mar atá tú, ar domhan?"
myTemplate = JORzTemplate(parameter1=message)
myTemplate.run(1)
print(myTemplate.pi)
myTemplate.jorz_static_method()



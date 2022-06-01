'''
Class Template by JOR
'''


# By convention, use camel case to name classes
class JORzAbstractClass():
    # Define a class object attribute, it will be the same for any instance of the class
    pi = 3.142

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, parameter1):
        print("Running constructor for Template")


class JORzTemplate(JORzAbstractClass):
    # Define a class object attribute, it will be the same for any instance of the class
    pi = 3.142

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, parameter1):
        print("Running constructor for Template")
        # Create attributes and set initial values
        self.debug = False
        self.parameter1 = parameter1
        self.test_message = ""

    # Methods
    def jorz_do_stuff1(self, numberz):
        if self.debug:
            print("Executing the jorz_do_stuff1 method of template class")
            print(f"This method was passed {self.parameter1} as a tag for the object" )

    def jorz_do_stuff2(self):
        if self.debug == True:
            print("Executing the jorz_do_stuff2 method of template class")
            print(f"test_message was set to {self.parameter1}" )

    @staticmethod
    def jorz_static_method():
        print("Executing the jorz_do_stuff1 method of template class")
        print(f"Class variable is {JORzTemplate.pi}")





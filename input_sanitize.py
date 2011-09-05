import string

##Designed for use in prevention of code injection and for keeping assorted inputs clean... a test prompt is at the bottom##
valid_chars = string.ascii_letters + string.digits

class sanitized_string(str):
    """This will sanitize a string for use and prevention of code injection."""
    def __init__(self, inval):
        self.string = ''
        for character in inval:
            if character in valid_chars or character == ' ':
                print character
                if character == ' ':
                    self.string += '-'
                else:
                    self.string += character
                    
    def returnvalue(self):
        return self.string
    def printVal(self):
        print self.string

def string_prompt():
    question = raw_input("Please enter a string you wish to use: ")
    answer = sanitized_string(question)
    answer.printVal()

string_prompt()


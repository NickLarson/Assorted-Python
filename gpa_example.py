import fileinput

##What to write for today....
##Put the classes on the odd lines and grades
##Too lazy to make it work for + and - so far... only doing solid A, B, C, D, F

class gpa():
    def __init__(self, string):
        test_file = open(string)
        self.classes = {}
        self.grades = {}
        self.gpa = 0
        self.letters = ['a', 'b', 'c', 'd', 'f'] ##The implementation in python is still fast to search for runtime
        self.points = {1: 4, 2: 3, 3: 2, 4: 1, 5: 0} ##You can add corresponding ones...
                                                     ##might add functionality later
        count = 1
        for line in fileinput.input(string):
            if fileinput.lineno()%2 == 0:
                self.grades[count] = line.strip('\n')
                count += 1
            else:
                self.classes[count] = line.strip('\n')
    def printGPA(self):
        location = 0
        for row in self.grades:
            location = self.letters.index(self.grades[row].lower())+1 ##Dictionaries index from a different start value
            self.gpa += self.points[location]
        print self.gpa/len(self.classes) ##The calculation for now..
    def printClasses(self):
        print self.classes
    def printGrades(self):
        print self.grades

test = gpa('test.txt')
test.printGrades()
test.printGPA()



                


##We're going to do a more robust recipe book with a different implementation##
##Had about 45 minutes or so... nothing big but I tried!##

class recipe_book():
    def __init__(self, rec, rat, knd):
        self.recipe = []    ##Parallel lists work out with good efficiency
        self.rating = []    ##Because python's underlying implementation uses
        self.kind = []      ##Fast member algorithms for lists
        ##Read the variables into the lists if the types are correct##
        ##Then go ahead and put each from the list into the respective lists##
        if type(rec) == list and type(rat) == list and type(knd) == list:
        ##We don't want empty lists either##
            if len(rec) > 0 and len(rat) > 0 and len(knd) > 0:
                for each in rec:
                    if type(each) == str:
                        self.recipe.append(each)
                for each in rat:
                    if type(each) == int:
                        self.rating.append(each)
                for each in knd:
                    if type(each) == str:
                        self.kind.append(each)
    def addRecipe(self, new_recipe, new_rating, new_kind):
        if type(new_recipe) == str and type(new_rating) == int and type(new_kind) == str:
        ##After you check the type correctness, make sure to insert into the list##
            self.recipe.append(new_recipe)
            self.rating.append(new_rating)
            self.kind.append(new_kind)
        else:
            print "Enter a valid set of entries"
    def printRecipes(self):
        for each in self.recipe:
            print each
    def printRated(self, whatrating):
        location = 0                ##Start at index 0, where python starts lists
        while location <= len(self.rating)-1: ##Compensate that length doesn't index from 0
            if whatrating == self.rating[location]:
                print self.recipe[location]
            location += 1
    def printKind(self, whatkind):
        location = 0                ##Start at index 0, where python starts lists
        while location <= len(self.kind)-1: ##Compensate that length doesn't index from 0
            if whatkind == self.kind[location]:
                print self.recipe[location]
            location += 1
    
##I don't like putting test code in the same file, but for ease of use I might as well##
foods = ["Cookie", "Pizza", "Hamburger"]
ratings = [5, 4, 5]
types = ["Sweets", "Supper", "Supper"]
book = recipe_book(foods, ratings, types)
print "Alright, lets see the book"
book.printRecipes()
book.addRecipe("Chicken", 1, "Lunch")
book.addRecipe("Brownies", 1, "Sweets")
book.addRecipe("Cake", 5, "Sweets")
print "\n\nWe added a few new recipes... lets see it now"
book.printRecipes()
print "\n\nI want some all star recipes... lets get all the 5 rated things!"
book.printRated(5)
print "\n\nNow lets get the sweets out of here... I have a sweet tooth!"
book.printKind("Sweets")
                
            
        

class recipe_pair():
    """This will form a recipe pair.  More functionality to come!"""
    def __init__(self, recipe, rating):
        if type(rating) != int:
            print "Malformed rating, not an integer!"
            return
        if type(recipe) != str:
            print "Malformed recipe, not a name or string!"
        else:
            self.food = recipe
            self.rate = rating
    def get_food(self):
        return self.food
    def get_rating(self):
        return self.rate      
    


            


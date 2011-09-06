import recipe_pair

class recipe_book(dict):
    """This will be a dictionary or book of recipe pairs. More functionality to come!"""
    def __init__(self, recipe):
        self.book = {}
        self.entry = []
        self.size = 0
        ##Todo: Properly formed recipe.
        self.entry += recipe.get_food(), recipe.get_rating()
        self.book[self.size+1] = self.entry
        ++self.size
    def __getitem__(self, index):
        return self.book[index]
    def __setitem__(self, index, recipe):
        if not book.has_key(index):
            self.book[index] = [recipe.get_food(), recipe.get_rating()]
    def printBook(self):
        print self.book

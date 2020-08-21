from Chef import Chef

class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken") # This is included to override the same dish in the Chef.py file.

    def make_fried_rice(self):
        print("The chef makes fried rice")

#Inheritance Can be used instead of copy and pasting functions from Chef.py into here.
# This allows for existing fuctionality to be inherited from a different class into this one with out having to write it out.

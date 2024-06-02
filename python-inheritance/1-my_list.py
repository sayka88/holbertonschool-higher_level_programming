class MyList(list):
    """Class MyList inherits from list with a method to print sorted list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        if self:
            sorted_list = sorted(self)
            print(sorted_list)
        else:
            print("The list is empty.")

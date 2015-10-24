'''
Created on Oct 24, 2015

@author: dbrady
'''
from collections import UserDict
from io import StringIO
from contextlib import redirect_stdout
 
class OrderDict(UserDict):
   
    def __init__(self, key = "", value = ""):
        super().__init__
        self.data = {}
        self.order = {} # Dictionary to track order in which entries are added to the dictionary
        self.count = 0
        self.flag = True
        self._iterData = None
        self.iterFlag = True
        
    def __setitem__(self, key, value):
        # A dicitionary is an iterable so we can check to see if the key is already in the data dictionary
        if key not in self:
            # Increment count every time a new value that does not already exist is added
            self.order[self.count] = key
            self.count += 1
        # Either one of the following two lines will work to add the dictionary entry to the data attribute.
        #super(Odict, self).__setitem__(key, value)
        super().__setitem__(key, value)
       
    def __iter__(self):
        return iter(self.data)
   
    def __next__(self):
        if self._iterData == None:
            self._iterData = iter(self)
        try:
            nextEl = next(self._iterData)
            yield self.data[nextEl]
        except StopIteration:
            self._iterData = None
            self.iterFlag = False
           
    def __orderItems(self):
        ''' Returns a sorted view of items in the self.order dictionary using count stored in the key field
            The items() function on a dictionary returns a list of tuples consisting of the key and value
            pairs in the dictionary. The k[0] refers to the key (i.e. count) stored in the order dictionary
            to sort the dictionary.'''
        return sorted(self.order.items(), key = lambda k: k[0])
 
    def __str__(self):
        ''' Override the print function by defining the __str__ method. This __str__ method returns the
            dictionary in the order entries were added to the "data" dictionary.'''
        odItems = self.__orderItems()
        buf = StringIO()
        with redirect_stdout(buf):
            if self.flag:
                print("\nSorted view of Odict object's dictionary based on order of entry:\n")
                for c, k in odItems:
                    print("Order #: {0} \t Key: {1} \t Value: {2}".format(c, k, self[k]))
            else:
                print(self.items())
        return(buf.getvalue())

def main():
    # Some test code  
    od = OrderDict()
    # Don't need to refer to od.data as the dictionary because the "data" attribute is automatically
    # made available by Python as a List or Dictionary as defined within the __init__ function.
    # At least I think that’s the case…it works anyway.
    od["holidays"] = ["Presidents Day", "Easter", "4th of July", "Labor Day"]
    od["name"] = "Dave Brady"
    od["nums"] = [1, 2, 3]
    od[10] = 10
    od[1] = "One"
    od["mon"] = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    od["ten"] = 10
       
    od.flag = True # Flag which is used by __str__ to print a more detailed version of Odict
    print(od)  # Print command will invoke the Odict.__str__ function because it was over-ridden in the class.
       
    while od.iterFlag:
        # next() will invoke the __next__() method in the Odict class (22 Oct 15)
        el = next(od)
        # Using genObj as the variable because a generator object is returned due to use of the yield keyword in next() (22 Oct 15)
        for genObj in el:
            print(genObj)     
     
if __name__ == "__main__":
    main()
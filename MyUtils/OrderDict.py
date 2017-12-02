'''
Created on Oct 24, 2015

Updated on 16 January 2016

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
        # A dictionary is an iterable so we can check to see if the key is already in the data dictionary
        if key not in self:
            # Increment count every time a new value that does not already exist is added
            self.order[self.count] = key
            self.count += 1
        # Either one of the following two lines will work to add the dictionary entry to the data attribute.
        super(OrderDict, self).__setitem__(key, value)
        #super().__setitem__(key, value)
       
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
    
    def getItems(self):
        # Public method to retrieve items in order...does the exact same thing as __orderItems()
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

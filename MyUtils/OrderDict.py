'''
Created on Oct 24, 2015

Updated on 2 December 2017

@author: dbrady
'''
from collections import UserDict
from io import StringIO
from contextlib import redirect_stdout
 
class OrderDict(UserDict):
   
    def __init__(self, key = "", value = ""):
        super().__init__
        # The data attribute is inherited from UserDict (djb - 2 Dec 17)
        self.data = {}
        self.count = 0
        self.flag = True
        self._iterData = None
        self.iterFlag = True
        if (len(key) > 0 and len(value) > 0):
            self[key] = value

    def __setitem__(self, key, value):
        # Either one of the following two lines will work to add the dictionary entry to the data attribute.
        #super(OrderDict, self).__setitem__((self.count, key), value)
        super().__setitem__((self.count, key), value)
        # A dictionary is an iterable so we can check to see if the key is already in the data dictionary
        if key not in self:
            # Increment count every time a new value that does not already exist is added
            self.count += 1

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
        ''' Returns a sorted view of items in the self.order dictionary based on the order elements were added to the dictionary.
            Each key is a tuple consisting of the order a value was added (i.e. count) and the provided key (djb - 2 Dec 17)'''
        return sorted(self.data.items(), key = lambda k : k[0][0])
    
    def getItems(self):
        # Public method to retrieve items in order...does the exact same thing as __orderItems()
        return sorted(self.data.items(), key=lambda k: k[0][0])
    

    def __str__(self):
        # Override the print function by defining the __str__ method. This __str__ method returns the
        #    dictionary in the order entries were added to the "data" dictionary.
        odItems = self.__orderItems()
        buf = StringIO()
        with redirect_stdout(buf):
            if self.flag:
                print("\nSorted view of Odict object's dictionary based on order of entry:\n")
                for k, v in odItems:
                    print("Order #: {0} \t Key: {1} \t Value: {2}".format(k[0], k[1], v))
            else:
                print(self.items())
        return(buf.getvalue())

from MyUtils import *

def main():
    # Some test code  
    od = OrderDict.OrderDict()
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
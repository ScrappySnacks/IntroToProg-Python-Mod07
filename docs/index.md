# Assignment07:  A "pickled" Latin dictionary with exception handling
**Dev:** *T. Ward*   
**Date:** *12.1.2020*

## Introduction 
For assignment #7, we are to create a demo that demonstrates how pickling and structured error handling work.  To accomplish this, I have created a “pickled” Latin dictionary demo that also includes exception handling code.  This website will describe the steps taken to create the demo and ensure it works as expected.  As with past assignments PyCharm is used here for script development.

## Resources
Before script development commenced, internet research was performed on pickling and exception handling resources.   I found that the same sources had very helpful instructional material on both topics.  These sources are listed below along with reasoning for their recommendation: 

### Helpful Pickling Resources
(1) https://www.datacamp.com/community/tutorials/pickle-python-tutorial: In addition to containing well-written instructional material, Datacamp provides an opportunity for additional practice.  This site was the most helpful to the pickling portion of demo development.
(2) https://realpython.com/python-pickle-module/: This external resource puts pickling in a larger context and introduces concepts that were not introduced thus far in the course (e.g., serialization and deserialization).
(3) https://docs.python.org/2/library/pickle.html: This website succinctly covers important concepts on pickling.

### Helpful Exception Handling Resources
(1) https://www.datacamp.com/community/tutorials/exception-handling-python: This well-written site introduces basic concepts and additional opportunities for practice.
(2) https://realpython.com/lessons/introduction-exceptions/: This site has a 101 class on exceptions that was very well done and easy to understand.
(3) https://docs.python.org/3/tutorial/errors.html: This site was the most helpful to the exception handling portion of demo development. 

## Demo Development
The “pickled” Latin dictionary program takes three existing dictionaries with English to Latin translation (Latin colors, Latin Animals, Latin Objects), pickles them and writes them to file.  The user can also recall the dictionaries from file (i.e., “unpickling”).  In addition to pickling, the program also handles three exceptions through existing exception classes and one custom created class. The remainder of this webpage describes the functionality of the code organized by Separation of Concerns.  The detailed python script can be found in Appendix A.

## Summary

## Appendix A - Python code


```
#-------------------------------------------------#
# Title: A "pickled" Latin dictionary
# Description: Demonstrates pickling and exception handling in one script
# ChangeLog: N/A, Rev New
# T. Ward Dev, 12/01/2020 , created script
#-------------------------------------------------#
# Pickle resources: See demo write-up for more information
# https://www.datacamp.com/community/tutorials/pickle-python-tutorial
# https://realpython.com/python-pickle-module/
# https://docs.python.org/2/library/pickle.html

# Exception handling resources: See demo write-up for more information
# https://www.datacamp.com/community/tutorials/exception-handling-python
# https://docs.python.org/3/tutorial/errors.html
# https://realpython.com/lessons/introduction-exceptions/

#--- Import pickle module --- #
import pickle

#--- Declare variables and custom classes --- #

lstTable = []

class NotValidChoice(Exception): # Custom exception class for reminding the user that there are only 3 choices.
    def __str__(self):
        return 'Please enter a valid option: 1, 2 or 3' + "\n"

# -- Define data dictionaries -- #

LatColors = {"red":"rebrum", "orange":"aurantiaco", "yellow":"flavo","green": "viridi", "blue":"caeruleum",
             "purple": "purpura"}

LatAnimals = {"bird":"avem", "dog":"canis", "cat":"cattus", "horse":"equus", "snake":"anguis", "chicken":"pullum",
              "pig":"porcus"}

LatObjects = {"bed": "lectulo", "lamp":"lucerna", "bread":"panem", "wine":"vinum", "chair":"sella", "flower": "flos",
              "pot":"ollam", "water":"aqua"}

# -- Processing -- #
def PickleToFile(dic1,dic2,dic3, filename):  # This function opens the file pickles the data dictionaries to file.
    # If the file does not exist, this function will create it.
    outfile = open(filename,'wb')
    pickle.dump(dic1,outfile)
    pickle.dump(dic2,outfile)
    pickle.dump(dic3,outfile)
    outfile.close()

def UnpickleFromFile(r1, r2, r3, filename): # This function unpickles the data dictionaries to file.
    infile = open(filename, "rb")
    r1 = pickle.load(infile)
    r2 = pickle.load(infile)
    r3 = pickle.load(infile)
    infile.close()
    return r1, r2, r3

# -- Presentation (I/O) -- #
def PrintDataFromFile(r1,r2, r3):  # This function unpacks displays data in a more appealing way.
    lstTable = [r1, r2, r3]
    print("English word = Latin equivalent:")
    i = 0  # Declare local variable
    while i < int(len(lstTable)):
        for english, latin in lstTable[i].items():
            print(english, "=", latin)
        i += 1

# -- Main Script Body -- #
while True:  # This while loop contains if / then to run functions base on selection and includes error handling and
    # raising a custom exception class, if the user tries to enter a choice other than 1, 2 or 3.
    try:
        intChoice = int(input("\n"+ "Please choose action: 1 = pickle, 2 = unpickle, 3 = exit: "+ "\n"))
        if intChoice == 1:
            filename = str(input("Please enter the file name for storing the dictionary: " + "\n")).lower()
            print("Now pickling the following dictionary: " + "\n")
            PrintDataFromFile(LatColors, LatAnimals, LatObjects)
            PickleToFile(LatColors, LatAnimals, LatObjects, filename.strip())
        elif intChoice == 2:
            filename = str(input("Please enter the file name for accessing the dictionary: " + "\n")).lower()
            UnpickleFromFile(LatColors, LatAnimals, LatObjects, filename.strip())
            print("File found!  Now printing dictionary: ")
            PrintDataFromFile(LatColors, LatAnimals, LatObjects)
        elif intChoice == 3:
            break  # and exit the program
        else:
            raise NotValidChoice()
    except ValueError as e:
        print("That was not a number! Try again.")
        print("The built-in Python error message is: ")
        print(e, "\n")
    except FileNotFoundError as e:
        print("That file was not found. Try again.")
        print("The built-in Python error message is: ")
        print(e, "\n")
    except Exception as e:
        print("The built-in Python error message is: ")
        print(e, "\n")
```

![add txt] (/docs/Figure1.png "tool tip")
#### Figure 1: 

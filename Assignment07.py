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

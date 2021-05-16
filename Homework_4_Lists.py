"""
Homework Assignment #4: Lists

Details:

Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.

Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""

myUniqueList = []
myUniqueListTitle = " The Unique list is "

myLeftovers = []
myLeftoversTitle = " The LeftOvers list is "

inputList = ["Song", "Artist", "Genre", "Title", "Lyrics"]
inputListTitle = "Inject the following items to myUniqueList: Song, Artist, Genre, Title, Lyrics"


# Inject a few items to myUniqueList
def injectMyUniqueList():
    for inputinlist in inputList:
        if inputinlist not in myUniqueList:
            myUniqueList.append(inputinlist)


# If unique append to myUniqueList
def appendMyUniqueList(element):
    if element in myUniqueList:
        appendMyLeftOversList(element)
        return False

    else:
        myUniqueList.append(element)
        return True


# Append non unique items to myLeftovers
def appendMyLeftOversList(element):
    myLeftovers.append(element)


if __name__ == '__main__':
    # Call injectMyUniqueList function
    injectMyUniqueList()
    print(f"{inputListTitle.center(50, '#')}")
    print(f"{myUniqueList}")
    print('---------------------------\n')

    # Validate injectMyUniqueList function
    print(f"Adding unique item to the list: Youtube")
    print(appendMyUniqueList("Youtube"))
    print(f"{myUniqueListTitle.center(50, '#')}")
    print(f"{myUniqueList}\n")
    print(f"{myLeftoversTitle.center(50, '#')}")
    print(f"{myLeftovers}")
    print('---------------------------\n')

    # Validate appendMyLeftOversList function
    print(f"Adding repeated item to the list: Artist")
    print(appendMyUniqueList("Artist"))
    print(f"{myUniqueListTitle.center(50, '#')}")
    print(f"{myUniqueList}\n")
    print(f"{myLeftoversTitle.center(50, '#')}")
    print(f"{myLeftovers}")
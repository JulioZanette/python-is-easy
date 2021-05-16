"""
Homework Assignment #2: Functions

Details:
Let's return to the music example from assignment one. Pick 3 of the attributes you listed. For our example we're going to say "Genre", "Artist" and "Year". Create a new Python file and create 3 functions with the same name as those attributes. So in this example we'd have one function named "genre" another named "artist" and another called "year".
When someone calls any of those functions, that function should return the corresponding value for that attribute. For example, if we call the "Artist" function our function would return "Dave Brubeck". Yours should return whatever values make sense for your music choice.


Extra Credit:
One of the data types we haven't covered yet is called "booleans". When a variable is set to True or False, that's a boolean. For extra credit, see if you can figure out how to use booleans, and add an extra function that returns a boolean value instead of a String or Number. Hint: make sure to capitalize the first letter in the words True or False when you use them. We'll cover booleans more in the lecture on "if" statements coming up next in the course.
"""

import time


def Song():
    Song = "Oceans (Where Feet May Fail)"
    print(f"{Song.center(50, '#')}")
    return


def Lyrics():
    Lyrics = "https://www.letras.mus.br/hillsong-united/oceans-where-feet-may-fail/"
    print(f"You can find the Lyrics at {Lyrics}")
    return


def Youtube():
    Youtube = "https://youtu.be/1m_sWJQm2fs"
    print(f"Or watch at {Youtube}")
    return


def DurationInMinutes():
    DurationInSeconds = 350
    ty_res = time.gmtime(DurationInSeconds)
    DurationInMinutes = time.strftime("%M:%S", ty_res)
    print("Is this a Long Song?")
    print(DurationInMinutes)
    return


# This is the Best ever song in the whole World
Song()
Lyrics()
Youtube()
DurationInMinutes()

"""
Homework Assignment #3: "If" Statements

Details:
Create a function that accepts 3 parameters and checks for equality between any two of them.
Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.

Extra Credit:
Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you convert strings to Integers.
"""

Song = "Oceans (Where Feet May Fail)"
Artist = "Hilsong United"
Lyrics = "https://www.letras.mus.br/hillsong-united/oceans-where-feet-may-fail/"
Youtube = "https://youtu.be/1m_sWJQm2fs"

option1 = input("Enter a letter a or b: a = Song | b = Artist \n")
option2 = int(input("Enter a number 1 or 2: 1 = Lyric | 2 = Youtube \n"))


def BestSong(option1, option2):
    if option1 == "a" and option2 == 1:
        return f"\nThe best Song in the whole World is \"{Song}\"\nThe best Artist in the whole World is \"{Lyrics}\""

    elif option1 == "b" and option2 == 1:
        return f"\nThe best Artist in the whole World is \"{Song}\"\nThe best song in the whole World is \"{Youtube}\""

    elif option1 == "a" and option2 == 2:
        return f"\nThe best Song in the whole World is \"{Artist}\"\nThe best Artist in the whole World is \"{Lyrics}\""

    elif option1 == "b" and option2 == 2:
        return f"\nThe best Artist in the whole World is \"{Artist}\"\nThe best song in the whole World is \"{Youtube}\""

    else:
        return "You need to pick a combination from:  [a and 1], [a and 2], [b and 1] or [b and 2]"


if __name__ == '__main__':
    print(BestSong(option1, option2))

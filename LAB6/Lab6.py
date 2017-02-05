# Jose Capestany
# Cameron Meier
# CS126L 3/11/2016
# LAB6: Banners


def print_banner(str, vertical=1):
    # Makes the string lowercase
    str = str.lower()
    # Dictionary of letters and their representation
    letters = {'a': ['    ', '### ', '# # ', '### ', '# # '],
               'b': ['    ', '#   ', '### ', '# # ', '### '],
               'c': ['    ', '### ', '#   ', '#   ', '### '],
               'd': ['    ', '##  ', '# # ', '# # ', '##  '],
               'e': ['    ', '    ', '### ', '##  ', '### '],
               'f': ['    ', '### ', '#   ', '##  ', '#   '],
               'g': ['    ', '### ', '#   ', '# # ', '### '],
               'h': ['    ', '# # ', '# # ', '### ', '# # '],
               'i': ['    ', '### ', ' #  ', ' #  ', '### '],
               'j': ['    ', '### ', ' #  ', ' #  ', '##  '],
               'k': ['    ', '# # ', '##  ', '##  ', '# # '],
               'l': ['    ', '#   ', '#   ', '#   ', '### '],
               'm': ['    ', '# # ', '### ', '# # ', '# # '],
               'n': ['    ', '# # ', '### ', '### ', '# # '],
               'o': ['    ', '### ', '# # ', '# # ', '### '],
               'p': ['    ', '### ', '# # ', '### ', '#   '],
               'q': ['    ', '### ', '# # ', '# # ', ' ## '],
               'r': ['    ', '### ', '# # ', '##  ', '# # '],
               's': ['    ', '### ', '##  ', ' ## ', '### '],
               't': ['    ', '### ', ' #  ', ' #  ', ' #  '],
               'u': ['    ', '# # ', '# # ', '# # ', '### '],
               'v': ['    ', '# # ', '# # ', '# # ', ' #  '],
               'w': ['    ', '# # ', '# # ', '### ', '### '],
               'x': ['    ', '# # ', ' #  ', ' #  ', '# # '],
               'y': ['    ', '# # ', '### ', ' #  ', ' #  '],
               'z': ['    ', '### ', ' ## ', '##  ', '### ']}
    # Checks if the vertical input is true (Default is TRUE)
    if vertical:
        for j in str:
            for k in range(5):
                # Print the rows of a letter then move to next letter
                print(letters[j][k])
    # If vertical is not true run horizontal
    else:
        for k in range(5):
            for j in str:
                # Prints the letter's first row and then the following
                print(letters[j][k], end='')
            print("")

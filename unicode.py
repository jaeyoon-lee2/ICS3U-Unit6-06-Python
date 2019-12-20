#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Dec 2019
# This program finds the hexadecimal of letter


def main():
    # this function finds the hexadecimal of letter

    Unicode = {}
    some_info = {'item1': 1,
                 'item2': 2,
                 }
    characters = []

    # adding items
    Unicode['J'] = "4a"
    Unicode['L'] = "4c"
    Unicode['a'] = "61"
    Unicode['e'] = "65"
    Unicode['y'] = "79"

    some_string = input("Enter the string: ")
    characters = list(some_string)

    for counter in characters:
        if counter in Unicode.keys():
            print("{0} ".format(Unicode[counter]), end="")
        else:
            print("That characters are not in dictionary.")
            break
    print("")


if __name__ == "__main__":
    main()

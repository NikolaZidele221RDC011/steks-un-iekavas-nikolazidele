from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
simboli = []
pozicijas = []
nepoz = []
booo = True


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        pozicijas.append(i)
        nepoz.append(i)

        if next in "([{":
            # Process opening bracket, write your code here
            simboli.append(next)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            #pass

            if next == "}":
                if(len(simboli)==0):
                    print(pozicijas[-1] + 1)
                    #pievieno ka nav jaizvada success
                    booo = False
                    break
                if(simboli[-1]) == "{":
                    simboli.pop()
                    nepoz.remove(nepoz[-2])
                    nepoz.remove(nepoz[-1])
                else:
                    print(pozicijas[-1]+1)
                    break

            if next == "]":
                if(len(simboli)==0):
                    print(pozicijas[-1] + 1)
                    booo = False
                    break
                if(simboli[-1]) == "[":
                    simboli.pop()
                    nepoz.remove(nepoz[-2])
                    nepoz.remove(nepoz[-1])
                else:
                    print(pozicijas[-1]+1)
                    break

            if next == ")":
                if(len(simboli)==0):
                    print(pozicijas[-1] + 1)
                    booo = False
                    break
                if(simboli[-1]) == "(":
                    nepoz.remove(nepoz[-2])
                    nepoz.remove(nepoz[-1])
                    simboli.pop()
                else:
                    print(pozicijas[-1]+1)
                    break

        pass

    if pozicijas[-1] == len(text)-1:
        if len(simboli) != 0:
            print(nepoz[0]+1)
        else:
            if booo==True:
                print("Success")



def main():
    text = input()
    mismatch = find_mismatch(text) #so nokomentejam
    # Printing answer, write your code here


if __name__ == "__main__":
    main()




# python3

# from collections import namedtuple

# Bracket = namedtuple("Bracket", ["char", "position"])


# def are_matching(left, right):
#     return (left + right) in ["()", "[]", "{}"]


# def find_mismatch(text):
#     opening_brackets_stack = []
#     for i, next in enumerate(text):
#         if next in "([{":
#             # Process opening bracket, write your code here
#             pass

#         if next in ")]}":
#             # Process closing bracket, write your code here
#             pass


# def main():
#     text = input()
#     mismatch = find_mismatch(text)
#     # Printing answer, write your code here


# if __name__ == "__main__":
#     main()
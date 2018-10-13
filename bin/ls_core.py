import os
workdir = os.getcwd()

def CommandExecution(argument):
    ls = os.listdir(argument)
    column = 0
    for row in ls:
        for elem in row:
            print(elem,end='')
        print(end="  ")
        column = column + 1
        if column == 5:
            column = 0
            print()
    if column != 0 and column != 5:
        print()

def AnotherCommandExecution():
    ls = os.listdir(workdir)
    column = 0
    for row in ls:
        for elem in row:
            print(elem,end='')
        print(end="  ")
        column = column + 1
        if column == 5:
            column = 0
            print()
    if column != 0 and column != 5:
        print()
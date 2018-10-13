import os
workdir = os.getcwd()

def CommandExecution(argument):
    try:
        os.makedirs(argument)
    except:
        print("ERROR: Directory exists or access denied")
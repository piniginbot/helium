# == Dependencies ==
import os
workdir = os.getcwd()
# == ~~~~~~~~~~~~ ==

def CommandExecution(argument):
    try:
        if os.path.exists(argument) == True:
            os.rmdir(argument)
        else:
            print("ERROR: Directory isn't empty")
    except:
        print("ERROR: Directory isn't empty")
#!/usr/bin/python3

#
# === License: ===
# === ISC ===
# === Copyright (c) 2016-2017, Maksim Pinigin <pinigin_official@mail.ru> ===
#

# -*- coding: utf-8 -*-
# === Importing ===
import os
import math
import datetime
import time
import sys
# === Import /bin ===
sys.path.append(os.getcwd() + '//bin')
import hello
import pinos
import helium
import mth
import rd_core
import md_core
import ls_core
# === Variables ===
global text
global command
global workdir
global ifcd
global login
global username
try:
    workdir = os.getcwd()
    ifcd = 1
except:
    workdir = 0
    ifcd = 0
# ===

try:
    login = os.getlogin()
except:
    login = "user"

# === Shell ===
while True:

        if login == "root":
            if ifcd == 1:
                text = input("# " + workdir + ": ")
            else:
                text = input("# /: ")
        else:
            if ifcd == 1:
                text = input("$ " + workdir + ": ")
            else:
                text = input("$ /: ")

        if text:
            command = text.split(' ') # SCS

            if command[0] == "hello":
                hello.CommandExecution()
            elif command[0] == "md":
                if len(command) == 2:
                    md_core.CommandExecution(command[1])
                else:
                    print("USAGE: md [path/to/directory]")
            elif command[0] == "rd":
                if len(command) == 2:
                    rd_core.CommandExecution(command[1])
                else:
                    print("USAGE: rd [path/to/directory]")
            elif command[0] == "python":
                copyright()
            elif command[0] == "python_commands":
                help()
            elif command[0] == "pinos":
                pinos.CommandExecution()
            elif command[0] == "helium":
                helium.CommandExecution()
            elif command[0] == "array":
                print(command[1:])
            #elif command[0] == "pfh":
            #...
            # === Official modules ===
            #elif command[0] == "omod":
                # === Math ===
            #    try:
            #        if command[1] == "oldmath": # from 2016
            #            global primer
            #            print("Math for Pinos by Maxim Pinigin. License ISC")
            #            print("Copyright (c) 2016, Maksim Pinigin <maksim@pinig.in>")
            #            while True:
            #                primer = input("Math> ")
            #                if primer == "exit":
            #                    break
            #                elif primer == "+":
            #                    one = int(input("One: "))
            #                    two = int(input("Two: "))
            #                    otv = one+two
            #                    print(otv)
            #                elif primer == "-":
             #                   one = int(input("One: "))
              #                  two = int(input("Two: "))
               #                 otv = one-two
                #                print(otv)
                 #           elif primer == "/":
                  #              one = int(input("One: "))
                   #             two = int(input("Two: "))
                    #            otv = one/two
                     #           print(otv)
                      #      elif primer == "*":
                       #         one = int(input("One: "))
                        #        two = int(input("Two: "))
                         #       otv = one*two
                          #      print(otv)
                           # elif primer == "pi":
                            #    print(math.pi)
                            #elif primer == "help":
                            #    print("+ or - or / or * or pi")
                            #else:
                             #   print("Unknown command")
                    # ===
                    # ===
                    #else:
                    #    print("Module is not found.")
                #except:
                #    print("Error!")
            # ===
            elif command[0] == "math":
                mth.CommandExecution()
            elif command[0] == "cd":
                if len(command) == 2:
                    if os.path.exists(command[1]):
                        if command[1] == "-":
                            ifcd = 0
                        else:
                            ifcd = 1
                            workdir = command[1]
                            #os.chdir(command[1])
                    else:
                        print("Error. Maybe, directory is not exists?")
                else:
                    print("USAGE: cd [/path/to/directory]")
            elif command[0] == "dir" or command[0] == "ls":
                if len(command) > 1:
                    ls_core.CommandExecution(command[1])
                else:
                    ls_core.AnotherCommandExecution()
            # Phew...
            #elif command[0] == "chmod":
            #    try:
            #        try:
            #            mode = command[1]
            #            filename = command[2]
            #            #group = command[3]
            #            os.chmod(workdir + "/" + filename,mode)
            #        except:
            #            print("FATAL ERROR!1")
            #    except:
            #        print("Error. Maybe, file(or directory?) is not exists?")
            #elif command[0] == "chown":
            #    try:
            #        try:
            #            filename = command[1]
            #            owner = command[2]
            #            group = command[3]
            #            os.chown(workdir + "/" + filename,owner,group)
            #        except:
            #            print("FATAL ERROR!1")
            #    except:
            #        print("Error. Maybe, file(or directory?) is not exists?")
            elif command[0] == "vf":
                if len(command) == 2:
                    if command[1][0] == "/":
                        file_to_open = command[1]
                    else:
                        file_to_open = workdir + "/" + command[1]
                    try:
                        f = open(file_to_open, 'r')
                        readed = f.read()
                        print(readed)
                        f.close()
                    except:
                        print("ERROR: File is't exists or access denied")
                else:
                    print("USAGE: vf [path/to/file]")
            elif command[0] == "rf":
                if len(command) == 2:
                    if command[1][0] == "/":
                        file_to_delete = command[1]
                    else:
                        file_to_delete = workdir + "/" + command[1]
                    try:
                        os.remove(file_to_delete)
                    except:
                        print("ERROR: File is't exists or access denied")
                else:
                    print("USAGE: rf [path/to/file]")
            elif command[0] == "getlogin":
                print(login)
            elif command[0] == "mf":
                if len(command) == 3:
                    if command[1][0] == "/":
                        file_to_move = command[1]
                    else:
                        file_to_move = workdir + "/" + command[1]
                    if command[2][0] == "/":
                        new_name = command[2]
                    else:
                        new_name = workdir + "/" + command[2]
                    try:
                        os.rename(file_to_move, new_name)
                    except:
                        print("ERROR: File is't exists or access denied")
                else:
                    print("USAGE: mf [old/path] [new/path]")
            elif command[0] == "wf":
                if len(command) > 2:
                    text_to_write = text.replace('wf ' + command[1] + ' ', '')
                    if command[1][0] == "/":
                        filename = command[1]
                    else:
                        filename = workdir + "/" + command[1]
                    if os.path.exists(filename) == True:
                        f = open(filename, 'r')
                        old_text = f.read()
                        f.close()
                        try:
                            f = open(filename, 'w')
                            f.write(old_text + "\n" + text_to_write)
                            f.close()
                        except:
                            print("ERROR: Access denied or directory is't exists")
                    else:
                        try:
                            f = open(filename, 'w')
                            f.write(text_to_write)
                            f.close()
                        except:
                            print("ERROR: Access denied or directory is't exists")
                else:
                    print("USAGE: wf [file] [text..]")
            elif text[0] == "!":
                execute_text = text.replace('!', '')
                os.system(execute_text)
            elif command[0] == "exit":
                print("Goodbye!")
                exit()
            else:
                print("Command not found")
# ===

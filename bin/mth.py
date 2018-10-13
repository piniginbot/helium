def CommandExecution():
    print("Math for Pinos by Maxim Pinigin.")
    while True:
        textmath = input("Math> ")
        commandmath = textmath.split(' ')
        if commandmath[0] == "exit":
            break
        try:
            if commandmath[1] == "+":
                one = int(commandmath[0])
                two = int(commandmath[2])
                otv = one+two
                print(otv)
            elif commandmath[1] == "-":
                one = int(commandmath[0])
                two = int(commandmath[2])
                otv = one-two
                print(otv)
            elif commandmath[1] == "/":
                one = int(commandmath[0])
                two = int(commandmath[2])
                otv = one/two
                print(otv)
            elif commandmath[1] == "*":
                one = int(commandmath[0])
                two = int(commandmath[2])
                otv = one*two
                print(otv)
        except:
            print('Error')
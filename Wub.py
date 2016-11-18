def func(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)
opening= input("Welcome to our Calculus program. Press 'h' for help, press 'f' to insert a function, or press 'q' to quit. ") 
while opening not in ["q", "z"]:
    if opening not in ["h", "f", "z"]:
        opening=input("It seems you entered an incorrect command, please try again. Enter e to encrypt, d to decrypt, or q to quit: ")
    if opening=="h":
        helping=input("What do you need help with? Press 'f' for how to enter a function, press 'b' for how to enter boundaries, or press 'r' to return to the previous screen. ")
        if helping=="r":
            opening= input("Welcome to our Calculus program. Press 'h' for help, press 'f' to insert a function, or press 'q' to quit. ") 
        if helping =="f":
            func=input("A function should be entered in the manner of '3(x)^2+2(x)+8'. Press any button to return to the original screen.")
            opening= input("Welcome to our Calculus program. Press 'h' for help, press 'f' to insert a function, or press 'q' to quit. ") 
        if helping=="b":
            bound=input("For boundaries, input the lower boundary first, such as '-5', then input the upper boundary, such as '5'. Doing this in the incorrect order will cause the program to fail. Press 'return' to return to the opening screen.") 
            opening= input("Welcome to our Calculus program. Press 'h' for help, press 'f' to insert a function, or press 'q' to quit. ") 
        if helping not in ["h", "f", "r"]:
           helping=input("It seems you entered an incorrect command, please try again. Press 'f' for how to enter a function, press 'b' for how to enter boundaries, or press 'r' to return to the previous screen. ")
    if opening=="f":
        function=input("f(x)= ")
        lwrbound=float(input("What is the lower boundary of the function? "))
        upprbound=float(input("What is the upper boundary of the function? "))
        opening="z"
        func(f=sin, x=0, h=.01)
if opening== "q":
    print("Goodbye!")
if opening== "z":
    print(" ")
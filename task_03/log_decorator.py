def log_it(func):
    
    def implementation(*args, **kwargs):
        statement = "[LOG] %s (%s %s) ==>" 
        statement = statement % (func, args, kwargs)  # fstring 

        ret = func(*args, **kwargs)
        print(statement, ret, type(ret)) # memory address in hex
        return ret # return this in case function has a return
    return implementation

@log_it # basically just calling log_it(test)()
def test():
    print("test")

# log_it(test)()

# args: filename is the name of the file to be read
#       resources is defaulted to the resources folder
#       but can be changed

@log_it
def cat(filename, resources="./resources/"):
    with open(resources+filename) as filehandle:
        for line in filehandle:
            print(line, end='')

@log_it
def add(x, y):
    return x+y

@log_it
def sub(x, y):
    return x-y

@log_it
def mult(x, y):
    return x*y

@log_it
def div(x, y):
    return x/y

def add2(x, y):
    return x+y


def main():
    stri = ""

    
    # print("Please enter a 1 for debug mode or a 0 for no debug logs")
    # mode =""
    # mode = str(input())
    # while (mode != "0" and mode != "1"):
    #     print("invalid input, try again")
    #     print("Please enter a 1 for debug mode or a 0 for no debug logs")
    #     mode = input();

    
    print("Please enter a 0 followed by a filename located in resources")
    print("OR enter a 1 followed by add, sub, mult, div for the arithmetic operation")
    print("follow the operator by the two numbers")
    print("OR enter exit to quit program")
    while (stri != 'exit'):
        stri = str(input())
        tokens = stri.split()
        if (tokens[0] == "0"):
            cat(tokens[1])
        elif(tokens[0] == "1"):
            if (tokens[1] == "add"):
                add(int(tokens[2]), int(tokens[3])) #add
            elif (tokens[1] == "sub"):
                sub(int(tokens[2]), int(tokens[3])) #sub
            elif (tokens[1] == "mult"):
                mult(int(tokens[2]), int(tokens[3])) #multiply
            elif (tokens[1] == "div"):
                div(int(tokens[2]), int(tokens[3])) #divide


if __name__ == "__main__":
    main()
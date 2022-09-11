from cmath import log
from functools import wraps

def log_it(func):
    @wraps(func) # allows for unwrapping of decorator
    def implementation(*args, **kwargs):
        """A wrapper function"""
    
        statement = "[LOG] %s (%s %s) ==>" 
        try:
            statement = statement % (func, args, kwargs)  # fstring 

            ret = func(*args, **kwargs)
            print(statement, ret, type(ret)) # memory address in hex
        except FileNotFoundError as e: # most common exception
            print("File not found. Try creating the file and trying again.")
            ret = None
            print(statement, ret, type(ret)) # memory address in hex
            raise e
        except ValueError as e: # can this even be reached?
            ret = None
            print("Invalid value error.")
            print(statement, ret, type(ret)) # memory address in hex
            raise e
        except Exception as e: # prevents crashing for rest of uncommon exceptions
            ret = None
            print("See error description: " + e.__str__())
            print(statement, ret, type(ret)) # memory address in hex
            raise e

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

# call with log_it(add)(1,2) for example of no annotation decorator implementation
# def add(x,y):
#     return x+y



def main():
    stri = "" # used for cmd line
    # huh = log_it(lambda a,b: a*b)(1,2)
    # print (huh)
    # implicit string
    openingStatement = ("Please enter a 0 followed by a filename located in resources\n"
                       "OR enter a 1 followed by add, sub, mult, div for the arithmetic operation\n"
                       "follow the operator by the two numbers\n"
                       "OR enter exit to quit program")
    print(openingStatement)
    while (stri != 'exit'):
        stri = str(input())
        tokens = stri.split()
        try:
            if(len(tokens) > 1):
                if (tokens[0] == "0"):
                    cat(tokens[1])
                elif(tokens[0] == "1"):
                    if (tokens[1] == "add"):
                        add(int(tokens[2]), int(tokens[3])) # add
                    elif (tokens[1] == "sub"):
                        sub(int(tokens[2]), int(tokens[3])) # sub
                    elif (tokens[1] == "mult"):
                        mult(int(tokens[2]), int(tokens[3])) # multiply
                    elif (tokens[1] == "div"):
                        div(int(tokens[2]), int(tokens[3])) # divide
                    else:
                        print("Wrong input, try again.") # TODO refactor
                else:
                    print("Wrong input, try again.")
            else:
                print("Wrong input, try again.")
        except Exception as e:
            # e.__str__() just converts object to string
            print("Error raised in cmd line!: " + e.__str__()) # catch ValueError errors of int() in logger since they happen before it


if __name__ == "__main__":
    main()
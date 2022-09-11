from datetime import date
from pathlib import Path

logFileName =  "" #drastically simplifying log file creation if I use a global

def newLogFile():
    """used to reassign global logFileName. A new file is created on every call to the main function.
    """
    ourNewLogFile = "[LOGFILE]" +date.today().strftime("%d_%m_%Y") +".txt" #makes a log file with today's date
    path = Path("./logs/"+ourNewLogFile)
    counter = 0
    # loops over files until it finds an unused filename, and then makes it
    while(path.is_file()):
        newName = "[LOGFILE]" +date.today().strftime("%d_%m_%Y")+"at"+str(counter) +".txt" 
        path = Path("./logs/"+newName)
        ourNewLogFile = newName
        counter+=1
    return ourNewLogFile


def setLogFileName(name="default"):
    """reassigns global logFileName"""
    global logFileName 
    if name == "default":
        logFileName = newLogFile()
    else: 
        logFileName = name
        

def writeToLogFile(statement, filename=logFileName, path = "./logs/"):
    """Writes to the file created during runtime. Will use a new file if first time running."""
    path = Path("./logs/"+filename)
    writer = None
    if (path.is_file()):
        writer = open(str(path), "a") # append if file exists
    else:
        writer = open(str(path), "w") # make new file if doesn't exist
    writer.write(statement+"\n")
    writer.close()




def log_it(func):
    """logging decorator with exception and function details """
    def implementation(*args, **kwargs):
        """A wrapper function"""
    
        statement = "[LOG] %s (%s %s) ==> " 
        fullStatement = ""
        ret = None
        
        try:
            statement = statement % (func, args, kwargs)  # fstring 
            ret = func(*args, **kwargs)
            #if no error just set fullstatment up
            fullStatement = statement+str(ret)+" " +str(type(ret))
        except FileNotFoundError as e: # most common exception
            errMessage = "FileNotFoundError: Try creating a new one."
            ret = None
            fullStatement =errMessage+"\n" +statement+str(ret)+" "+str(type(ret))  # how to refactor?
            raise e
        except ValueError as e: # can this even be reached?
            ret = None
            errMessage = "ValueError: Invalid value."
            fullStatement = errMessage+"\n"+statement+str(ret)+" "+str(type(ret))
            raise e
        except ZeroDivisionError as e:
            ret = None
            errMessage = "ZeroDivisionError: Divided by zero."
            fullStatement =errMessage+"\n" +statement+str(ret)+" "+str(type(ret))
            raise e
        except TypeError as e:
            ret = None
            errMessage = "TypeError: Incompatible types."
            fullStatement = errMessage+"\n"+statement+str(ret)+" "+str(type(ret))
            raise e
        except Exception as e: # prevents crashing for rest of uncommon exceptions
            ret = None
            errMessage = "Miscellaneous: " + e.__str__()
            fullStatement = errMessage+"\n"+statement+str(ret)+" "+str(type(ret))
            raise e
        finally: 
            print(fullStatement)
            writeToLogFile(fullStatement, filename=logFileName, path="./logs/")
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
    
    global logFileName 
    logFileName = newLogFile()
    
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
            print("Error caught in cmd line!: " + e.__str__()) # catch ValueError errors of int() in logger since they happen before it


if __name__ == "__main__":
    main()
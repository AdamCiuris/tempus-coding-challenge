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


def main():
    cat("test.txt")
    add(23, 42)


if __name__ == "__main__":
    main()
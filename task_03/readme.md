<h2>Python Logging Decorator</h2>

<h3>How to run (ubuntu 22)</h3>

```python3 init.py```

Then, follow the instructions for the command line interface.

For tests:
```sudo apt install python3pip```

```sudo pip install pytest```

run ```pytest test.py``` to complete tests.

<h3>What is a decorator?</h3>
A decorator is a way to modify the behavior of a function or method without changing the lower level implementation details. 


<h3>How does it use lambda functions?</h3>

Since functions are first-class in python, which means they can be passed as parameters, we pass in the base class to the decorator and execute it with ```ret = func(*args, **kwargs)```. They are inline functions. In C++ the inline keyword lets the compiler decide whether or not to create a new stack frame and do all the overhead for a function. I wonder if python does the same for lambdas?

ret is the return of the function.

*args are non keyword arguments. * is the symbol to pass variable length arguments much like ... in Java. 

**kwargs are passed as a dictionary. An example would be naming a variable like ```Age=22```.

<h3>@Annotation vs Regular Lambda</h3>

When we implement a decorator on a function using the annotation there is no longer a way to call the base function. If we were to use the log_it function normally by passing in the function to be logged like ```log_it(add)(1,2)``` then we would still have the option to run the function add without the log. 
# import task_03.log_decorator as log_decorator
from log_decorator import *
import sys
import logging
import pytest

# @pytest.fixture()
# def logger():
#     logger = logging.getLogger('Some.Logger')
#     logger.setLevel(logging.INFO)

#     return logger
def setup_function(function):
    """
    for stdout -s flag logging
    """
    print("setting up", function) 

def test_answer_add():

    assert add(3,2) == 3+2
    assert add(-99,-99) == -99+-99
    assert add(0,99) == 0+99
    assert add(99,0) == 0+99

def test_answer_sub():
    assert sub(3,2) == 3-2
    assert sub(3,0) == 3-0
    assert sub(0,3) == 0-3
    assert sub(99,99) == 99-99
    assert sub(-99,-99) == -99-(-99)

def test_answer_mult():
    assert mult(3,2) == 3*2
    assert mult(3,0) == 3*0
    assert mult(0,3) == 3*0
    assert mult(-99,-99) == -99*-99

def test_answer_div():
    assert div(3,2) == 1.5
    assert div(0,3) == 0
    assert div(-99,-99) == -99/-99
    assert div(-99,99) == -99/99

def test_answer_cat():
    assert cat("test.txt") == None # I/O stuff doesn't return anything


def test_log01(capsys):
    """
    captures output from logger for add and tests it for correctness
    """
    # address = hex(id(add(0,99)))
    add(0,99)
    out, err = capsys.readouterr() #captures stdout 
    sys.stdout.write("out:"+ out + "end out")
    # sys.stdout.write(address)

    assert out.startswith("[LOG] <function add at ") # no guarentee that address is the same
    assert out.endswith("> ((0, 99) {}) ==> 99 <class 'int'>\n")
    
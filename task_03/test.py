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

# @pytest.mark.parametrize("add_params1", "add_params2", "add_expected", [
#     (3,2, 3+2)


# ])


def test_answer_add():

    assert add(3, 2) == 3+2
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


def test_logAdd01(capsys):
    """captures output from logger for add and tests it for correctness"""
    add(0,99)
    out, err = capsys.readouterr() #captures stdout 
    sys.stdout.write("out:"+ out + "end out")
    assert out.startswith("[LOG] <function add at ") # no guarantee that address is the same
    assert out.endswith("> ((0, 99) {}) ==> 99 <class 'int'>\n")

def test_logSub01(capsys):
    """captures output from logger for sub and tests it for correctness"""
    sub(0,99)
    out, err = capsys.readouterr() #captures stdout 
    assert out.startswith("[LOG] <function sub at ") # no guarantee that address is the same
    assert out.endswith("> ((0, 99) {}) ==> -99 <class 'int'>\n")

def test_logMult01(capsys):
    """captures output from logger for mult and tests it for correctness"""
    ret = mult(0,99)
    assert ret == 0
    out, err = capsys.readouterr() #captures stdout 
    assert out.startswith("[LOG] <function mult at ") # no guarantee that address is the same
    assert out.endswith("> ((0, 99) {}) ==> 0 <class 'int'>\n")

def test_logDiv01(capsys):
    """captures output from logger for div and tests it for correctness"""
    ret = div(-99,-99)
    assert ret == 1
    out, err = capsys.readouterr() #captures stdout
    assert out.startswith("[LOG] <function div at ") # no guarantee that address is the same
    assert out.endswith("> ((-99, -99) {}) ==> 1.0 <class 'float'>\n")


def test_TypeError01():
    """tests log decorator when it receives incorrect inputs for an operation"""
    try:
        ret = add('asfd', 24)
        assert False # no exception raise
    except TypeError as e:
        assert True

def test_TypeError02():
    """testing that underlying mult will work with strings without cmd line"""
    try:
        assert mult('asfd', 2) == 'asfdasfd'
        assert True 
    except TypeError as e:
        assert False # should NOT raise exception

def test_ZeroDivisionError():
    """tests log decorator when function divides by zero"""
    try:
        div(1, 0)
        assert False # no exception raise
    except ZeroDivisionError as e:
        assert True

def test_FileNotFoundError():
    try:
        cat("&(*#$&*HFJKDSJHLKSD") # unlikely filename
        assert False #no exception
    except FileNotFoundError as e:
        assert True


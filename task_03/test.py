# import task_03.log_decorator as log_decorator
import log_decorator

def test_answer_add():

    assert log_decorator.add(3,2) == 3+2
    assert log_decorator.add(-99,-99) == -99+-99
    assert log_decorator.add(0,99) == 0+99
    assert log_decorator.add(99,0) == 0+99

def test_answer_sub():
    assert log_decorator.sub(3,2) == 3-2
    assert log_decorator.sub(3,0) == 3-0
    assert log_decorator.sub(0,3) == 0-3
    assert log_decorator.sub(99,99) == 99-99
    assert log_decorator.sub(-99,-99) == -99-(-99)

def test_answer_mult():
    assert log_decorator.mult(3,2) == 3*2
    assert log_decorator.mult(3,0) == 3*0
    assert log_decorator.mult(0,3) == 3*0
    assert log_decorator.mult(-99,-99) == -99*-99

def test_answer_div():
    assert log_decorator.div(3,2) == 1.5
    assert log_decorator.div(0,3) == 0
    assert log_decorator.div(-99,-99) == -99/-99
    assert log_decorator.div(-99,99) == -99/99

def test_answer_cat():
    assert log_decorator.cat("test.txt") == None # I/O stuff doesn't return anything

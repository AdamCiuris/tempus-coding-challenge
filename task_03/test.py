# import task_03.log_decorator as log_decorator
import log_decorator

def test_answer_add():
    assert log_decorator.add(3,2) == 5

def test_answer_sub():
    assert log_decorator.sub(3,2) == 1

def test_answer_mult():
    assert log_decorator.mult(3,2) == 6

def test_answer_div():
    assert log_decorator.div(3,2) == 1.5

def test_answer_cat():
    assert log_decorator.cat("test.txt") == None # I/O stuff doesn't return anything
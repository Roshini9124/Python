import pytest
from maths import *
def test_add():
    assert add(5,4)==9
    assert add(-1,-4)==-8


    '''Unit testing is a software testing technique where we test the smallest individual parts (units) of a program separately to verify that they work correctly.

A unit usually means:

A function
A method
A class

Instead of testing the entire application at once, we test each small component independently.'''
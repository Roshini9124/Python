import pytest
from maths import *
def test_add():
    assert add(5,4)==9
    assert add(-1,-4)==-5
    assert sub(9,11)==2


    '''Unit testing is a software testing technique where we test the smallest individual parts (units) of a program separately to verify that they work correctly.

A unit usually means:

A function
A method
A class

Instead of testing the entire application at once, we test each small component independently.'''

'''A fixture in pytest is a function that prepares some data or environment before a test runs and cleans it up afterward (if needed).

Think of a fixture as a helper function that provides resources to your tests.

Instead of writing the same setup code in every test, you write it once in a fixture and reuse it.'''
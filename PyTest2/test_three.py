'''
Created on Apr 23, 2021

@author: martinyanev
'''
import pytest
from collections import namedtuple

Dinner = namedtuple('Dinner',  ['food', 'cook', 'ready', 'id'])
Dinner.__new__.__defaults__ = (None, None, True, None)

def test_defaults():
    t1 = Dinner()
    t2 = Dinner(None, None, False, None)
    assert t1 == t2


@pytest.mark.run_first
def test_num_access():
    t = Dinner('potatoes', 'Sam')
    assert t.food == 'potatoes'
    assert t.cook == 'Sam'
    assert (t.ready, t.id) == (True, None)

    
    
    
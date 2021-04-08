import pytest
from gendiff.generate_diff import generate_diff
   
def test_one():
    x = generate_diff('file1.json','file2.json')
    y = open("fixtures.txt", "r")
    assert x == y.read()

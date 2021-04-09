import pytest
from gendiff.generate_diff import generate_diff
   
def test_one():
    x = generate_diff('tests/fixtures/test1_file1.json','tests/fixtures/test1_file2.json')
    y = open("tests/fixtures/test1.txt", "r")
    assert x == y.read()

    
def test_two():
    x = generate_diff('tests/fixtures/test2_file1.json','tests/fixtures/test2_file2.json')
    y = open("tests/fixtures/test2.txt", "r")
    assert x == y.read()


def test_three():
    x = generate_diff('tests/fixtures/test3_file1.json','tests/fixtures/test3_file2.json')
    y = open("tests/fixtures/test3.txt", "r")
    assert x == y.read()


def test_four():
    x = generate_diff('tests/fixtures/test4_file1.json','tests/fixtures/test4_file2.json')
    y = open("tests/fixtures/test4.txt", "r")
    assert x == y.read()


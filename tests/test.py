import pytest
from gendiff.generate_diff import generate_diff
   
def test_one():
    x = generate_diff('tests/fixtures/test for json/test1_file1.json','tests/fixtures/test for json/test1_file2.json')
    y = open("tests/fixtures/test for json/test1.txt", "r")
    assert x == y.read()

    
def test_two():
    x = generate_diff('tests/fixtures/test for json/test2_file1.json','tests/fixtures/test for json/test2_file2.json')
    y = open("tests/fixtures/test for json/test2.txt", "r")
    assert x == y.read()


def test_three():
    x = generate_diff('tests/fixtures/test for json/test3_file1.json','tests/fixtures/test for json/test3_file2.json')
    y = open("tests/fixtures/test for json/test3.txt", "r")
    assert x == y.read()


def test_four():
    x = generate_diff('tests/fixtures/test for json/test4_file1.json','tests/fixtures/test for json/test4_file2.json')
    y = open("tests/fixtures/test for json/test4.txt", "r")
    assert x == y.read()


def test_one_yaml():
    x = generate_diff('tests/fixtures/test for yaml/test1_file1.yml', 'tests/fixtures/test for yaml/test1_file2.yml')
    y = open("tests/fixtures/test for json/test1.txt", "r")
    assert x == y.read()


def test_two_yaml():
    x = generate_diff('tests/fixtures/test for yaml/test2_file1.yml', 'tests/fixtures/test for yaml/test2_file2.yml')
    y = open("tests/fixtures/test for json/test2.txt", "r")
    assert x == y.read()
    

def test_three_yaml():
    x = generate_diff('tests/fixtures/test for yaml/test3_file1.yml', 'tests/fixtures/test for yaml/test3_file2.yml')
    y = open("tests/fixtures/test for json/test3.txt", "r")
    assert x == y.read()


def test_four_yaml():
    x = generate_diff('tests/fixtures/test for yaml/test4_file1.yml', 'tests/fixtures/test for yaml/test4_file2.yml')
    y = open("tests/fixtures/test for json/test4.txt", "r")
    assert x == y.read()

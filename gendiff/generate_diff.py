"""Module flat json file comparison."""
import json

import yaml

encoder = {
    True: 'true',
    False: 'false',
    None: 'null',
}



def opener(file1,file2):
    if file1.split('.')[1] == 'json' and file2.split('.')[1] == 'json':
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
    elif file1.split('.')[1] == 'yml' and file2.split('.')[1] == 'yml':
        file1 = yaml.safe_load(open(file1))
        file2 = yaml.safe_load(open(file2))
    return file1, file2


def generate_diff(file1, file2):
    """Do this flat json file comparison.

    Args:
        file1: json or yml file
        file2: json or yml file

    Returns:
        different: string changes of two json files
    """
    different = []
    file1, file2 = opener(file1, file2)
    file1 = set(file1.items())
    file2 = set(file2.items())
    for key, value in file1 & file2:
        value = str(encoder.get(value, value))
        different.append((' ', '{0}:'.format(key), value))
    for key, value in file1 - file2:
        value = str(encoder.get(value, value))
        different.append(('-', '{0}:'.format(key), value))
    for key, value in file2 - file1:
        value = str(encoder.get(value, value))
        different.append(('+', '{0}:'.format(key), value))
    different.sort(key=lambda item: item[1])
    different = map(' '.join, different)
    different = '{\n  ' + '\n  '.join(different) + '\n}\n'
    return different

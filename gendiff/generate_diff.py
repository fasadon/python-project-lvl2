"""Module flat json file comparison."""
import json
import yaml


def not_changed(file1,file2,encoder):
    lst = []
    for key, value in file1 & file2:
        lst.append((' ', '{0}:'.format(key), str(encoder.get(value,value))))
    return lst


def deleted(file1,file2,encoder):
    lst = []
    for key, value in file1 - file2:
        lst.append(('-', '{0}:'.format(key), str(encoder.get(value,value))))
    return lst


def new(file1,file2,encoder):
    lst = []
    for key, value in file2 - file1:
        lst.append(('+', '{0}:'.format(key), str(encoder.get(value,value))))
    return lst


def generate_diff(file1, file2):
    """Do this flat json file comparison.

    Args:
        file1: json or yml file
        file2: json or yml file

    Returns:
        generate_different: string changes of two json files
    """
    generate_different = []
    encoder = {
        True: 'true',
        False: 'false',
        None: 'null'
    }
    if file1.endswith('.json') and file2.endswith('.json'):
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
    else:
        file1 = yaml.safe_load(open(file1))
        file2 = yaml.safe_load(open(file2))
    file1 = set(file1.items())
    file2 = set(file2.items())
    generate_different.extend(not_changed(file1,file2,encoder))
    generate_different.extend(deleted(file1,file2,encoder))
    generate_different.extend(new(file1,file2,encoder))
    generate_different.sort(key=lambda item: item[1])
    generate_different = map(' '.join, generate_different)
    generate_different = '{\n  ' + '\n  '.join(generate_different) + '\n}\n'
    return generate_different

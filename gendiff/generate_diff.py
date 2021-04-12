"""Module flat json file comparison."""
import json
import yaml

def generate_diff(file1, file2):
    """Do this flat json file comparison.

    Args:
        file1: json file
        file2: json file

    Returns:
        generate_different: string changes of two json files
    """
    generate_different = []
    print(file1)
    print(file2)
    if file1.endswith('.json') and file1.endswith('.json'):
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
        encoder = json.dumps
    elif file1.endswith('.yml') and file1.endswith('.yml'):
        file1 = yaml.safe_load(open(file1))
        file2 = yaml.safe_load(open(file2))
        encoder = yaml.dump
    file1 = set(file1.items())
    file2 = set(file2.items())
    for key, value in file1 & file2:
        generate_different.append((' ', '{0}:'.format(key), encoder(value).replace('\n...\n','')))
    for key, value in file1 - file2:
        generate_different.append(('-', '{0}:'.format(key), encoder(value).replace('\n...\n','')))
    for key, value in file2 - file1:
        generate_different.append(('+', '{0}:'.format(key), encoder(value).replace('\n...\n','')))
    generate_different.sort(key=lambda item: item[1])
    generate_different = map(' '.join, generate_different)
    generate_different = '{\n  ' + '\n  '.join(generate_different) + '\n}\n'
    generate_different = generate_different.replace('"', '')
    return generate_different

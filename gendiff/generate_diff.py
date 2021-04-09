import json


def generate_diff(file1,file2):
    generate_different = []
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    file1 = set(file1.items())
    file2 = set(file2.items())
    for key, value in file1 & file2:
        generate_different.append((' ','{}:'.format(key), json.dumps(value)))
    for key, value in file1 - file2:
        generate_different.append(('-','{}:'.format(key), json.dumps(value)))
    for key, value in file2 - file1:
        generate_different.append(('+', '{}:'.format(key), json.dumps(value)))
    generate_different.sort(key= lambda y: y[1])
    generate_different = list(map(' '.join, generate_different))
    generate_different = '{\n  ' + '\n  '.join(generate_different) + '\n}\n'
    generate_different = generate_different.replace('"','')
    return generate_different

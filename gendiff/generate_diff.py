import json


def generate_diff(file1,file2):
    generate_different = []
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    file1 = set(file1.items())
    file2 = set(file2.items())
    not_change = file1 & file2
    new_changes = file2 - file1
    deleted = file1 - file2
    for key, value in not_change:
        generate_different.append('  {0}: {1}'.format(key, value))
    for key, value in new_changes:
        generate_different.append('+ {0}: {1}'.format(key, value))
    for key, value in deleted:
        generate_different.append('- {0}: {1}'.format(key, value))
    generate_different.sort(key= lambda x: x[2])
    print(generate_different)

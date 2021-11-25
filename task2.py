import argparse


def create_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str)
    return parser


def create_file(filename):
    try:
        with open(filename, 'r') as f:
            nums = f.read()
    except IOError:
        print('File with current name did not find. Try another name')
        quit()
    return nums.replace('\n', ' ')


def find_words(data):
    data = data.split(' ')
    for i in range(len(data)):
        for symbol in data[i]:
            if not (str(symbol).isalpha()):
                data[i] = data[i].replace(symbol, '')
    return data


parser = create_parse()
namespace = parser.parse_args()
workspace = create_file(namespace.filename)
newfile = find_words(workspace)
print(workspace.split(' '))
print(newfile)

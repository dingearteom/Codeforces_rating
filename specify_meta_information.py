import json
import os

def files_creation():
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/contests_id.txt'):
        os.mknod('data/contests_id.txt')
    if not os.path.exists('data/nicknames.txt'):
        os.mknod('data/nicknames.txt')
    if not os.path.exists('data/meta.txt'):
        os.mknod('data/meta.txt')

def specify_meta_information():
    m = {}

    print('Specify meta information:')
    print("Input name of the group:")
    m['Group'] = input().strip()
    print('Input desirable name of the excel file:')
    m['FILE_NAME_DISK'] = input().strip()
    print('Input your Codeforces API key:')
    m['API_KEY'] = input().strip()
    print('Input your Codeforces Secret key:')
    m['SECRET'] = input().strip()
    with open('data/meta.txt', 'w') as file:
        json.dump(m, file, ensure_ascii=False)

if __name__ == '__main__':
    files_creation()
    specify_meta_information()


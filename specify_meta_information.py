import json

def specify_meta_information():
    m = {}

    print('Specify meta information:')
    print("Input name of the group:")
    m['Group'] = input().strip()
    print('Input desirable name of the excel file:')
    m['FILE_NAME_DISK'] = input().strip()

    with open('data/meta.txt', 'w') as file:
        json.dump(m, file, ensure_ascii=False)

if __name__ == '__main__':
    specify_meta_information()


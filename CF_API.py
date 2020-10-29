import requests
import json
import warnings
import ssl
import random
import hashlib
import time
import pandas as pd
from meta import API_KEY, SECRET

warnings.filterwarnings('ignore', message='Unverified HTTPS request')
ssl._create_default_https_context = ssl._create_unverified_context

HOST = "https://codeforces.com/api"
HEADER = {"Content-Type": "application/json"}

def print_pretty_json(data):
    print(json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False))


def ApiSeg(method, **kwargs):
    n = ""
    digits = [chr(ord('0') + i) for i in range(10)]
    for i in range(6):
        n += random.choice(digits)
    s = f"{n}/{method}?"
    arr = []
    for attr, key in kwargs.items():
        arr.append((attr, key))
    arr.sort()
    ind = 0
    for attr, key in arr:
        s += f"{attr}={key}"
        if (ind != len(arr) - 1):
            s += "&"
        ind += 1
    s += f"#{SECRET}"
    return n + hashlib.sha512(s.encode('utf-8')).hexdigest()

def get_contest(id):
    try:
        t = str(round(time.time()))
        s = ApiSeg("contest.standings", apiKey=API_KEY, contestId=id, time=t)
        request = requests.get(f"{HOST}/contest.standings?apiKey={API_KEY}&contestId={id}&time={t}&apiSig={s}",
                 headers=HEADER,
                 verify=False)
        request.raise_for_status()
        data = request.json()['result']
        return data
    except Exception as exc:
        request_json = request.json()
        if (request_json['comment'] == "Call limit exceeded"):
            time.sleep(1)
            return get_contest(id)
        else:
            print(exc)
            print_pretty_json(request.json())

def get_contest_name(id):
    return get_contest(id)['contest']['name']

def data_contest(id):
    nicknames = []
    with open('data/nicknames.txt') as file:
        for line in file:
            nicknames.append(line)
    data = pd.DataFrame(index=list(map(lambda s : s.strip(), nicknames)))
    a = get_contest(id)
    for t in a['problems']:
        data[t['index']] = [0 for i in range(len(nicknames))]
    for t in a['rows']:
        name = t['party']['members'][0]['handle']
        for s in range(len(t['problemResults'])):
           data.at[name, chr(s + ord('A'))] = t['problemResults'][s]['points']
    return data

def data_all_contests():
    with open('data/contests_id.txt') as file:
        m = {}
        for id in file:
            id = int(id)
            m[get_contest_name(id)] = data_contest(id)
        return m

def sort_data(data):
    m = {}
    with open('data/nicknames.txt') as file:
        for line in file:
            line = line.strip()
            m[line] = 0
    with open('data/contests_id.txt') as file:
        for id in file:
            id = int(id.strip())
            name_contest = get_contest_name(id)
            index = data[name_contest].index
            columns = data[name_contest].columns
            for i in range(data[name_contest].shape[0]):
                for j in range(data[name_contest].shape[1]):
                    m[index[i]] += data[name_contest].iat[i, j]
    with open('data/contests_id.txt') as file:
        for id in file:
            id = int(id.strip())
            name_contest = get_contest_name(id)
            index = data[name_contest].index
            data[name_contest] = data[name_contest].sort_index(key=lambda x: list(map(lambda y : m[y], x)), ascending=False)
    with open('data/nicknames.txt', 'w') as file:
        arr = []
        for key, value in m.items():
            arr.append((-value, key))
        arr.sort()
        for p in arr:
            key = p[1]
            file.write(key + '\n')
    return data
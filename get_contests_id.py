import time
from CF_API import HOST, API_KEY, HEADER
from CF_API import ApiSeg
from meta import Group
import requests

def get_contest_list():
    try:
        t = str(round(time.time()))
        s = ApiSeg("contest.list", apiKey=API_KEY, gym="true", time=t)
        request = requests.get(f"{HOST}/contest.list?apiKey={API_KEY}&gym=true&time={t}&apiSig={s}",
                 headers=HEADER,
                 verify=False)
        request.raise_for_status()
        data = request.json()
        return data['result']
    except Exception as exc:
        request_json = request.json()
        if (request_json['comment'] == "Call limit exceeded"):
            time.sleep(1)
            return get_contest_list()
        else:
            print(exc)
            print_pretty_json(request.json())

def get_contests_id():
    a = get_contest_list()
    our_contests_pair = []
    for contest in a:
        if ('description' in contest and 'startTimeSeconds' in contest and contest[
            'description'] == f'Group:{Group}'):
            our_contests_pair.append((contest['startTimeSeconds'], contest['id']))
    our_contests_pair.sort()
    our_contests = []
    for p in our_contests_pair:
        contest_id = p[1]
        our_contests.append(contest_id)
    with open('data/contests_id.txt', 'w') as file:
        for contest_id in our_contests:
            file.write(str(contest_id) + '\n')



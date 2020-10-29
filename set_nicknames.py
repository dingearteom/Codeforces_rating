from CF_API import get_contest

def get_nicknames(id):
    data = get_contest(id)
    nicks = []
    #print_pretty_json(data)
    for t in data['rows']:
        #print_pretty_json(t['party']['members'][0]['handle'])
        nicks.append(t['party']['members'][0]['handle'])
    return nicks

def write_nicknames():
    file = open("data/contests_id.txt")
    nicks = set()
    for id in file:
        a = get_nicknames(int(id))
        for s in a:
            nicks.add(s)
    with open('data/nicknames.txt', 'w') as file1:
        for s in nicks:
            file1.write(s + '\n')

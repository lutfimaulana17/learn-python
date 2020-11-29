import json

# menulis
# data = {}
# data['member'] = [
#     {'name': 'JetLee', 'skill': 'nafas naga'},
#     {'name': 'Lutfi', 'skill': 'makan'},
#     {'name': 'Maulana', 'skill': 'minum'}
# ]

# with open('member.txt', 'w') as memberfile:
#     json.dump(data, memberfile)

# membaca
with open('member.txt', 'r') as memberfile:
    data = json.load(memberfile)

    for member in data['member']:
        print('namanya adalah ' + member['name'] + ' punya skill ' + member['skill'])
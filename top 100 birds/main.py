import csv
import re


def normalize_name(name):
    out = name.lower()
    out = re.sub('[ -]', '', out)
    out = re.sub('grey', 'gray', out)
    return out


birds = []
with open('birds.csv') as f:
    for line in csv.reader(f):
        birds.append({
            'name': line[0],
            'freq': line[3]
        })

name_to_id = {}
with open('../ebird bird name to bird id/data.csv') as f:
    for line in csv.reader(f):
        name_to_id[normalize_name(line[0])] = line[1]

out = []
for bird in birds:
    bid = name_to_id.get(normalize_name(bird['name']), '-')
    out.append({**bird, 'id': bid})

with open('out.csv', 'w') as f:
    w = csv.DictWriter(f, out[0].keys())
    w.writeheader()
    w.writerows(out)
    print(out)

# need to manually fix up some bird names

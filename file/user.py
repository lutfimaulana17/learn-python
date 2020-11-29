import csv

# rows = []

# with open('person.csv', 'r') as csvfile:
    # csvreader = csv.reader(csvfile)
    # read sebagai object or dictionary
    # csvreader = csv.DictReader(csvfile)
    # cara1
    # for row in csvreader:
    #     rows.append(row)
    # cara2
    # rows = list(csvreader)
    # print('total baris : ', csvreader.line_num)


# for row in rows[:5]:
#     print(row[0] + " - " + row[1])

# for row in rows[:5]:
#     print(row['first_name'] + " - " + row['email'])

# menulis file csv

rows = [
    {
        'nama' : 'Lutfi',
        'skill' : 'Python',
        'power' : 100
    },
    {
        'nama' : 'Maulana',
        'skill' : 'Php',
        'power' : 75
    },
    {
        'nama' : 'Moch',
        'skill' : 'Node Js',
        'power' : 90
    }
]

with open('data.csv', 'a') as csvfile:
    fields = ['nama', 'skill', 'power']
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(rows)
    # writer.writerow({
    #     'nama' : 'Lutfi',
    #     'skill' : 'Python',
    #     'power' : 100
    # })
     
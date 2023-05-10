book = { }
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, Ny',
    'phone' : '098282'

}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': '23434'
}


import json
s = json.dumps(book)
with open("C:\Dell\PycharmProjects\practice code in python 100 days of code\jsonbook.txt", 'w') as f:
    f.write(s)
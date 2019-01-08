import random

import sqlite3
conn = sqlite3.connect('G:\SQLiteDatabaseBrowserPortable\Data\pythonsqlite.db')
cur = conn.cursor()

def randomTag():
    tagList = list()
    tags = ['i','b', 'p', 'div']
    attributes = ['style = "font-size: 48px; color:blue"','style = "font-size: 12px"', 'style = "font-size: 36px"']
    tag = random.choice(tags)
    attribute = random.choice(attributes)
    tagList.append('<'+tag+' '+attribute+'>')
    tagList.append('</'+tag+'>')
    return tagList

def sizeTag():
    sizeList = list()
    size = ['12','16', '20', '24', '28', '32', '36']
    s = random.choice(size)
    sizeList.append('<p style="font-size:'+s+'px">')
    sizeList.append('</p>')
    return sizeList
print(sizeTag())
def add_tags(contents):
    str =''
    for item in contents:
        tags = randomTag()
        sizes = sizeTag()
        str += '<tr><td>%s%s%s</td><td style="padding: 30px"></td><td>%s%s%s</td></tr>' %(tags[0],item[0],tags[1],sizes[0],item[1],sizes[1])
    return str
print(randomTag())

contents = list()
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:

    item = (row[0],row[1])
    contents.append(item)

print(contents[0][0])
print(add_tags(contents))
conn.close()
filename = 'randomTag.html'
with open(filename, 'w') as f:
    f.write('<title>Random Tags</title>')
    f.write('<div style= "position: absolute; left: 100px; top: 10px">')
    f.write('<table style="width:100%; border:0">')
    f.write('<caption style="margin-bottom: 20px;"><b style="font-size:36px">Tracks</b></caption>')
    f.write('<tr>')
    f.write('<th style="font-size:30px">Title</th><th></th>&nbsp;&nbsp;&nbsp;<th  style="font-size:30px">Plays</th>')
    f.write('</tr>')
    f.write(add_tags(contents))
    f.write('</table>')
    f.write('</div>')


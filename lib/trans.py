#!/usr/bin/env python3

fi = open('table.txt', encoding='UTF-8')
fo = open('dtable.txt', 'w', encoding='UTF-8')

fo.write('var table = {\n')

while True:
    line = fi.readline()
    if len(line) == 0:
        break
    line = line.replace('=', ':') 
    des = '\'' + line[0] + '\'' + line[1] + '\'' + line[2] + '\'' + ',' + '\n'
    fo.write(des)

fo.write('}\n')

fi.close()
fo.close()

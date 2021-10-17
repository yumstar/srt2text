import re

justreadnum = False
justreadinterval = False
filename = 'example.srt'
with open(filename, 'r') as srtFile,  open('text.txt', 'w') as textFile:
    textFile.write('\n')
    for line in srtFile:
        if re.match(r'^\d+\n$', line):
            justreadnum = True
            print(line.replace('\n', '', 1))
        elif justreadnum and re.match(r'^\d{2,}:[0-5][0-9]:[0-5][0-9],\d{3} --> \d{2,}:[0-5][0-9]:[0-5][0-9],\d{3}\n$', line):
            print(line)
            justreadnum = False
            justreadinterval = True
        elif justreadinterval:
            textFile.write(line)
    srtFile.close()
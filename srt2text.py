import re

just_read_num = False
just_read_interval = False
one_per_interval = True
one_line = True
output_line = ''
filename = 'example.srt'
with open(filename, 'r') as srtFile,  open('text.txt', 'w') as textFile:
    for line in srtFile:
        if re.match(r'^\d+\n$', line):
            just_read_num = True
            just_read_interval = False
            output_line = line.replace('\n', '', 1)
            print(output_line)
        elif just_read_num and re.match(r'^\d{2,}:[0-5][0-9]:[0-5][0-9],\d{3} --> \d{2,}:[0-5][0-9]:[0-5][0-9],\d{3}\n$', line):
            output_line = line
            print(output_line)
            just_read_num = False
            just_read_interval = True
        elif just_read_interval:
            if one_line or one_per_interval and not line in '\n':
                output_line = line.replace('\n', '', 1) 
                if one_line:
                     output_line = (" %s" % output_line)        
            else:
                output_line = line
            textFile.write(output_line)
               
        # elif justreadinterval and not line in '\n':
        #     textFile.write(line.replace('\n', '', 1))
        # elif oneline and justreadinterval and line in '\n':
        #     textFile.write(line)
    srtFile.close()
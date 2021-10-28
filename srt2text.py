import re

just_read_num = False
just_read_interval = False
one_per_interval = False
one_line = False
output_line = ""
filename = 'example2.srt'
# open srt file and create text file and (later optional) srt timing file
with open(filename, 'r') as srtFile,  open('text.txt', 'w') as textFile, open("srtinfo.txt", "w") as srt_info:
    # process subtitle file line by line
    for line in srtFile:    
         # if line consists of single integer ==> sequence number ==> write inside timing file
        if re.match(r'^\d+\n$', line):
            just_read_num = True # mark down that integer was just read
            just_read_interval = False
            output_line = line
            srt_info.write(output_line)
         # if line consists of time interval ==> subtitle timing ==> write inside timing file
        elif just_read_num and re.match(r'^\d{2,}:[0-5][0-9]:[0-5][0-9],\d{3} --> \d{2,}:[0-5][0-9]:[0-5][0-9],\d{3}\n$', line):
            just_read_num = False 
            just_read_interval = True # mark down that time interval was just read
            output_line = line
            srt_info.write(output_line + '\n')
        # if interval was just read (meaning number was read two lines ago), current line is subtile text
        # or space between subtitle timing block  ==> write line to text file
        elif just_read_interval:
            # if special options chose, current line will not start new line at end
            if one_line or one_per_interval and not line in '\n': 
                output_line = line.replace('\n', '', 1)
                # if one line needed, current text is positioned a space away from previous text 
                if one_line:
                     output_line = (" %s" % output_line)        
            else:
                output_line = line
            textFile.write(output_line)
import re
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("subtitle_file", help="name of the subtitle to extract text from")
parser.add_argument("-o","--output-file", help="the name of the resulting text file")
parser.add_argument("-t", "--timing-save",
                    help="save subtitle timing info into the following file path: name of input_file + \"_srt_info.txt\"", action="store_true")
print_options = parser.add_mutually_exclusive_group()
print_options.add_argument("-i", "--interval-in-one-line", help="subtitle text will be printed in one seperate line for each and every interval", action="store_true")
print_options.add_argument("-a", "--all-in-one-line", help="subtitle text will be printed in one line (block) for all intervals", action="store_true")
print_options.add_argument("-p", "--preserve-lines", help="(default) lines will be in the text files with the same formatting as the subtitle file", action="store_true")
arguments_parsed = parser.parse_args()

just_read_num = False
just_read_interval = False
srt_info_file = None
srt_info = None
output_line = ""

assert(Path(arguments_parsed.subtitle_file).suffix == ".srt"),"Input file provided is not a .srt file"
subtitle_file_name = arguments_parsed.subtitle_file 
if arguments_parsed.timing_save:
    srt_info_file = subtitle_file_name.replace('.srt', "_srt_info.txt", 1)
text_file_name = arguments_parsed.output_file if arguments_parsed.output_file else arguments_parsed.subtitle_file.replace(".srt", ".txt", 1)

# open srt file and create text file and (optional) srt timing file
with open(subtitle_file_name, 'r') as srt_file,  open(text_file_name, 'w') as text_file:
    if srt_info_file:
        srt_info = open(srt_info_file, "w")
    # process subtitle file line by line
    for line in srt_file:    
         # if line consists of single integer ==> sequence number ==> write inside timing file
        if re.match(r'^\d+\n$', line):
            just_read_num = True # mark down that integer was just read
            just_read_interval = False
            output_line = line
            if srt_info:
                srt_info.write(output_line)
         # if line consists of time interval ==> subtitle timing ==> write inside timing file
        elif just_read_num and re.match(r'^\d{2,}:[0-5][0-9]:[0-5][0-9],\d{3} --> \d{2,}:[0-5][0-9]:[0-5][0-9],\d{3}\n$', line):
            just_read_num = False 
            just_read_interval = True # mark down that time interval was just read
            output_line = line
            if srt_info: 
                srt_info.write(output_line + '\n')
        # if interval was just read (meaning number was read two lines ago), current line is subtile text
        # or space between subtitle timing block  ==> write line to text file
        elif just_read_interval:
            # if special options chose, current line will not start new line at end
            if arguments_parsed.all_in_one_line or arguments_parsed.interval_in_one_line and not line in '\n': 
                output_line = line.replace('\n', '', 1)
                # if one line needed, current text is positioned a space away from previous text 
                if arguments_parsed.all_in_one_line:
                     output_line = (" %s" % output_line)
            else:
                output_line = line
            text_file.write(output_line)
    if srt_info_file:
        srt_info.close()
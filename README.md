# `.Srt` To Text Converter
Python program that converts a SubRip (`.srt`) into a text file. It provides a few options for formatting and can extract the subtitle timing specification as a template file that can be filled in to add new subtitles for each interval.

Example of an `.srt` file (`some_subtitles.srt`):

```
1
00:01:00,000 --> 00:02:00,000
This is the first subtitle text.
It is multiple lines.

2
00:03:00,000 --> 00:04:00,000
This is some other subtitle text.
```

## Usage and Options

````
usage: srt2text.py [-h] [-o OUTPUT_FILE] [-t] [-i | -a | -p] subtitle_file

positional arguments:
  subtitle_file         name of the subtitle to extract text from

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        the name of the resulting text file
  -t, --timing-save     save subtitle timing info into the following file path: name of input_file + "_srt_info.txt"
  -i, --interval-in-one-line
                        subtitle text will be printed in one seperate line for each and every interval
  -a, --all-in-one-line
                        subtitle text will be printed in one line (block) for all intervals
  -p, --preserve-lines  (default) lines will be in the text files with the same formatting as the subtitle file (a line between blocks)
````

## Formatting Options

If the `--preserve-lines ` option or `-p` flag is provided, lines in the text file will be separated in the original block format so as to preserve the original format without including timing information (i.e. with a line between each between block of text). This is the default format and will be applied if no other formatting option is provided.

e.g.:

```
# resulting text file (some_subtitles.txt)
This is the first subtitle text.
It is multiple lines.

This is some other subtitle text.
```

If the `--interval-in-one-line` option or `-i` flag is provided, all subtitle text for each interval will be all together one line for that specific interval regardless if the original file has the text separated in multiple lines:

e.g.:

```
# resulting text file (some_subtitles.txt)
This is the first subtitle text.It is multiple lines.
This is some other subtitle text.
```

If the `--all-in-one-line` option or `-a` flag is provided, all subtitle text in the file will be printed in one line:

e.g.:

```
# resulting text file (some_subtitles.txt)
 This is the first subtitle text. It is multiple lines.  This is some other subtitle text.
```



### Timing Saving

To save the timing information to a file, use the ` --timing-save` option or `-t` flag

e.g.: 

```
# original srt file (some_subtitles.srt)
1
00:01:00,000 --> 00:02:00,000
This is the first subtitle text.
It is multiple lines.

2
00:03:00,000 --> 00:04:00,000
This is some other subtitle text.

=========================================
# timing file (some_subtitles_srt_info.txt)
1
00:01:00,000 --> 00:02:00,000

2
00:03:00,000 --> 00:04:00,000
```


import re
import os
import argparse

parser = argparse.ArgumentParser(description="User stories mark down formater")
parser.add_argument("--file", type=str, help="File containing the original stories")
parser.add_argument("--output", type=str, default="output.md",help="File containing the formating stories")

args = parser.parse_args()
file_name = args.file
output_file_name = args.output

original_file = open(file_name, "r")
lines = original_file.readlines()

output_file = open(output_file_name, "w+")

def write(text):
    output_file.write(text + os.linesep)
    output_file.write(os.linesep)

set_title = False
inside_list = False
count = 0

lists = r'(Scenario|Task)'
types = r'(FEATURE|CHORE)'

for line in lines:
    if line != "\n":
        current_line = line.strip()
        print("Line{}: {}".format(count, current_line))

        if not set_title:
            write(f"# {current_line}")
            set_title = True
       
        if re.search(lists, current_line):
            write(f"**{current_line}**")
            inside_list = True
        elif re.search(types, current_line):
            write(f"**{current_line[current_line.find('['):]}**")
            inside_list = False 
        elif inside_list:
            write(f"- {current_line}")
        else:
            write(f"## {current_line}")

    count += 1

original_file.close()
output_file.close()

import argparse
import re
from itertools import groupby

parser = argparse.ArgumentParser(description='Compressing strings')

parser.add_argument('input_file', help='a path to the file with strings to be compressed')
parser.add_argument('output_file', help='a path to the file to write output')

args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

def write_to_file(s):
    with open(output_file,'a') as file:
        file.write(s + '\n')

def has_english_lowercase(s):
    return bool(re.search('^[a-z]+$', s))

def compress_string(s):
    groups = groupby(s)
    result = ''
    for label, group in groups:
      if label.isalpha():
        res = label + str(len(list(group)))
        result += res
    write_to_file(result)

def main():
    with open(input_file) as file:
        for line in file:
            if line.strip() and has_english_lowercase(line):
                compress_string(line)
            else:
                print('This line is empty or contains invalid characters', line)

if __name__ == '__main__':
    main()

# Time-space complexity analysis
# 1. Time and space complexity of reading the file and checking whether it contains only English alphabet is O(n*m):
# for-loop complexity is O(n) and if-statement complexity is strip() complexity - O(m) - plus
# has_english_lowercase complexity - O(m) = O(m), where m is a length of s atring and n is a number of strings,
# so it is n*m = => O(n*m)
# Since the file is read line by line, it is not loaded into the memory as a whole.
# 2. Time and space complexity of iterools.groupby is O(m).
# Time complexity of for-loop is O(m) and of if-statement is O(1), because the label is one character.
# Time complexity of str(len(list(group))) is O(m), because time complexity of list() is O(m) in worst case scenario,
# time complexity of len() is O(1) and and we can think of time complexity of str(), which is O(s),
# where s is a length of integer, as a constant.
# Overall time complexity of compress_string function is O(m^2).
# 3. Time and space complexity of writing to file is O(n).
# 4. Overall time complexity of the script is O(n*m*m^2) = O(n*m^3).
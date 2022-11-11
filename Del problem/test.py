import re
import os

# make fasta data into single line format
fr = open('Tcongo_epimastigote.fas', 'r')  # read, and it is the input data(make sure it is in the same folder of this script)
fw = open('single_line.fas', 'w')  # write
seq = {}
for line in fr:
    if line.startswith('>'):  # judge if it starts from ‘>’
        name = line.split()[0]  # Use spaces as delimiters
        seq[name] = ''
    else:
        seq[name] += line.replace('\n', '')
fr.close()
for i in seq.keys():
    fw.write(i)
    fw.write('\u0020')  # space
    fw.write(seq[i])
    fw.write('\n')
fw.close()

# Find '-' and delete data containing it
missing = re.compile(r'[A-T]-|-{2,}|-[A-T]')
file = open('single_line.fas', 'r')
result = []
for line in file:
    if missing.search(line):
        pass
    else:
        result.append(line)
file.close()

file = open(r'del_Tcongo_epimastigote.fas', 'w') # rename the out put data here
for j in result:
    file.write(j)
file.close()
os.remove('single_line.fas') # delete single_line.fas caz dont need it

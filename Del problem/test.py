
import re

# make fasta data into single line format
fr = open('dash.fas', 'r')  # read
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

# Find 'A-T' like thing and delete data containing this
missing = re.compile(r'[A-T]\-[A-T]')
file = open('single_line.fas', 'r')
result = []
for line in file:
    print(line)
    print(missing.search(line))
    if missing.search(line):
        pass
    else:
        result.append(line)
file.close()

file = open(r'del_data.txt', 'w')
for j in result:
    file.write(j)
file.close()

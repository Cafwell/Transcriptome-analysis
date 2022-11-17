import re
import os
import sys
import shutil
import glob
import fileinput


def fas_pre():
    # get fasta file paths and names
    mypath = os.getcwd()
    files = glob.glob(os.path.join(mypath, '*.fas'))
    for file in files:
        fasta_names = os.path.basename(file)
        print(file)
        print(fasta_names)

    # get the number of fas files
    count = 0
    fas_files = os.listdir(mypath)
    for fas_file in fas_files:
        ext = os.path.splitext(fas_file)[-1]
        if ext == '.fas':
            count = count + 1
    while count > 1:
        print("There are " + str(count) + " '.fas' files")
        break
    else:
        print("There is only 1 '.fas' file")

    # copy and rename
    os.makedirs("monoline")
    for file_obj in fas_files:
        if file_obj.endswith('.fas'):
            file_path = os.path.join(mypath, file_obj)
            file_name, file_extend = os.path.splitext(file_obj)
            new_name = 'single_' + file_name + file_extend
            newfile_path = os.path.join("monoline", new_name)
            shutil.copyfile(file_path, newfile_path)


fas_pre()


# single line     missing = re.compile(r'[A-T]-|-{2,}|-[A-T]')
def single():
    os.chdir("monoline")
    new_path = os.getcwd()
    new_files = os.listdir(new_path)
    for filename in new_files:
        with open(filename) as f:
            line = f.read()
        with open(filename, 'w') as f:
            line = line.replace('\n', '').replace('>', '\n>')
            for aa in line:
                f.write(aa)
            f.close()


single()


'''
def del_dash():
    
del_dash()
'''

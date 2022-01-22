import os
import shutil
import platform

if platform.system() != 'Linux':
    print('Cannot run on any OS apart from linux.....exiting.')
    exit()
dir_names_for_extensions_dict = {
    'pdf' :'PDFs',
    'txt' : 'Text',
    'mp3' : 'MP3',
    'mp4' : 'MP4',
    'doc' : 'Docs'
}

path = str(input('Enter the path to a directory ( slash separated path ) ::'))
print('Files in your dir are -------- \n ')
all_files = os.listdir(path)

files_grouped_by_types = {}

for file in all_files:
    file_info = file.split('.')
    if len(file_info) < 2:
        continue
    print(file_info)
    if file_info[1] not in files_grouped_by_types.keys():
        files_grouped_by_types[file_info[1]] = []
    files_grouped_by_types[file_info[1]].append(file_info[0])

if len(files_grouped_by_types) == 0:
    print('Error...No files detected in given path to be grouped !')
    exit()
    
for ext, file_names in files_grouped_by_types.items():
    print(dir_names_for_extensions_dict[ext] + ' files are -> ')
    for file in file_names:
        print(file)
    print('\n\n')

print('Creating appropriate dirs for your files and grouping them........')

for ext,file_names in files_grouped_by_types.items():
    if ext not in dir_names_for_extensions_dict.keys():
        continue
    dir_name_for_ext = dir_names_for_extensions_dict[ext]

    if dir_name_for_ext not in all_files:
        os.makedirs(os.path.join(path, dir_name_for_ext))
    
    for file_name in file_names:
        full_file_name = file_name +'.'+ ext
        shutil.move(os.path.join(path,full_file_name), os.path.join(path, dir_name_for_ext))
    
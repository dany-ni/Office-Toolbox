import os
import shutil
import pandas as pd
import copy

# if a subfolder does not exist in a folder, create it
def create_folder(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)



# remove empty folder
def remove_empty_folder(folder_path):
    num = 0
    for entry in os.scandir(folder_path):
        if entry.is_file():
            num += 1
    if num == 0:
        shutil.rmtree(folder_path)



# move one file from one folder to another folder if it is not in another folder
def move_file(file_name, source_folder_path, destination_folder_path):
    source_path = os.path.join(source_folder_path, file_name)
    destination_path = os.path.join(destination_folder_path, file_name)

    if not os.path.exists(destination_folder_path):
        os.makedirs(destination_folder_path)

    # if file is not in destination folder, move it to destination folder
    if not os.path.exists(destination_path):
        shutil.move(source_path, destination_path)



# move files listed in an excel from one folder to another folder. file names are in 'column_of_file_name' in one excel
def move_files(excel_path, column_of_file_name, source_folder_path, destination_folder_path):
    files_and_dirs_list = os.listdir(source_folder_path)
    files_list = [f for f in files_and_dirs_list if os.path.isfile(os.path.join(source_folder_path, f))]
    df = pd.read_excel(excel_path)
    files_no_need_to_move_list = copy.deepcopy(files_list)
    files_not_found_list = []

    for file_name in df[column_of_file_name].values:
        if file_name in files_list:
            source_path = os.path.join(source_folder_path, file_name)
            destination_path = os.path.join(destination_folder_path, file_name)
            shutil.move(source_path, destination_path)
            files_no_need_to_move_list.remove(file_name)
        else:
            print('cannot move ', file_name, 'because it is not found in', source_folder_path)
            files_not_found_list.append(file_name)

    print('files in excel not found in source folder: ', files_not_found_list)
    print('files not in excel but in source folder: ', files_no_need_to_move_list)

   

# move all csv from a folder (including subfolders) to another folder
def move_all_csv(source_folder_path, destination_folder_path):
    for root, dirs, files in os.walk(source_folder_path):
        for file in files:
            if file.endswith((".CSV", '.csv')):
                try:
                    shutil.move(os.path.join(root, file), destination_folder_path)
                except shutil.Error as e:
                    error_message = f'shutil error: {file} - {e}'
                    print(error_message)
                    with open(r'destination_folder_path\error_log.txt', 'a') as f:
                        f.write(error_message + '\n')



# move all pdf from a folder (including subfolders) to another folder
def move_all_pdf(source_folder_path, destination_folder_path):
    for root, dirs, files in os.walk(source_folder_path):
        for file in files:
            if file.endswith((".PDF", '.pdf')):
                try:
                    shutil.move(os.path.join(root, file), destination_folder_path)
                except shutil.Error as e:
                    error_message = f'shutil error: {file} - {e}'
                    print(error_message)
                    with open(r'destination_folder_path\error_log.txt', 'a') as f:
                        f.write(error_message + '\n')

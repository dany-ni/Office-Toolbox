import os
import pandas as pd

def extract_csv_name_with_extension(folder_path):
    file_name_list = os.listdir(folder_path)
    csv_name_with_extension_list = []

    for file_name in file_name_list:
        if file_name.endswith(('.CSV', '.csv')):
            csv_name_with_extension_list.append(file_name)
    
    df = pd.DataFrame(csv_name_with_extension_list, columns=['csv name with extension'])
    excel_path = os.path.join(folder_path, 'csv name with extension.xlsx')
    df.to_excel(excel_path, index=False)



def extract_csv_name_without_extension(folder_path):
    file_name_list = os.listdir(folder_path)
    csv_name_with_extension_list = []

    for file_name in file_name_list:
        if file_name.endswith(('.CSV', '.csv')):
            csv_name_without_extension = str(os.path.splitext(file_name)[0])
            csv_name_with_extension_list.append(csv_name_without_extension)
    
    df = pd.DataFrame(csv_name_with_extension_list, columns=['csv name without extension'])
    excel_path = os.path.join(folder_path, 'csv name without extension.xlsx')
    df.to_excel(excel_path, index=False)



def extract_pdf_name_with_extension(folder_path):
    file_name_list = os.listdir(folder_path)
    pdf_name_with_extension_list = []

    for file_name in file_name_list:
        if file_name.endswith(('.PDF', '.pdf')):
            pdf_name_with_extension_list.append(file_name)
    
    df = pd.DataFrame(pdf_name_with_extension_list, columns=['pdf name with extension'])
    excel_path = os.path.join(folder_path, 'pdf name with extension.xlsx')
    df.to_excel(excel_path, index=False)



def extract_pdf_name_without_extension(folder_path):
    file_name_list = os.listdir(folder_path)
    pdf_name_without_extension_list = []

    for file_name in file_name_list:
        if file_name.endswith(('.PDF', '.pdf')):
            pdf_name_without_extension = str(os.path.splitext(file_name)[0])
            pdf_name_without_extension_list.append(pdf_name_without_extension)
    
    df = pd.DataFrame(pdf_name_without_extension_list, columns=['pdf name without extension'])
    excel_path = os.path.join(folder_path, 'pdf name without extension.xlsx')
    df.to_excel(excel_path, index=False)

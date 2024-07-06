import pandas as pd
import os
import shutil

# Verify that each PDF has a corresponding CSV, and each CSV has a corresponding PDF. Move the CSV files that do not have a corresponding PDF to the folder 'csv without pdf', and move the PDF files that do not have a corresponding CSV to 'pdf without csv'.
# Premise: each pair of CSV and PDF files share identical names.

def csv_pdf_pairing(csv_folder_path, pdf_folder_path, excel_path):

    csv_list = [ele for ele in os.listdir(csv_folder_path) if ele.endswith(('.CSV', '.csv'))]
    pdf_list = [ele for ele in os.listdir(pdf_folder_path) if ele.endswith(('.PDF', '.pdf'))]
    file_list_df = pd.DataFrame({'csv name':csv_list, 'pdf name':'no pdf'}, dtype='str')

    find_pdf_list = []
    for i in range(file_list_df.shape[0]):
        for pdf_name in pdf_list:
            if file_list_df.loc[i, 'csv name'][:-4] == pdf_name[:-4]:
                file_list_df.loc[i, 'pdf name'] = pdf_name
                find_pdf_list.append(pdf_name)
                break
        
    if len(pdf_list) != len(find_pdf_list):
        for pdf_name in pdf_list:
            if pdf_name not in find_pdf_list:
                file_list_df.loc[file_list_df.index[-1]+1, 'pdf name'] = pdf_name
                file_list_df.loc[file_list_df.index[-1], 'csv name'] = 'no csv'
        
    csv_without_pdf_folder_path = os.path.join(csv_folder_path, 'csv without pdf')
    if not os.path.exists(csv_without_pdf_folder_path):
        os.mkdir(csv_without_pdf_folder_path)
    
    pdf_without_csv_folder_path = os.path.join(pdf_folder_path, 'pdf without csv')
    if not os.path.exists(pdf_without_csv_folder_path):
        os.mkdir(pdf_without_csv_folder_path)    

    for i in range(file_list_df.shape[0]):
        if file_list_df.loc[i, 'pdf name'] == 'no pdf':
            csv_path = os.path.join(csv_folder_path, file_list_df.loc[i, 'csv name'])
            shutil.move(csv_path, csv_without_pdf_folder_path)
        elif file_list_df.loc[i, 'csv name'] == 'no csv':
            pdf_path = os.path.join(pdf_folder_path, file_list_df.loc[i, 'pdf name'])
            shutil.move(pdf_path, pdf_without_csv_folder_path)

    def remove_empty_folder(folder_path):
        num = 0
        for entry in os.scandir(folder_path):
            if entry.is_file():
                num += 1
        if num == 0:
            shutil.rmtree(folder_path)

    remove_empty_folder(csv_without_pdf_folder_path)
    remove_empty_folder(pdf_without_csv_folder_path)


    file_list_df.to_excel(excel_path, index=False)


                
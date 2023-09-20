import pandas as pd
import subprocess
import csv
def remove_first_row(filename):
    with open(filename, 'r') as file:
        csv_data=csv.reader(file)
        data_list=list(csv_data)
    data_list=data_list[1:]
    with open(filename, 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerows(data_list)
# input_file='date_coordinate\\design1_table.xlsx'
input_file=r'C:\\Users\\user\\git\\github\\py2305_graph\\data_coordinate\\table_design1.xlsx'
# output_file='date_coordinate\\table_design1.csv'
# output_file='coordinate_design1.csv'
output_file=r'C:\\Users\\user\\git\\github\\py2305_graph\\data_coordinate\\coordinate_design1.csv'
df=pd.read_excel(input_file)
df=df.drop(df.columns[[0, 1, 2, 4]], axis=1)
df=df.applymap(lambda x:str(x).replace('"', ''))
df=df.applymap(lambda x:str(x).replace('mm', ''))
new_df=pd.DataFrame()
for i in range(len(df)):
    new_row=pd.DataFrame([[df.iloc[i, 0]]], columns=[df.columns[0]])
    new_df=new_df.append(new_row, ignore_index=True)
    new_row=pd.DataFrame([[df.iloc[i, 1]]], columns=[df.columns[0]])
    new_df=new_df.append(new_row, ignore_index=True)
new_df=new_df.stack().reset_index(drop=True)
new_df.to_csv(output_file, index=False)
remove_first_row(output_file)
subprocess.Popen(['start', output_file], shell=True)
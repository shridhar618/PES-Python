#Excel File Operations
import openpyxl
#Load the workbook
wb=openpyxl.load_workbook('sample.xlsx')

#Get the active sheet
sheet=wb.active

#Read a cell value
cell_value=sheet['A1'].value
print(f"Value in A1: {cell_value}")

#Write a value to a cell
sheet['B1']=42

#Save the workbook
wb.save('sample_modified.xlsx')

#Create a new workbook and add data
new_wb=openpyxl.Workbook()
#call the active sheet
new_sheet=new_wb.active
new_sheet['A1']="Hello, Excel!"
new_sheet['B1']=100
new_wb.save('new_sample.xlsx')

#Read the data from a cell
print(f'The value stored in cell D5 is : {sheet["D5"].value}')

#Iterate through rows and columns
for row in sheet.iter_rows(min_row=1, max_row=5, min_col=1, max_col=2):
    for cell in row:
        print(cell.value, end=' ')
    print()
    
    
#Get sheet names
sheet_names=wb.sheetnames
print(f"Sheet names in the workbook: {sheet_names}")


#Create a new sheet             
new_sheet=wb.create_sheet(title="NewSheet")
wb.save('sample_modified.xlsx')


#Delete a sheet
del wb['NewSheet']
wb.save('sample_modified.xlsx')


#Get max row and columns
max_row=sheet.max_row
max_column=sheet.max_column
print(f"Max Row: {max_row}, Max Column: {max_column}")



#reading data from a range of cells
list1=list()
for value in sheet.iter_rows(min_row=1, max_row=4, min_col=1, max_col=4, values_only=True):
    list1.append(value)
print(list1)


#Merge cells
sheet.merge_cells('C1:D1')
sheet['C1']="Merged Cell"
wb.save('sample_modified.xlsx')


#Unmerge cells
sheet.unmerge_cells('C1:D1')
wb.save('sample_modified.xlsx') 


#Displaying the values in a tabular method
for e1,e2,e3,e4 in list1:
    '''unpacking of a tuple'''
    print("{:<10} {:<35} {:<10} {:<5}".format(e1,e2,e3,e4))
    
    
#wite to a cell
sheet['K1']='Total Sales'
sheet['K2']=1500
sheet['K3']=2000
sheet['K4']=2500
wb.save('sample_modified.xlsx')


#add values in the 4 columns to get total sales
r_pos=2
col_pos=11 #column K
t_sales=((sheet.cell(row=r_pos, column=col_pos).value) +
         (sheet.cell(row=r_pos+1, column=col_pos).value) +
         (sheet.cell(row=r_pos+2, column=col_pos).value))
sheet.cell(row=r_pos+3, column=col_pos).value=t_sales
wb.save('sample_modified.xlsx')

#create a loop to sum the sales value in each row
r_pos=1
for i in range(1,sheet.max_row+1):
    r_pos+=1
    N_sales=sheet.cell(row=r_pos, column=11).value
    S_sales=sheet.cell(row=r_pos, column=12).value
    E_sales=sheet.cell(row=r_pos, column=13).value
    W_sales=sheet.cell(row=r_pos, column=14).value
    total_sales=N_sales+S_sales+E_sales+W_sales
    sheet.cell(row=r_pos, column=15).value=total_sales
wb.save('sample_modified.xlsx')
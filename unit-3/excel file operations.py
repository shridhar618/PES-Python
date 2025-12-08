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


#Merge cells
sheet.merge_cells('C1:D1')
sheet['C1']="Merged Cell"
wb.save('sample_modified.xlsx')


#Unmerge cells
sheet.unmerge_cells('C1:D1')
wb.save('sample_modified.xlsx') 
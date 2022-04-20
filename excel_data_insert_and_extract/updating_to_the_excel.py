'''
emp_id | emp_name | job_name  | manager_id | hire_date  | salary  | commission | dep_id
--------+----------+-----------+------------+------------+---------+------------+--------
  68319 | KAYLING  | PRESIDENT |            | 1991-11-18 | 6000.00 |            |   1001\n
  66928 | BLAZE    | MANAGER   |      68319 | 1991-05-01 | 2750.00 |            |   3001\n
  67832 | CLARE    | MANAGER   |      68319 | 1991-06-09 | 2550.00 |            |   1001\n
  65646 | JONAS    | MANAGER   |      68319 | 1991-04-02 | 2957.00 |            |   2001\n
  67858 | SCARLET  | ANALYST   |      65646 | 1997-04-19 | 3100.00 |            |   2001\n
  69062 | FRANK    | ANALYST   |      65646 | 1991-12-03 | 3100.00 |            |   2001\n
  63679 | SANDRINE | CLERK     |      69062 | 1990-12-18 |  900.00 |            |   2001\n
  64989 | ADELYN   | SALESMAN  |      66928 | 1991-02-20 | 1700.00 |     400.00 |   3001\n
  65271 | WADE     | SALESMAN  |      66928 | 1991-02-22 | 1350.00 |     600.00 |   3001\n
  66564 | MADDEN   | SALESMAN  |      66928 | 1991-09-28 | 1350.00 |    1500.00 |   3001\n
  68454 | TUCKER   | SALESMAN  |      66928 | 1991-09-08 | 1600.00 |       0.00 |   3001\n
  68736 | ADNRES   | CLERK     |      67858 | 1997-05-23 | 1200.00 |            |   2001\n
  69000 | JULIUS   | CLERK     |      66928 | 1991-12-03 | 1050.00 |            |   3001\n
  69324 | MARKER   | CLERK     |      67832 | 1992-01-23 | 1400.00 |            |   1001
'''

#------------------------------------------------------------------------------------------------------------

import openpyxl
from openpyxl.utils import column_index_from_string as cifs


# updating value into the excel file
def update_values(file_name, sheet_name, row_start, row_end, col_start, col_end):

    wb = openpyxl.load_workbook(file_name)
    sheet = wb[sheet_name]
    
    # updating values in the list
    for i, r in enumerate(range(row_start, row_end + 1)):
        a = data[2:][i].split("|")
        for j, c in enumerate(range(col_start, col_end + 1)):
            sheet.cell(row=r, column=c).value = a[j].split("\n")[0].strip()

    # saving the excel file
    try:
        wb.save('Book1.xlsx')
    except PermissionError:
        print("The Excel file is already open!!! Please close it first...")
    else:
        print("Done")



# values
file_name = 'Book1.xlsx'
sheet_name =  'Sheet1'

# starting row and end row
row_start = 14
row_end = 27

# starting column and end column
col_start = cifs('B')
col_end = cifs('I')



# opening the data file
try:
    with open("data.dat") as f_obj:
        data = f_obj.readlines()
except Exception as e:
    print(e)
    print("Data is not inserted!!!")
else:
    update_values(file_name, sheet_name, row_start, row_end, col_start, col_end)




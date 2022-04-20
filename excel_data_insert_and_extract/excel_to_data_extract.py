import openpyxl as op
import datetime as dt


def func(work_book, start, end):
    wb = op.load_workbook(work_book)
    l = []
    for row in wb['Sheet1'][start: end]:
        m = []
        for c in row:
            if type(c.value) == dt.datetime:
                m.append(str(c.value).split(" ")[0])
            elif c.value == None:
                m.append('')
            else:
                m.append(c.value)
        l.append(tuple(m))
    
    [print(f"\t{i}",end=",\n") for i in l]


file_name = 'Book1.xlsx'
start = 'B14'
end = 'I27'

l = func(file_name, start, end)







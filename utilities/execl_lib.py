import pytest

from xlrd import open_workbook

objpath=f"C:/Users/Gowtham p/PycharmProjects/pythonProject2/shoppersstack/data/objects.xls"
def read_locators(sheetname):
    book=open_workbook(objpath)
    sheet=book.sheet_by_name(sheetname)
    used_row=sheet.nrows
    data={}
    for i in range(1,used_row):
        row=sheet.row_vlaues(i)
        data[row[0]]=(row[1],row[2])

    return data

def attach_element(sheetname):
    def _attach_elements(cls):
        book=open_workbook(objpath)
        sheet=book.sheet_by_name(sheetname)
        used_row=sheet.nrows
        for i in range(1,used_row):
            row=sheet.row_values(i)
            setattr(cls,row[0],(row[1],row[2]))
        return cls
    return _attach_elements

path= f"/data/testdata.xls"
def read_headers(sheetname,test_case_name):
    book=open_workbook(path)
    sheet=book.sheet_by_name(sheetname)
    used_row=sheet.nrows

    for i in range(0,used_row):
        row=sheet.row_values(i)
        if row[0] == test_case_name:
            headers=sheet.row_values(i-1)
            valid_header=[ item.strip() for item in headers if item.strip()]
            return ",".join(valid_header[2:])


def read_data(sheetname,test_case_name):

    book=open_workbook(path)
    sheet=book.sheet_by_name(sheetname)
    used_rows=sheet.nrows
    final_data=[]
    for i in range(0,used_rows):
        row=sheet.row_values(i)
        if row[0] == test_case_name:
            temp_record=[item.strip() for item in row if item.strip()]
            if temp_record[1].upper() == "YES":
                final_data.append(tuple(temp_record[2:]))

    return final_data











































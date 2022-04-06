import xlrd,os,time

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'..\element_info_dates\element_ingo.xlsx')

wordbook = xlrd.open_workbook(excel_path)
sheet = wordbook.sheet_by_name('logo_page')

# value = sheet.cell_value(1,0)
row_cout =sheet.nrows  #获取行数
element_infos = { }
for i in range(1,row_cout):
    element_info = {}
    element_info['element_name'] = sheet.cell_value(i,1)
    element_info['locatar_type'] = sheet.cell_value(i, 2)
    element_info['locator_value'] = sheet.cell_value(i, 3)
    element_info['timeout'] = sheet.cell_value(i, 4)
    element_infos[sheet.cell_value(i,0)] = element_info
    # {self.username_inputbox = {'element_name':'用户名输入框',} {键：{值}}
print(element_infos)
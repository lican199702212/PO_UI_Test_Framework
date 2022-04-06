import xlrd
import os

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'..\element_info_dates\element_ingo.xlsx')
class ElementdataUtiles:
    def __init__(self,page_name,element_path = excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.row_cout = self.sheet.nrows  # 获取行数

    def get_element_info(self):
        element_infos = { }
        for i in range(1,self.row_cout):
            element_info = {}
            element_info['element_name'] = self.sheet.cell_value(i,1)
            element_info['locatar_type'] = self.sheet.cell_value(i, 2)
            element_info['locator_value'] = self.sheet.cell_value(i, 3)
            element_info['timeout'] = self.sheet.cell_value(i, 4)
            element_infos[self.sheet.cell_value(i,0)] = element_info
            # {self.username_inputbox = {'element_name':'用户名输入框',} {键：{值}}
        return element_infos

if __name__ == '__main__':
    elements = ElementdataUtiles('logo_page').get_element_info()
    print(elements)
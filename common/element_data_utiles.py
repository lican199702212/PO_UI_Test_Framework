import xlrd
import os
from common.config_utiles import local_config

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'..\element_info_dates\element_ingo.xlsx')
class ElementdataUtiles:
    def __init__(self,module_name,page_name,element_path = excel_path):#module_name模块 page_name页面名称
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(module_name)
        self.page_name = page_name
        self.row_cout = self.sheet.nrows  # 获取行数

    def get_element_info(self):
        element_infos = { }
        for i in range(1,self.row_cout):
            if self.sheet.cell_value(i, 2) ==self.page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i,1)
                element_info['locatar_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                timeout_value = self.sheet.cell_value(i, 5)
                element_info['timeout'] = timeout_value if isinstance(timeout_value,float) else local_config.time_out
                element_infos[self.sheet.cell_value(i,0)] = element_info
                # {self.username_inputbox = {'element_name':'用户名输入框',} {键：{值}}
        return element_infos

if __name__ == '__main__':
    elements = ElementdataUtiles('login','logo_page').get_element_info()
    print(elements)
    for i in elements.values():
        print(i)
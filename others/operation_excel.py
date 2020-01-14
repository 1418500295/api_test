import xlrd

# testdata = xlrd.open_workbook("../dataconfig/interface.xlsx")
# # 根据sheet编号获取指定sheet
# table = testdata.sheet_by_index(0)
# # 打印行数
# print(table.nrows)
# # 通过坐标获取指定数据
# testdata = table.cell_value(2, 3)
# print(testdata)

class OperationExcel():
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id

        else:
            self.file_name = "../dataconfig/interface.xlsx"
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheet_by_index(self.sheet_id)
        return tables

    # 获取sheet的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取指定单元格的数据
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

if __name__ == '__main__':
    opera = OperationExcel()
    print(opera.get_data().nrows)
    print(opera.get_lines())
    print(opera.get_cell_value(1, 2))


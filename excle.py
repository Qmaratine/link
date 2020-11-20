import xlrd,xlwt

wb = xlrd.open_workbook('F:\\python\\py\\data\\眉山市56张表格-9.25cyp\\14-附表2.2.4-1 眉山市水资源量情况调查表.xls')
excle_name = wb.sheet_names()[0]

'''
wbook = xlwt.Workbook(encoding="utf-8",style_compression= 0)
wtable = wbook.add_sheet('sheet1',cell_overwrite_ok= True)

count = 0
keyword = unicode('东坡区','utf-8')
wb.ragged_rows
# for i in range()
'''
sheet_object = wb.sheets() #获取所有sheet对象
sheet1_object = wb.sheet_by_index(0) # 通过index获取第一个sheet对象
# 获取sheet1中的有效行数
nrows = sheet1_object.nrows
print(nrows) 

# 获取sheet1中第3行的数据
all_row_values = sheet1_object.row_values(rowx=nrows-1)
print(all_row_values) 
# 获取sheet1中第rowx+1行，第colx+1列的单元对象的str值
cell_info = sheet1_object.cell(rowx=nrows-1, colx=5).value
print(cell_info) 
print(type(cell_info)) 
# 获取sheet1中第rowx+1行，第colx+1列的单元对象
cell_info = sheet1_object.cell(rowx=nrows-1, colx=5)
print(cell_info) 
print(type(cell_info)) 

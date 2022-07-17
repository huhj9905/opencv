import pandas as pd

def sortExcel(path,sheet,tableHeader):
    data = pd.read_excel(path, sheet)
    data.sort_values(by=tableHeader, inplace=True, ascending=False)

    data.to_excel(path, index=False)
    return "处理成功"

sortExcel(r"D:\MyNode\github\opencv\test.xlsx","Sheet1","表头.2")




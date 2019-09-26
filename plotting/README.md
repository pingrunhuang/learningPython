# Read data
* numpy.loadtxt('path/file.csv', dtype='string', delimiter=',')
* numpy.genfromtxt()
* Read data from microsoft: `pip install xlrd`
    ```python
    import xlrd
    file = 'path/file.xlsx'
    wb = xlrd.open_workbook(filename=file)
    ws = wb.sheet_by_name('Sheet1')
    dataset = []
    for row in range(ws.nrows):
      col = []
      for col in range(ws.ncols):
          col.append(ws.cell(row, col).value)
          dataset.append(col)
    ``` 

# plotting libs 
1. matplotlib
2. seaborn
3. py-echart
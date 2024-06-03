from common import get_col

col_data = get_col('Data/inventory2.csv', 'quant')
med = col_data.median()
print("Median", med)

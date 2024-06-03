from common import get_col

col_data = get_col('Data/inventory.csv', 'price')
avg = col_data.mean()
std = col_data.std()
print("Average price", avg)
print("Std Dev:", std)

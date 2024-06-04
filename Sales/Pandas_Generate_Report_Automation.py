#!/usr/bin/env python
# coding: utf-8

# # Report the Annual Profit for each product

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

sns.set()

# Loading the dataset
df = pd.read_csv('toys.csv')

# Creating a pivot table
df_pvt = ( df
         .drop(columns=['Quarter'])
         .pivot_table(index="Product",
                     aggfunc="sum")
        )

# Calculate the profit
df_pvt.loc[:, 'Profit'] = df_pvt.Revenue - df_pvt.Expenditure


# Plotting the graph
fig, ax = plt.subplots(figsize=(4, 2))

ax = sns.barplot(
        data = (df_pvt
               .reset_index()
               .sort_values('Profit',
                            ascending=False)
               ),
        x = "Product",
        y = "Profit",
        ax = ax
    );

plt.title("Annual Profit Per Product");
plt.tight_layout()
plt.savefig('annual_report.png')

# Export to excel file
excel_filename = "Annual_Report.xlsx"
worksheet_name = "2014"


image_data = BytesIO()
ax.figure.savefig(image_data)

with pd.ExcelWriter(excel_filename, engine="xlsxwriter") as FH:
    df_pvt.sort_values('Profit', ascending=False)\
            .to_excel(FH, sheet_name = worksheet_name)
    shobj = FH.sheets[worksheet_name]
    shobj.insert_image('F4', '' , {'image_data': image_data})

print("Generated Annual report")

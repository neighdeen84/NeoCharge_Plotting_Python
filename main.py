# This is a Python script to graph real power and temperature vs a timestamp.

import pandas as pd
import matplotlib.pyplot as plt

# Reading in the output CSV:
output = pd.read_csv("output_w_NeoCharge.csv")

# Finding the column labels to extract:
#WH = pd.read_csv("wh1.csv")
# Checking column labels for the WH (this worked when I had all the columns imported, and it helped me pick em):
#for col in df_WH.columns:
#    print(col)

# Reading in the WH CSV:
col_list = ["# timestamp", " temperature"] # watch out, get the exact labels. white space counts
WH = pd.read_csv("wh1.csv", usecols=col_list)

# Putting the CSVs into a dataframe:
df_output = pd.DataFrame(data=output)
df_WH = pd.DataFrame(data = WH)

#print(df1)




#print(df_output)

# Naming the columns:
#df_output.columns = ['Time', 'Power', 'unwanted_col_1', 'unwanted_col_2']

# Popping the last two NaN columns (not sure why this happened, will investigate):
#df_output.pop("unwanted_col_1")
#df_output.pop("unwanted_col_2")

# Getting rid of PST:
#df_output['Time'] = df_output['Time'].str.replace("PST", "")

# Checking for NaN values:
#print(df_output.isnull().values.any())

# Printing the data:
#print(df_output)


# Plotting:
#df_output.plot(x ='Time', y='Power', kind = 'line')
#plt.show()

df_WH.plot(x ='# timestamp', y=' temperature', kind = 'line')
plt.show()


print("Generating Unified file")
# # Master Node Unification

# Importing Modules
import csv
import pandas as pd

# Importing CSVs
df_0 = pd.read_csv("./processedFiles/node_0.csv")
df_1 = pd.read_csv("./processedFiles/node_1.csv")
df_2 = pd.read_csv("./processedFiles/node_2.csv")

# Adding Results from Node CSV Files
ca_col = df_0["Casos_activos_covid"] + df_1["Casos_activos_covid"] + df_2["Casos_activos_covid"]
def_col = df_0["Defunciones"] + df_1["Defunciones"] + df_2["Defunciones"]

# Getting Final CSV File with info for Covid Map (Mexico)
df = pd.DataFrame({"Estados":df_0["Estados"],"Casos_activos_covid": ca_col, "Defunciones":def_col})
df

# Saving Final CSV File
df.to_csv('./processedFiles/covid_data.csv')

print("Done!")



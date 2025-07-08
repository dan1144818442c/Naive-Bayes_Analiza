import kagglehub
import pandas as pd
# Download latest version
# path = kagglehub.dataset_download("eswarchandt/phishing-website-detector")
#
# print("Path to dataset files:", path)
# print(pd.read_csv('DATA_CSV/CSV_phishing.csv'))
df = pd.read_csv(r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_buy_comuter.csv")
print(df.value_counts(df.columns[-1]))
print()
dic = {}
for i , j  in df.value_counts(df.columns[-1]).items():
    print(i , j)
    dic[i] = j
print(df)
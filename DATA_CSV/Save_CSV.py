import pandas as pd
from  DATA_CSV import clean_data
def save_CSV():
    df = pd.read_csv(r"C:\Users\1\Downloads\titanic\train.csv", index_col='PassengerId')
    df =  clean_data.clean_nall_and_duplicates(df)
    df.to_csv('CSV_titanic.csv')
def save_CSV_titanic():
    df = pd.read_csv(r"C:\Users\1\Downloads\titanic\train.csv", index_col='PassengerId')
    df = df.drop(columns=["Name", "Ticket", "Cabin", "PassengerId"], errors='ignore')

    df["Age"] = pd.cut(df["Age"], bins=[0, 60, 90], labels=["Child","Adult"])
    df["Fare"] = pd.qcut(df["Fare"], q=3, labels=["Low", "Medium", "High"])

    df["Parch"] = pd.cut(df["Parch"], bins=[-1, 0, 2, 6], labels=["None", "Few", "Many"])
    df["SibSp"] = pd.cut(df["SibSp"], bins=[-1, 0, 1, 8], labels=["Alone", "One", "Many"])

    df = df.dropna().drop_duplicates().reset_index(drop=True)


    df.to_csv("CSV_titanic.csv", index=False)

#
# def get_test_CSV_titanic():
#     df = pd.read_csv(r"C:\Users\1\Downloads\titanic\test.csv", index_col='PassengerId')
#     df = df.drop(columns=["Name", "Ticket", "Cabin", "PassengerId"], errors='ignore')  # עמודות מיותרות
#     df["Age"] = pd.cut(df["Age"], bins=[0, 60, 90], labels=["Child","Adult"])
#     df["Fare"] = pd.qcut(df["Fare"], q=3, labels=["Low", "Medium", "High"])
#     df = clean_data.clean_nall_and_duplicates(df)
#
#     return df
save_CSV_titanic()
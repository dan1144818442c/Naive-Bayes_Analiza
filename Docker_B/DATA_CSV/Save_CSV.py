import pandas as pd
from  DATA_CSV import clean_data
def save_CSV():
    df = pd.read_csv(r"C:\Users\1\Downloads\ex.csv")
    df =  clean_data.clean_nall_and_duplicates(df)
    df.to_csv('CSV_titanic.csv',index=False)
    # print(df["Survived"].value_counts(normalize=True))

# save_CSV()

# from sklearn.model_selection import train_test_split
# #
# def save_CSV_titanic_clean_split():
#     df = pd.read_csv(r"C:\Users\1\Downloads\titanic\train.csv")
#
#     # Drop עמודות לא שימושיות
#     df.drop(columns=["Ticket", "Cabin"], inplace=True)
#
#     # חילוץ תואר מהשם
#     df["Title"] = df["Name"].str.extract(' ([A-Za-z]+)\.', expand=False)
#     df["Title"] = df["Title"].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr',
#                                        'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
#     df["Title"] = df["Title"].replace({'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'})
#     title_map = {"Mr": 0, "Miss": 1, "Mrs": 2, "Master": 3, "Rare": 4}
#     df["Title"] = df["Title"].map(title_map).fillna(4).astype(int)
#
#     # המרה של Sex
#     df["Sex"] = df["Sex"].map({'male': 0, 'female': 1}).astype(int)
#
#     # Embarked
#     df["Embarked"] = df["Embarked"].fillna("S")
#     df["Embarked"] = df["Embarked"].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)
#
#     # FamilySize ו-IsAlone
#     df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
#     df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
#
#     # מילוי גיל לפי Sex ו־Pclass
#     df["Age"] = df.groupby(['Sex', 'Pclass'])["Age"].transform(lambda x: x.fillna(x.median()))
#
#     # מילוי Fare חסרים
#     df["Fare"] = df["Fare"].fillna(df["Fare"].median())
#
#     # חלוקה ל־Train ו־Test לפני יצירת AgeBand/FareBand
#     train_df, test_df = train_test_split(df, test_size=0.3, random_state=42, stratify=df["Survived"])
#
#     # קביעת גבולות על פי train בלבד
#     age_bins = pd.cut(train_df["Age"], 5, retbins=True)[1]
#     fare_bins = pd.qcut(train_df["Fare"], 4, retbins=True, duplicates="drop")[1]
#
#     # יצירת AgeBand ו־FareBand לפי אותם גבולות גם ב־test
#     for d in [train_df, test_df]:
#         d["AgeBand"] = pd.cut(d["Age"], bins=age_bins, labels=[0, 1, 2, 3, 4], include_lowest=True)
#         d["FareBand"] = pd.cut(d["Fare"], bins=fare_bins, labels=[0, 1, 2, 3], include_lowest=True)
#
#     # איחוד מחדש, המרה ל־int
#     df_clean = pd.concat([train_df, test_df])
#     df_clean["AgeBand"] = df_clean["AgeBand"].astype(int)
#     df_clean["FareBand"] = df_clean["FareBand"].astype(int)
#
#     # רק העמודות החשובות
#     df_clean = df_clean[["Survived", "Pclass", "Sex", "AgeBand", "FareBand", "Embarked", "Title", "FamilySize", "IsAlone"]]
#
#     # שמירה
#
#     df_clean.to_csv("CSV_titanic_clean.csv", index=False)

#     # הדפסת איזון נתונים
#     # print("📊 אחוזי הישרדות בדאטה החדש:")
#     # print(df_clean["Survived"].value_counts(normalize=True))

# save_CSV_titanic_clean_split()

def get_test_CSV_titanic():
    df = pd.read_csv(r"C:\Users\1\Downloads\titanic\test.csv", index_col='PassengerId')
    df = df.drop(columns=["Name", "Ticket", "Cabin", "PassengerId"], errors='ignore')  # עמודות מיותרות
    df["Age"] = pd.cut(df["Age"], bins=[0, 60, 90], labels=["Child","Adult"])
    df["Fare"] = pd.qcut(df["Fare"], q=3, labels=["Low", "Medium", "High"])
    df = clean_data.clean_nall_and_duplicates(df)
    df.to_csv("CSV_titanic_clean.csv", index=False)

    return df
get_test_CSV_titanic()
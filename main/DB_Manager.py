import kagglehub
import pandas as pd
import model.Base_classified as Base_classified
import os
from logging_ import Logging
import importlib.util

# class DB_Manager:
#     def __init__(self):
#         self.file_to_class = {
#             "classified_computer_csv.py": "classified",
#             "classified_phishing_csv.py": "classified",
#             "classified_titanic.py": "classified"
#         }
#
#     def show_all_DB(self):
#         files = []
#         for file_name in os.listdir("UI_all_CSV_DB"):
#             if file_name.endswith(".py"):
#                 files.append(file_name)
#         files = files[1::]
#         for idx, name in enumerate(files):
#             print(f"choose {idx} for:", name)
#         return files
#
#     def load_class_object(self):
#         Logging.Log("Load the correct classifier's class.")
#         files = self.show_all_DB()
#         # try:
#
#         while True:
#             try:
#                 choice = int(input(f"Enter your choice (0 to {len(files) - 1}): "))
#                 if 0 <= choice < len(files):
#                     selected_file = files[choice]
#                     print(f"You selected: {selected_file}")
#                     break
#                 else:
#                     print("Number out of range. Try again.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")
#
#         full_path = os.path.join("UI_all_CSV_DB", selected_file)
#
#         class_name = self.file_to_class.get(selected_file)
#         # print(class_name)
#         if not class_name:
#             print("Unknown class for selected file.")
#             return None
#
#         module_name = selected_file[:-3]
#         spec = importlib.util.spec_from_file_location(module_name, full_path)
#         module = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(module)
#
#         ClassObj = getattr(module, class_name)
#         instance = ClassObj()
#         # print(f"Created instance of {class_name}")
#         Logging.Log("Created successfully instance : " + class_name )
#         return instance
#
#         # except Exception as e:
#         #     print(f"Error: {e}")
#         #     return None
#
#     def predict_by_input(self , instance,dic_input=False):
#         # return instance.predict_by_input_of_all_columns()
#         return instance.predict_by_input_of_spsific_columns(dic_input)
#
# # a = DB_Manager()
# # a.load_class_object().predict_by_input()

from DATA_CSV.clean_data import get_clean_df , clean_nall_and_duplicates
from logging_ import Logging

class DB_Manager:
    def __init__(self):
        self.datasets_config = {
            "Titanic": {
                "file": r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_titanic.csv",
                "target": "Survived",
                "preprocess_fn": clean_nall_and_duplicates,
                "index_col": None
            },
            "Phishing": {
                "file": r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_phishing.csv",
                "target": "Label",
                "preprocess_fn": clean_nall_and_duplicates,
                "index_col": "Index"
            },
            "Computer": {
                "file": r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\DATA_CSV\CSV_buy_comuter.csv",
                "target": "Category",
                "preprocess_fn": clean_nall_and_duplicates,
                "index_col": "id"
            }
        }

    def show_all_DB(self):
        for idx, name in enumerate(self.datasets_config.keys()):
            print(f"choose {idx} for:", name)
        return list(self.datasets_config.keys())

    def load_classifier(self):
        Logging.Log("Load the correct classifier's class.")
        dataset_names = self.show_all_DB()

        while True:
            try:
                choice = int(input(f"Enter your choice (0 to {len(dataset_names) - 1}): "))
                if 0 <= choice < len(dataset_names):
                    selected_name = dataset_names[choice]
                    print(f"You selected: {selected_name}")
                    break
                else:
                    print("Number out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        config = self.datasets_config[selected_name]
        file_path = config["file"]
        target_column = config['target']
        index_col = config['index_col']
        preprocess_fn = config['preprocess_fn']

        df = get_clean_df(file_path=file_path , index_col=index_col , preprocess_fn=preprocess_fn)

        classifier = Base_classified.classified(data_frame=df , target_column=target_column)

        Logging.Log("Created successfully instance : classified")
        return classifier

    def predict_by_input(self, instance, dic_input=False):
        return instance.predict_by_input_of_all_columns()
        # return instance.predict_by_input_of_spsific_columns(dic_input)

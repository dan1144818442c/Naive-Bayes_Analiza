import kagglehub
import pandas as pd
import UI_all_CSV_DB
import os
import importlib.util


import os
import importlib.util

class DB_Manager:
    def __init__(self):
        self.file_to_class = {
            "classified_computer_csv.py": "classified",
            "classified_phishing_csv.py": "classified"
        }

    def show_all_DB(self):
        files = []
        for file_name in os.listdir("UI_all_CSV_DB"):
            if file_name.endswith(".py"):
                files.append(file_name)
        for idx, name in enumerate(files):
            print(f"choose {idx} for:", name)
        return files

    def load_class_object(self):
        files = self.show_all_DB()
        try:
            choice = int(input("Enter your choice: "))
            selected_file = files[choice]
            full_path = os.path.join("UI_all_CSV_DB", selected_file)

            class_name = self.file_to_class.get(selected_file)
            if not class_name:
                print("Unknown class for selected file.")
                return None

            module_name = selected_file[:-3]
            spec = importlib.util.spec_from_file_location(module_name, full_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            ClassObj = getattr(module, class_name)
            instance = ClassObj()
            print(f"Created instance of {class_name}")
            return instance

        except Exception as e:
            print(f"Error: {e}")
            return None

    def predict_by_input(self , instance,dic_input=False):
        # return instance.predict_by_input_of_all_columns()
        return instance.predict_by_input_of_spsific_columns(dic_input)

# a = DB_Manager()
# a.load_class_object().predict_by_input()

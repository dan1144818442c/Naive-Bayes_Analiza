import pandas as pd
import logging_.Logging


class Naive_Bayes:
    def __init__(self , df , target_column =False ):
        self.df = df
        self.dict_ = {}
        if not target_column or target_column not in self.df.columns:

            self.target_column = self.df.columns[-1]
        else:
            self.target_column = target_column
            # print(target_column)
        self.dic_detiels_target = self.get_dic_of_detelis_Target_variable()

    def get_dic_after_updetes(self):
        return self.update_if_have_zero()


    def get_len_dict_target_val(self):
        num = 0
        for key,val in self.dic_detiels_target.items():
            num += val
        return num
    def get_df_Target_variable(self):
        df_Target_variable  = self.df.value_counts(self.target_column)
        # print(df_Target_variable)
        return df_Target_variable

    def get_dic_of_detelis_Target_variable(self):
        df_target = self.get_df_Target_variable()
        dic_deteils_target = {}
        for key, val in df_target.items():
            dic_deteils_target[key] = val

        return dic_deteils_target

    def get_all_dic_with_0(self):
        val_target = self.get_dic_of_detelis_Target_variable().keys()

        for key in val_target:
            self.dict_[key] = {}
            for colum in self.columsname_without_target():
                self.dict_[key][colum] = self.get_dic_of_val_count_with_0(colum)

        return self.dict_


    def columsname_without_target(self):
        columns = self.df.columns
        list_resulot = [col for col in columns if col != self.target_column]
        return list_resulot

    def get_dic_of_val_count_with_0(self,column):
        dic = {}
        for val in self.df.value_counts(column).index.to_list():
            dic[val] = 0
        return dic

    def fiil_dict(self):
        logging_.Logging.Log("Creates a dictionary full of values with the probability")
        dict_with_0 = self.get_all_dic_with_0()

        for key_terget  , val in dict_with_0.items():
            for column , key_column in val.items():
                for val_count  , val_of_val_count in  key_column.items():
                    num_count = self.get_num_of_val_count_in_target(name_target= self.target_column , val_target=key_terget , name_column=column ,name_valu_count=val_count)
                    num_target =self.dic_detiels_target[key_terget]
                    dict_with_0[key_terget][column][val_count] =num_count / num_target
        new_dic_with_val = dict_with_0
        # print(new_dic_with_val)
        self.dict_ = new_dic_with_val
        return new_dic_with_val


    def chek_have_zero_colomn_level(self , colomn_val):
        for name , val in colomn_val.items():
            if val == 0:
                # print(val , " " , name)
                return True
        return False
    def  update_if_have_zero(self):
        logging_.Logging.Log("update the dictionary if_have_zero.")

        self.fiil_dict()
        for key_terget, val in self.dict_.items():
            have_zero_level_column = False

            for column, key_column in val.items():
                have_zero_level_column = self.chek_have_zero_colomn_level(key_column)
                if have_zero_level_column:
                    for val_count, val_of_val_count in key_column.items():
                        num_count = self.get_num_of_val_count_in_target(name_target=self.target_column,
                                                                        val_target=key_terget, name_column=column,
                                                                        name_valu_count=val_count) +1
                        num_target = self.dic_detiels_target[key_terget] +1

                        self.dict_[key_terget][column][val_count] = num_count / num_target
        return self.dict_


    def get_num_of_val_count_in_target(self ,  name_target , val_target , name_column , name_valu_count):
        count =self.df[(self.df[name_column] == name_valu_count) & (self.df[name_target] == val_target)].shape[0]
        return count

    def get_dic_by_input(self):
        logging_.Logging.Log("Prompts the user for values to create a dictionary")
        dic_choice = {}
        for target_name , value_target in self.dict_.items():
            for column , val_column in value_target.items():
                choice = self.get_choice_by_valu( column ,val_column )
                dic_choice[column] = choice
            break
        return dic_choice
    def predict__by_full_dic_columns(self , dic_choice):
        logging_.Logging.Log("predict according to dictionary")
        dic_res = {}
        for target_name, value_target in self.dict_.items():
            predict_num = 1
            for column, val_column in value_target.items():
                predict_num *= val_column[dic_choice[column]]
            target_percent = (self.dic_detiels_target[target_name])/ self.get_len_dict_target_val()
            predict_num *=target_percent
            # print(target_name ," : " , predict_num)
            dic_res[target_name] = predict_num
        max_key = max(dic_res, key=dic_res.get)
        return (max_key , self.target_column)

    def predict_by_row(self , dic_choice):
        dic_res = {}
        for target_name, value_target in self.dict_.items():
            predict_num = 1
            for column, val_column in value_target.items():
                try:
                    if column != self.target_column:
                        predict_num *= val_column[dic_choice[column]]
                except KeyError as e:
                    print(f"KeyError: column={column}, value={dic_choice[column]}")
                    raise


            target_percent = (self.dic_detiels_target[target_name]) / self.get_len_dict_target_val()
            predict_num *= target_percent
            # print(target_name + " : " ,  predict_num)
            dic_res[target_name] = predict_num
        max_key = max(dic_res, key=dic_res.get)
        return max_key

    def get_choice_by_valu(self, column_name: str, column_val: dict):
        keys = list(column_val.keys())

        while True:
            print(f"\n Select a value for column '{column_name}':")
            for idx, key in enumerate(keys, start=1):
                print(f"Enter {idx} to select '{key}'")

            choice = input("Enter your choice: ")

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            choice = int(choice)
            if 1 <= choice <= len(keys):
                selected_key = keys[choice - 1]
                print(f" You selected '{selected_key}' for column '{column_name}'\n")
                return selected_key
            else:
                print(" Invalid choice. Try again.\n")


from DB_Manager import DB_Manager
import json
class MainApp:
    def action(self):
        print("Welcome to the Prediction System!")
        print("==================================\n")

        manager = DB_Manager()

        while True:
            instance = manager.load_classifier()

            if not instance:
                print("Error loading the class. Trying again...\n")
                continue


            print(f"Success rate: {instance.Accuracy_percentages}")
            # dic = json.loads(input("enter dic of choice"))
            # res, target_column = manager.predict_by_input(instance=instance , dic_input=dic)
            res, target_column = manager.predict_by_input(instance=instance )
            print("\n Prediction Result:")
            print(f"The probability that '{target_column}' will be: {res}!!")
            print("#############################################################################\n")
            # except Exception as e:
            #     print(f"Error during prediction: {e}")

            again = input("Would you like to make another prediction? (y/n): ").lower()
            if again != 'y':
                print("Goodbye!")
                break

if __name__ == "__main__":
    MainApp().action()







    
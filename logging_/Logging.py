import  datetime

def Log(message):
    path = r"C:\Users\1\Desktop\DATA_Analiza\Naive Bayes\logging_\log.txt"
    with open(path , 'a') as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write('\n' + message + "     : " + current_time + '\n')

import  datetime

def Log(message):
    path = "logging_/log.txt"
    with open(path , 'a') as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write('\n' + message + "     : " + current_time + '\n')

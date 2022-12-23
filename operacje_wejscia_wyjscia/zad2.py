import os
import datetime

print("Current directory is", os.getcwd())
currentDir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(currentDir, filename)
print("\nThe constructed file path is: ", fullpath)

data_input_catalog = 'c:\\temp\data_input'
data_output_catalog = 'c:\\temp\data_output'
today = datetime.date.today()
today_output_catalog = today.strftime("%Y-%m-%d")
is_input_catalog = os.path.isdir(data_input_catalog)
is_output_catalog = os.path.isdir(data_output_catalog)
is_today_catalog = not os.path.isdir(today_output_catalog) and not os.path.isfile(today_output_catalog)



if is_input_catalog and is_output_catalog and is_today_catalog:
    print("conditions met!, we can continue")

else:
    print("brakuje jednego z katalogu")

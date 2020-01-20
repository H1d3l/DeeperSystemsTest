import json


try:
    file_json = open('source_file_2.json','r')
    data_json = json.load(file_json)
    print(data_json)

except Exception as erro:
    print("ocorreu um erro ao carregar o arquivo")
    print("o erro é:{}".format(erro))
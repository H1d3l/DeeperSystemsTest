import json
from operator import itemgetter


try:
    file_json = open('source_file_2.json','r')
    data_json = json.load(file_json)
    data_json_sorted = sorted(data_json,key=itemgetter('priority'))

    dict_managers = {}

    for value in data_json_sorted:
        for i in value['managers']:
            if(i in value['managers']):
                dict_managers.update({'managers':i,'name':value['name']})
                print(dict_managers)


    #print(json.dumps(data_json_sorted, sort_keys=True, indent=4))
except Exception as erro:
    print("ocorreu um erro ao carregar o arquivo")
    print("o erro é:{}".format(erro))
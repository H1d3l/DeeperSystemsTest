import json
from operator import itemgetter


try:
    file_json = open('source_file_2.json','r')
    data_json = json.load(file_json)
    data_json_sorted = sorted(data_json,key=itemgetter('priority'))


    dict_managers = {}
    dict_watchers = {}

    for values in data_json_sorted:
        for i in values:
            for k in values['managers']:
                if(k not in dict_managers):
                    dict_managers.update({k:[values[ 'name']]})
                else:
                    if(values['name'] in dict_managers[k]):
                        pass
                    else:
                        dict_managers[k].append(values['name'])

    for values in data_json_sorted:
        for i in values:
            for k in values['watchers']:
                if(k not in dict_watchers):
                    dict_watchers.update({k:[values[ 'name']]})
                else:
                    if(values['name'] in dict_watchers[k]):
                        pass
                    else:
                        dict_watchers[k].append(values['name'])

    dict_managers_json = json.dumps(dict_managers, sort_keys=True, indent=4)
    dict_watchers_json = json.dumps(dict_watchers, sort_keys=True, indent=4)
    data_json_sorted = json.dumps(data_json_sorted, sort_keys=True, indent=4)

    save_dict_managers = open('manager.json','w')
    save_dict_watchers = open('watchers.json','w')
    save_dict_source_file = open('source_file_sorted.json','w')

    save_dict_managers.write(dict_managers_json)
    save_dict_watchers.write(dict_watchers_json)
    save_dict_source_file.write(data_json_sorted)


    save_dict_managers.close()
    save_dict_watchers.close()
    save_dict_source_file.close()

except Exception as erro:
    print("ocorreu um erro ao carregar o arquivo")
    print("o erro é:{}".format(erro))
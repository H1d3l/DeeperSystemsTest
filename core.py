import json


try:
    file_json = open('source_file_2.json','r')
    data_json = json.load(file_json)

    dict_managers = {}
    list_managers = []
    for value in data_json:
        for i in value['managers']:
            #if(i not in dict_managers):
            #if(i in value['managers'] and i not in dict_managers):
            dict_managers.update({'managers':i,'name':list_managers.append(value['name'])})  
            
                #dict_managers.update({'managers':i,'name':list_managers.append(value['name'])   })
                #print(i,value['managers'])
            #print(list_managers)
            #print(True,i,value['managers'],value['name'],dict_managers)
        print(dict_managers)        
        
        
except Exception as erro:
    print("ocorreu um erro ao carregar o arquivo")
    print("o erro é:{}".format(erro))
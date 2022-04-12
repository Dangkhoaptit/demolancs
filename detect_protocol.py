import json
import glob,os

listDeProName = []
listDeProNameok = []
dataList = []
listServer = []
listServerOk = []
dictServer = dict()

def ktra(s):
    ok = False
    for x in listDeProNameok:
        if (s==x):
            ok = True
            break
    return(ok)

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files :
            all_files.append (os.path.abspath(f))
    return all_files
songs = get_files ('/home/le_dang_khoa/Downloads/Telegram Desktop/24_5e_be_5c_a1_49/24:5e:be:5c:a1:49')


for single_file in songs:
    dataList.append(single_file)
newdataList = sorted(dataList)

for file in newdataList:
    with open(file) as json_file:
        try:
            data = json.load(json_file)
            try:
                for u in data['flows']['br-lan']:
                    try:
                        for i in range(0, len(u)):
                            try:
                                data_name = data['flows']['br-lan'][i]['detected_protocol_name']
                                # host_server_name = data['flows']['br-lan'][i]['host_server_name']
                                # host_server_ip = data['flows']['br-lan'][i]['local_ip']

                                listDeProName.append(data_name)
                                # dictServer["host_server_name"] = host_server_name
                                # dictServer["host_server_ip"] = host_server_ip
                                # listServer.append(dictServer)
                                
                            
                                # print(DetProNam)

                            except:
                                print("skipping_1")
                    except:
                        print("skipping_2")
            except:
                print("skipping_3")
        except KeyError:
            print(f'Skipping')
                               

for x in listDeProName:
    if(ktra(x) == False):
        listDeProNameok.append(x)

for x in listDeProNameok:
    NumAppe = listDeProName.count(x)
    data_dict = {
            "detected_protocol_name" : x,
            "number of appearances" : NumAppe
        }
    print(x, "ok")
    with open("detected_protocol_name123.json", 'a+') as file:
        json.dump(data_dict, file, sort_keys=True, indent=4)
        file.write(",\n")

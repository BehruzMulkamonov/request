# import requests
# url = 'http://api.weatherapi.com/v1'
# response = requests.get(url + '/current.json', params={'key': 'f32b2cd7fe364abd8d8182803230603', 'q': 'Tashkent'})
# datas = response.json()
# for data in datas:
#     print(data)
#     for key,value in datas.items():
#         print(key, value)
#         print('\n')
#
# for i in datas[data]:
#     for key, value in i.items():
#         print( key, value)
#     print("\n")


# import requests
#
# url = 'http://api.weatherapi.com/v1'
# r = requests.get(url + '/current.json', params={'key': 'f32b2cd7fe364abd8d8182803230603', 'q': 'Tashkent'})
# coin = r.json()
# for i in coin:
#     print(i, ":")
#     for key, value in coin[i].items():
#         print(" ", key, value)
#     print("\n")
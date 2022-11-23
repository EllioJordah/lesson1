MoscowCity={"city": "Москва", 
    "temperature": "20"}
print(type(MoscowCity['city']))
MoscowCity['temperature']=int(MoscowCity['temperature'])
MoscowCity['temperature']=MoscowCity['temperature']-5
print(MoscowCity)
print(MoscowCity.get('country',"RUSSIA"))
#MoscowCity['country']='RUSSIA'
MoscowCity['date']='27.05.2019'
print(MoscowCity)
print(len(MoscowCity))
import json

sonlar = (12 , 24 , 38 , 44)
sonlar_json = json.dumps(sonlar)

bemor = {
    "ism" : "Otabek Xurramov",
    "yosh" : 18 ,
    "oila" : True ,
    "farzandlar" : ("Dovud" , "Kamola"),
    "alergiya" : None ,
    "dorilar" : [
        {"nomi" : "Analgin" , "miqdori" : 0.5 },
        {"nomi" : "Panadol" , "miqdori" : 1.2}
    ]
}

bemor_json = json.dumps(bemor , indent = 4)

with open('sonlar.json' , 'w') as f:
    json.dump(sonlar , f)

bemor2 = json.loads(bemor_json)
print(bemor2)
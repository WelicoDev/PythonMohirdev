import json

files = ['talaba1.json' , 'talaba2.json' , 'talaba3.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        print(f"{filename} file mavjud emas !")
    else:
        print(talaba["ism"])
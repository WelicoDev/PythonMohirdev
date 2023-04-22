#FILeError

filename = 'date.txt'
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"{filename} file mavjud emas !")
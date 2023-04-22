# mehmonlar =["Islom" , "Javohir" , "Akbar" ,"Ozodbek","jahongir"]
# for mehmon in mehmonlar:
#     print("Salom ",mehmon)

# starts=['********','*******','******','*****','****','***','**','*','**','***','****','*****','******','*******']
# for star in starts:
#     print(star)
# for mehmon in mehmonlar :
#     print(f"Xurmatli mehmon {mehmon} sizni 20-oktabr kuni 19:00 da Turkiston to'yxonasida bo'ladigan to'yga taklif etamiz !")
#     print("Hurmat bilan Xudoynazarovlar oilasi !\n")

# numbers=list(range(1,21))
# for item in numbers:
#     print(f"{item} soning kvadrati {item**2} ga teng ")

# numbers=list(range(16))
# numberpow=[]
# for num in numbers:
#     numberpow.append(num**2)

# print(numbers)
# print(numberpow)

freinds=[]
print("Yaqin do'stlaringiz kim ?")
n=int(input("Ularni sonini kiriting >>>"))
for dost in range(n):
    freinds.append(input(f"{dost+1} - chi do'stingizni ismini kiriting : "))

print(freinds)
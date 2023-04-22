from googletrans import Translator

tarjimon = Translator()

# text_uz = "Python - dunyodagi eng mashhur dasturlash tili "
#
# tarjima = tarjimon.translate(text_uz)
# print(tarjima.origin)
# print(tarjima.text)
# print(tarjima.src)
#
# tarjima_ru = tarjimon.translate(text_uz , dest='ru')
# print(tarjima_ru.text)
#
# # Ingliz tilidan tarjima
# matn_en = "Tashkent is the capital of Uzbekitan"
# tarjima_uz = tarjimon.translate(matn_en , dest='uz')
# print(tarjima_uz.text)

msg = "Tarjima uchun so'z kiriting (chiqib ketish uchun \'\q' deb yozing ) : >>> "
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text,src ='uz',dest='en')
        print(tarjima.text)

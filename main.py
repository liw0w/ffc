word = input("Введите непонятное слово (большими буквами!): ")
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "КРИНЖ": "Что-то странное, стыдное"
            }
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("упс, такого мы еще не слышали! видимо мы не настолько молоды😄")

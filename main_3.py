import requests

txt = """
1.en -> uz
2.uz -> en
3.stop
ma'lumot kirit:
"""
while 1:

    a = int(input(txt))
    if a == 1:
        uz_text = input("inglizga kiriting:")
        uz = f'http://127.0.0.1:8000/uz_en/{uz_text}'
        resp = requests.get(uz)
        print(resp.json()["en"])
    elif a == 2:
        en_text=input('uzbekcha kiriting:')
        en = f'http://127.0.0.1:8000/en_uz/{en_text}'
        resp2 = requests.get(en)
        print(resp2.json()['uz'])
    else:
        print('thank you')
        break

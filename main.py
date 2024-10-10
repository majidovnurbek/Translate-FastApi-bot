from fastapi import FastAPI
from dataAPI import translate_text,translate_texta

app = FastAPI()


@app.get('/uz_en/{namee}')
async def uz_en(namee: str):
    data = translate_text(namee)
    return {
        'en': data
    }


@app.get('/en_uz/{name}')
async def en_uz(name: str):
    dat = translate_texta(name)
    return {
        'uz': dat
    }
print()
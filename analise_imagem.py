from PIL import Image
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)
imagem = Image.open(r'C:\Users\86297\Desktop\RPA\RPA\imagens\tidalwave_payoff_poster_brazil_caf2354b.jpeg')

resposta = client.models.generate_content(
    model= 'gemini-3.6-flash',
    contents=[
        'Descreve a qual filme pertence o cartaz.',
        imagem
        ]
)

print(resposta.text)
import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN_API_VALIDAR_CPF_CNPJ = os.getenv('VALIDAR_CNPJ_CPF_TOKEN')

st.title('Consulta de CNPJ')

with st.form('consulta de CNPJ'):
    cnpj = st.text_input('CNPJ', max_chars=14, placeholder='02694984000137')
    consultar = st.form_submit_button('Consultar')

    if consultar:
        url = f'https://api.invertexto.com/v1/validator?token={TOKEN_API_VALIDAR_CPF_CNPJ}&value={cnpj}&type=cnpj'
        req = requests.get(url)
        if req.status_code == 200:
            if req.json()['valid']:
                req = requests.get(f'https://publica.cnpj.ws/cnpj/{cnpj}').json()
                st.write(req)
                # url = f"https://publica.cnpj.ws/cnpj/{cnpj}."
                # response = requests.request("GET", url).json()
                # st.write(response)
            else:
                st.write('CNPJ INEXISTENTE')
        else:
            st.write(req.status_code)





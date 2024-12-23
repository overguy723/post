from openai import OpenAI
import openai
import streamlit as st

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

st.title("🎁 제폼 홍보 포스터 생성기")
keyword = st.text_input("키워드를 입력하세요.")

if st.button("생성하기🔥"):
    with st.spinner('생성 중입니다.'):
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model='gpt-4',
            messages=[
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 작성해줘"
                },
                {
                    "role": "user",
                    "content": keyword,
                }
            ]
        )

        result = response.choices[0].message.content
        st.write(result)
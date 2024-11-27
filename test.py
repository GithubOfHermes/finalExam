import streamlit as st
import requests
from urllib.parse import quote

KAKAO_API_KEY = "94725ef93944f848cca35aa808d1deee"

# HTML을 렌더링하기 위한 기본 템플릿
def generate_map_link_html(query):
    encoded_query = quote(query)
    return f"""
    <div>
        <a href="https://map.kakao.com/link/search/{encoded_query}" target="_blank">여기를 클릭하여 '{query}' 지도 보기</a>
    </div>
    """

# Streamlit 앱 구현
def main():
    st.title("Kakao Map Search")
    st.write("검색하고자 하는 장소를 입력하세요.")

    user_input = st.text_input("검색어를 입력하세요:")

    if user_input:
        if " 지도" in user_input:
            query = user_input.replace(" 지도", "")
            map_html = generate_map_link_html(query)
            st.components.v1.html(map_html, height=100)
        else:
            st.warning("'지도'를 붙여서 입력해 주세요 (예: '서울 지도').")

if __name__ == "__main__":
    main()

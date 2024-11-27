import streamlit as st
import requests
from urllib.parse import quote

KAKAO_API_KEY = "94725ef93944f848cca35aa808d1deee"

# HTML을 렌더링하기 위한 기본 템플릿
def generate_map_iframe_html(query):
    encoded_query = quote(query)
    return f"""
    <iframe
        width="800"
        height="400"
        src="https://map.kakao.com/?q={encoded_query}"
        frameborder="0"
        allowfullscreen>
    </iframe>
    """

# Streamlit 앱 구현
def main():
    st.title("여행 가이드 챗봇")
    st.write("검색하고자 하는 장소를 입력하세요.")

    user_input = st.text_input("검색어를 입력하세요:")

    if user_input:
        if " 지도" in user_input:
            query = user_input.replace(" 지도", "")
            map_html = generate_map_iframe_html(query)
            st.components.v1.html(map_html, height=400)
        else:
            st.warning("'지도'를 붙여서 입력해 주세요 (예: '서울 지도').")

if __name__ == "__main__":
    main()

import streamlit as st
import requests
from urllib.parse import quote

KAKAO_API_KEY = "94725ef93944f848cca35aa808d1deee"

# HTML을 렌더링하기 위한 기본 템플릿
def generate_map_iframe_html(query, width, height):
    encoded_query = quote(query)
    return f"""
    <iframe
        width="{width}"
        height="{height}"
        src="https://map.kakao.com/link/search/{encoded_query}"
        frameborder="0"
        allowfullscreen>
    </iframe>
    """

# Streamlit 앱 구현
def main():
    # 화면 너비 제한 해제 설정
    st.set_page_config(layout="wide")

    st.title("여행 가이드 챗봇")
    st.write("검색하고자 하는 장소를 입력하세요.")

    user_input = st.text_input("질문을 입력하세요:")

    if user_input:
        if " 지도" in user_input:
            query = user_input.replace(" 지도", "")
            map_html = generate_map_iframe_html(query, 800, 500)
            st.components.v1.html(map_html, height=500)
        elif " 맛집" in user_input:
            query = user_input.replace(" 맛집", "")
            col1, col2 = st.columns([2, 1])
            with col1:
                map_html_1 = generate_map_iframe_html(query, 800, 500)
                st.components.v1.html(map_html_1, height=500)
            with col2:
                map_html_2 = generate_map_iframe_html(query, 380, 500)
                st.components.v1.html(map_html_2, height=500)
        else:
            st.warning("'지도' 또는 '맛집'을 붙여서 입력해 주세요 (예: '서울 지도', '춘천 닭갈비 맛집').")

if __name__ == "__main__":
    main()

import streamlit as st
import requests

# フォームの設定
st.title("レコビュ - レビューを投稿して次に読む本を見つけよう")

st.subheader("レビューを投稿する")
with st.form("review_form"):
    book_title = st.text_input("本のタイトル")
    positive_points = st.text_area("ポジティブポイント")
    negative_points = st.text_area("ネガティブポイント")
    submit_button = st.form_submit_button("送信")

# フォームが送信された場合
if submit_button:
    # APIエンドポイントにデータを送信
    data = {
        "book_title": book_title,
        "positive_points": positive_points,
        "negative_points": negative_points
    }
    response = requests.post("http://localhost:8000/submit_review/", json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"レビューを投稿しました: {book_title}")
        st.subheader("次におすすめの本")
        st.write(f"おすすめの本: {result['recommended_book']}")
    else:
        st.error("レビューの投稿に失敗しました。")


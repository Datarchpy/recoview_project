import streamlit as st

# ヘッダー
st.title("レコビュ - レビューを投稿して次に読む本を見つけよう")

# フォーム
st.subheader("レビューを投稿する")
with st.form("review_form"):
    book_title = st.text_input("本のタイトル")
    positive_points = st.text_area("ポジティブポイント")
    negative_points = st.text_area("ネガティブポイント")
    submit_button = st.form_submit_button("送信")

# フォームが送信された場合
if submit_button:
    st.success(f"レビューを投稿しました: {book_title}")
    st.subheader("次におすすめの本")
    # 固定されたレコメンドを表示
    st.write("おすすめの本: 'サンプル本タイトル'")

import streamlit as st

# ------------------------------------------------------------
# メインエリア
st.set_page_config(page_title="📝MemoMemo📝", layout="wide")
st.title("✒️ MemoMemo")
col1, col2 = st.columns([7, 3])


with col1:
    tab1, tab2 = st.tabs(["🔖 タグ検索", "📝 メモ一覧"])

    # tab1 タグ検索
    with tab1:
        st.write("ここにはタグ検索を表示します。")
    # tab2 メモ一覧表示
    with tab2:
        st.write("ここにはメモ一覧を表示します。")

with col2:
    st.write("ここにはタグ一覧を表示します。")

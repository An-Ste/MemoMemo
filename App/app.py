import streamlit as st
from data.memo_class import generate_memo, show_all_memos, search_by_tag, manage_tags

# ------------------------------------------------------------
# メインエリア
st.set_page_config(page_title="📝MemoMemo📝", layout="wide")
st.title("✒️ MemoMemo")
col1, col2 = st.columns([7, 3])


with col1:
    generate_memo()
    tab1, tab2 = st.tabs(["📝 メモ一覧", "🔖 タグ検索"])

    # tab1 タグ検索
    with tab1:
        st.write("ここにはメモ一覧を表示します。")
        show_all_memos()
    # tab2 メモ一覧表示
    with tab2:
        st.write("ここにはタグ検索を表示します。")
        search_by_tag()

with col2:
    st.write("ここにはタグ一覧を表示します。")
    manage_tags()

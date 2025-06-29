import streamlit as st
import pandas as pd

# CSVファイルを読み込む
try:
    df = pd.read_csv("万博概要.csv")
except Exception as e:
    st.error(f"CSVファイルの読み込みに失敗しました: {e}")
    st.stop()

# 🔍 検索欄
keyword = st.text_input("パビリオン名を検索", "")

# 🔍 部分一致で名称を検索（空欄なら全件表示）
if keyword:
    matched = df[df["名称"].astype(str).str.contains(keyword, case=False, na=False)]
else:
    matched = df.copy()

if not matched.empty:
    for idx, row in matched.iterrows():
        with st.expander(f"📍 {row['名称']}"):
            st.markdown(f"""
            - **エリア**: {row['エリア']}（{row['エリア詳細']}）  
            - **入場方式**: {row['入場方式']}  
            - **所要時間**: {row['所要時間']}   
            - **備考**: {row['備考']}
            """)
            if st.button(f"⏰ {row['名称']}の予約解放時刻を見る", key=idx):
                st.success(f"📅 当日予約解放予定時刻: {row['当日予約解放予定時刻']}")
else:
    st.warning("一致するパビリオンが見つかりませんでした。")

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(
    page_title="국가별 MBTI 분석",
    layout="wide"
)

st.title("🌍 국가별 MBTI 분석")

# ---------------------------
# 데이터 불러오기
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# ---------------------------
# 국가 선택
# ---------------------------
country_list = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "국가를 선택하세요",
    country_list
)

# ---------------------------
# 선택 국가 데이터
# ---------------------------
country_data = df[df["Country"] == selected_country].iloc[0]

mbti_columns = [
    "INFJ", "ISFJ", "INTP", "ISFP",
    "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP",
    "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

mbti_values = country_data[mbti_columns].astype(float)

# ---------------------------
# 내림차순 정렬
# ---------------------------
sorted_data = (
    pd.DataFrame({
        "MBTI": mbti_columns,
        "Value": mbti_values.values
    })
    .sort_values(by="Value", ascending=False)
)

# ---------------------------
# 색상 설정
# 1등 = 핫핑크
# 나머지 = 초록색 그라데이션
# ---------------------------
green_colors = [
    "#0b6623",
    "#1b7d35",
    "#2f9e44",
    "#40c057",
    "#69db7c",
    "#8ce99a",
    "#b2f2bb",
    "#d3f9d8",
    "#e9fac8",
    "#f4fce3",
    "#d8f5a2",
    "#c0eb75",
    "#94d82d",
    "#74b816",
    "#66a80f"
]

colors = ["hotpink"] + green_colors[:15]

# ---------------------------
# Plotly 그래프
# ---------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=sorted_data["MBTI"],
        y=sorted_data["Value"],
        marker_color=colors,
        text=sorted_data["Value"].round(2),
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2f}%<extra></extra>"
    )
)

# ---------------------------
# 그래프 꾸미기
# ---------------------------
fig.update_layout(
    title=f"{selected_country}의 MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율(%)",
    height=600,
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# 최고 비율 MBTI 표시
# ---------------------------
top_mbti = sorted_data.iloc[0]

st.success(
    f"🏆 {selected_country}에서 가장 높은 MBTI는 "
    f"'{top_mbti['MBTI']}' "
    f"({top_mbti['Value']:.2f}%) 입니다."
)

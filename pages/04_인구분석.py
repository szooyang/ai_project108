import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import re

st.set_page_config(
    page_title="행정구별 인구수",
    layout="wide"
)

st.title("📊 행정구별 인구수")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():

    filename = "population.csv"

    for enc in ["utf-8", "cp949", "euc-kr"]:
        try:
            return pd.read_csv(filename, encoding=enc)
        except:
            continue

    st.error("CSV 파일을 읽을 수 없습니다.")
    st.stop()


df = load_data()

# -----------------------------
# 행정구 열 찾기
# -----------------------------
district_col = df.columns[0]

# 서울시 전체 행 제거 (선택사항)
districts = df[district_col].dropna().unique()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택한 행정구
row = df[df[district_col] == selected_district].iloc[0]

# -----------------------------
# 나이 데이터 추출
# -----------------------------
ages = []
populations = []

for col in df.columns:

    col_str = str(col)

    # 0세 ~ 100세 이상 포함된 열만 선택
    if "세" in col_str:

        match = re.search(r'(\d+)세', col_str)

        if match:
            age = int(match.group(1))

            try:
                value = int(str(row[col]).replace(",", ""))
            except:
                continue

            ages.append(age)
            populations.append(value)

# 데이터프레임 생성
graph_df = pd.DataFrame({
    "Age": ages,
    "Population": populations
})

graph_df = graph_df.sort_values("Age")

# -----------------------------
# 그래프
# -----------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=graph_df["Age"],
        y=graph_df["Population"],
        mode="lines",
        line=dict(
            color="skyblue",
            width=4
        ),
        hovertemplate=
        "<b>나이</b>: %{x}세<br>" +
        "<b>인구수</b>: %{y:,}명<extra></extra>"
    )
)

fig.update_layout(
    title=f"{selected_district} 연령별 인구수",
    height=650,

    plot_bgcolor="#f2f2f2",
    paper_bgcolor="white",

    hovermode="x unified",

    xaxis=dict(
        title="나이",
        showgrid=True,
        gridcolor="white",
        range=[0, 100]
    ),

    yaxis=dict(
        title="인구수",
        showgrid=True,
        gridcolor="white"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# 요약 통계
# -----------------------------
st.subheader("📌 기본 통계")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "총 인구",
        f"{sum(populations):,}명"
    )

with col2:
    max_idx = graph_df["Population"].idxmax()
    st.metric(
        "인구가 가장 많은 나이",
        f"{graph_df.loc[max_idx,'Age']}세"
    )

with col3:
    st.metric(
        "최고 인구수",
        f"{graph_df['Population'].max():,}명"
    )

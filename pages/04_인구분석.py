import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="행정구별 인구 분석",
    layout="wide"
)

st.title("📊 행정구별 인구 분석")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("population.csv", encoding="utf-8")
    return df

df = load_data()

# 첫 번째 열을 행정구로 사용
district_col = df.columns[0]

districts = df[district_col].unique()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택한 행정구 데이터
row = df[df[district_col] == selected_district].iloc[0]

ages = []
population = []

for col in df.columns[1:]:

    age_text = str(col)

    # 숫자 추출
    numbers = ''.join(filter(str.isdigit, age_text))

    if numbers:
        ages.append(int(numbers))
        population.append(row[col])

# 데이터프레임 생성
graph_df = pd.DataFrame({
    "Age": ages,
    "Population": population
})

graph_df = graph_df.sort_values("Age")

# Plotly 그래프
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
    plot_bgcolor="#f2f2f2",
    paper_bgcolor="white",
    height=650,

    xaxis=dict(
        title="나이",
        showgrid=True,
        gridcolor="white"
    ),

    yaxis=dict(
        title="인구수",
        showgrid=True,
        gridcolor="white"
    ),

    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

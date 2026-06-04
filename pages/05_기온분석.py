import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="서울 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
@st.cache_data
def load_data():
    encodings = ["cp949", "euc-kr", "utf-8"]

    for enc in encodings:
        try:
            df = pd.read_csv("seoul.csv", encoding=enc)
            return df
        except:
            continue

    raise ValueError("파일을 읽을 수 없습니다.")

df = load_data()

# -----------------------------------
# 컬럼명 정리
# -----------------------------------
df.columns = df.columns.str.strip()

date_col = df.columns[0]
avg_col = df.columns[2]
min_col = df.columns[3]
max_col = df.columns[4]

# 날짜 변환
df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

df = df.dropna(subset=[date_col])

df["연도"] = df[date_col].dt.year
df["월"] = df[date_col].dt.month
df["일"] = df[date_col].dt.day

# -----------------------------------
# 날짜 선택
# -----------------------------------
st.sidebar.header("날짜 선택")

month = st.sidebar.selectbox(
    "월 선택",
    sorted(df["월"].unique())
)

day_list = sorted(
    df[df["월"] == month]["일"].unique()
)

day = st.sidebar.selectbox(
    "일 선택",
    day_list
)

# -----------------------------------
# 선택 날짜 데이터
# -----------------------------------
selected = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

selected = selected.sort_values("연도")

selected[max_col] = pd.to_numeric(
    selected[max_col],
    errors="coerce"
)

selected[min_col] = pd.to_numeric(
    selected[min_col],
    errors="coerce"
)

selected = selected.dropna(
    subset=[max_col, min_col]
)

# -----------------------------------
# 그래프
# -----------------------------------
st.subheader(f"📈 {month}월 {day}일의 연도별 기온 변화")

fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=selected["연도"],
        y=selected[max_col],
        mode="lines+markers",
        name="최고기온",
        line=dict(
            color="hotpink",
            width=3
        ),
        marker=dict(size=6),
        hovertemplate=
        "연도: %{x}<br>" +
        "최고기온: %{y:.1f}℃<extra></extra>"
    )
)

# 최저기온
fig.add_trace(
    go.Scatter(
        x=selected["연도"],
        y=selected[min_col],
        mode="lines+markers",
        name="최저기온",
        line=dict(
            color="lightskyblue",
            width=3
        ),
        marker=dict(size=6),
        hovertemplate=
        "연도: %{x}<br>" +
        "최저기온: %{y:.1f}℃<extra></extra>"
    )
)

fig.update_layout(
    height=650,
    hovermode="x unified",
    xaxis_title="연도",
    yaxis_title="기온(℃)",
    legend_title="구분",
    template="plotly_white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------------
# 통계
# -----------------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "최고기온 평균",
        f"{selected[max_col].mean():.1f}℃"
    )

with col2:
    st.metric(
        "최저기온 평균",
        f"{selected[min_col].mean():.1f}℃"
    )

# -----------------------------------
# 데이터 보기
# -----------------------------------
with st.expander("데이터 보기"):
    st.dataframe(
        selected[
            ["연도", max_col, min_col]
        ].rename(
            columns={
                max_col: "최고기온",
                min_col: "최저기온"
            }
        ),
        use_container_width=True
    )

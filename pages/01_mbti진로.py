
import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천기",
    page_icon="✨",
    layout="centered"
)

# MBTI별 진로 데이터
mbti_data = {
    "INTJ": [
        {
            "career": "🧠 데이터 사이언티스트",
            "major": "인공지능학과, 컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석을 좋아하는 사람에게 잘 맞아요.",
            "salary": "평균 연봉 약 6,000만 원"
        },
        {
            "career": "📊 전략 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "계획 세우기와 문제 해결을 좋아하는 성격에 적합해요.",
            "salary": "평균 연봉 약 7,000만 원"
        }
    ],

    "INTP": [
        {
            "career": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "새로운 아이디어와 기술 탐구를 좋아하는 사람에게 좋아요.",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "깊게 생각하고 탐구하는 성향과 잘 어울려요.",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],

    "ENTJ": [
        {
            "career": "🏢 CEO",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표 달성을 좋아하는 사람에게 적합해요.",
            "salary": "평균 연봉 약 8,000만 원"
        },
        {
            "career": "📈 마케팅 매니저",
            "major": "광고홍보학과, 경영학과",
            "personality": "사람을 이끄는 능력과 추진력이 강한 성격과 잘 맞아요.",
            "salary": "평균 연봉 약 5,500만 원"
        }
    ],

    "ENTP": [
        {
            "career": "🎤 크리에이터",
            "major": "미디어학과, 영상학과",
            "personality": "아이디어가 많고 새로운 도전을 즐기는 사람에게 추천해요.",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "career": "🚀 스타트업 창업가",
            "major": "경영학과, IT융합학과",
            "personality": "도전 정신이 강하고 창의적인 성격에 잘 어울려요.",
            "salary": "성공 시 매우 높은 수익 가능!"
        }
    ],

    "INFJ": [
        {
            "career": "🧡 상담사",
            "major": "심리학과, 상담학과",
            "personality": "공감 능력이 뛰어난 사람에게 잘 맞아요.",
            "salary": "평균 연봉 약 4,000만 원"
        },
        {
            "career": "✍️ 작가",
            "major": "문예창작학과",
            "personality": "감수성이 풍부하고 상상력이 좋은 사람에게 추천해요.",
            "salary": "평균 연봉 약 3,500만 원"
        }
    ],

    "INFP": [
        {
            "career": "🎨 디자이너",
            "major": "시각디자인학과",
            "personality": "창의적이고 감성이 풍부한 사람에게 적합해요.",
            "salary": "평균 연봉 약 4,000만 원"
        },
        {
            "career": "📚 웹소설 작가",
            "major": "문예창작학과",
            "personality": "상상력이 풍부하고 자기 표현을 좋아하는 사람에게 좋아요.",
            "salary": "인기에 따라 큰 차이가 있어요!"
        }
    ],

    "ENFJ": [
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람을 돕고 이끄는 걸 좋아하는 성격에 잘 맞아요.",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "🤝 인사담당자",
            "major": "경영학과",
            "personality": "소통 능력이 뛰어난 사람에게 추천해요.",
            "salary": "평균 연봉 약 5,200만 원"
        }
    ],

    "ENFP": [
        {
            "career": "🎬 방송 PD",
            "major": "신문방송학과",
            "personality": "열정적이고 아이디어가 많은 사람에게 좋아요.",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "📱 콘텐츠 기획자",
            "major": "미디어학과",
            "personality": "트렌드에 민감하고 창의적인 성격과 잘 어울려요.",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ],

    "ISTJ": [
        {
            "career": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 있는 사람에게 추천해요.",
            "salary": "평균 연봉 약 7,000만 원"
        },
        {
            "career": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "안정적이고 체계적인 성격과 잘 맞아요.",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],

    "ISFJ": [
        {
            "career": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 성실한 사람에게 적합해요.",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "따뜻하고 책임감 있는 성격에 잘 맞아요.",
            "salary": "평균 연봉 약 3,800만 원"
        }
    ],

    "ESTJ": [
        {
            "career": "📋 프로젝트 매니저",
            "major": "경영학과",
            "personality": "리더십과 추진력이 강한 사람에게 좋아요.",
            "salary": "평균 연봉 약 6,500만 원"
        },
        {
            "career": "🏛️ 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 성격에 잘 맞아요.",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ],

    "ESFJ": [
        {
            "career": "💄 승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람에게 추천해요.",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "career": "🏨 호텔리어",
            "major": "호텔관광학과",
            "personality": "사람을 챙기는 걸 좋아하는 성격에 잘 맞아요.",
            "salary": "평균 연봉 약 4,200만 원"
        }
    ],

    "ISTP": [
        {
            "career": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 만드는 걸 좋아하는 사람에게 적합해요.",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "🚗 자동차 개발자",
            "major": "자동차공학과",
            "personality": "실용적이고 문제 해결 능력이 뛰어난 성격과 잘 맞아요.",
            "salary": "평균 연봉 약 6,000만 원"
        }
    ],

    "ISFP": [
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 자유로운 성격에 잘 어울려요.",
            "salary": "평균 연봉 약 3,500만 원"
        },
        {
            "career": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "예술 감각이 뛰어난 사람에게 추천해요.",
            "salary": "경력에 따라 차이가 커요!"
        }
    ],

    "ESTP": [
        {
            "career": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 사람 만나는 걸 좋아하는 성격에 적합해요.",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "🎮 e스포츠 선수",
            "major": "e스포츠학과",
            "personality": "도전적이고 순발력이 좋은 사람에게 추천해요.",
            "salary": "실력에 따라 큰 차이가 있어요!"
        }
    ],

    "ESFP": [
        {
            "career": "🎤 배우",
            "major": "연극영화과",
            "personality": "에너지가 넘치고 표현력이 좋은 사람에게 잘 맞아요.",
            "salary": "인지도에 따라 달라져요!"
        },
        {
            "career": "📺 방송인",
            "major": "방송연예과",
            "personality": "사람들 앞에서 활동하는 걸 좋아하는 성격에 적합해요.",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ]
}

# 제목
st.title("✨ MBTI 진로 추천기")
st.write("나의 MBTI에 어울리는 진로를 알아보자! 🚀")

# MBTI 선택
selected_mbti = st.selectbox(
    "👇 MBTI를 선택해 주세요!",
    list(mbti_data.keys())
)

# 결과 출력
st.subheader(f"🌟 {selected_mbti} 추천 진로")

for job in mbti_data[selected_mbti]:
    st.markdown(f"""
    ---
    ## {job['career']}
    
    🎓 **추천 학과**  
    {job['major']}
    
    🧩 **어울리는 성격**  
    {job['personality']}
    
    💰 **평균 연봉**  
    {job['salary']}
    """)

st.info("💡 MBTI는 참고용이에요! 가장 중요한 건 내가 좋아하고 잘할 수 있는 일을 찾는 거예요 😊")

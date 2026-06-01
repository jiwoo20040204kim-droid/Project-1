import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="나의 여행일지 ✈️",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Premium Design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

    /* Font Setup */
    html, body, [class*="css"], .stApp {
        font-family: 'Outfit', 'Noto Sans KR', sans-serif;
    }

    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #020617 100%);
        color: #f8fafc;
    }

    /* Title Styling */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.05em;
    }
    
    .sub-title {
        font-size: 1.2rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 300;
    }

    /* Container for Travel Card */
    .travel-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        margin-top: 0.5rem;
        transition: all 0.3s ease;
    }

    .travel-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.15);
    }

    /* Image Styling */
    .stImage img {
        border-radius: 20px !important;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: transform 0.5s ease !important;
    }
    
    .stImage img:hover {
        transform: scale(1.02) !important;
    }

    /* City Info Styling */
    .city-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 2px solid rgba(255, 255, 255, 0.05);
        padding-bottom: 0.8rem;
    }
    
    .city-desc {
        font-size: 1.15rem;
        color: #cbd5e1;
        line-height: 1.7;
        margin-bottom: 2rem;
    }

    /* Styled Badges/Cards */
    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
        margin-top: 1.5rem;
    }

    .info-item {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.25rem;
        transition: all 0.3s ease;
    }

    .info-item:hover {
        background: rgba(15, 23, 42, 0.8);
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-2px);
    }

    .info-label {
        font-size: 0.9rem;
        font-weight: 700;
        color: #818cf8;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .info-value {
        font-size: 1.05rem;
        color: #f1f5f9;
        font-weight: 400;
        line-height: 1.5;
    }

    /* Styling Default Streamlit Buttons to look elegant and glow */
    div.stButton > button {
        background: rgba(30, 41, 59, 0.6) !important;
        color: #cbd5e1 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 14px !important;
        padding: 0.7rem 1rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        border-color: #818cf8 !important;
        box-shadow: 0 10px 20px -3px rgba(99, 102, 241, 0.4) !important;
        transform: translateY(-3px) !important;
    }

    div.stButton > button:active {
        transform: translateY(-1px) !important;
    }

    /* Active button styling through context helper */
    .active-btn-style button {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        border-color: #818cf8 !important;
        box-shadow: 0 10px 20px -3px rgba(99, 102, 241, 0.4) !important;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 6rem;
        font-size: 0.85rem;
        color: #64748b;
        font-weight: 300;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Application Header
st.markdown('<div class="main-title">나의 여행일지 ✈️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">설레는 마음으로 다녀왔던 특별한 도시들의 기록과 기억</div>', unsafe_allow_html=True)

# City Database (Curated High-Quality Aesthetic Travel Photos)
cities_data = {
    "상하이": {
        "flag": "🇨🇳",
        "english": "Shanghai",
        "image_url": "https://images.unsplash.com/photo-1548919973-5cef591cdbc9?q=80&w=1200&auto=format&fit=crop",
        "description": "화려한 와이탄의 야경과 미래적인 동방명주 타워가 어우러진 전통과 극도의 첨단 문명이 한데 공존하는 중국 최고의 경제 중심 도시입니다.",
        "best_time": "10월 - 11월 (선선하고 쾌적한 완벽한 가을)",
        "attractions": "와이탄 야경 거리, 동방명주 타워, 신천지 노천 카페, 상하이 디즈니랜드, 전통 예원정원",
        "food": "육즙 가득한 샤오롱바오 (소룡포), 달콤 짭조름한 훙사오로우, 고소한 상하이 털게 요리",
        "tip": "와이탄의 상징적인 야경 조명(라이트업)은 보통 저녁 7시부터 10시까지 점등되니 일몰 시간에 맞춰 황포강 유람선을 예약하시는 것을 추천합니다!"
    },
    "홍콩": {
        "flag": "🇭🇰",
        "english": "Hong Kong",
        "image_url": "https://images.unsplash.com/photo-1506970845246-18f21d533b20?q=80&w=1200&auto=format&fit=crop",
        "description": "홍콩영화의 낭만이 깃든 거리 분위기, 빽빽하게 솟은 화려한 빌딩 숲과 빅토리아 하버의 환상적인 하모니, 쇼핑과 식도락의 도시입니다.",
        "best_time": "11월 - 2월 (습도가 낮고 화창하며 시원한 겨울)",
        "attractions": "빅토리아 피크 트램 전망대, 침사추이 소호 미드레벨 에스컬레이터, 센트럴 란콰이퐁 야간 맥주 거리, 옹핑 360 케이블카",
        "food": "샤오마이와 하가우 등 무한한 종류의 딤섬, 달콤하고 부드러운 에그타르트, 깊은 국물의 완탕면, 홍콩식 밀크티와 프렌치 토스트",
        "tip": "매일 밤 8시 침사추이 해변 산책로에서 펼쳐지는 무료 대형 레이저 쇼 '심포니 오브 라이트'를 놓치지 마세요. 해질 무렵 타는 스타페리 위에서의 조망도 끝내줍니다."
    },
    "도쿄": {
        "flag": "🇯🇵",
        "english": "Tokyo",
        "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?q=80&w=1200&auto=format&fit=crop",
        "description": "최첨단의 번화함 속에서도 골목골목 전통적인 정취와 아기자기함이 아름답게 조화되어 전 세계 여행객들의 발길이 끊이지 않는 매력적인 아시아 대표 메트로폴리스입니다.",
        "best_time": "3월 - 4월 (분홍빛 흐드러진 벚꽃철) 또는 11월 (단풍과 시원한 날씨)",
        "attractions": "시부야 크로싱 스퀘어 & 시부야 스카이, 유서 깊은 아사쿠사 센소지 사원, 불 밝힌 도쿄 타워 전망대, 도심 속 오아시스 신주쿠 교엔, 오다이바 인공섬",
        "food": "눈앞에서 쥐어주는 신선한 초밥, 바삭함이 살아있는 돈카츠 & 규카츠, 진한 풍미의 라멘, 맛있는 타코야키와 말차 파르페",
        "tip": "도쿄 도청 전망대는 입장료가 완전히 무료이며 날씨가 매우 화창하고 미세먼지가 없는 날에는 저 멀리 웅장한 설산인 후지산의 만년설까지 조망할 수 있습니다."
    },
    "괌": {
        "flag": "🇬🇺",
        "english": "Guam",
        "image_url": "image/괌.webp",
        "description": "비행 시간도 짧고 안전한 치안과 끝없이 투명한 에메랄드빛 해변, 그리고 평화로운 휴식을 원하는 모두를 위한 진정한 지상낙원 남태평양 섬입니다.",
        "best_time": "12월 - 5월 (비가 거의 오지 않는 상쾌한 건기)",
        "attractions": "사랑의 절벽 노을 스팟, 하얀 모래와 얕고 맑은 투몬 비치, 스노클러들의 천국 리티디안 비치, 이나라한 천연 해수 풀장",
        "food": "특유의 양념이 배어 있는 차모로 전통 바베큐, 붉은색을 띠는 레드 라이스, 신선한 코코넛 크랩 요리, 매콤새콤 피나데니 소스",
        "tip": "하루쯤은 꼭 렌터카를 대여하여 해안선을 따라 펼쳐지는 괌 남부 지역을 드라이브 해 보세요. 사람 없는 한적한 해변과 야자수 아래 완벽한 휴식을 찾을 수 있습니다."
    },
    "하와이": {
        "flag": "🇺🇸",
        "english": "Hawaii",
        "image_url": "image/Honolulu-cover.jpg",
        "description": "환영의 뜻인 '알로하' 정신이 가득한 웅장하고 신비로운 활화산의 섬들, 세계 서퍼들이 사랑하는 푸른 태평양의 거대한 파도와 활기찬 문화가 숨쉬는 곳입니다.",
        "best_time": "4월 - 6월 / 9월 - 11월 (연중 내내 환상적이지만 가장 온화하고 쾌적한 시기)",
        "attractions": "오아후섬의 와이키키 해변, 하이킹 코스인 다이아몬드 헤드 분화구, 환상의 스노클링 파크 하나우마 베이, 노스 쇼어 서핑 타운",
        "food": "참치 등 신선한 생선회를 버무린 웰빙 포케(Poke), 하와이식 함박 스테이크 덮밥 로코모코, 설탕을 묻힌 따끈한 말라사다 도넛, 달콤 시원한 쉐이브 아이스",
        "tip": "수중 해양보호구역인 하나우마 베이는 입장객 수가 엄격히 제한되어 100% 온라인 사전 예약을 성공해야 갈 수 있으니 최소 여행 몇 주 전에 티켓팅 스케줄을 확인해 두어야 합니다."
    },
    "보스턴": {
        "flag": "🇺🇸",
        "english": "Boston",
        "image_url": "image/보스턴.webp",
        "description": "미국 역사와 독립운동의 숨결이 골목 구석구석 서려 있는 곳이자 하버드 대학교, MIT 등 세계 최고 지성들이 모여 숨쉬는 품격 있고 차분한 역사와 학문의 도시입니다.",
        "best_time": "9월 - 10월 (강변을 따라 뉴잉글랜드 지방의 화려한 단풍이 번지는 완벽한 가을)",
        "attractions": "붉은 벽돌 선을 따라 걷는 역사 산책 프리덤 트레일, 하버드 대학교 & MIT 캠퍼스 투어, 보스턴 커먼 공원 호숫가, 활기찬 퀸시 마켓 푸드코트",
        "food": "진하고 고소한 조개 크림 수프 뉴잉글랜드 클램 차우더, 싱싱하고 꽉 찬 살의 랍스터 롤, 클래식 디저트 보스턴 크림 파이",
        "tip": "하버드 대학 캠퍼스에서는 재학생들이 직접 들려주는 위트 있고 흥미진진한 교내 역사 워킹 투어 프로그램(Hahvahd Tour)을 꼭 체험해 보세요. 아주 값진 경험이 됩니다."
    }
}

# State Management for Selected City
if "selected_city" not in st.session_state:
    st.session_state.selected_city = "상하이"

# Generate Navigation Buttons (Columns layout)
cols = st.columns(6)
cities_list = list(cities_data.keys())

for i, city in enumerate(cities_list):
    with cols[i]:
        flag = cities_data[city]["flag"]
        button_label = f"{flag} {city}"
        
        # Apply active class if current city is selected
        if st.session_state.selected_city == city:
            st.markdown('<div class="active-btn-style">', unsafe_allow_html=True)
            st.button(button_label, key=f"btn_{i}")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button(button_label, key=f"btn_{i}"):
                st.session_state.selected_city = city
                st.rerun()

# Layout: Split into Left (Image) and Right (Information Card)
selected_city = st.session_state.selected_city
data = cities_data[selected_city]

st.markdown("<br>", unsafe_allow_html=True)

content_col1, content_col2 = st.columns([1.1, 1])

with content_col1:
    # Display stunning, full-bleed high resolution image
    st.image(data["image_url"], width='stretch')

with content_col2:
    # Display highly styled information card
    st.markdown(f"""
        <div class="travel-card">
            <div class="city-title">
                {data['flag']} {selected_city} 
                <span style="font-size: 1.5rem; color: #818cf8; font-weight: 300; margin-left: 10px; font-family: 'Outfit';">
                    {data['english']}
                </span>
            </div>
            <div class="city-desc">{data['description']}</div>
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-label">📅 최적의 시즌</div>
                    <div class="info-value">{data['best_time']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">📍 핵심 방문 명소</div>
                    <div class="info-value">{data['attractions']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">🍽️ 현지 추천 푸드</div>
                    <div class="info-value">{data['food']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">💡 여행 전문가의 꿀팁</div>
                    <div class="info-value">{data['tip']}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Beautiful Custom Footer
st.markdown("""
    <div class="footer">
        © 2026 나의 여행일지(My Travel Log) - All rights reserved.<br>
        Designed with elegant aesthetics and powered by Streamlit & uv
    </div>
""", unsafe_allow_html=True)

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
        font-size: 3.0rem;
        font-weight: 800;
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.04em;
    }
    
    .title-text {
        background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    .airplane-emoji {
        display: inline-block;
        animation: flyUp linear;
        animation-timeline: scroll(root block);
        transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        transform-origin: bottom left;
    }

    .airplane-emoji:hover {
        transform: translate(20px, -20px) rotate(15deg) scale(1.15);
    }

    @keyframes flyUp {
        from {
            transform: translate(0, 0) rotate(0deg);
        }
        to {
            transform: translate(60px, -60px) rotate(12deg);
        }
    }
    
    .sub-title {
        font-size: 1.1rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 300;
        letter-spacing: -0.01em;
    }

    /* Container for Travel Card */
    .travel-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        margin-top: 0px;
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
        font-size: 2.1rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 1.1rem;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 2px solid rgba(255, 255, 255, 0.05);
        padding-bottom: 0.4rem;
    }
    
    .city-desc {
        font-size: 1.02rem;
        color: #cbd5e1;
        line-height: 1.75;
        margin-bottom: 3.2rem;
        word-break: keep-all;
    }

    /* Styled Badges/Cards */
    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
        margin-top: 2.8rem;
    }

    .info-item {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.0rem 1.15rem;
        transition: all 0.3s ease;
    }

    .info-item:hover {
        background: rgba(15, 23, 42, 0.8);
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-2px);
    }

    .info-label {
        font-size: 1.05rem;
        font-weight: 700;
        color: #818cf8;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .info-value {
        font-size: 0.92rem;
        color: #f1f5f9;
        font-weight: 400;
        line-height: 1.6;
        text-align: left;
        word-break: keep-all;
        hyphens: none;
        -webkit-hyphens: none;
        -ms-hyphens: none;
    }

    /* Styling Default Streamlit Buttons to look elegant and glow */
    div.stButton > button {
        background: rgba(30, 41, 59, 0.6) !important;
        color: #cbd5e1 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 0.6rem 1rem !important;
        font-size: 0.98rem !important;
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
        background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%) !important;
        color: #ffffff !important;
        border: 2px solid #38bdf8 !important;
        box-shadow: 0 0 15px 3px rgba(56, 189, 248, 0.5), inset 0 0 10px rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-2px) !important;
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

    /* Section Title Styling */
    .section-title {
        font-size: 1.75rem;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 4rem;
        margin-bottom: 1.5rem;
        letter-spacing: -0.03em;
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Activity Row Card Styling */
    .activity-row-card {
        background: rgba(30, 41, 59, 0.35);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.1rem 1.4rem;
        margin-bottom: 0.75rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    }
    
    .activity-row-card:hover {
        background: rgba(49, 46, 129, 0.3);
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateX(5px);
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.15);
    }

    /* Restaurant Card Styling */
    .restaurant-card {
        background: rgba(30, 41, 59, 0.35);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.5rem;
        height: 320px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }
    
    .restaurant-card:hover {
        background: rgba(20, 83, 45, 0.25);
        border-color: rgba(34, 197, 94, 0.3);
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(34, 197, 94, 0.15);
    }

    .restaurant-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.4rem;
        letter-spacing: -0.02em;
        text-align: left;
    }

    .restaurant-tag {
        font-size: 0.75rem;
        font-weight: 700;
        color: #4ade80;
        margin-bottom: 0.8rem;
        display: inline-block;
        background: rgba(34, 197, 94, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 8px;
        text-align: left;
        letter-spacing: 0.03em;
    }

    .restaurant-desc {
        font-size: 0.85rem;
        color: #cbd5e1;
        line-height: 1.6;
        font-weight: 400;
        text-align: left;
        word-break: keep-all;
        height: 80px;
        margin-bottom: 1rem;
    }

    /* Gallery Item Label Styling */
    .gallery-caption {
        text-align: center;
        margin-top: 0.8rem;
        font-size: 1.05rem;
        font-weight: 600;
        color: #cbd5e1;
        letter-spacing: -0.02em;
    }
    </style>
""", unsafe_allow_html=True)

# Application Header
st.markdown('<div class="main-title"><span class="title-text">나의 여행일지</span> <span class="airplane-emoji">✈️</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">설레는 마음으로 다녀왔던 특별한 도시들의 기록과 기억</div>', unsafe_allow_html=True)

cities_data = {
    "상하이": {
        "flag": "🇨🇳",
        "english": "Shanghai",
        "image_url": "https://images.unsplash.com/photo-1548919973-5cef591cdbc9?q=80&w=1200&auto=format&fit=crop",
        "description": "화려한 와이탄의 야경과 미래적인 동방명주 타워가 어우러진 전통과 극도의 첨단 문명이 한데 공존하는 중국 최고의 경제 중심 도시입니다.",
        "best_time": "10월 ~ 11월 (선선하고 쾌적한 완벽한 가을)",
        "attractions": "와이탄 야경 거리, 동방명주 타워, 신천지 노천 카페, 상하이 디즈니랜드, 전통 예원정원",
        "food": "육즙 가득한 샤오롱바오 (소룡포), 달콤 짭조름한 훙사오로우, 고소한 상하이 털게 요리",
        "tip": "와이탄의 상징적인 야경 조명(라이트업)은 보통 저녁 7시부터 10시까지 점등되니 일몰 시간에 맞춰 황포강 유람선을 예약하시는 것을 추천합니다!",
        "things_to_do": [
            {"place": "황포강 유람선", "desc": "유람선을 타고 화려한 와이탄 야경 관람하기"},
            {"place": "예원 상가", "desc": "골목에서 육즙 가득한 샤오롱바오 맛보기"},
            {"place": "신천지 카페거리", "desc": "노천 카페에서 여유로운 브런치 즐기기"},
            {"place": "동방명주 타워", "desc": "유리 전망대에서 스릴 넘치는 전경 조망하기"},
            {"place": "상하이 디즈니랜드", "desc": "아시아 최초의 트론 라이트사이클 파워 런 타기"}
        ],
        "restaurants": [
            {
                "name": "佳家汤包 (가포)",
                "tag": "샤오롱바오",
                "desc": "상하이에서 가장 유명한 게살/돼지고기 샤오롱바오 전문점입니다. 얇은 피와 풍부한 육즙이 일품입니다.",
                "booking": "현장 대기만 가능하며, 오픈 시간(오전 7:30) 맞춰 방문 시 대기를 대폭 줄일 수 있습니다."
            },
            {
                "name": "Lost Heaven (로스트 헤븐)",
                "tag": "운남 요리",
                "desc": "와이탄 근처의 이국적이고 고급스러운 아시안 퓨전 요리 전문점입니다. 태국 스타일과 운남 요리가 조화롭게 어우러집니다.",
                "booking": "공식 홈페이지 또는 Dianping 앱을 통해 사전 예약 필수이며, 와이탄 야경 창가석은 2주 전에 예약해야 안전합니다."
            },
            {
                "name": "소양생전 (Yang's Dumpling)",
                "tag": "만두 / 성젠바오",
                "desc": "바삭하게 구운 만두피와 촉촉하고 육즙 가득한 돼지고기 소가 특징인 상하이의 대표 만두 브랜드입니다.",
                "booking": "매장 무인 키오스크나 알리페이 미니프로그램으로 선주문 후 수령하면 대기 시간 없이 포장 가능합니다."
            },
            {
                "name": "그랜드마더 레스토랑",
                "tag": "상하이 가정식",
                "desc": "달콤짭조름한 훙사오로우와 마파두부를 합리적인 가격에 맛볼 수 있는 와이탄 근처 홈스타일 맛집입니다.",
                "booking": "별도의 예약 시스템이 없어 식사 피크 타임인 정오(12시)나 오후 6시 전후를 피해 방문하시는 것을 추천합니다."
            }
        ],
        "attractions_gallery": [
            {"name": "와이탄", "image_url": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?q=80&w=600&auto=format&fit=crop"},
            {"name": "동방명주", "image_url": "https://images.unsplash.com/photo-1474181487882-5abf3f016c2d?q=80&w=600&auto=format&fit=crop"},
            {"name": "예원", "image_url": "https://images.unsplash.com/photo-1522083165195-342750297f05?q=80&w=600&auto=format&fit=crop"},
            {"name": "신천지", "image_url": "https://images.unsplash.com/photo-1541849546-216509041df4?q=80&w=600&auto=format&fit=crop"},
            {"name": "상하이 디즈니랜드", "image_url": "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?q=80&w=600&auto=format&fit=crop"}
        ]
    },
    "홍콩": {
        "flag": "🇭🇰",
        "english": "Hong Kong",
        "image_url": "https://images.unsplash.com/photo-1506970845246-18f21d533b20?q=80&w=1200&auto=format&fit=crop",
        "description": "홍콩영화의 낭만이 깃든 거리 분위기, 빽빽하게 솟은 화려한 빌딩 숲과 빅토리아 하버의 환상적인 하모니, 쇼핑과 식도락의 도시입니다.",
        "best_time": "11월 ~ 2월 (습도가 낮고 화창하며 시원한 겨울)",
        "attractions": "빅토리아 피크 트램 전망대, 침사추이 소호 미드레벨 에스컬레이터, 센트럴 란콰이퐁 야간 맥주 거리, 옹핑 360 케이블카",
        "food": "샤오마이와 하가우 등 무한한 종류의 딤섬, 달콤하고 부드러운 에그타르트, 깊은 국물의 완탕면, 홍콩식 밀크티와 프렌치 토스트",
        "tip": "매일 밤 8시 침사추이 해변 산책로에서 펼쳐지는 무료 대형 레이저 쇼 '심포니 오브 라이트'를 놓치지 마세요. 스타페리 위에서의 조망도 끝내줍니다.",
        "things_to_do": [
            {"place": "피크 트램 & 빅토리아 피크", "desc": "전망대에 올라 빌딩 숲의 환상적인 야경 감상하기"},
            {"place": "미드레벨 에스컬레이터", "desc": "소호 거리 곳곳의 벽화 and 이국적인 상점 탐방하기"},
            {"place": "침사추이 해변 산책로", "desc": "심포니 오브 라이트 레이저 쇼 감상하기"},
            {"place": "스타페리", "desc": "클래식한 페리를 타고 빅토리아 하버 건너기"},
            {"place": "란콰이퐁", "desc": "활기찬 펍에서 세계 각국의 수제 맥주 마시기"}
        ],
        "restaurants": [
            {
                "name": "Tim Ho Wan (팀호완)",
                "tag": "딤섬",
                "desc": "미쉐린 스타를 획득한 딤섬 맛집으로, 달콤바삭한 비비큐 번(Baked BBQ Pork Bun)이 대표 메뉴입니다.",
                "booking": "센트럴점은 대기가 매우 길어 매장 오픈 20분 전에 미리 도착하거나, 붐비는 12시~2시 식사 시간을 피하시는 것이 좋습니다."
            },
            {
                "name": "Kau Kee (카우키)",
                "tag": "완탕면 / 소고기 국수",
                "desc": "유명 홍콩 스타들의 단골집으로 진하고 깊은 육수와 부드러운 소고기가 듬뿍 올라간 국수 전문점입니다.",
                "booking": "예약이 절대 불가하며 오직 현금 결제만 가능하므로 미리 홍콩 달러를 준비해 줄을 서야 합니다. (일요일 휴무)"
            },
            {
                "name": "타이청 베이커리",
                "tag": "에그타르트",
                "desc": "홍콩식 쿠키 도우 에그타르트의 원조로, 입안에서 사르르 녹는 달콤한 커스터드 크림이 매력적입니다.",
                "booking": "예약 없이 현장 테이크아웃 전용입니다. 평일 오전 시간대에 방문하면 갓 구워낸 따끈하고 부드러운 에그타르트를 즉시 즐기실 수 있습니다."
            },
            {
                "name": "Lan Fong Yuen (란퐁유엔)",
                "tag": "밀크티 & 토스트",
                "desc": "홍콩식 차찬탱의 대명사로 스타킹 필터로 걸러낸 진한 밀크티와 프렌치 토스트의 조합이 훌륭합니다.",
                "booking": "줄이 항상 있으나 테이블 회전율이 빨라 대기 시간이 짧습니다. 1인당 최소 주문 금액 제한이 있는 합석 기반 매장입니다."
            }
        ],
        "attractions_gallery": [
            {"name": "빅토리아 피크", "image_url": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?q=80&w=600&auto=format&fit=crop"},
            {"name": "침사추이", "image_url": "https://images.unsplash.com/photo-1536599018102-9f803c140fc1?q=80&w=600&auto=format&fit=crop"},
            {"name": "미드레벨 에스컬레이터", "image_url": "https://images.unsplash.com/photo-1518235506717-e1ed3306a89b?q=80&w=600&auto=format&fit=crop"},
            {"name": "옹핑 360", "image_url": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?q=80&w=600&auto=format&fit=crop"},
            {"name": "란콰이퐁", "image_url": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?q=80&w=600&auto=format&fit=crop"}
        ]
    },
    "도쿄": {
        "flag": "🇯🇵",
        "english": "Tokyo",
        "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?q=80&w=1200&auto=format&fit=crop",
        "description": "최첨단의 번화함 속에서도 골목골목 전통적인 정취와 아기자기함이 아름답게 조화되어 전 세계 여행객들의 발길이 끊이지 않는 매력적인 아시아 대표 메트로폴리스입니다.",
        "best_time": "3월 ~ 4월 (분홍빛 흐드러진 벚꽃철) 또는 11월 (단풍과 시원한 날씨)",
        "attractions": "시부야 크로싱 스퀘어 & 시부야 스카이, 유서 깊은 아사쿠사 센소지 사원, 불 밝힌 도쿄 타워 전망대, 도심 속 오아시스 신주쿠 교엔, 오다이바 인공섬",
        "food": "눈앞에서 쥐어주는 신선한 초밥, 바삭함이 살아있는 돈카츠 & 규카츠, 진한 풍미의 라멘, 맛있는 타코야키와 말차 파르페",
        "tip": "도쿄 도청 전망대는 입장료가 완전히 무료이며 날씨가 화창하고 깨끗한 날에는 후지산의 만년설까지 조망할 수 있습니다.",
        "things_to_do": [
            {"place": "시부야 스카이", "desc": "전망대의 시부야 엣지에서 교차로와 도쿄 전망 감상하기"},
            {"place": "아사쿠사 센소지", "desc": "오미쿠지를 뽑고 카미나리몬 사진 찍으며 전통 분위기 느끼기"},
            {"place": "도쿄 타워", "desc": "도쿄의 상징인 타워 아래에서 영화 속 한 장면 같은 야경 감상하기"},
            {"place": "신주쿠 교엔", "desc": "도심 속 거대한 정원에서 일본식 말차를 마시며 산책하기"},
            {"place": "오다이바 해변공원", "desc": "레인보우 브릿지와 미니 자유의 여신상을 배경으로 인생샷 남기"}
        ],
        "restaurants": [
            {
                "name": "츠키지 장외시장",
                "tag": "스시 & 카이센동",
                "desc": "신선한 해산물이 가득한 시장입니다. 즉석에서 만들어주는 초밥과 달콤한 계란말이가 명물입니다.",
                "booking": "예약이 불가능하며, 다이와스시 등 극도로 유명한 초밥 매장은 새벽 5시~6시쯤 방문하셔야 대기를 최소화할 수 있습니다."
            },
            {
                "name": "이치란 라멘",
                "tag": "돈코츠 라멘",
                "desc": "개별 독서실 형태의 좌석에서 취향대로 커스텀하여 즐기는 진하고 깊은 국물의 돈코츠 라멘 전문점입니다.",
                "booking": "현장 식권 자판기 주문 방식입니다. 라인(LINE) 모바일 메신저 대기 기능을 연동해 덜 붐비는 대기 현황을 사전에 조회해 보세요."
            },
            {
                "name": "규카츠 모토무라",
                "tag": "규카츠",
                "desc": "겉은 바삭하고 속은 부드러운 소고기를 개인 미니 화로에 원하는 굽기로 구워 먹는 맛집입니다.",
                "booking": "지점에 따라 구글 맵 사전 예약을 지원하므로 출발 전 확인이 필요합니다. 워크인 대기 시간은 최소 40분 이상입니다."
            },
            {
                "name": "돈카츠 마이센",
                "tag": "돈카츠",
                "desc": "젓가락으로 잘릴 정도로 극도로 부드러운 육질을 자랑하는 흑돼지 돈카츠 전문점입니다.",
                "booking": "구글 맵 예약 시스템 또는 일본 맛집 플랫폼 타벨로그(Tabelog)를 통해 저녁 피크 타임의 메인 테이블석 사전 확보가 가능합니다."
            }
        ],
        "attractions_gallery": [
            {"name": "시부야 크로싱", "image_url": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=600&auto=format&fit=crop"},
            {"name": "도쿄 타워", "image_url": "https://images.unsplash.com/photo-1540959733332-eab4deceeaf7?q=80&w=600&auto=format&fit=crop"},
            {"name": "아사쿠사 센소지", "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?q=80&w=600&auto=format&fit=crop"},
            {"name": "신주쿠 교엔", "image_url": "https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?q=80&w=600&auto=format&fit=crop"},
            {"name": "오다이바", "image_url": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?q=80&w=600&auto=format&fit=crop"}
        ]
    },
    "괌": {
        "flag": "🇬🇺",
        "english": "Guam",
        "image_url": "image/guam.jpg",
        "description": "비행 시간도 짧고 안전한 치안과 끝없이 투명한 에메랄드빛 해변, 그리고 평화로운 휴식을 원하는 모두를 위한 진정한 지상낙원 남태평양 섬입니다.",
        "best_time": "12월 ~ 5월 (비가 거의 오지 않는 상쾌한 건기)",
        "attractions": "사랑의 절벽 노을 스팟, 하얀 모래와 얕고 맑은 투몬 비치, 스노클러들의 천국 리티디안 비치, 이나라한 천연 해수 풀장",
        "food": "특유의 양념이 배어 있는 차모로 전통 바베큐, 붉은색을 띠는 레드 라이스, 신선한 코코넛 크랩 요리, 매콤새콤 피나데니 소스",
        "tip": "하루쯤은 꼭 렌터카를 대여하여 해안선을 따라 펼쳐지는 괌 남부 지역을 드라이브 해 보세요. 사람 없는 한적한 해변과 야자수 아래 완벽한 휴식을 찾을 수 있습니다.",
        "things_to_do": [
            {"place": "사랑의 절벽", "desc": "노을 스팟에 올라 끝없는 파도와 오렌지빛 남태평양 일몰 바라보기"},
            {"place": "투몬 비치", "desc": "잔잔하고 투명한 해변에서 패들보드나 스노클링을 즐기며 힐링하기"},
            {"place": "리티디안 비치", "desc": "괌 최고의 청정 해역에서 야생 산호초와 열대어 관찰하기"},
            {"place": "이나라한 해수풀", "desc": "천연 해수 풀장의 다이빙대에서 수영하며 현지 분위기 느끼기"},
            {"place": "차모로 야시장", "desc": "수요일 저녁 갓 구운 바베큐 꼬치 맛보고 공예품 구경하기"}
        ],
        "restaurants": [
            {
                "name": "PROA (프로아)",
                "tag": "차모로 바베큐",
                "desc": "현지인들이 꼽는 최고의 바베큐 맛집으로 갈비, 돼지고기, 닭고기가 모두 훌륭한 바베큐 플래터가 유명합니다.",
                "booking": "괌 최고의 로컬 인기 맛집이므로 여행 1~2일 전에 오픈테이블(OpenTable) 온라인 앱이나 유선으로 예약을 마치는 것을 추천합니다."
            },
            {
                "name": "Joinus Keyaki (조이너스 키야키)",
                "tag": "철판 데판야끼",
                "desc": "눈앞에서 셰프가 화려한 불쇼를 선보이며 스테이크와 해산물을 구워내는 인기 런치 레스토랑입니다.",
                "booking": "철판 불쇼 테이블은 한정되어 있어 점심 런치 특선을 즐기시려면 최소 2~3주 전 오픈테이블(OpenTable) 앱 사전 예약이 필수적입니다."
            },
            {
                "name": "Terry's Local Kitchen (테리스)",
                "tag": "전통 차모로식",
                "desc": "괌 전통 가정식을 고수하는 레스토랑으로 코코넛 크랩와 매콤새콤 피나데니 소스 갈비 요리가 일품입니다.",
                "booking": "구글 맵 간편 예약을 정식 지원하며, 일반 워크인(예약 없이 방문) 시에도 비교적 대기 없이 편안한 좌석 확보가 쉬운 편입니다."
            },
            {
                "name": "Pika's Cafe (피카스 카페)",
                "tag": "로컬 브런치",
                "desc": "차모로식 로코모코와 특제 에그 베네딕트로 유명한 현지 1등 브런치 카페입니다.",
                "booking": "예약을 지원하지 않으며 오직 현장 선착순 대기만 받습니다. 번잡한 오전 10시 전후 시간대에 대기 번호표를 등록하고 차에서 대기하세요."
            }
        ],
        "attractions_gallery": [
            {"name": "사랑의 절벽", "image_url": "https://images.unsplash.com/photo-1515238152791-8216bfdf89a7?q=80&w=600&auto=format&fit=crop"},
            {"name": "투몬 비치", "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&auto=format&fit=crop"},
            {"name": "리티디안 포인트", "image_url": "https://images.unsplash.com/photo-1519046904884-53103b34b206?q=80&w=600&auto=format&fit=crop"},
            {"name": "이나라한 해수풀", "image_url": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?q=80&w=600&auto=format&fit=crop"},
            {"name": "차모로 빌리지", "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=600&auto=format&fit=crop"}
        ]
    },
    "하와이": {
        "flag": "🇺🇸",
        "english": "Hawaii",
        "image_url": "image/Honolulu-cover.jpg",
        "description": "환영의 뜻인 '알로하' 정신이 가득한 웅장하고 신비로운 활화산의 섬들, 세계 서퍼들이 사랑하는 푸른 태평양의 거대한 파도와 활기찬 문화가 숨쉬는 곳입니다.",
        "best_time": "4월 ~ 6월 / 9월 ~ 11월 (연중 내내 환상적이지만 가장 온화하고 쾌적한 시기)",
        "attractions": "오아후섬의 와이키키 해변, 하이킹 코스인 다이아몬드 헤드 분화구, 환상의 스노클링 파크 하나우마 베이, 노스 쇼어 서핑 타운",
        "food": "참치 등 신선한 생선회를 버무린 웰빙 포케(Poke), 하와이식 함박 스테이크 덮밥 로코모코, 설탕을 묻힌 따끈한 말라사다 도넛, 달콤 시원한 쉐이브 아이스",
        "tip": "수중 해양보호구역인 하나우마 베이는 입장객 수가 엄격히 제한되어 100% 온라인 사전 예약을 성공해야 갈 수 있으니 최소 여행 몇 주 전에 티켓팅 스케줄을 확인해 두어야 합니다.",
        "things_to_do": [
            {"place": "와이키키 해변", "desc": "서핑 강습을 받고 파도를 헤치며 와이키키 서핑 즐기기"},
            {"place": "다이아몬드 헤드", "desc": "분화구 정상에 올라 끝없이 펼쳐진 호놀룰루 전경 조망하기"},
            {"place": "하나우마 베이", "desc": "에메랄드 바다에서 알록달록한 산호와 야생 바다거북과 스노클링하기"},
            {"place": "노스 쇼어 새우 트럭", "desc": "명물 트럭에서 갈릭 쉬림프와 시원한 맥주 맛보기"},
            {"place": "루아우 디너 쇼", "desc": "하와이 전통 훌라 댄스 공연과 전통 돼지구이 요리 감상하기"}
        ],
        "restaurants": [
            {
                "name": "Ono Seafood (오노 씨푸드)",
                "tag": "하와이안 포케",
                "desc": "참치와 연어를 특제 비법 양념에 버무려 밥 위에 올려 먹는 호놀룰루 최고의 로컬 포케 전문점입니다.",
                "booking": "주문 포장(Take-out) 중심 매장으로 별도 예약은 불가하지만, 매일 재료가 소진되면 즉시 조기 영업 종료하므로 오후 2시 이전에 찾아가세요."
            },
            {
                "name": "Wolfgang's Steakhouse",
                "tag": "드라이에이징 스테이크",
                "desc": "뜨거운 접시에 지글지글 끓으며 서빙되는 명품 드라이에이징 티본 스테이크 맛집입니다.",
                "booking": "최소 1~2개월 전에 오픈테이블(OpenTable) 앱을 통한 테이블 예약을 강력 추천합니다. 해피아워 전용 카운터석은 예약 불가입니다."
            },
            {
                "name": "Leonard's Bakery (레오나즈)",
                "tag": "말라사다 도넛",
                "desc": "겉은 바삭하고 속은 쫄깃하며 설탕이 듬뿍 묻어있는 하와이 대표 간식 도넛 전문점입니다.",
                "booking": "방문 전 유선 통화나 전용 온라인 웹사이트로 사전 픽업 주문(Pre-order)을 접수하면, 한결 긴 대기줄을 바로 우회하여 바로 수령할 수 있습니다."
            },
            {
                "name": "House Without A Key",
                "tag": "다이닝 & 라이브 바",
                "desc": "바다 전망의 오픈 에어 레스토랑으로 라이브 훌라 공연을 보며 일몰 아래 칵테일을 즐길 수 있습니다.",
                "booking": "공식 리조트 홈페이지 혹은 오픈테이블(OpenTable) 예약 필수입니다. 매일 일몰과 함께하는 라이브 공연 뷰는 보통 1개월 전에 마감됩니다."
            }
        ],
        "attractions_gallery": [
            {"name": "와이키키 해변", "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&auto=format&fit=crop"},
            {"name": "다이아몬드 헤드", "image_url": "https://images.unsplash.com/photo-1542224566-6e85f2e6772f?q=80&w=600&auto=format&fit=crop"},
            {"name": "하나우마 베이", "image_url": "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?q=80&w=600&auto=format&fit=crop"},
            {"name": "진주만 기념관", "image_url": "https://images.unsplash.com/photo-1580137189272-c9379f8864fd?q=80&w=600&auto=format&fit=crop"},
            {"name": "노스 쇼어", "image_url": "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=600&auto=format&fit=crop"}
        ]
    },
    "보스턴": {
        "flag": "🇺🇸",
        "english": "Boston",
        "image_url": "image/boston.jpeg",
        "description": "미국 역사와 독립운동의 숨결이 골목 구석구석 서려 있는 곳이자 하버드 대학교, MIT 등 세계 최고 지성들이 모여 숨쉬는 품격 있고 차분한 역사와 학문의 도시입니다.",
        "best_time": "9월 ~ 10월 (강변을 따라 뉴잉글랜드 지방의 화려한 단풍이 번지는 완벽한 가을)",
        "attractions": "붉은 벽돌 선을 따라 걷는 역사 산책 프리덤 트레일, 하버드 대학교 & MIT 캠퍼스 투어, 보스턴 커먼 공원 호숫가, 활기찬 퀸시 마켓 푸드코트",
        "food": "진하고 고소한 조개 크림 수프 뉴잉글랜드 클램 차우더, 싱싱하고 꽉 찬 살의 랍스터 롤, 클래식 디저트 보스턴 크림 파이",
        "tip": "하버드 대학 캠퍼스에서는 재학생들이 직접 들려주는 위트 있고 흥미진진한 교내 역사 워킹 투어 프로그램(Hahvahd Tour)을 꼭 체험해 보세요. 아주 값진 경험이 됩니다.",
        "things_to_do": [
            {"place": "보스턴 커먼 공원", "desc": "백조 보트를 타고 가을 호수를 건너며 낙엽 산책 즐기기"},
            {"place": "프리덤 트레일", "desc": "시내 바닥의 붉은 벽돌 선을 걸으며 미국 독립 역사 탐험하기"},
            {"place": "하버드 대학교 캠퍼스", "desc": "존 하버드 동상의 구두 발등을 문지르며 합격 소원 빌기"},
            {"place": "퀸시 마켓", "desc": "푸드코트 아케이드에서 살이 꽉 찬 뉴잉글랜드 랍스터 롤 먹기"},
            {"place": "찰스 강변", "desc": "카약을 타고 강바람을 맞으며 보스턴의 아름다운 마천루 감상하기"}
        ],
        "restaurants": [
            {
                "name": "Union Oyster House",
                "tag": "굴 요리 & 클램 차우더",
                "desc": "1826년 개업한 미국에서 가장 오래된 역사적인 식당으로 생굴과 정통 클램 차우더가 대표적입니다.",
                "booking": "전화나 오픈테이블(OpenTable) 앱 예약을 지원합니다. 예약 시 케네디 대통령이 주말마다 찾던 JFK 전용 지정 부스석 예약 가능 여부를 문의해 보세요."
            },
            {
                "name": "Neptune Oyster",
                "tag": "랍스터 롤",
                "desc": "보스턴 노스엔드의 대기 필수 맛집으로 버터에 버무린 따뜻하고 푸짐한 랍스터 롤을 맛볼 수 있습니다.",
                "booking": "사전 예약은 받지 않으며 매장 앞 종이 리스트 대기 방식입니다. 점심 시간의 경우 최소 1시간에서 최고 2시간 반의 대기 시간이 생깁니다."
            },
            {
                "name": "Legal Sea Foods",
                "tag": "해산물 다이닝",
                "desc": "대통령 취임식에도 쓰이는 전통 깊은 해산물 브랜드로 대구 구이와 신선한 랍스터 찜이 일품입니다.",
                "booking": "오픈테이블(OpenTable)이나 구글 맵 사전 예약을 활용해 주말 저녁 시간 테이블 예약을 확보해 두는 것을 권장합니다."
            },
            {
                "name": "Mike's Pastry (마이크스 패스트리)",
                "tag": "이탈리안 카놀리",
                "desc": "이탈리안 타운 노스엔드의 대표 디저트 가게로 크림이 꽉 찬 파삭한 카놀리가 대표 명물입니다.",
                "booking": "예약을 받지 않는 포장 전문 빵집입니다. 줄이 매우 길지만 회전율이 빨라 대기 시간은 짧습니다. 오직 현금 결제(Cash only)만 지원합니다."
            }
        ],
        "attractions_gallery": [
            {"name": "프리덤 트레일", "image_url": "https://images.unsplash.com/photo-1579244095400-84a141b714b6?q=80&w=600&auto=format&fit=crop"},
            {"name": "하버드 대학교", "image_url": "https://images.unsplash.com/photo-1564982752274-38c415908757?q=80&w=600&auto=format&fit=crop"},
            {"name": "보스턴 커먼", "image_url": "https://images.unsplash.com/photo-1569336415962-a4bd9f69cd83?q=80&w=600&auto=format&fit=crop"},
            {"name": "퀸시 마켓", "image_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=600&auto=format&fit=crop"},
            {"name": "MIT 캠퍼스", "image_url": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=600&auto=format&fit=crop"}
        ]
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

content_col1, content_col2 = st.columns([1.1, 1], vertical_alignment="top")

with content_col1:
    # Display stunning, full-bleed high resolution image
    st.image(data["image_url"], width='stretch')

with content_col2:
    # Display highly styled information card
    st.markdown(f"""
        <div class="travel-card">
            <div class="city-title">
                {data['flag']} {selected_city} 
                <span style="font-size: 1.25rem; color: #818cf8; font-weight: 300; margin-left: 10px; font-family: 'Outfit';">
                    {data['english']}
                </span>
            </div>
            <div class="city-desc">{data['description']}</div>
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-label"><span>📅</span><span>최적의 시즌</span></div>
                    <div class="info-value">{data['best_time']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">📍 핵심 방문 명소</div>
                    <div class="info-value">{data['attractions']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label"><span>🍽️</span><span>현지 추천 푸드</span></div>
                    <div class="info-value">{data['food']}</div>
                </div>
                <div class="info-item">
                    <div class="info-label">💡 여행 전문가의 꿀팁</div>
                    <div class="info-value">{data['tip']}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Full-width: Recommended Activities Section
st.markdown('<div class="section-title">현지 추천 액티비티 & 버킷리스트</div>', unsafe_allow_html=True)
for idx, activity in enumerate(data["things_to_do"]):
    st.markdown(f"""
        <div class="activity-row-card">
            <div style="font-weight: 700; color: #818cf8; font-size: 1.05rem; margin-bottom: 0.3rem;">{activity['place']}</div>
            <div style="font-size: 0.9rem; color: #cbd5e1; font-weight: 400; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{activity['desc']}</div>
        </div>
    """, unsafe_allow_html=True)

# Full-width: Recommended Restaurants Section
st.markdown('<div class="section-title">🍽️ 현지 추천 맛집 리스트</div>', unsafe_allow_html=True)
rest_cols = st.columns(4)
for idx, restaurant in enumerate(data["restaurants"]):
    with rest_cols[idx]:
        st.markdown(f"""
            <div class="restaurant-card">
                <div class="restaurant-name">{restaurant['name']}</div>
                <div class="restaurant-tag">{restaurant['tag']}</div>
                <div class="restaurant-desc">{restaurant['desc']}</div>
                <div style="width: 100%; padding-top: 0.75rem; border-top: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.8rem; color: #38bdf8; font-weight: 500; line-height: 1.5; text-align: left; word-break: keep-all;">
                    📌 &nbsp;{restaurant['booking']}
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



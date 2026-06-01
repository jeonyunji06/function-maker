import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 폰트 기본 설정 및 마이너스 부호 깨짐 방지
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# 페이지 기본 세팅
st.set_page_config(page_title="2022 개정 교육과정 무리함수 탐구", layout="wide")

# 사이드바: 전 단원 자유 탐구형 메뉴 구성
st.sidebar.title("📘 무리함수 디지털 교구")
st.sidebar.write("2022 개정 교육과정 수학 교과서 반영")
menu = st.sidebar.radio(
    "학습 단계를 선택하세요",
    [
        "1. 무리식의 정의와 실수가 될 조건",
        "2. 무리함수의 뜻과 정의역",
        "3. 무리함수 y = ±√(±ax)의 그래프 (기본형)",
        "4. 🔍 내가 직접 살펴보고 싶은 그래프 입력"
    ]
)

# 1단계: 무리식의 정의
if menu == "1. 무리식의 정의와 실수가 될 조건":
    st.title("🧪 1. 무리식의 정의와 실수가 될 조건")
    st.markdown("""
    ### 💡 무리식이란 무엇일까요?
    근호($\\sqrt{\\quad}$) 안에 문자가 포함되어 있는 식 중에서 유리식으로 나타낼 수 없는 식을 **무리식**이라고 합니다.
    
    ### ⚠️ 무리식의 값이 '실수'가 되기 위한 필수 조건
    무리식의 값이 실수가 되려면 **근호 안의 식의 값이 0 이상**이어야 합니다. 
    """)
    st.write("---")
    
    st.subheader("🔍 내 맘대로 만드는 무리식 판별기")
    st.write("원하는 무리식의 형태를 고르고 숫자를 입력한 뒤, $x$값을 움직여보세요!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        expr_style = st.radio("1. 탐구할 무리식 형태 선택", ["기본 무리식 형태: √(ax + b)", "분모 무리식 형태: 1 / √(ax + b)"])
        a_1 = st.number_input("2. x의 계수 (a) 입력", value=1.0, step=0.5, key="a_1")
        b_1 = st.number_input("3. 루트 안의 상수항 (b) 입력", value=2.0, step=1.0, key="b_1")
        
        if expr_style == "기본 무리식 형태: √(ax + b)":
            st.markdown(f"### 현재 식: $\\sqrt{{{a_1}x + ({b_1})}}$")
        else:
            st.markdown(f"### 현재 식: $\\frac{{1}}{{\\sqrt{{{a_1}x + ({b_1})}}}}$")

    with col2:
        x_input = st.slider("4. x의 값을 움직이며 실수가 되는지 확인해보세요.", -10, 10, 0)
        inside = a_1 * x_input + b_1
        st.write(f"👉 현재 대입한 $x = {x_input}$ 일 때, 근호 안의 식의 값: ${a_1} \\times {x_input} + ({b_1}) = {inside}$")
        
        if expr_style == "기본 무리식 형태: √(ax + b)":
            if inside >= 0:
                st.success(f"✨ 결과값: $\\sqrt{{{inside}}} \\approx {np.sqrt(inside):.2f}$ 이므로 **실수**입니다! (좌표평면에 점을 찍을 수 있어요)")
            else:
                st.error(f"❌ 결과값: $\\sqrt{{{inside}}}$ 은 **허수**입니다! (근호 안이 음수이므로 실수가 아니며, 좌표평면에 그릴 수 없어요)")
        else:
            if inside > 0:
                st.success(f"✨ 결과값: $\\frac{{1}}{{\\sqrt{{{inside}}}}} \\approx {1/np.sqrt(inside):.2f}$ 이므로 **실수**입니다!")
            elif inside == 0:
                st.error("❌ 분모가 0이 되어 수학적으로 정의되지 않는 상태(불능)입니다! 분모는 0이 될 수 없어요.")
            else:
                st.error(f"❌ 결과값: $\\frac{{1}}{{\\sqrt{{{inside}}}}}$ 은 **허수**입니다! 분모 근호 안이 음수이므로 실수가 아닙니다.")

# 2단계: 무리함수의 뜻과 정의역
elif menu == "2. 무리함수의 뜻과 정의역":
    st.title("📌 2. 무리함수의 뜻과 정의역")
    st.markdown("""
    ### 💡 무리함수의 정의역 유도 원리
    무리함수에서 정의역이 특별히 주어지지 않은 경우, **근호 안의 식의 값이 0 이상이 되도록 하는 실수 전체의 집합**을 구하면 됩니다.
    즉, $y = \\sqrt{ax+b}$ 라면 $ax + b \\ge 0$ 이라는 일차부등식을 풀면 됩니다!
    """)
    st.write("---")
    
    st.subheader("🧮 나만의 무리함수 정의역 유도기")
    st.write("함수 식의 계수들을 직접 입력하면 시스템이 자동으로 정의역을 계산하고 풀어줍니다.")
    
    a_2 = st.number_input("x의 계수 (a)를 입력하세요.", value=-1.0, step=0.5, key="a_2")
    b_2 = st.number_input("루트 안의 상수항 (b)를 입력하세요.", value=2.0, step=1.0, key="b_2")
    
    if a_2 == 0:
        st.error("⚠️ x의 계수(a)가 0이면 무리함수가 되지 않아요! 0이 아닌 숫자를 입력해주세요.")
    else:
        st.markdown(f"### 🔍 탐구 중인 함수: $y = \\sqrt{{{a_2}x + ({b_2})}}$")
        
        st.info("📊 **정의역 조건 유도 과정**")
        st.write(f"1단계 (근호 안은 0 이상이어야 함):  ${a_2}x + ({b_2}) \\ge 0$")
        st.write(f"2단계 (상수항 이항하기):  ${a_2}x \\ge {-b_2}$")
        
        limit_x = -b_2 / a_2
        if a_2 > 0:
            st.write(f"3단계 (양수 $a={a_2}$로 나누기, 부등호 그대로):  $x \\ge \\frac{{{-b_2}}}{{{a_2}}} \\implies x \\ge {limit_x:.1f}$")
            st.success(f"🎯 최종 정의역 집합: $\\{{ x \\mid x \\ge {limit_x:.1f} \\}}$")
        else:
            st.write(f"3단계 (음수 $a={a_2}$로 나누기, **부등호 방향 반대로!**):  $x \\le \\frac{{{-b_2}}}{{{a_2}}} \\implies x \\le {limit_x:.1f}$")
            st.success(f"🎯 최종 정의역 집합: $\\{{ x \\mid x \\le {limit_x:.1f} \\}}$")

# 3단계: 기본형 그래프 사분면 탐구
elif menu == "3. 무리함수 y = ±√(±ax)의 그래프 (기본형)":
    st.title("📐 3. 무리함수 기본형 그래프와 사분면 방향")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("⚙️ 형태 선택")
        graph_type = st.radio(
            "어떤 형태의 그래프를 보시겠습니까?",
            [
                "① y = √x  (제1사분면)",
                "② y = √(-x) (제2사분면)",
                "③ y = -√(-x) (제3사분면)",
                "④ y = -√x  (제4사분면)"
            ]
        )
        st.markdown("""
        **💡 방향을 기억하는 치트키!**
        - **$x$ 앞의 부호**: 그래프의 **좌우** 방향 결정 (양수면 우측, 음수면 좌측)
        - **루트 앞의 부호**: 그래프의 **상하** 방향 결정 (양수면 위쪽, 음수면 아래쪽)
        """)
    with col2:
        fig, ax = plt.subplots(figsize=(7, 5))
        x_pts = np.linspace(0, 10, 400)
        
        if "①" in graph_type:
            ax.plot(x_pts, np.sqrt(x_pts), color='#1d4ed8', lw=3, label="$y=\\sqrt{x}$")
        elif "②" in graph_type:
            ax.plot(-x_pts, np.sqrt(x_pts), color='#b91c1c', lw=3, label="$y=\\sqrt{-x}$")
        elif "③" in graph_type:
            ax.plot(-x_pts, -np.sqrt(x_pts), color='#047857', lw=3, label="$y=-\\sqrt{-x}$")
        elif "④" in graph_type:
            ax.plot(x_pts, -np.sqrt(x_pts), color='#f59e0b', lw=3, label="$y=-\\sqrt{x}$")
            
        ax.axhline(0, color='black', lw=1.2)
        ax.axvline(0, color='black', lw=1.2)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.legend(loc="upper right", fontsize=11)
        st.pyplot(fig)

# 4단계: 자유 탐구 공간 (그래프 내 한글 제거하여 깨짐 원천 차단)
else:
    st.title("🔍 4. 내가 직접 살펴보고 싶은 그래프 입력")
    st.write("궁금하거나 확인해보고 싶은 무리함수 식을 마음대로 입력하고, 그래프가 어떻게 그려지는지 자유롭게 탐구해보세요!")
    st.write("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("✏️ 나만의 함수 식 설계하기")
        
        type_sign = st.radio("1단계: 그래프의 상하 방향을 정할 루트 앞 부호", ["+", "-"])
        sign_val = 1.0 if type_sign == "+" else -1.0
        
        a = st.number_input("2단계: 그래프의 좌우 방향과 폭을 정할 x 앞의 계수 (a)", value=1.0, step=0.5)
        b = st.number_input("3단계: 루트 안의 평행이동에 영향을 주는 상수항 (b)", value=0.0, step=1.0)
        c = st.number_input("4단계: 그래프를 위아래로 움직일 루트 밖의 상수항 (c)", value=0.0, step=1.0)
        
        display_sign = "" if type_sign == "+" else "-"
        st.markdown(f"""
        ### 📊 내가 설계한 함수식:
        ## $y = {display_sign}\\sqrt{{{a}x + ({b})}} + ({c})$
        """)

    with col2:
        if a == 0:
            st.error("⚠️ x의 계수(a)가 0이면 무리함수가 성립하지 않아요! 값을 다시 변경해볼까요?")
        else:
            start_x = -b / a
            start_y = c
            
            if a > 0:
                x_vals = np.linspace(start_x, start_x + 12, 400)
            else:
                x_vals = np.linspace(start_x - 12, start_x, 400)
                
            y_vals = sign_val * np.sqrt(a * x_vals + b) + c
            
            fig, ax = plt.subplots(figsize=(8, 6))
            # 범례 한글을 수학 수식 기호인 $y = f(x)$ 로 변경
            ax.plot(x_vals, y_vals, color='#1e3a8a', lw=3, label="$y = f(x)$")
            
            # 범례 한글을 깔끔하게 'Start' 문구로 변경
            ax.plot(start_x, start_y, 'ro', markersize=10, label=f"Start ({start_x:.1f}, {start_y:.1f})")
            ax.text(start_x + 0.5, start_y + 0.5, f"({start_x:.1f}, {start_y:.1f})", color='red', weight='bold')
            
            ax.axhline(0, color='black', lw=1.2)
            ax.axvline(0, color='black', lw=1.2)
            ax.grid(True, linestyle='--', alpha=0.6)
            
            ax.set_xlim(start_x - 15, start_x + 15)
            ax.set_ylim(start_y - 15, start_y + 15)
            ax.legend(loc="upper right")
            
            st.pyplot(fig)
            
            st.info(f"""
            📌 **이 그래프의 비밀 노트**
            - **출발하는 시작점**: $({start_x:.1f}, {start_y:.1f})$
            - **그래프가 존재하는 x의 범위(정의역)**: $\\{{ x \\mid x \\ge {start_x:.1f} \\}}$ 이라면,
            - **그래프가 존재하는 y의 범위(치역)**: $\\{{ y \\mid y \\ge {start_y:.1f} \\}}$ 형태입니다.
            """)
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정 및 마이너스 부호 깨짐 방지
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# 페이지 기본 세팅
st.set_page_config(page_title="2022 개정 교육과정 무리함수 탐구", layout="wide")

# 사이드바: 교과서의 대단원/소단원 흐름 그대로 구성
st.sidebar.title("📘 무리함수 디지털 교구")
st.sidebar.write("2022 개정 교육과정 수학교과서 반영")
menu = st.sidebar.radio(
    "학습 단계를 선택하세요",
    [
        "1. 무리식의 정의와 실수가 될 조건",
        "2. 무리함수의 뜻과 정의역",
        "3. 무리함수 y = ±√(±ax)의 그래프 (기본형)",
        "4. 무리함수 y = a√(k(x-p)) + q 탐구 (일반형)"
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
    만약 분모에 무리식이 있다면 분모는 0이 될 수 없으므로 0보다 커야 합니다.
    """)
    st.write("---")
    st.subheader("🔍 실시간 실수 조건 판별기")
    
    expr_type = st.selectbox("탐구할 식의 형태를 고르세요.", ["√(x - 3)", "1 / √(x - 1)"])
    x_input = st.slider("x의 값을 움직이며 식의 변화를 관찰해보세요.", -10, 10, 0)
    
    if expr_type == "√(x - 3)":
        inside = x_input - 3
        st.write(f"현재 근호 안의 식: ${x_input} - 3 = {inside}$")
        if inside >= 0:
            st.success(f"✨ 결과값은 $\\sqrt{{{inside}}} \\approx {np.sqrt(inside):.2f}$ 이므로 **실수**입니다. (좌표평면에 표현 가능!)")
        else:
            st.error(f"❌ 근호 안이 음수(${inside}$)이므로 **허수**입니다. (좌표평면에 그릴 수 없음!)")
            
    elif expr_type == "1 / √(x - 1)":
        inside = x_input - 1
        st.write(f"현재 분모 근호 안의 식: ${x_input} - 1 = {inside}$")
        if inside > 0:
            st.success(f"✨ 결과값은 $1 / \\sqrt{{{inside}}} \\approx {1/np.sqrt(inside):.2f}$ 이므로 **실수**입니다.")
        elif inside == 0:
            st.error("❌ 분모가 0이 되므로 수학적으로 정의되지 않는 식입니다!")
        else:
            st.error(f"❌ 근호 안이 음수(${inside}$)이므로 **허수**입니다.")

# 2단계: 무리함수의 뜻과 정의역
elif menu == "2. 무리함수의 뜻과 정의역":
    st.title("📌 2. 무리함수의 뜻과 정의역")
    st.markdown("""
    ### 💡 무리함수란?
    변수 $x$에 대한 무리식으로 나타내어지는 함수를 **무리함수**라고 합니다.
    
    ### 🧩 무리함수의 정의역
    무리함수에서 정의역이 특별히 주어지지 않은 경우, **근호 안의 식의 값이 0 이상이 되도록 하는 실수 전체의 집합**을 정의역으로 정합니다.
    """)
    st.write("---")
    st.subheader("🧮 함수별 정의역 직접 확인하기")
    
    func_select = st.selectbox("확인할 함수 선택", ["y = √(2x - 4)", "y = √(-3x + 6)"])
    
    if func_select == "y = √(2x - 4)":
        st.info("정의역 조건: $2x - 4 \\ge 0 \\implies 2x \\ge 4 \\implies x \\ge 2$")
        st.markdown("**정의역:** $\\{ x \\mid x \\ge 2 \\}$")
    elif func_select == "y = √(-3x + 6)":
        st.info("정의역 조건: $-3x + 6 \\ge 0 \\implies -3x \\ge -6 \\implies x \\le 2$ (음수로 나누면 부등호 방향이 바뀝니다!)")
        st.markdown("**정의역:** $\\{ x \\mid x \\le 2 \\}$")

# 3단계: 기본형 그래프 사분면 탐구
elif menu == "3. 무리함수 y = ±√(±ax)의 그래프 (기본형)":
    st.title("📐 3. 무리함수 기본형 그래프와 사분면 방향")
    st.write("부호의 조합에 따라 그래프가 사분면의 어느 방향으로 뻗어나가는지 확인하세요.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("⚙️ 형태 선택")
        graph_type = st.radio(
            "어떤 형태의 그래프를 보시겠습니까?",
            [
                "① y = √x  (x ≥ 0, y ≥ 0) → 제1사분면",
                "② y = √(-x) (x ≤ 0, y ≥ 0) → 제2사분면",
                "③ y = -√(-x) (x ≤ 0, y ≤ 0) → 제3사분면",
                "④ y = -√x  (x ≥ 0, y ≤ 0) → 제4사분면"
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

# 4단계: 일반형 및 평행이동 탐구
else:
    st.title("🎯 4. 무리함수 일반형 (평행이동) 마스터")
    st.write("슬라이더를 통해 대칭이동과 평행이동이 결합된 종합 그래프를 시각적으로 확인해봅니다.")
    
    with st.sidebar:
        st.header("⚙️ 일반형 변수 조절")
        a = st.slider("a (루트 밖의 계수: 상하 방향 및 폭)", -5.0, 5.0, 1.0, step=0.5)
        k = st.slider("k (루트 안 x의 계수: 좌우 방향 및 폭)", -5.0, 5.0, 1.0, step=0.5)
        p = st.slider("p (x축 방향 평행이동)", -10.0, 10.0, 0.0, step=1.0)
        q = st.slider("q (y축 방향 평행이동)", -10.0, 10.0, 0.0, step=1.0)

    if k == 0 or a == 0:
        st.warning("⚠️ a 또는 k가 0이 되면 무리함수의 형태가 만들어지지 않습니다. 다른 값을 선택해주세요!")
    else:
        if k > 0:
            x_domain = np.linspace(p, p + 12, 400)
        else:
            x_domain = np.linspace(p - 12, p, 400)
            
        y_domain = a * np.sqrt(k * (x_domain - p)) + q
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_domain, y_domain, color='#1e3a8a', lw=3, label=f"$y = {a}\\sqrt{{{k}(x-{p})}} + {q}$")
        
        ax.plot(p, q, 'ro', markersize=9, label=f"시작점 ({p}, {q})")
        ax.text(p + 0.4, q + 0.4, f"({p}, {q})", color='red', weight='bold', fontsize=11)
        
        ax.axhline(0, color='black', lw=1.2)
        ax.axvline(0, color='black', lw=1.2)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.legend(loc="upper right")
        
        st.pyplot(fig)
        
        st.subheader("💡 초보자를 위한 무리함수 그리기 3단계 법칙")
        st.markdown(f"""
        1. **시작점 포착**: 근호 안을 0으로 만드는 $x={p}$와 그때의 $y={q}$를 조합하여 **시작점 ({p}, {q})**에 점을 콕 찍습니다.
        2. **방향 판단**: 
           - $k$의 부호가 **{'+ (양수)' if k>0 else '- (음수)'}**이므로 시작점 기준 **{f"오른쪽" if k>0 else "왼쪽"}**으로 향합니다.
           - $a$의 부호가 **{'+ (양수)' if a>0 else '- (음수)'}**이므로 시작점 기준 **{f"위쪽" if a>0 else "아래쪽"}**으로 향합니다.
           - ✨ 즉, 종합하면 **{f"오른쪽 위" if (k>0 and a>0) else "왼쪽 위" if (k<0 and a>0) else "왼쪽 아래" if (k<0 and a<0) else "오른쪽 아래"}** 방향으로 곡선을 그립니다.
        3. **매끄럽게 연결**: 시작점부터 확인한 방향을 향해 완만하고 부드러운 포물선의 절반 모양 곡선을 이어 나갑니다.
        """)
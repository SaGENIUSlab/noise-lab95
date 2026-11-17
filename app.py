"""NO!SE LAB 95 — Streamlit Community Cloud entrypoint.

Keep the complete original Y2K HTML and its four learning tools intact.
Use Streamlit's *local HTML file* iframe support, NOT /app/static/*.html:
static serving deliberately gives .html files Content-Type: text/plain.
"""
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="NO!SE LAB 95 | AI 윤리 융합 실험실",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container { max-width: 100%; padding: 0.2rem 0.45rem 1rem !important; }
    [data-testid="stAppViewContainer"] { background: #e8deee; }
    header[data-testid="stHeader"] { background: #e8deee; }
    footer { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_file = Path(__file__).resolve().parent / "static" / "noise_lab.html"

if not html_file.is_file():
    st.error("실습실 파일을 찾을 수 없습니다. GitHub에서 static/noise_lab.html 파일을 확인해 주세요.")
    st.stop()

# Local Path is read and embedded as HTML with JavaScript support.
# Unlike /app/static/noise_lab.html, it is NOT served as text/plain.
st.iframe(html_file, width="stretch", height=1080)

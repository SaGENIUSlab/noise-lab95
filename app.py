"""NO!SE LAB 95: Streamlit Community Cloud entrypoint.

Original Y2K HTML is kept intact in static/noise_lab.html.
The live app and all four activities run in the browser; the server doesn't
receive photos used in the HTML widgets.
"""
import streamlit as st

st.set_page_config(
    page_title="NO!SE LAB 95 | AI 윤리 융합 실험실",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_URL = "/app/static/noise_lab.html"

st.markdown(
    """
    <style>
      .block-container { max-width: 100%; padding: .25rem .55rem .55rem !important; }
      #MainMenu, header[data-testid="stHeader"], footer { visibility: hidden; }
      [data-testid="stAppViewContainer"] { background: #e8deee; }
      [data-testid="stIFrame"] { border: 2px solid #82798b; }
      .launchbar { font-family: 'Malgun Gothic',sans-serif; display:flex; align-items:center;
        justify-content:space-between; gap:12px; flex-wrap:wrap; padding:6px 12px;
        background:#dcd5df; color:#333046; border:2px solid;
        border-color:#fff #82798b #82798b #fff; margin-bottom:5px; }
      .launchbar strong {font-size:14px;}
      .launchbar a {color:#332d42!important;text-decoration:none!important; font-weight:700;
        background:#f5e8f8;padding:7px 14px;border:2px solid;
        border-color:#fff #82798b #82798b #fff;}
      .launchbar a:hover {background:#f3cbe4;}
    </style>
    <div class="launchbar">
      <strong>💾 NO!SE LAB 95 · AI 융합 실험실</strong>
      <a href="/app/static/noise_lab.html" target="_blank" rel="noopener noreferrer">
        ↗ 전체 화면에서 열기 · 카메라 사용 권장
      </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.iframe(APP_URL, width="stretch", height=900)

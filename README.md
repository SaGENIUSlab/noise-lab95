# 💾 NO!SE LAB 95 | Streamlit 배포용

4개 실습 프로그램을 **Y2K / Windows 95** 스타일의 햄버거 메뉴로 묶은 통합 실습실입니다.

## 폴더 구성

```text
.
├── app.py                    # Streamlit 시작 파일(이름을 바꾸지 마세요)
├── requirements.txt         # 자동 설치되는 파이썬 패키지
├── .streamlit/
│   └── config.toml          # HTML 파일 제공 기능 활성화
└── static/
    └── noise_lab.html      # 4개 기능이 모두 들어 있는 원본 통합 HTML
```

## GitHub → Streamlit Community Cloud 배포

1. 이 배포용 ZIP을 **압축 해제**하세요. GitHub에 ZIP 파일 하나만 올리면 동작하지 않습니다.
2. [github.com/new](https://github.com/new)에서 새 저장소를 생성합니다. 예: `noise-lab95`. 공개 저장소라면 앱을 누구나 열 수 있습니다. 학생 개인정보나 비밀번호를 저장소에 올리지 마세요.
3. GitHub 저장소에서 **Add file → Upload files**를 눌러 위 파일과 **폴더를 모두** 올립니다. `.streamlit/config.toml`과 `static/noise_lab.html`이 빠지면 안 됩니다. (빈 폴더가 아니라 안에 파일이 포함되도록)
4. [share.streamlit.io](https://share.streamlit.io)로 이동해 GitHub로 로그인한 다음 **Create app → Yup, I have an app**을 선택합니다.
5. Repository: `내아이디/noise-lab95` / Branch: `main` / Main file path: **`app.py`**로 지정합니다.
6. App URL: 예를 들어 `noise-lab95-sua` 입력 시, 사용 가능하다면 `https://noise-lab95-sua.streamlit.app`에 배포됩니다. `.streamlit.app` 앞부분만 직접 정합니다.
7. **Advanced settings**에서 Python **3.11**을 선택합니다. 이 프로젝트는 **Secrets가 필요 없으니 비워 둡니다**. Python 버전은 이후 Settings → General에서 바로 변경할 수 없으며, 변경하려면 삭제·재배포가 필요합니다.
8. **Deploy**를 클릭합니다. 배포되면 앱 페이지를 확인합니다.
9. 앱 재시작이 필요한 경우, [share.streamlit.io](https://share.streamlit.io)의 해당 앱 **⋮ → Reboot**를 사용합니다. 단순 GitHub 코드 변경은 보통 자동으로 반영되므로 매번 Reboot할 필요는 없습니다.
10. `https://선택한주소.streamlit.app`로 접속해 메뉴 및 4개 기능을 확인합니다. **사진 촬영은 화면 상단의 `전체 화면에서 열기` 링크로 연 뒤 허용**하는 것이 더 안정적입니다.

## 확인 항목

- [ ] ☰ 햄버거 메뉴에서 4개 실습실 전환
- [ ] RGB 픽셀 선택 / 정규화 / 클리핑
- [ ] 웹캠 권한 허용 후 자동 촬영 / ZIP 저장
- [ ] Wikimedia Commons 검색 결과 / 대조군 사진 ZIP 저장 (인터넷 연결 필요)
- [ ] 노이즈 강도·알고리즘 전환 / 표·그래프 / ZIP 저장
- [ ] 휴대전화에서도 메뉴 동작

## 주의사항

- **원본 HTML 기능은 정적 프런트엔드에서 실행**됩니다. Streamlit은 그 HTML을 웹에 제공하는 호스트입니다.
- **카메라 사용**은 HTTPS와 브라우저 사용자 권한이 필요합니다. Streamlit 내부 미리보기(iframe)에서 권한이 막히면 **전체 화면에서 열기**를 이용해 직접 웹페이지를 여세요.
- Wikimedia Commons 이미지 검색, 특정 외부 자바스크립트·폰트 자원은 네트워크 상태에 따라 차단될 수 있습니다.
- 원본 코드에서 브라우저 메모리에 보관하는 사진은 Streamlit 서버 데이터베이스에 저장되지 않습니다. 그러나 **Teachable Machine에 직접 업로드할 때는 외부 서비스 전송**이 발생합니다.
- 공개 저장소 및 앱은 다른 사람이 접속할 수 있습니다. 비공개로 쓰려면 GitHub/Streamlit 공유 설정을 확인하세요. 고정 URL을 안다고 해서 자동으로 비공개가 되는 것은 아닙니다.
- 이 프로젝트에는 API 키가 없으므로 `.streamlit/secrets.toml` 파일을 만들거나 업로드하지 마세요. 추후 실제 비밀 키가 필요한 기능을 추가한 경우에만 Streamlit Cloud의 Secrets 영역을 사용하세요.

## 로컬 실행(선택)

```bash
pip install -r requirements.txt
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 열 수 있습니다. 웹캠 작동 여부는 기기와 브라우저 권한에 따라 다릅니다.

## 업데이트

디자인이나 실습 기능을 수정한 뒤 GitHub에서 `static/noise_lab.html`만 새 파일로 교체하여 Commit하면 Streamlit Community Cloud가 변경 사항을 감지합니다.
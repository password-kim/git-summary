# 📋 Git 커밋 요약기 (Git Commit Summary Tool)

> 로컬 Git 저장소에서 작성자와 날짜 범위를 지정하면  
> 해당 기간 동안의 커밋 로그를 추출하여 요약하고 `.txt` 파일로 저장하는 도구입니다.

---

## ✨ 주요 기능

- 📁 Git 프로젝트 폴더 선택
- 👤 작성자 이름 필터링 (필수)
- 📅 시작일 / 종료일 설정
- 🔍 커밋 메시지 추출 및 요약 표시
- 📥 커밋 내역 `.txt` 파일로 저장
- 🧾 `requirements.txt` 자동 생성

---

## 🖥 실행 방법 (Python 환경)

1. Python 설치: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. 저장소 클론:
   ```bash
   git clone https://github.com/yourname/git-weekly-summary.git
   cd git-weekly-summary

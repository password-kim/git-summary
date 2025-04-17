import zipfile
import os
import sys

# 버전 받아오기
version = sys.argv[1] if len(sys.argv) > 1 else "unknown"

# ✅ 원하는 저장 경로 설정 (상대 경로 또는 절대 경로)
output_dir = "release"  # 또는 "C:/KYH/Exports"
os.makedirs(output_dir, exist_ok=True)

output_zip = os.path.join(output_dir, f"GitSummary_v{version}.zip")

files_to_include = [
    "dist/main.exe",
    "README.md"
]

with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_include:
        if os.path.exists(file):
            zipf.write(file, os.path.basename(file))
            print(f"✅ 추가됨: {file}")
        else:
            print(f"❌ 파일 없음: {file}")

print(f"\n📦 압축 완료 → {output_zip}")

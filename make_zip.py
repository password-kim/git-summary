import zipfile
import os
import sys

# 버전명 받아오기
version = sys.argv[1] if len(sys.argv) > 1 else "unknown"

output_zip = f"GitSummary_v{version}.zip"

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

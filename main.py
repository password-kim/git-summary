import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from collections import Counter
import os

# ✅ requirements.txt 자동 생성
def create_requirements_if_needed():
    if not os.path.exists("requirements.txt"):
        try:
            with open("requirements.txt", "w", encoding="utf-8") as f:
                result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE, text=True)
                f.write(result.stdout)
        except Exception as e:
            print("requirements.txt 생성 실패:", str(e))

create_requirements_if_needed()  # 실행 시 1회 호출

# 🔍 커밋 추출
def get_commits(repo_path, author, since, until):
    cmd = ["git", "-C", repo_path, "log", "--pretty=format:%s", f"--author={author}"]
    if since:
        cmd.append(f"--since={since}")
    if until:
        cmd.append(f"--until={until}")

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        if result.returncode != 0:
            return [f"[실패] Git 로그 불러오기 실패:\n{result.stderr}"]
        if not result.stdout:
            return ["[결과 없음] 해당 기간에 커밋 없음"]
        return result.stdout.strip().split("\n")
    except Exception as e:
        return [f"[예외 발생] {str(e)}"]

def browse_folder():
    path = filedialog.askdirectory()
    if path:
        repo_path_entry.delete(0, tk.END)
        repo_path_entry.insert(0, path)

def on_submit():
    repo_path = repo_path_entry.get().strip()
    author = author_entry.get().strip()
    since = since_entry.get().strip()
    until = until_entry.get().strip()

    if not repo_path or not author:
        messagebox.showerror("오류", "프로젝트 경로와 작성자 이름은 필수입니다.")
        return

    commits = get_commits(repo_path, author, since, until)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "\n".join(commits))

    global last_commits
    last_commits = commits

def save_txt():
    if not last_commits:
        messagebox.showwarning("저장 실패", "먼저 요약을 실행해주세요.")
        return

    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            for line in last_commits:
                f.write(line + "\n")
        messagebox.showinfo("저장 완료", f"{path} 로 저장했습니다.")

# 🖼 Tkinter GUI
root = tk.Tk()
root.title("📋 Git 커밋 요약기")
root.geometry("700x600")

tk.Label(root, text="📁 Git 프로젝트 경로:").pack()
frame1 = tk.Frame(root)
frame1.pack()
repo_path_entry = tk.Entry(frame1, width=60)
repo_path_entry.pack(side=tk.LEFT)
tk.Button(frame1, text="찾아보기", command=browse_folder).pack(side=tk.LEFT)

tk.Label(root, text="👤 작성자 이름 (필수):").pack()
author_entry = tk.Entry(root, width=40)
author_entry.pack()

tk.Label(root, text="📅 시작일 (예: 2024-04-01):").pack()
since_entry = tk.Entry(root, width=20)
since_entry.pack()

tk.Label(root, text="📅 종료일 (예: 2024-04-15):").pack()
until_entry = tk.Entry(root, width=20)
until_entry.pack()

tk.Button(root, text="🔍 요약하기", command=on_submit).pack(pady=10)

result_text = tk.Text(root, height=20)
result_text.pack()

tk.Button(root, text="📥 TXT 저장", command=save_txt).pack(pady=10)

last_commits = []
root.mainloop()

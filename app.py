from flask import Flask, render_template, request, send_file
from summary import get_summary
import os

app = Flask(__name__)
last_commits = []  # 마지막 커밋 리스트 저장용

@app.route('/', methods=['GET', 'POST'])
def index():
    global last_commits
    summary = None
    if request.method == 'POST':
        repo_path = request.form.get('repo_path')
        author = request.form.get('author')
        since = request.form.get('since')
        until = request.form.get('until')
        summary = get_summary(repo_path, author, since, until)
        last_commits = summary['commits']  # 다운로드용으로 저장
    return render_template('index.html', summary=summary)

@app.route('/download')
def download():
    global last_commits
    path = "commits.txt"
    with open(path, "w", encoding="utf-8") as f:
        for line in last_commits:
            f.write(line + "\n")
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

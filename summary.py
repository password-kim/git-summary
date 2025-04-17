import subprocess
from datetime import datetime
from collections import Counter

def get_git_log_custom(repo_path, author_name=None, since_date=None, until_date=None):
    cmd = ["git", "-C", repo_path, "log", "--pretty=format:%an||%s"]  # %an: 작성자 이름

    if since_date:
        cmd.append(f"--since={since_date}")
    if until_date:
        cmd.append(f"--until={until_date}")

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        if result.returncode != 0:
            return [f"[Git 실행 실패]\n{result.stderr}"]
        if not result.stdout:
            return ["[조회된 커밋이 없습니다]"]

        lines = result.stdout.strip().split("\n")
        commits = [line.split("||")[1] for line in lines if line.startswith(author_name + "||")]
        return commits

    except Exception as e:
        return [f"[예외 발생] {str(e)}"]

def summarize_commits(commits):
    words = []
    for msg in commits:
        words += msg.lower().split()
    counter = Counter(words)
    return counter.most_common(10)

def get_summary(repo_path, author_name=None, since_date=None, until_date=None):
    commits = get_git_log_custom(repo_path, author_name, since_date, until_date)
    summary = summarize_commits(commits)
    return {
        'commits': commits,
        'keywords': summary
    }

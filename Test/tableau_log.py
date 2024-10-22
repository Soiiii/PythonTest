import os

# Tableau 로그 파일 경로 지정
log_path = r"/**/My Tableau Repository/Logs"

# 로그 파일 읽기
for log_file in os.listdir(log_path):
    if log_file.endswith(".log"):
        with open(os.path.join(log_path, log_file), 'r') as file:
            print(f"Reading {log_file}...")
            print(file.read())

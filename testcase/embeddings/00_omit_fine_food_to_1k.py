import sqlite3
import csv

## 

# SQLite 데이터베이스 파일 경로
database_file = 'data/database.sqlite'

# 연결 및 커서 생성
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# 테이블에서 최대 1000개의 데이터 조회
query = "SELECT * FROM Reviews LIMIT 1000"
cursor.execute(query)
rows = cursor.fetchall()

# 테이블의 열 이름 가져오기
column_names = [description[0] for description in cursor.description]

# 데이터베이스 연결 종료
conn.close()

# CSV 파일로 데이터 저장
csv_file = 'data/fine_food_reviews_1k.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # CSV 파일에 열 이름 쓰기
    writer.writerow(column_names)

    # CSV 파일에 데이터 쓰기
    writer.writerows(rows)

print(f"데이터가 '{csv_file}' 파일에 저장되었습니다.")

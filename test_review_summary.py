from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

import pandas as pd

datafile_path = "data/cookie_reviews_100.csv"
# 엑셀 데이터 로드
df = pd.read_csv(datafile_path)  # 엑셀 파일 경로 입력
df.fillna('', inplace=True)  # 결측치 처리

# 데이터 결합 (리뷰 텍스트를 모두 하나의 텍스트로 결합)
all_reviews = ' '.join(df['Text'].astype(str))

def summarize_all_reviews(all_reviews):
	completion = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=[
			{"role": "system", "content": "You're an ecommerce product analyst."},
			{"role": "assistant", "content": ""},
			{"role": "user", "content": "Here are some product reviews:\n\n`${all_reviews}`\n\nPlease summarize the key points mentioned in this review and translate them into Korean."}
		],
		max_tokens=200,
		n=1,
		temperature=0.5
	)

	return completion.choices[0].message

# 전체 리뷰 요약 요청
summary = summarize_all_reviews(all_reviews)

print("Summary:", summary)
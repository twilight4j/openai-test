from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

import pandas as pd

"""
# 리뷰분석
## 절차
1. 리뷰DB 조회
2. 리뷰데이터를 하나의 텍스트로 결합
3. 결합한 테스트를 Prompt 로 입력하여 요약 요청
## 요약결과
response.usage: CompletionUsage(completion_tokens=196, prompt_tokens=6909, total_tokens=7105)
Summary: ChatCompletionMessage(content='이 쿠키는 매우 부드럽고 맛있으며, 건강한 간식으로 적합하다는 긍정적인 평가가 많습니다. 많은 리뷰어들이 쿠키의 부드러운 질감과 고소한 맛을 칭찬했으며, 특히 자녀들이 좋아한다는 언급이 많았습니다. 개별 포장으로 인해 신선함과 편리함이 유지된다는 점도 강조되 었습니다. 칼로리와 영양 성분이 비교적 좋은 편이며, 가벼운 간식으로 적합하다는 의견이 많았습니다. 그러나 일부 리뷰어는 쿠키의 맛이 상업적으로 제조된 것 같고, 자주 사용되는 향신료(특히 시나몬과 올스파이스)가 과하다고 느꼈습니다. 전반적으로 이 쿠키는 건강한 간식으로 추천받고 있으며, 많은 사람들이 재구매 의사를 밝혔습니다.', role='assistant', function_call=None, tool_calls=None, refusal=None)
## 분석
리뷰 데이터를 Prompt 로 입력하여 대량의 토큰사용 발생
response.usage: CompletionUsage(completion_tokens=196, prompt_tokens=6909, total_tokens=7105)
"""

datafile_path = "data/cookie_reviews_100.csv"
# 엑셀 데이터 로드
df = pd.read_csv(datafile_path)  # 엑셀 파일 경로 입력
df.fillna('', inplace=True)  # 결측치 처리

# 데이터 결합 (리뷰 텍스트를 모두 하나의 텍스트로 결합)
all_reviews = ' '.join(df['Text'].astype(str))

def summarize_all_reviews(all_reviews):
	
	prompt = f"Here are some product reviews:\n\n{all_reviews}\n\nPlease summarize the key points mentioned in this review and translate them into Korean. Provide only the Korean summary without the English summary."
	
	response = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=[
			{
				"role": "system", "content": "You're an ecommerce product analyst."
			},
			{
				"role": "user", "content": prompt
			}
		],
		temperature=0.5,
		max_tokens=500,
		top_p=1
	)
	print("response.usage:", response.usage)

	return response.choices[0].message

# 전체 리뷰 요약 요청
summary = summarize_all_reviews(all_reviews)

print("Summary:", summary)
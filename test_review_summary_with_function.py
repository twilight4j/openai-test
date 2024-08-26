import sqlite3
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()


"""
# 리뷰분석
## 절차
1. Query 를 Prompt 로 입력하여 DB조회 후 리뷰 요약 요청
## 요약결과

## 분석

"""

# SQLite 데이터베이스 파일 경로
DB_FILE = 'data/database.sqlite'


def get_reviews_for_one_product(product_id: str) -> str:
    # Connect to the database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

  # 테이블에서 특정 상품 데이터 조회
    query = "SELECT Text FROM REVIEWS WHERE PRODUCTID = ? LIMIT 100"
    cursor.execute(query, (product_id,))
    rows = cursor.fetchall()

  # 리뷰 데이터를 하나의 문자열로 결합
    combined_reviews = ' '.join([row[0] for row in rows])
    # 데이터베이스 연결 닫기
    cursor.close()
    conn.close()

    return combined_reviews


def summarize_all_reviews(prompt):

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_reviews_for_one_product",
                "description": "Get the review data for the requested product. For example, if a customer requests a summary of reviews for a specific product, this is called to retrieve the review data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The product ID requested by the customer."
                        }
                    },
                    "required": ["product_id"],
                    "additionalProperties": False
                }
            }
        }
    ]

    messages = []
    messages.append({"role": "system", "content": "You're an ecommerce product review analyst. Use the supplied tools to assist the user."})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        temperature=0.5,
        max_tokens=500,
        top_p=1
    )

    print("response.usage:", response.usage)

    return response.choices[0].message


# 전체 리뷰 요약 요청
prompt = "Could you summarize the reviews for product ID B007JFMH8M?"
summary = summarize_all_reviews(prompt)

print("Summary:", summary)

import pandas as pd
import numpy as np
from ast import literal_eval
from utils.embeddings_utils import get_embedding, cosine_similarity

datafile_path = "output/fine_food_reviews_with_embeddings_1k.csv"

# search through the reviews for a specific product
def search_reviews(df, product_description, n=3, pprint=True):
    product_embedding = get_embedding(
        product_description,
        model="text-embedding-3-small"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)[["ProductId", "combined"]]
    )

    results["combined"] = results.combined.str.replace("Title: ", "").str.replace("; Content:", ": ")

    if pprint:
        for _, row in results.iterrows():
            print(f"ProductId: {row['ProductId']}")
            print(row['combined'][:200])
            print()

def main():
    df = pd.read_csv(datafile_path)
    df["embedding"] = df.embedding.apply(literal_eval).apply(np.array)

    while True:
        user_query = input("검색할 리뷰 키워드를 입력하세요 (종료하려면 'q' 입력): ")
        
        if user_query.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        if not user_query.strip():
            print("키워드를 입력해주세요.")
            continue

        results = search_reviews(df, user_query, n=3)
        
        print("\n")  # 결과 사이에 빈 줄 추가
        
if __name__ == "__main__":
    main()
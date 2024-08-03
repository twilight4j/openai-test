import pandas as pd  # for storing text and embeddings data
import ast  # for converting embeddings saved as strings back to arrays
from scipy import spatial  # for calculating vector similarities for search
from IPython.display import display
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-small"
GPT_MODEL = "gpt-4o-mini"

# download pre-chunked text and pre-computed embeddings
# this file is ~200 MB, so may take a minute depending on your connection speed
# embeddings_path = "https://cdn.openai.com/API/examples/data/winter_olympics_2022.csv"
embeddings_path = "output/fine_food_reviews_with_embeddings_1k.csv"

df = pd.read_csv(embeddings_path)

# convert embeddings from CSV str type back to list type
df['embedding'] = df['embedding'].apply(ast.literal_eval)


# search function
def strings_ranked_by_relatedness(
    query: str,
    df: pd.DataFrame,
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
    top_n: int = 5
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatednesses, sorted from most related to least."""
    # 사용자쿼리를 embedding 으로 변환
    query_embedding_response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query,
    )
    query_embedding = query_embedding_response.data[0].embedding
    # 배열에 컨텐츠와 연관성(relatednesses) 담기
    strings_and_relatednesses = [
        (row["combined"], relatedness_fn(query_embedding, row["embedding"]))
        for i, row in df.iterrows()
    ]
    # 연관성 큰 순서대로 정렬하여 상위 n 개 리턴
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]


# examples
user_query = 'Vegetarians'

strings, relatednesses = strings_ranked_by_relatedness(user_query, df, top_n=5)
for string, relatedness in zip(strings, relatednesses):
    print(f"{relatedness=:.3f}")
    display(string)
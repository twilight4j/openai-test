from dotenv import load_dotenv
from openai import OpenAI
import numpy as np

load_dotenv()
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding[:256]

def cosine_similarity(vec1, vec2):
    # 벡터를 NumPy 배열로 변환
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    # 내적 계산
    dot_product = np.dot(vec1, vec2)
    
    # 벡터의 노름 계산
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    # 코사인 유사도 계산
    return dot_product / (norm_vec1 * norm_vec2)
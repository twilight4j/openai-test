from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

REVIEW = "Title: cookies!; Content: these cookies are really good. i love oatmeal, and i love soft-baked cookies. so i definitely love these. they're really healthy and good to take on the go because they come in individual packs."

response = client.embeddings.create(
    input=REVIEW,
    model="text-embedding-3-small"
)

EMBEDDED_REVIEW = response.data[0].embedding
print(EMBEDDED_REVIEW)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Summarize the product review."},
    {"role": "user", "content": REVIEW}
  ]
)

print(completion.choices[0].message)
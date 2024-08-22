from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt=
    "Logo Design Guidelines:\n\n- Brand Name: Abyzzz (a combination of 'abyss' and 'zzz' for sleep)\n- Purpose: Sleep improvement products\n- Design Requirements:\n  - The logo must include 'Abyzzz'\n  - I'd like the 'zzz' in the logo name to convey a sense of sleeping.\n  - No use of shading or shadows\n  - Simple expression with only two colors",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)
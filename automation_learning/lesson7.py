import google.generativeai as genai


genai.configure(api_key=API_KEY)

# select model

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Write a 4 lines poem on python")

print(response.text)


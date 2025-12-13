import google.generativeai as genai

API_KEY = "AIzaSyBpvMjzMw6RBIAPD55Wt6N1H4fP7JlBSQQ"


genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

quote = "Automation is the backbone of the modren AI systems with the snake overflow"

prompt = f"Summarize this quote and also give enhance version of this {quote}"


response = model.generate_content(prompt)

with open("ai_response.txt","w") as file:

            file.write(response.text)

print("AI Response Saved Succesfully in the File")
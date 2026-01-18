from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_response(user_prompt):

    messages = [
        {"role": "system", "content": "You are an professor with years of experience in teaching and research about computer scince."},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=.5,
        max_tokens=100,
    )

    result = response.choices[0].message.content

    return result

if __name__ == "__main__":
    prompt = "Explain what a variable is in python in a short and simple way"
    answer = generate_response(prompt)
    
    with open("output.txt", "w") as file:
        file.write(answer)

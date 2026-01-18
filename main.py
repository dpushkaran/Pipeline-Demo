from openai import OpenAI

client = OpenAI()

def generate_response(user_prompt):

    messages = [
        {"role": "system", "content": "You are an professor with years of experience in teaching and research about computer scince."},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        max_tokens=500,
        n = 3
    )

    result = response.choices[0].message.content

    return result

if __name__ == "__main__":
    prompt = "Explain the concept of an API"
    answer = generate_response(prompt)
    print("Response from the professor:")
    print(answer)

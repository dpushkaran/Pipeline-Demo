from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def generate_response(pdf_path):
    file = client.files.create(
        file=open(pdf_path, "rb"),
        purpose="user_data"
    )
    messages = [
        {"role": "system", "content": "You are a professor with years of experience in teaching and research about computer science."},
        {
            "role": "user",
            "content": [
                {"type": "file", "file": {"file_id": file.id}},
                {"type": "text", "text": "Summarize this PDF with key points and conclusions."}
            ]
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=.5,
        max_tokens=2000,
    )
    result = response.choices[0].message.content
    client.files.delete(file.id)
    return result

if __name__ == "__main__":
    pdf_path = "./04 Intro to Probability.pdf"
    answer = generate_response(pdf_path)
    
    with open("output.txt", "w") as file:
        file.write(answer)
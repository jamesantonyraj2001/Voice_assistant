import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.getenv("")

# Load the ChatGPT model
model_engine = "text-davinci-002"
model_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nUser: Hello, how are you?\nAI: I'm doing well, thank you for asking. How can I help you today?\n\n"
chatgpt = openai.Completion.create(
    engine=model_engine,
    prompt=model_prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

# Define a function to generate responses
def generate_response(prompt):
    prompt_text = f"{model_prompt}User: {prompt}\nAI:"
    chatgpt = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response = chatgpt.choices[0].text.strip()
    return response

# Example usage
user_input = input("User: ")
while user_input.lower() != "exit":
    response = generate_response(user_input)
    print(f"AI: {response}")
    user_input = input("User: ")


import ollama

# Select the model
model = "llama3.2:3b"

# Send a prompt to the LLM
response = ollama.generate(
    model=model,
    prompt="What is Machine Learning?"

)

# Display the response
print("\nLLM Response:")
print(response.response)
# Import required libraries
import groq # Used to connect to the Groq API for AI chat completions
import os # Helps interact with the operating system
import time # Allows us to add typing delays for a more human-like effect

# Initialize chat history with a system message to set the AI's personality
chat_history = [
  {"role": "system", "content": "You are a therapist who gives friendly responses and constructive feedback."}
]

# Function to simulate typing by printing one character at a time
def type_print(message, delay=0.05):
  for char in message:
    print(char, end='', flush=True) # Print characters one by one
    time.sleep(delay) # Wait a bit between each character to simulate typing
  print() # Move to a new line after the message

# Create a Groq client using your API key
client = groq.Groq(api_key="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")

# Initial greeting from the chatbot
print("Hello hello! I'm Bumblebee 🐝, your AI assistant. What's your name?")

# Start chat loop
while True:
  user_input = input("You: ") # Get user input
  # If user types 'exit' end the chat
  if user_input.lower() == 'exit':
    type_print("Goodbye! 👋 Have a great day!", 0.05)
    break

  # Add the user's message to the chat history
  chat_history.append({"role": "user", "content": user_input})

  # Simulated AI typing
  type_print("Bumblebee is typing... ⏳", 0.05)
  time.sleep(1) # Wait before responding

  # Send chat history to Groq API to generate a new response
  response = client.chat.completions.create(
    model = "llama3-8b-8192", # Specify model
    messages=chat_history # Pass the convo so far
  )

  # Extract AI's reply from the API response
  reply = response.choices[0].message.content
  # Print AI's reply with a typing effect
  type_print(f"Bumblebee 🐝: {reply}", 0.05)

  # Add AI response to chat history so future replies have context
  chat_history.append({"role": "assistant", "content": reply})
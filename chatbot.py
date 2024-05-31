from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
model_name = "gpt2"  # You can change this to other models like "gpt2-medium", "gpt2-large", or "gpt2-xl"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize a conversation history
conversation = []

# Start the conversation loop
while True:
    user_input = input("you: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    # Append user message to the conversation
    conversation.append("you: " + user_input)

    # Generate a response
    input_ids = tokenizer.encode("\n".join(conversation), return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # Decode and print multiple responses
    for i, response_id in enumerate(response_ids):
        chatbot_reply = tokenizer.decode(response_id, skip_special_tokens=True)
        print(f"Chatbot {i + 1}:", chatbot_reply)

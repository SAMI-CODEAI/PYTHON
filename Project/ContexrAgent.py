from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ContextAwareChatbot:
    def __init__(self, model_name='microsoft/DialoGPT-medium'):
        print("Loading model... (this may take a few seconds)")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history_ids = None

    def get_response(self, user_input):
        # Encode user input and add end-of-string token
        new_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')

        # Concatenate with chat history
        if self.chat_history_ids is not None:
            bot_input_ids = torch.cat([self.chat_history_ids, new_input_ids], dim=-1)[-1000:]
        else:
            bot_input_ids = new_input_ids

        # Generate a response
        self.chat_history_ids = self.model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=self.tokenizer.eos_token_id,
            top_k=50,
            top_p=0.95,
            temperature=0.8
        )

        # Decode response tokens
        response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

if __name__ == "__main__":
    bot = ContextAwareChatbot()
    print("\nContext-Aware Chatbot is ready! Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print("Chatbot:", response)

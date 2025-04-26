import random
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# --- Predefined smart topic responses ---
topic_responses = {
    "side hustle": [
        "🚀 Try freelancing, content creation, dropshipping, or selling digital products online. Hustle smart, not hard!",
        "💼 Great side hustles include tutoring, blogging, or reselling items online. Build assets, not liabilities!",
    ],
    "savings": [
        "💰 Try the 50/30/20 rule: 50% needs, 30% wants, 20% savings. Automate it, forget it!",
        "🪙 Start by saving 10% of every rupee/dollar you earn. Your future self will thank you!",
    ],
    "investing": [
        "📈 Start small with index funds or ETFs. Stay consistent and think long term!",
        "💡 Dollar-cost averaging into the stock market can reduce risk and build steady gains.",
    ],
    "stocks": [
        "📊 Stocks are ownership in companies. Pick strong businesses, think long term, ignore noise.",
        "📈 Diversify your portfolio. Don't put all your eggs in one basket!",
    ],
    "10000$": [
        "💸 With $10,000, diversify: Index funds, ETFs, some bonds, and keep some cash ready for opportunities!",
        "🧠 Invest $10K smartly across stocks, real estate crowdfunding, or even into building a small side business.",
    ],
    "matrix": [
        "🔵🔴 Forget about 'Matrix' theories bro. Focus on hard work, investing smartly, and leveling up in real life! 🚀",
    ],
}

# --- Predefined casual personal question replies ---
personal_responses = {
    "how are you": "😎 Grinding and shining bro! Hope you're doing awesome too!",
    "what's your name": "💸 I'm Finance Bro Bot, your personal money sensei!",
    "what is your age": "📆 Age is just a number, bro! Mindset is what counts. 😉",
    "who are you": "🧠 I'm your financial sidekick, helping you escape the rat race!",
}

# --- Random fallback motivational quotes ---
fallback_quotes = [
    "💬 Wealth is built by consistency, not luck. Stay steady, bro!",
    "📈 Money grows when you do. Invest in yourself first!",
    "🚀 Start small. Think big. Act now.",
    "💡 Financial freedom > Flexing for strangers!",
    "🏗️ Build assets while others flex liabilities. That's how legends are made!",
]

# --- Start chat ---
print("Finance Bro Bot 💸: Yo, welcome to the money dojo 🧠💵. Ask me anything — savings, side hustles, investing, all that good stuff.")

# Persona introduction
persona_intro = (
    "You are 'Finance Bro Bot 💸', a chill and smart money guide. You give friendly, helpful, and motivating advice "
    "about saving, investing, side hustles, and wealth-building. Use casual, positive, upbeat language. Add emojis. Keep answers short."
)

# Initialize conversation history
chat_history_ids = tokenizer.encode(persona_intro + tokenizer.eos_token, return_tensors='pt')

step = 0

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["exit", "quit", "bye"]:
        print("Finance Bro Bot 💸: Stay rich, stay wise 🧠💵. Catch you later, legend! ✌️")
        break

    matched_response = None

    # Check personal casual replies
    for keyword in personal_responses.keys():
        if keyword in user_input:
            matched_response = personal_responses[keyword]
            break

    # Check financial topics
    if not matched_response:
        for keyword in topic_responses.keys():
            if keyword in user_input:
                matched_response = random.choice(topic_responses[keyword])
                break

    # If matched, respond with predefined response
    if matched_response:
        print(f"Finance Bro Bot 💸: {matched_response}")
    else:
        # No match: Use DialoGPT to generate response
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)

        chat_history_ids = model.generate(
            bot_input_ids,
            max_length=bot_input_ids.shape[-1] + 100,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_p=0.92,
            top_k=50,
            temperature=0.7,
            repetition_penalty=1.2,
        )

        reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

        # If reply doesn't make sense, fallback
        if len(reply.strip()) == 0 or "?" in reply and user_input not in ["who are you", "what is your age"]:
            reply = random.choice(fallback_quotes)

        print(f"Finance Bro Bot 💸: {reply}")

    step += 1

    # Reset chat history every 6 turns
    if step % 6 == 0:
        chat_history_ids = tokenizer.encode(persona_intro + tokenizer.eos_token, return_tensors='pt')

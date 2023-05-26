import random

# Define the investment options and their descriptions
investment_options = {
    "stocks": "Investing in stocks allows you to buy shares of publicly traded companies.",
    "bonds": "Bonds are debt securities that pay interest over a fixed period of time.",
    "mutual funds": "Mutual funds pool money from multiple investors to invest in a diversified portfolio of stocks, bonds, or other assets.",
    "real estate": "Investing in real estate involves purchasing properties to generate income or appreciation.",
    "cryptocurrency": "Cryptocurrency is a digital or virtual form of currency that uses cryptography for security.",
}

# Define the chatbot's responses
greetings = ["Hello! How can I assist you with your investments today?", "Hi there! How can I help you invest your money?"]
farewells = ["Goodbye! Happy investing!", "Have a great day!"]

# Function to handle user input and provide investment suggestions
def suggest_investment(user_input):
    user_input = user_input.lower()
    
    if "stocks" in user_input:
        return "I recommend considering stocks for potential long-term growth. " + investment_options["stocks"]
    elif "bonds" in user_input:
        return "Bonds can be a good option for stable income. " + investment_options["bonds"]
    elif "mutual funds" in user_input:
        return "Mutual funds offer diversification and professional management. " + investment_options["mutual funds"]
    elif "real estate" in user_input:
        return "Real estate can provide both rental income and potential appreciation. " + investment_options["real estate"]
    elif "cryptocurrency" in user_input:
        return "Cryptocurrency has shown high volatility but also significant returns. " + investment_options["cryptocurrency"]
    else:
        return "I'm sorry, I couldn't understand your request. Could you please be more specific?"
        
# Main chat loop
def chat():
    print(random.choice(greetings))
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() in ["bye", "goodbye"]:
            print(random.choice(farewells))
            break
        
        response = suggest_investment(user_input)
        print(response)

# Start the chatbot
chat()

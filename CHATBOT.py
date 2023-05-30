# Importing necessary libraries
import random
responses = {
    "hi": "Hello! How can I help you with your college admission process?",
    "requirements": "To get admission, you need to have a high school diploma or equivalent, as well as meet the minimum GPA and test score requirements.",
    "application": "You can apply online on the college's website or by submitting a paper application to the admissions office.",
    "deadline": "The deadline for admission applications is usually in the early spring for the fall semester, but it can vary by college.",
    "financial_aid": "Financial aid is available to eligible students. You can fill out the FAFSA to apply for federal financial aid, and the college may also have its own financial aid programs.",
    "contact": "You can contact the admissions office by phone or email to get more information about the college's admission process.",
    "default": "I'm sorry, I don't understand. Can you please ask me another question?"
}

# Defining the chatbot function
def chatbot():
    print("Welcome to the college admission process chatbot! How can I assist you?")
    while True:
        user_input = input().lower()
        if user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Thank you for using the chatbot. Good luck with your admission process!")
            break
        else:
            response = responses.get(user_input, responses["default"])
            print(response)

# Starting the chatbot
chatbot()
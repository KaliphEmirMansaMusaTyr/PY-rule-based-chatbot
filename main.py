import json
from difflib import get_close_matches

#loading the json file named knowledge_base.json
def load_knowledge_base(file_path):
    with open(file_path,'r') as file:
        data = json.load(file)
    return data

#saving new data to json file named knowledge_base.json
def save_knowledge_base(file_path,data):
    with open(file_path,'w') as file:
        json.dump(data, file, indent=2)
    
#here we use a mach for the question in the knowledge_base.json
#when a mach occurs the "question" will be returned
def find_best_mach(user_question,question):
    matches = get_close_matches(
        user_question,
        question,
        n=1,        #for repetition
        cutoff=0.5  #for the % of mach(0.7 = 70%)
    )
    return matches[0] if matches else None

# checks for the question in the given DB/file and return the answer
def get_answer_for_question(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

# This is for added a new response; means adding data into the knowledge_base.json file
def add_new_response(user_input, knowledge_base):
    print(f"Bot: I don't know the answer. So can you teach me the answer?")
    new_answer= input('Type your answer or "__skip" to skip:')
    if new_answer and new_answer.lower() != '__skip':
        knowledge_base["questions"].append({"question": user_input, "answer" : new_answer})
        save_knowledge_base('knowledge_base.json', knowledge_base)
        print("Bot: Thank you! I learned a new response!")


#this is the main function
def chat():
    knowledge_base = load_knowledge_base('knowledge_base.json')

    user_input = input("You: ")

    if not user_input:
        print("Bot: Please provide a query!\n")
        return
    elif user_input.lower() == '__quit':
        print("Bye")
        exit()

    best_mach = find_best_mach(user_input, [q["question"] for q in knowledge_base["questions"]])

    if best_mach:
        answer = get_answer_for_question(best_mach, knowledge_base)
        print("Bot:", answer)
    else:
        add_new_response(user_input, knowledge_base)
    
    print("\n", end='')


if __name__ == '__main__':
    print("Bot: Hello, I'm a basic rule-based chatbot. How can I help you?\n'__quit' for exit")
    while True:
        chat()

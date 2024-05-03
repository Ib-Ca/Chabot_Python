import json
from difflib import get_close_matches #obtener las respuestas aprox

def load_info(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
        return data


def save_info(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list= get_close_matches(user_question, questions, n=1, cutoff=0.6)  #la respuesta es 60% similar
    if matches:
        return matches[0]
    else:
        return None
    
    
def get_answer(question: str, database: dict) -> str | None:
    for a in database["questions"]:
        if a["question"] == question:
            return a["answer"]
    return None
        
def chatbot():
    database: dict = load_info("database.json")
    
    while True:
        u_input: str = input("Yo: ")
        if u_input.lower()=="stap":
            break
        
        best_match: str | None= find_best_match(u_input, [a["question"] for a in database["questions"]])
        
        if best_match:
            answer: str =get_answer(best_match, database)
            print(f'Roboto: {answer}')
        else:
            print('Esa no me la se. Te la robo?')
            new_answer: str =input("Escribe la respuesta o skip para skip: ")
            
            if new_answer.lower()!='skip':
                database["questions"].append({"question":u_input,"answer": new_answer})
                save_info('database.json', database)
                print("Robao")
                
                
if __name__=='__main__':
    chatbot()
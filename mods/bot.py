import google.generativeai as genai

genai.configure(api_key= "AIzaSyCifS1L0hQJ-_UGZHpfY1RC55MRL68So5w")
model = genai.GenerativeModel('gemini-1.5-flash',
                              system_instruction="you are a cat named 'kitty'")

def get_response(prompt):
    return model.generate_content(prompt).text

def save(response):
    with open("response.txt", "a", encoding="utf-8") as f:
        f.write(response)

def read():
    with open("response.txt", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    print("generating...")
    # print(get_response("reply your answer in hinglish language,\
    #                     return your response in json format where the structure of the response should be :\
    #                     {'response': your response, 'language': language of your response, 'tone': the tone of the user question}\
    #                     heres's the question ->whats your name?"))
    prompt = "reply your answer in hinglish language,\
                    return your response in json format where the structure of the response should be :\
                    {'response': your response, 'language': language of your response, 'tone': the tone of the user question,\
                    'is_remember': true or false depending on whether the user prompt contains something that should be remembered, ex: his/her name, hobbies, favourite food,color,song or movie, etc. If it's just a normal prompt then return False,\
                    'to_remember': the thing or events that should be remembered for future use case and if there is no such thing to remeber then return ''}\
                    heres's the question -> "

    reminder = "Here are some information about the user you are responding to, these info you can be helpful to you while responding to user prompt, note: use the information \
                wisely, use it specifically and only when necessary. don't use all the information for one single prompt when its not necessary to mention -> "
    reminder += read()


    while True:
        user = input("user: ")
        if user == "exit": break
        user = reminder + prompt + user
        response = get_response(user)
        print(response)
        save(response)
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai
from mods.text_to_speech import TTS
from mods.read import read_persona
from mods.save_users import User
from mtranslate import translate
from os import environ
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key= environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash',
                              system_instruction= read_persona())

tts = TTS(voice= 'en-IN-NeerjaNeural')


def register_newUser(username: str, email: str, password: str) -> list:
    user = User()
    # Check Username and mail
    validation: bool|str = user.check_user(username, email)

    # return invalid if any of the above exists
    if validation: return [False, validation]
    
    # save username, mail and password if it doesnt exists
    else:
        user.write_users([username + " ", email])
        user.save_psswrd(username, password)
    
    # return succesfull registration
    return [True, ""]

def login_existingUser(username: str, password: str) -> bool | str:

    user = User()
    # check username
    validate: bool|str = user.check_user(username)

    if not validate:
        # return no user exists
        return "no_user"
    
    # check password
    elif validate == "username":
        users_list = user.get_psswrd()

        if users_list:
            for user in users_list:
                if user["password"] == password:
                    return True
            return False

        else:
            return "error" 


# Create your views here.
def index(request):

    context = {"timestamp": int(now().timestamp()),               
               "username": '',
               "mail": '',
               "password": '',
               "invalid": '',
               "type": "login"
            }
    
    # return HttpResponse("<h1>Hey This Is Test 1</h1>")
    # return render(request= request, template_name= "aarna.html", context= {"timestamp": int(now().timestamp())})
    return render(request= request, template_name= "login/login.html", context= context)

def user_verification(request):
    
    if request.method == 'POST':
        form_type = request.POST.get('type')
        
        if form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            context = {"timestamp": int(now().timestamp()),               
               "username": username,
               "mail": '',
               "password": password,
               "invalid": '',
               "type": "login"
            }

            validation: bool | str = login_existingUser(username, password)
            if not validation:
                context['invalid'] = "incorrect password !"
                return render(request= request, template_name= 'login/login.html', context= context)

            else:
                if validation == "no_user":
                    context['invalid'] = "username doesn't exists !"
                    return render(request= request, template_name= 'login/login.html', context= context)
                elif validation == "error":
                    context['invalid'] = "oops, something went wrong !"
                    return render(request= request, template_name= 'login/login.html', context= context)
                else:
                    return render(request= request, template_name= 'aarna.html', context= {"timestamp": int(now().timestamp())})

        else:
            username = request.POST['username']
            mail = request.POST['mail']
            password = request.POST['password']

            context = {"timestamp": int(now().timestamp()),               
               "username": username,
               "mail": mail,
               "password": password,
               "invalid": '',
               "type": "signup"
            }

            is_registered: list = register_newUser(username, mail, password)
        
            if not is_registered[0]:
                if is_registered[1] == "username":
                    context["invalid"] = "username already exists !"
                    return render(request= request, template_name= 'login/login.html', context= context)
                
                elif is_registered[1] == "mail":
                    context["invalid"] = "mail already exists !"
                    return render(request= request, template_name= 'login/login.html', context= context)

                
            else:
                return render(request= request, template_name= 'aarna.html', context= {"timestamp": int(now().timestamp())})


@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data['user_prompt']
        print("\n\n\n")
        print(prompt)
        print("\n\n\n")

        # Update prompt with persona info
        # with open("static/data/persona_v1.01.txt") as persona:
        #     prompt = f"{persona.read()} , Here is the question that the user asked -> {prompt}"

        prompt = translate(prompt, 'en', 'hinglish')
        response = model.generate_content(prompt).text
        
        
        response = response.replace("json", '')
        response = response.replace("null", 'None')
        response = response.replace("```", '').strip()
        
        response = eval(response)
        reply = response['response']
        print(reply)

        # tts.generate_audio(response)
        # response = "Hi ! myself Aarna"

        # Process the data
        response_data = {'message': 'Data received successfully',
                         "voice_output": False}

        if response != '':
            response_data['bot_reply'] = reply
        
        return JsonResponse(response_data, status = 200)
    
    return JsonResponse({'error': 'Invalid request'}, status=404)
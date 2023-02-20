#!/usr/bin/python3
##########################################################
#Script Name : gpt
#Author      : Jinto Philip
#Date        : 18/02/2023
#Version     : 1.0.0
#Script to talk to ChatGPT using API call
#########################################################
import openai
openai.api_key = "YOUR_API_KEY"  #Create and get your api key from https://platform.openai.com/account/api-keys 
#Ask to gpt
def asking(question):
    try:
       response = openai.Completion.create(engine="text-davinci-003", prompt=question, n=1, stop=None, temperature=0.7,  max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0)
       return response['choices'][0]['text']
    except:
       return "Unable to connect to GPT right now, Try again! "


if __name__ == "__main__":
    print("\nGPT: Hi How can I Help you ?\n")
    while True:
        # Get the user input
        text = input("Me: ")
        if text.lower() != "bye":
            answer = asking(text)
            print("GPT: ", answer)
        else:
            print("GPT: Goodbye! see you later!")
            exit()

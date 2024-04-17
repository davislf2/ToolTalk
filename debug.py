import openai
import requests

####### no functions
# model = 'gpt-3.5-turbo'
# openai_history = [
#     {'role': 'system', 'content': 'You are a helpful assistant. Here is some user data:\nlocation: New York\ntimestamp: 2023-09-11 13:00:00\nusername (if logged in): justinkool'}, 
#     {'role': 'user', 'content': 'Hey I have class tonight at 7. Can you set an alarm for 6:30?'}
# ]

# openai_response = openai.ChatCompletion.create(
#     model=model,
#     messages=openai_history,
#     # functions=api_docs,
# )
# print("openai_response:", openai_response)

####### functions with OOD
model = 'gpt-3.5-turbo'
openai_history = [
    {
        "role": "user",
        "content": "Could you tell me what's the weather tomorrow?"
    }
]

api_docs = [
    {
        "name": "AddAlarm",
        "description": "Adds an alarm for a set time.",
        "parameters": {
            "type": "object",
            "properties": {
                "time": {
                    "type": "string",
                    "description": "The time for alarm. Format: %H:%M:%S"
                }
            }
        },
        "required": [
            "time"
        ]
    },
    {
        "name": "DeleteAlarm",
        "description": "Deletes an alarm given an alarm_id.",
        "parameters": {
            "type": "object",
            "properties": {
                "alarm_id": {
                    "type": "string",
                    "description": "8 digit alarm ID."
                }
            }
        },
        "required": [
            "alarm_id"
        ]
    }
]
openai_response = openai.ChatCompletion.create(
    model=model,
    messages=openai_history,
    functions=api_docs,
)
print("openai_response:", openai_response)


# model = 'command-r-plus-8k'
# openai_history = [
#     # {'role': 'system', 'content': 'You are a helpful assistant. Here is some user data:\nlocation: New York\ntimestamp: 2023-09-11 13:00:00\nusername (if logged in): justinkool'}, 
#     {'role': 'user', 'content': 'Hey I have class tonight at 7. Can you set an alarm for 6:30?'}
# ]

# cohere_response = requests.post(f'http://144.25.31.124:8461/v1/chat/completions', json={
#         "model": model,
#         "messages": openai_history,
#         # "functions": api_docs,
#     }, verify=False, proxies={
#         "http": "",
#         "https": "",
#     }).json()

# print("cohere_response:", cohere_response)

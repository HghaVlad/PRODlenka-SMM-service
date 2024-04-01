import requests


def generate_text(role, text):
    role = "Ты ассистент СММ специалиста. " + role

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwMxCC7FdTPArzCnHr6aQ3MfIXvg2Ln1Hud0P"
    }
    prompt = {
        "modelUri": "gpt://b1gbq3bio0sr32ptb3v4/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": role
            },
            {
                "role": "user",
                "text": text
            },
        ]
    }

    response = requests.post(url, headers=headers, json=prompt)
    return response

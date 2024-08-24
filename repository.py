from dotenv import load_dotenv
import os
from openai import OpenAI
from prompt import system_prompt


def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("APIキーが見つかりません")
    return api_key


def get_openai_client():
    api_key = load_api_key()
    return OpenAI(api_key=api_key)


def get_response(text):
    client = get_openai_client()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
    )
    res = completion.choices[0].message.content
    return res

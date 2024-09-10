from openai import OpenAI

from assis.local_openia.utils import openai_statements


def generate_doc(statement:str) -> dict:
    client = OpenAI()

    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role":"system", "content": openai_statements('system')},
          {"role":"user", "content": statement}
      ]
    )

    return {
        "doc": completion.choices[0].message.content,
        "input_token": completion.usage.prompt_tokens,
        "output_token": completion.usage.completion_tokens,
    }
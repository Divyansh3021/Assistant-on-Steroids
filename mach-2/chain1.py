from langchain_google_genai import GoogleGenerativeAI as genai
import dotenv
from langchain.prompts import PromptTemplate
import os

dotenv.load_dotenv()

key = os.getenv(
                'GOOGLE_API_KEY'
                )

model = genai(
        model = "gemini-pro",
        google_api_key = key
        )

from langchain.prompts import PromptTemplate

introduction = """Hi Gemini, I am Divyansh, I am Vice-President of Software Development Cell. I want you to be my digital assistant. Here are some more details about how I want you to work:

```
1. If the task means writing an email you will return the email only in this array format [reciever's email address, subject of email, email body].
2. If the task means writing content like summary, report etc. You will return the output in this array format [content_heading, content].
```

make sure to comply to these rules.

"""

prompt = PromptTemplate.from_template(
                                introduction
                                )

chain = prompt | model

response = model.invoke(
                        introduction
                        )

task = "Write a report on impact of Apollo mission on USA."

response = model.invoke(
                        task
                        )
print(
    response
    )

summary = "Write me a summary of this report."

response = model.invoke(
    summary
)

print(response)
import google.generativeai as genai
import dotenv
import os
import streamlit as st

dotenv.load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

task = "Write a report on impact of Apollo mission on USA."

query = f"""
I am Divyansh, Vice-President of Software Development Cell, USICT.

I want you to do this task, here are some considerations to keep in mind:

1. If the task means writing an email you will return the email only in this format [reciever's email address, subject of email, email body].
2. If the task means writing content like summary, report etc. You will return the output only in correct format.

here is the task:

```
{task}
```
        """

response = model.generate_content(query)
print(response.text)


# task = "Write a report on impact of Apollo mission on USA."

# introduction = """Hi Gemini, I am Divyansh, I am Vice-President of Software Development Cell. I want you to be my digital assistant. Here are some more details about how I want you to work:

# ```
# 1. If the task means writing an email you will return the email only in this format [reciever's email address, subject of email, email body].
# 2. If the task means writing content like summary, report etc. You will return the output only in this format [content_heading, content].
# ```

# """
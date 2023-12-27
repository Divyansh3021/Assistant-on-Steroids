import google.generativeai as genai
import dotenv
import os
from sendmail import compose_email
import re

dotenv.load_dotenv()

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

tasks = ["send email", 'set a reminder', 'writing a report', 'take notes']

query = "Send an email to Ayush4002@gmail.com and tell him to meet me today at 2 PM in office."

response = model.generate_content(f"""From this tasks array {tasks}, tell me the task that is signified in this query: ``` 
                                  {query}
                                  ```
                                  """)

print(response.text)

if response.text == "send email":
    email_content = f"""Extract the recepient's address, subject and write the content of email covering the subject from this query
        ```{query}```

        and output the response in this format:
        [recepient's address, subject, content]

    My Name is Divyansh. So don't use any placeholders.
    """
    response = model.generate_content(email_content)

    # Extract email
    email_match = re.search(r'\[([^\]]+)', response.text)
    email = email_match.group(1) if email_match else None

    # Extract subject
    subject_match = re.search(r',\s([^,]+),', response.text)
    subject = subject_match.group(1) if subject_match else None

    # Extract body
    body_match = re.search(r',\s([^,]+),(.+)]', response.text, re.DOTALL)
    body = body_match.group(2).strip() if body_match else None

    # print("Email:", email)
    # print("Subject:", subject)
    print("Body:", body)

    # print(response.text)
    compose_email(email, subject, f"""{body}""")
import google.generativeai as genai
import dotenv
import os
from sendmail import compose_email
import re
import pyperclip
from notification import send_notification
from speechToText import recognise_text
from extractTextFromDoc import extract_text


dotenv.load_dotenv()

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

tasks = ["send email", 'set a reminder', 'write report', 'take notes']

email_query = "Send an email to Ayush4002@gmail.com and tell him to meet me today at 2 PM in office."
report_query = "Write a report on E-waste for my college assignment"
notes_query = "help me taking notes."

response = model.generate_content(f"""From this tasks array {tasks}, tell me the task that is signified in this query: ``` 
                                  {notes_query}
                                  ```
                                  """)

print(response.text)

if response.text == "send email":
    email_content = f"""Extract the recepient's address, subject and write the content of email covering the subject from this query
        ```{email_query}```

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

elif response.text == "write report":
    report_content = f"""Extract the topic and other useful information about the report from this query: 
    ```
    {report_query}
    ```
    and write a report about the topic, keeping other information in perspective
    """

    response = model.generate_content(report_content)
    pyperclip.copy(response.text)
    send_notification("Assistant", "Report copied to clipboard!", 5)

elif response.text == "take notes":
    # text = recognise_text("speech_recog_test.wav")
    text = extract_text("Bidirectional LSTM.pdf")
    if text:
        notes_content = f"""This is the text 
        ```
        {text}
        ```
        make well structured notes out of this.
        """

        response = model.generate_content(notes_content)
        pyperclip.copy(response.text)
        send_notification("Assistant", "Notes copied to clipboard!", 5)
    else:
        send_notification("Assistant", "Unsupported doc format!", 5)
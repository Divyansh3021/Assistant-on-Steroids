import webbrowser
import urllib.parse

def compose_email(to, subject, body):
    body = urllib.parse.quote(body)
    # Construct the mailto URL with parameters
    mailto_url = f"mailto:{to}?subject={subject}&body={body}"

    # Open the default web browser with the mailto URL
    webbrowser.open(mailto_url)

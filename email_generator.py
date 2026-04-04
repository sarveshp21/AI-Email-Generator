import ollama

def generate_email(topic, tone, recipient, points, length, template):

    prompt = f"""
    Write an email based on the following details.

    Email Template: {template}
    Topic: {topic}
    Recipient: {recipient}
    Tone: {tone}
    Email Length: {length}
    Key Points: {points}

    Instructions:
    - Generate a clear subject line
    - Use the specified tone
    - Follow the email template style
    - Keep the email length as requested
    - Write in a professional structure

    The email must include:
    Subject
    Greeting
    Body
    Closing
    """

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
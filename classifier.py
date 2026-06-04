import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def classify_ticket(ticket_text):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        messages=[
            {
                "role": "user",
                "content": f"""You are an IT support ticket classifier. Analyze the following support ticket and respond ONLY in this format:

Category: [Network / Hardware / Software / Access / Other]
Priority: [Low / Medium / High / Critical]
Suggested Action: [One sentence recommendation]
Reasoning: [One sentence explanation]

Ticket:
{ticket_text}"""
            }
        ]
    )
    return message.content[0].text

tickets = [
    "I can't log into my email since this morning. I've tried resetting my password twice but it still says invalid credentials.",
    "My laptop screen is flickering and sometimes goes completely black. It happens every 10 minutes.",
    "The entire office lost internet connection about 20 minutes ago. None of us can access any internal systems."
]

for i, ticket in enumerate(tickets, 1):
    print(f"\n--- Ticket {i} ---")
    print(f"Input: {ticket}")
    print(f"\nClassification:\n{classify_ticket(ticket)}")
    print("-" * 50)
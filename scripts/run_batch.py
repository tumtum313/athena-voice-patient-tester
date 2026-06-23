import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def main(count: int = 1):
    sid = os.getenv("TWILIO_ACCOUNT_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_FROM_NUMBER")
    to_number = os.getenv("TARGET_NUMBER")
    base_url = os.getenv("PUBLIC_BASE_URL")

    if not all([sid, token, from_number, to_number, base_url]):
        raise RuntimeError("Missing env vars. Check .env")

    client = Client(sid, token)

    for i in range(count):
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url=f"{base_url}/twilio/voice",
            method="POST",
        )
        print(f"[{i+1}/{count}] call sid: {call.sid}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1)
    args = parser.parse_args()
    main(args.count)

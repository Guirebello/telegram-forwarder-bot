import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

if not API_ID or not API_HASH:
    raise RuntimeError("API_ID ou API_HASH não configurados no .env")


async def main():
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        print("✅ Logado como:", (await client.get_me()).first_name)
        session_str = client.session.save()
        print("\n=== SESSION STRING (guarde isso com carinho) ===\n")
        print(session_str)
        print("\n===============================================")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

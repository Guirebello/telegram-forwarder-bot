import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
TARGET_GROUP_ID = int(os.getenv("TARGET_GROUP_ID", "0"))

# Ex: "LinksBrazil,outro" -> ["LinksBrazil", "outro"]
CHANNEL_USERNAMES = [
    u.strip() for u in (os.getenv("CHANNEL_USERNAMES") or "").split(",") if u.strip()
]

if not API_ID or not API_HASH:
    raise RuntimeError("API_ID ou API_HASH não configurados no .env")

if not TARGET_GROUP_ID:
    raise RuntimeError("TARGET_GROUP_ID não configurado no .env")

if not CHANNEL_USERNAMES:
    raise RuntimeError("CHANNEL_USERNAMES vazio no .env")

client = TelegramClient("promo_forwarder_session", API_ID, API_HASH)


@client.on(events.NewMessage(chats=CHANNEL_USERNAMES))
async def forward_from_channel(event):
    try:
        await client.forward_messages(TARGET_GROUP_ID, event.message)

        channel = event.chat
        channel_name = (
            getattr(channel, "title", None)
            or getattr(channel, "username", None)
            or channel.id
        )

        print(
            f"[FORWARD] De canal: {channel_name} -> grupo {TARGET_GROUP_ID} | msg_id={event.message.id}"
        )
    except Exception as e:
        print("Erro ao encaminhar mensagem:", e)


async def main():
    print("🔥 Forwarder ligado!")
    print("Canais monitorados:", CHANNEL_USERNAMES)
    print("Grupo destino:", TARGET_GROUP_ID)

    try:
        entity = await client.get_entity(TARGET_GROUP_ID)
        print("✅ Conectado ao grupo:", getattr(entity, "title", entity.id))
    except Exception as e:
        print("⚠️ Não consegui resolver o grupo alvo:", e)


async def runner():
    await client.start()
    await main()
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(runner())

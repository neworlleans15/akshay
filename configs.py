# (c) @User

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL"))
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
**Send me any file, I can store it in my database & give you a permanent link.

I work in channel too: Add me to any channel as Admin with Edit Permissions; I will add Shareable Button Link to every file that you post in that channel**.

🤖 **My Name:** [FoundU's File Bot](https://t.me/{BOT_USERNAME})

🧑🏻‍💻 **Developer:** Stranger Danger

👥 **Support Bot:** [Chat with Admin](https://t.me/Geeniee_bot)

📢 **Movies & Series:** [FoundU Channel](https://t.me/FoundU)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** [Stranger danger](https://t.me/Geeniee_bot)

🧑🏻‍💻 **Founder of** [FoundU](https://t.me/FoundU)

💸 **Keep this bot Alive:** [Donate here](https://t.me/Geeniee_bot)
"""
	HOME_TEXT = """
Hello [{}](tg://user?id={})\n\nThis is **FoundU's File Bot**.

**Join** our chat group @FoundUchat **to share your thoughts**.
"""

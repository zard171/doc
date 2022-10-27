# Cyberspace bot

##This source serves as a base for Cyberspace store bots.
##It aims to be as modular as possible, allowing adding new features with minor effort.

## Example config file

##```python
# Your Telegram bot token.
BOT_TOKEN = ""

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 
API_HASH = ""

# Chat used for logging errors.
LOG_CHAT = -1001625541801

# Chat used for logging user actions (like buy, gift, etc).
ADMIN_CHAT = -1001625541801
GRUPO_PUB = -1001516981869



# How many updates can be handled in parallel.
# Don't use high values for low-end servers.
WORKERS = 20

# Admins can access panel and add new materials to the bot.
ADMINS = [1827664718]

# Sudoers have full access to the server and can execute commands.
SUDOERS = [1827664718]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []

# Bote o Username do bot sem o @
# Exemplo: default
BOT_LINK = "null"



# Bote o Username do suporte sem o @
# Exemplo: suporte
BOT_LINK_SUPORTE = "null"
##```

# telethon-scripts
telethon python scripts I created for different purposes recently

#INSTALLATION
pip3 install telethon

the scripts are executable individually. Get your api credentials from https://my.telegram.org/apps in order to make use of the scripts as showed below, insert the values into the script where comments say so.

The example values won't work. You must get your own api_id and api_hash from https://my.telegram.org, under API Development.
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'

When executing a script for first time, it asks for bot token or user phone number for authentication purposes. Recommended to provide phone number post registering on the https://my.telegram.org/apps. A code is sent to your telegeram user ID that needs to be provided to the script stdin as Telethon demands. An user session is created for the user given.

Below scripts need more than one user for randomizing and user-swapping purposes. Please follow the above instruction for the first time execution.
circulation_general.py
stickers.py

The scripts in this repo, though they need paramerization and more user-friendliness, covers most of the user-bot hype purposes for telegram. Please raise an issue if any assistance needed.

Check out Read The Docs for a more in-depth explanation, with examples, troubleshooting issues, and more useful information about Telethon.

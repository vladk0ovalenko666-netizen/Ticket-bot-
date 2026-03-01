==========================================================================
                    LINKINGSYSTEM DISCORD BOT
                      Installation Guide
==========================================================================

WHAT IS THIS?
-------------
This is a Discord bot for the LinkingSystem plugin. It connects your 
Discord account with your Rust character. When you join the Rust server,
the bot automatically gives you a role in Discord.

WHAT YOU NEED
-------------
- Python 3.8 or newer
- A Discord bot token 
- Server access (Windows/Linux/Pterodactyl)
- LinkingSystem plugin running on your Rust server

==========================================================================
                         CREATING A DISCORD BOT
==========================================================================

1. CREATE AN APPLICATION
   • Go to https://discord.com/developers/applications
   • Click "New Application"
   • Enter a name (like "LinkingSystem Bot")
   • Click "Create"

2. CREATE THE BOT
   • In the left menu, click "Bot"
   • Click "Add Bot" -> "Yes, do it!"
   • Copy the TOKEN (you'll need this for config.json)

3. SET UP PERMISSIONS
   • In the "Bot" section, enable these Privileged Gateway Intents:
     ☑ PRESENCE INTENT
     ☑ SERVER MEMBERS INTENT
     ☑ MESSAGE CONTENT INTENT

4. INVITE BOT TO YOUR SERVER
   • In the left menu, go to "OAuth2" -> "URL Generator"
   • In "Scopes" select: ☑ bot
   • In "Bot Permissions" select:
     ☑ Manage Roles
     ☑ Manage Messages 
     ☑ Manage Webhooks
     ☑ Send Messages
     ☑ Read Messages
     ☑ Read Message History
     ☑ View Channels
   • Copy the generated link
   • Go to that link and invite the bot to your Discord server

==========================================================================
                           WINDOWS INSTALLATION
==========================================================================

1. INSTALL PYTHON
   • Download Python from https://python.org
   • During installation, make sure to check "Add Python to PATH"
   • Test it: open cmd and type "python --version"

2. INSTALL THE BOT
   • Extract LinkingSystem_DiscordBot.zip to a folder (like C:\LinkingBot\)
   • Open command prompt in the bot folder
   • Run: pip install -r requirements.txt

3. SETUP
   • Rename config.example.json to config.json
   • Open config.json in a text editor
   • Replace:
     - "YOUR_DISCORD_BOT_TOKEN_HERE" with your bot token
     - 1234567890123456789 with your Discord channel ID (right-click channel -> Copy ID)
     - "your_rcon_password" with your Rust server RCON password
     - HOST and PORT with your server details

4. RUNNING THE BOT
   • Open command prompt in the bot folder
   • Run: python main.py
   • The bot should connect and show online in Discord

5. AUTO-START (OPTIONAL)
   • Create a bat file to start the bot:
     @echo off
     cd /d "C:\path\to\your\bot\folder"
     python main.py
     pause
   • Add this bat file to Windows startup

==========================================================================
                            LINUX INSTALLATION
==========================================================================

1. INSTALL PYTHON (if not already installed)
   Ubuntu/Debian:
   sudo apt update
   sudo apt install python3 python3-pip
   
   CentOS/RHEL:
   sudo yum install python3 python3-pip

2. INSTALL THE BOT
   • Upload the archive to your server
   • Extract it: unzip LinkingSystem_DiscordBot.zip
   • Go to the folder: cd LinkingSystem_DiscordBot
   • Install dependencies: pip3 install -r requirements.txt

3. SETUP
   • Rename the config: mv config.example.json config.json
   • Edit the config: nano config.json
   • Replace values as described in the Windows section above

4. RUNNING THE BOT
   • Run in console: python3 main.py
   • Run in background: nohup python3 main.py &
   • View logs: tail -f nohup.out

5. AUTO-START (systemd)
   • Create service file: sudo nano /etc/systemd/system/linkingbot.service
   
   [Unit]
   Description=LinkingSystem Discord Bot
   After=network.target
   
   [Service]
   Type=simple
   User=your_user
   WorkingDirectory=/path/to/bot/folder
   ExecStart=/usr/bin/python3 main.py
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   
   • Enable the service:
     sudo systemctl daemon-reload
     sudo systemctl enable linkingbot
     sudo systemctl start linkingbot

==========================================================================
                       PTERODACTYL INSTALLATION
==========================================================================

1. CREATE A SERVER
   • In your Pterodactyl panel, create a new server
   • Choose type: Python (or Generic if Python isn't available)
   • Set resources (512MB RAM is enough)

2. UPLOAD FILES
   • Upload LinkingSystem_DiscordBot.zip through File Manager
   • Extract the archive
   • Delete the zip file after extracting

3. SETUP
   • Rename config.example.json to config.json
   • Edit config.json using the built-in editor
   • Replace values as described above

4. INSTALL DEPENDENCIES
   • Open the server console
   • Run: pip install -r requirements.txt
   • Wait for installation to complete

5. STARTUP SETTINGS
   • In server settings, find "Startup"
   • In "Startup Command" field, enter: python main.py
   • Save settings

6. START THE BOT
   • Click "Start" button in the control panel
   • Watch the logs in console
   • The bot should connect to Discord

==========================================================================
                            TROUBLESHOOTING
==========================================================================

COMMON PROBLEMS:

1. "Invalid Token" - wrong bot token
   → Check your token in Discord Developer Portal

2. "Missing Permissions" - bot doesn't have enough permissions
   → Make sure the bot has "Manage Roles" permission
   → Bot's role must be higher than the role it's trying to give

3. "Connection refused" - can't connect to server
   → Check HOST, PORT and PASS in config.json
   → Make sure RCON is enabled on your server

4. "Module not found" - dependencies not installed
   → Run: pip install -r requirements.txt

5. Bot doesn't respond to connections
   → Check that LinkingSystem plugin is configured properly
   → Make sure STATUS: true in config.json

CONFIGURATION TIPS:
• Discord Channel ID: right-click channel -> Copy ID
  (you need to enable Developer Mode in Discord settings)
• RCON port is usually: main_port + 1 (example: 28015 + 1 = 28016)
• The role must exist in your Discord server

==========================================================================
                              SUPPORT
==========================================================================

If you're having problems:
1. Check bot logs in console
2. Make sure all settings are correct
3. Verify that LinkingSystem plugin is working on your server

Join our Discord for help: https://discord.gg/mevent

==========================================================================
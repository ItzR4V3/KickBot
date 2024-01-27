# Discord Kick Bot

## Introduction

This Discord bot, named KickBot, is designed to manage server membership based on the age of user accounts. It automatically kicks new accounts that are less than one month old when they join the server.

## Features

- **Account Age Check:** New users with accounts less than 30 days old will be automatically kicked upon joining the server.
- **Account Age Command:** Users can check their own account age using the `!check_account` command.

## Requirements

- Python 3.6 or higher
- [discord.py](https://discordpy.readthedocs.io/) library
- Discord bot token

## Setup

1. **Clone the Repository:**

    git clone https://github.com/ItzR4V3/KickBot


2. **Replace 'BOT TOKEN' in the Script:**

    Replace `'BOT TOKEN'` in the last line of the script (`bot.run('BOT TOKEN')`) with your actual Discord bot token.

3. **Run the Bot:**


    python main.py


## Usage

- Invite the bot to your Discord server.
- Users will be automatically kicked if their account age is less than one month.
- Use `!check_account` command to check your own account age.

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---

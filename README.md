# remember_locations_bot
Backend for Telegram bot which helps to save an interesting locations you've spotted while on the go

# Setup and Run

Clone the repo:
```bash
git clone https://github.com/niki4/remember_locations_bot.git
```

Go to clonned repo folder on your command line. Create a virtual environment and install dependencies:
```bash
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt
``` 

Now go to Telegram client, add @BotFather and request for /newbot
You should get token to access the Telegram HTTP API. Copy it.

Set TELEGRAM_TOKEN environment variable with your token you've just copied, e.g.:
```bash
export TELEGRAM_TOKEN='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
```

You're all set. Simply run the bot:
```bash
python3 bot.py
```

You can also play around with the [bot instance running](https://t.me/remember_locations_bot) on Telegram:

![Bot basic usage](https://github.com/niki4/remember_locations_bot/blob/master/blob/basic_usage.png)

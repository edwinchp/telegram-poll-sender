## Telegram Poll Sender

This project aims to send Telegram polls as a way to challenge your knowledge about whatever certification you are studying or subject you're preparing for.
I believe that taking notes is important when you want to retain information, but wouldn't be great that these notes come back to you at some point?


## 🚀 Getting Started:
Create a bot in Telegram using [BotFather](https://t.me/botfather).

Create a Telegram Channel or Group.

Clone the repository:
```bash
git clone https://github.com/edwinchp/telegram-poll-sender
```

Enter project folder:
```bash
cd telegram-poll-sender/
```

### Setting up the virtual environment

1. Create a virtual environment (only needed once):
   ```bash
   # Windows
   python -m venv venv
   
   # Activate the virtual environment
   .\venv\Scripts\activate
   
   # On macOS/Linux
   # python3 -m venv venv
   # source venv/bin/activate
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

Create a .env file and add bot token and channel/group chat id:
```bash
cp .env-example .env
```

Run script:
```bash
python main.py
```


## 🧪 Run tests

Testing is crucial as you go adding more and more new questions.
To make sure you didn't break anything, run this command:

```bash
pytest -s --html=reports/test_report.html
```


👏 Thank you! I hope you find it useful.
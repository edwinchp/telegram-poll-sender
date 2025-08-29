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
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
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

## 🛠️ Jenkins Configuration

**Create a New Pipeline Job**
   - Click `New Item` > Enter a name > Select `Pipeline` > Click `OK`
   - Under `General` section, check `This project is parameterized`

### Jenkins Parameters Reference

| Parameter Name | Type | Description | Example |
|----------------|------|-------------|---------|
| `BOT_TOKEN`    | Credential (Secret text) | Your Telegram Bot Token from BotFather | `123456789:ABCdefGHI...` |
| `CHAT_ID`      | Credential (Secret text) | Your Telegram Chat/Channel ID | `-1001234567890` |
| `API_LINK`     | String | Base URL for the questions API | `http://localhost:8000` |
| `API_REQUEST_DIFFICULTY` | String | Difficulty level for questions | `any`, `easy`, `medium`, `hard` |
| `API_REQUEST_CATEGORY` | String | Category for questions | `YOUR-CATEGORY` |


## 🧪 Run tests

Testing is crucial as you go adding more and more new questions.
To make sure you didn't break anything, run this command:

```bash
pytest -s --html=reports/test_report.html
```


👏 Thank you! I hope you find it useful.
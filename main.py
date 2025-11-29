import time
from datetime import datetime
from factories.data_factory import DataFactory
from factories.question_factory import QuestionFactory
from services.telegram_service import TelegramService
from utils.environment_loader import EnvironmentLoader
from utils.file_downloader import FileDownloader

def print_header():
    print("=" * 60)
    print(f"🚀 Starting Telegram Poll Sender - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

def main():
    print_header()    
    try:
        print("- Loading environment variables...")
        bot_token = EnvironmentLoader.get_bot_token()
        chat_id = EnvironmentLoader.get_chat_id()
        host_api_link = EnvironmentLoader.get_api_link()
        telegram_service = TelegramService(bot_token)
        
        print("\n- Fetching question data...")
        data = DataFactory.get_data()

        # Accept an object (dict) or an array (list)
        if isinstance(data, dict):
            questions_data = [data]
        elif isinstance(data, list):
            questions_data = data
        else:
            raise ValueError("Data must be a dict (single question) or a list of dicts (multiple questions).")

        print(f"✅ Fetched {len(questions_data)} question(s).")

        for question_data in questions_data:
            question = QuestionFactory.create_question(question_data)
            
            print("-" * 60)
            print(f"- Processing question:\n{question_data}")
            
            if question.messages:
                print(f"\n- Sending {len(question.messages)} message(s)...")
                for i, message in enumerate(question.messages, 1):
                    print(f"  {i}. Sending message...")
                    telegram_service.send_message(chat_id, message)
            
            print("\n- Sending poll...")
            telegram_service.send_poll(chat_id, question)

            if question.photo is not None:
                print("\n- Sending photo...")
                photo_url = "/".join(host_api_link.split("/")[:3]) + question.photo
                photo_path = FileDownloader.download_file(photo_url)
                print(f"Image successfully downloaded and saved: {photo_path}")
                telegram_service.send_photo(chat_id, photo_path)
            
    except Exception as e:
        print("\n❌ Error:", str(e))
        raise

if __name__ == '__main__':
    main()
import time
from datetime import datetime
from factories.data_factory import DataFactory
from factories.question_factory import QuestionFactory
from services.telegram_service import TelegramService
from utils.environment_loader import EnvironmentLoader

def print_header():
    print("=" * 60)
    print(f"🚀 Starting Telegram Poll Sender - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

def main():
    print_header()
    start_time = time.time()
    
    try:
        print("🔑 Loading environment variables...")
        bot_token = EnvironmentLoader.get_bot_token()
        chat_id = EnvironmentLoader.get_chat_id()
        telegram_service = TelegramService(bot_token)
        
        print("\n🔄 Fetching question data...")
        data = DataFactory.get_data()
        for question_data in data: 
            question = QuestionFactory.create_question(question_data)
            
            print(f"\n📝 Processing question: {question.question[:50]}...")
            
            if question.messages:
                print(f"\n📤 Sending {len(question.messages)} message(s)...")
                for i, message in enumerate(question.messages, 1):
                    print(f"  {i}. Sending message...")
                    telegram_service.send_message(chat_id, message)
            
            if question.photos:
                print(f"\n🖼️  Sending {len(question.photos)} photo(s)...")
                for i, photo in enumerate(question.photos, 1):
                    print(f"  {i}. Sending photo: {photo}")
                    telegram_service.send_photo(chat_id, photo)
            
            print("\n📊 Sending poll...")
            telegram_service.send_poll(chat_id, question)
            
    except Exception as e:
        print("\n❌ Error:", str(e))
        raise

if __name__ == '__main__':
    main()
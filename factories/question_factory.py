import random
import re

from models.question import Question

class QuestionFactory:

    SUPPORTED_ANSWERS = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
    }

    @staticmethod
    def create_question(data):
        question = Question()
        question.id = data["id"]
        question.question = data["question_text"]
        question.explanation = data.get("short_explanation", "")
        
        # Shuffle the options
        shuffled_options = QuestionFactory.shuffle_options(data['options'])
        question.options = [opt["option_text"] for opt in shuffled_options]
        
        # Find the correct answer index after shuffling
        question.correct_option_id = QuestionFactory.get_correct_answer(shuffled_options)
        
        # Get the answer letter based on the index
        question.answer = QuestionFactory.find_key_by_value(
            QuestionFactory.SUPPORTED_ANSWERS, 
            question.correct_option_id
        )
        
        if 'messages' in data:
            question.messages = data["messages"]
        if 'photos' in data:
            question.photos = data['photos']
        if 'photo' in data:
            question.photo = data['photo']
            
        return question

    @staticmethod
    def get_answer_index(letter):
        pattern = r'[:.(),]'
        modified_letter = re.sub(pattern, '', letter).lower()
        return QuestionFactory.SUPPORTED_ANSWERS.get(modified_letter, -1)

    @staticmethod
    def shuffle_options(options):
        # Make a copy to avoid modifying the original list
        shuffled = options.copy()
        random.shuffle(shuffled)
        return shuffled

    @staticmethod
    def get_correct_answer(options):
        """
        Find the index of the correct answer in the options list.
        
        Args:
            options: List of dicts with 'option_text' and 'is_correct' keys
            
        Returns:
            int: Index of the correct answer, or -1 if not found
        """
        for i, option in enumerate(options):
            if option.get('is_correct', False):
                return i
        return -1

    @staticmethod
    def find_key_by_value(dictionary, index):
        for key, val in dictionary.items():
            if val == index:
                return key
        return None
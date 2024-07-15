import requests
import html

class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0
    
    def fetch_questions(self):
        url = "https://opentdb.com/api.php?amount=5&type=multiple"  # Example URL for fetching 5 multiple-choice questions
        response = requests.get(url)
        if response.status_code == 200:
            quiz_data = response.json()
            self.questions = quiz_data['results']
        else:
            print("Failed to fetch questions from the API")

    def display_question(self, question):
        print(html.unescape(f"\nQuestion: {question['question']}")) # Remove HTML entities
        
        # Remove HTML entities from options
        options = [html.unescape(option) for option in question['incorrect_answers']]
        options.append(html.unescape(question['correct_answer']))
        options = [option.strip().lower() for option in options]  # Normalize options
        
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option.capitalize()}")  # Display options with capitalization
        
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = question['correct_answer'].strip().lower()  # Normalize correct answer
        
        if user_answer == correct_answer or (user_answer.isdigit() and int(user_answer) == options.index(correct_answer) + 1):
            print("Correct!")
            self.score += 1
        else:
            # Find the correct option index for display
            correct_index = options.index(correct_answer) + 1
            print(f"Wrong! Correct answer is: {correct_index}. {question['correct_answer']}")

    def play_game(self):
        self.fetch_questions()
        # Welcome
        print("Welcome to the Quiz Game!\nAnswer the following 5 questions:")
        print("You can answer by typing the number corresponding to the answer or the text.")
        input("Press Enter to start the Quiz Game...")
        for question in self.questions:
            self.display_question(question)
        print(f"\nQuiz completed! Your score is: {self.score}/{len(self.questions)}")

# Main function to start the quiz game
def main():
    game = QuizGame()
    game.play_game()

if __name__ == "__main__":
    main()
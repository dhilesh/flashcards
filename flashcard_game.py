import random
import csv

flashcards = []
attempts = 1
score = 0

with open('wordlist.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        spanish_word = row[0]
        english_translation = row[1]
        flashcards.append((spanish_word, english_translation))

while(True):
    num_words = len(flashcards)
    rand = random.randint(0, num_words-1)
    word_es = flashcards[rand][0]
    word_en = flashcards[rand][1]
    user_ans = input(f'what is the english word for: {word_es}? ')
    if user_ans.lower() == word_en.lower():
        score += 1
        print(f'You\'re right! Your score is {score} out of {attempts} \n')
        flashcards.pop(rand)
    else:
        print(f'The correct answer is {word_en}')
        print(f'Try again. Your score is {score} out of {attempts} \n')
    attempts += 1
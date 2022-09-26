
import random


# word_list = ['ardak', 'john', 'susan']
# random_words = random.choice(word_list)

# letter = input("Guess a word: ").lower()

# for word in random_words:
#     if word == letter:
#         print("right")
#     else:
#         print("wrong")
new_word = input("Guess the word").lower()
new_list = list('_')

for letter in new_word:
    new_list.append('_')
    
print(new_list)
guess = input("Guess the letter: ").lower()
print(len(new_list))
for position in range(len(new_word)):
    letter = new_word[position]
    if letter == guess:
      new_list[position] = letter

print(new_list)


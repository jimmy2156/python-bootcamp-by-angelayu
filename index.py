
import random


# word_list = ['ardak', 'john', 'susan']
# random_words = random.choice(word_list)

# letter = input("Guess a word: ").lower()

# for word in random_words:
#     if word == letter:
#         print("right")
#     else:
#         print("wrong")
new_list = list('_')
new_word = "babbon"
for letter in new_word:
    new_list.append('_')
    
print(new_list)
new_letter = "b"
position_of_word = new_word.index(new_letter)
print(position_of_word)



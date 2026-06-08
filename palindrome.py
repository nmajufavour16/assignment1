# Palindrome Checker Program
my_list = ['mummy', 'hannah', 'murder for a jar of red rum', 'mom', 'seagull', 'tomato', 'no lemon, no melon', 'some men interpret nine memos', 'madam']

def palindrome(text):
    # Remove spaces and punctuation (input is already lowercase)
    cleaned_text = ''.join(char for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

for word in my_list:
    if palindrome(word):
        print(f"{word} is Palindrome")
    else:
        print(f"{word} is not a Palindrome")
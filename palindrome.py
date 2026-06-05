# Palindrome Checker Program
my_list = ['mummy', 'hannah', 'murder for a jar of red rum', 'mom', 'seagull', 'tomato', 'no lemon, no melon', 'some men interpret nine memos', 'madam']

def is_palindrome(text):
    # Remove spaces and punctuation (input is already lowercase)
    cleaned_text = ''.join(x for x in text if x.isalnum())
    
    # Check if the cleaned text is the same as its reverse
    return cleaned_text == cleaned_text[::-1]

# Check each item in the list
for x in my_list:
    if is_palindrome(x):
        print(f"{x} is Palindrome")
    else:
        print(f"{x} is not a palindrome")

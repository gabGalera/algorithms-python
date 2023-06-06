def is_palindrome_iterative(word):
    length = len(word)
    if not word:
        return False
    for letter_index in range(0, length // 2):
        start = word[letter_index]
        end = word[length - letter_index - 1]
        if start != end:
            return False
    return True


print(is_palindrome_iterative(""))

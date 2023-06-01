def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if low_index >= high_index:
        return True
    else:
        return (
            is_palindrome_recursive(word, low_index + 1, high_index - 1)
            and word[low_index] == word[high_index]
        )


print(is_palindrome_recursive("REVIVER", 0, 6))

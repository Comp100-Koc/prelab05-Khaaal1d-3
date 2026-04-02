def check_palindrome(text):
    return text == text[::-1]


def longest_palindromic_substring(s):
    longest = ""

    for start in range(len(s)):
        for end in range(start + 1, len(s)):
            current = s[start:end + 1]

            if check_palindrome(current):
                if len(current) > len(longest):
                    longest = current

    return longest

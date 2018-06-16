# Leetcode520_detectCapital.py

def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if len(word) <= 1:
        return True
    return all_letter_capitals(word) or all_not_capitals(word) or only_first_capital(word)

def all_letter_capitals(word):
    return all(c.isupper() for c in word)

def all_not_capitals(word):
    return all(c.islower() for c in word)

def only_first_capital(word):
    return word[0].isupper() and all_not_capitals(word[1:])

print(all_letter_capitals('word') == False)
print(all_letter_capitals('WORD') == True)
print(all_letter_capitals('Word') == False)

print([all_not_capitals(word) for word in ['word','WOrd','WORD']] == [True, False, False])

print([only_first_capital(word) for word in ['word','WOrd','WORD', 'Oddd']] == [False, False, False, True])



# solution: dictionaries
import re
def spellchecker(wordlist, queries):
    """
    :type wordlist: List[str]
    :type queries: List[str]
    :rtype: List[str]
    """
    words = {w: w for w in wordlist}
    lowercase = {w.lower(): w for w in wordlist if not w.islower()}
    novowels = {re.sub('[aeiou]', '*', w.lower()): w for w in wordlist}
    
    return [words.get(w) or lowercase.get(w.lower()) or novowels.get(re.sub('[aeiou]', '*', w.lower()), '') for w in queries]

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
output = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
print(spellchecker(wordlist, queries))
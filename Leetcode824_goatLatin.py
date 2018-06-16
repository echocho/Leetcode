# Leetcode824_goatLatin.py

def toGoatLatin(S):
    S = S.split()
    i = 1
    
    # k = 0
    # kk = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    # toCompare = kk.split()

    for word in S:
        if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            word += 'ma'
        else:
            word = word[1:] + word[0] + 'ma'
        word += 'a'*i
        i += 1
        S[i-2] = word
    S = ' '.join(S)
    return S

    # for (a,b) in zip(S, toCompare):
    #     print(a,b)
    #     if a != b:
    #         print('faulty-', (a,b))
            
    





# print(toGoatLatin('I speak Goat Latin')== "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
print(toGoatLatin('The quick brown fox jumped over the lazy dog')== "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
# print(toGoatLatin('I speak Goat Latin'))
# Leetcode804_uniqueMosrseCodeWords.py


def uniqueMorseRepresentations(words):
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
    characs = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    
    aset = set()
    for word in words:
        new_word = ''
        for i in word:
            i = characs[ord(i)-97]
            new_word += i
        aset.add(new_word)
    return len(aset)           

print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))



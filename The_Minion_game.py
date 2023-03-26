def minion_game(n):

    count_vowels=0
    count_consonants=0
    for i in range(0,len(n)):
        if n[i] in ('A','I','O','E','U','a','e','i','o','u'):
            count_vowels=count_vowels+len(n)-i
        else :
            count_consonants=count_consonants+len(n)-i
            
    if count_vowels>count_consonants:
        print("Kevin",count_vowels)
    elif count_vowels<count_consonants:
        print("Stuart",count_consonants)
    else:
        print("Draw")

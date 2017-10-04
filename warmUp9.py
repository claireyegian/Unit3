#Claire Yegian
#10/4/17
#warmUp9.py - prints vowels of a word capitalized

word = input('Enter a word: ')
for ch in word:
    if ch=='a' or ch=='i' or ch=='o' or ch=='e' or ch=='u':
        print(ch.upper(ch))
    else:
        print(ch)
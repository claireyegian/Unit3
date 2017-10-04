#Claire Yegian
#10/4/17
#warmUp9.py - prints vowels of a word capitalized

word = input('Enter a word: ')
for ch in word:
    if ch in 'aeiouAEIOU':
        print(ch.upper())
    else:
        print(ch)

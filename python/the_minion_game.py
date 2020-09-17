# Link: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    l = len(string)
    for idx_i, char_i in enumerate(string):
        n_gram_count = l - idx_i
        if char_i in vowels:
             kevin_score += n_gram_count
        else:
            stuart_score += n_gram_count
    if stuart_score > kevin_score:
        print('Stuart {}'.format(stuart_score))
    elif stuart_score < kevin_score:
        print('Kevin {}'.format(kevin_score))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

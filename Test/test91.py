# English Word Relay
# Suppose that "n" persons that are each given a number from 1 through "n" are playing a game of
# English word relay. English word relay is played based on the following rules.
# Starting from person number 1, each person says a word in turn.
# After the last person says a word, person number 1 starts again.
# A person should say a word that starts with the last character of the previously said word.
# A person cannot say a word that has already been said.
# Words with one character are not valid.
# The following shows a situation where 3 persons are playing English word relay.
# tank → kick → know → wheel → land → dream → mother → robot → tank
# The procedure of the word relay above is as follows.
# Person number 1 says tank at the first turn.
# Person number 2 says kick at the first turn.
# Person number 3 says know at the first turn.
# Person number 1 says wheel at the second turn.
# (Continued)
# As the word relay continues, person number 3 is eliminated because the word tank, said on the third turn,
# had already appeared.
# With the number of people "n" and the words said "words" as parameters, write a function "solution" to return
# the number given to the first dropout and in which turn he is eliminated.


def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

# def solution(n, words):
#     answer = []
#     dictList = {}
#     num = 1
#     for i in range(1,len(words)):
#         if words[i-1][-1] == words[i][0] :
#             if i % n == 0:
#                 dictList.update({num : words[i-n:i]})
#                 print(dictList)
#                 num += 1
#             elif i == len(words)-1 and (i+1) % n == 0:
#                 dictList.update({num : words[i-n:i]})
#         else:
#             answer.append(num-1)
#             print('answer',answer)
#             print(num-1, 'Different!!!!!!')
#     return answer
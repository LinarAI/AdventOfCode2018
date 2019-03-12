num_marble = 71250
num_player = 452

def arrange_marbles(n, p):
    scores = [0] * num_player
    marble_list = [0]
    current = 0
    score = 0
    for turn in range(n):
        if (turn+1) % 23 == 0:
            # add score
            pos = current - 7
            if pos < 0:
                pos += len(marble_list)

            score = marble_list.pop(pos) + turn + 1
            user = p if (turn + 1) % p == 0 else (turn + 1) % p
            scores[user - 1] += score
            current = pos
        else:
            pos = current + 2
            if pos > len(marble_list):
                pos -= len(marble_list)
            # print('pos', pos)
            marble_list.insert(pos, turn+1)
            # print(marble_list)
            current = pos
    # print(score)
    return max(scores)

print(arrange_marbles(num_marble, num_player))
print(arrange_marbles(num_marble * 100, num_player))

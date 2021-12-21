data = open("input.test").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]
ln1 = data[0].split(" ")
p1 = int(ln1[-1])

ln2 = data[1].split(" ")
p2 = int(ln2[-1])

# generate all possible game configurations

N = 21
d = {}
scores = {}
for p1pos in range(1, 11):
    for p2pos in range(1, 11):
        d[(p1pos, p2pos)] = 0
        scores[(p1pos, p2pos)] = []

d[(p1, p2)] = 1
scores[(p1, p2)].append((0,0))
p1win = 0
p2win = 0
iters = 0
while sum([d[game] for game in d]) > 0:
    for game in d:
        count = d[game]
        d[game] = 0
        if count == 0: continue
        print(game, count) 
        p1pos = game[0]
        p2pos = game[1]

        # different die possibilities
        for i1 in range(1,4):
            for j1 in range(1,4):
                for i2 in range(1, 4):
                    for j2 in range(1, 4):
                        for i3 in range(1, 4):
                            for j3 in range(1, 4):

                                p1pos_ = ((p1pos + i1+i2+i3)-1)%10 + 1
                                p2pos_ = ((p2pos + j1+j2+j3)-1)%10 + 1
                                
                                scores_ = scores[(p1, p2)].copy()
                                while scores_:
                                    score = scores_.pop()

                                    p1score_ = score[0] + p1pos_
                                    p2score_ = score[1] + p2pos_

                                    # p1 rolls first
                                    if p1score_ >= N:
                                        p1win += count
                                    elif p2score_ >= N:
                                        p2win += count
                                    else:
                                        # advance
                                        newgame = (p1pos_, p2pos_)
                                        d[newgame] += count
                                        scores[newgame].append((p1score_, p2score_))

print(max(p1win, p2win))



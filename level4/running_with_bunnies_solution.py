#the problem fixing 5 bunnies as the maximum number of bunnies incites to do
#a brute force solution iterating through all permutations of all bunny sets
#one thing is that we should make sure that when going from one bunny to another
#we should eb taking the shortest path, which is not necessarily the direct
#delay between the two, this delay becomes in this case useless and we should
#update the table times so all new direct delays represents the shortest path:
import itertools
def solution(time, time_limit):
    rows = len(time)
    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if time[i][j] > time[i][k] + time[k][j]:
                    time[i][j] = time[i][k] + time[k][j]
    def convert_to_path(perm):
        perm = list(perm)
        perm = [0] + perm + [-1]
        path = list()
        for i in range(1, len(perm)):
            path.append((perm[i - 1], perm[i]))
        return path
    bunnies=rows-2
    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_time += time[start][end]
            if total_time <= time_limit:
                return sorted(list(i - 1 for i in perm))
    return ([])

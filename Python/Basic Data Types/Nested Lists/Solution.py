# Author: Kai Tanaka

stud_score = {}

for _ in range(int(input())):
    name = input()
    score = float(input())
    stud_score[name]=score
# Get sorted set of scores  
unique_scores=sorted(list(set(stud_score.values())))
second_lowest = unique_scores[1]

stud = [stud for stud in stud_score.keys() if stud_score[stud]==second_lowest]
print("\n".join(sorted(stud)))
    
        
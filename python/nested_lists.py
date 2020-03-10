# Link: https://www.hackerrank.com/challenges/nested-list/problem

def get_second_lowest_score(student_vs_score):
    scores = [tup[1] for tup in student_vs_score]
    scores = list(set(scores))
    if scores[0] < scores[1]:
        first_min = scores[0]
        second_min = scores[1]
    else:
        first_min = scores[1]
        second_min = scores[0]
    for s_i in scores[2:]:
        if s_i < first_min:
            second_min = first_min
            first_min = s_i
        elif s_i < second_min:
            second_min = s_i
    return second_min

def print_second_lowest_score_name(student_vs_score):
    second_min = get_second_lowest_score(student_vs_score)
    found_student_names = []
    for (student_name, score_i) in student_vs_score:
        if score_i == second_min:
            found_student_names.append(student_name)
    found_student_names.sort()
    for name_i in found_student_names:
        print(name_i)

if __name__ == '__main__':
    student_vs_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_vs_score.append((name, score))
    print_second_lowest_score_name(student_vs_score)
    

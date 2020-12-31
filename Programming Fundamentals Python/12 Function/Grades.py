grade = float(input())


def score_text(score):
    if 2 <= score < 3:
        return 'Fail'
    if 3 <= score < 3.50:
        return 'Poor'
    if 3.50 <= score < 4.50:
        return 'Good'
    if 4.50 <= score < 5.50:
        return 'Very Good'
    if 5.50 <= score <= 6:
        return 'Excellent'


print(score_text(grade))
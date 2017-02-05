# Jose Capestany
# Colin Sperie
# LAB 4: Grade Calculator

# Homework variables
h_score_list = [39, 40, 29, 40, 0, 5]
h_max_list = [40, 40, 40, 40, 40, 5]
h_weight = .2

# Quiz variables
q_score_list = [10, 10, 9, 2, 10, 10, 10]
q_max_list = [10, 10, 10, 10, 10, 10, 10]
q_weight = .2

# Test variables
t_score_list = [293, 284, 300]
t_max_list = [300, 300, 300]
t_weight = .6


def percentage_per_category(score_list, max_list):
    return sum(score_list)/sum(max_list)  # Returns the average


def letter_grade(percent):  # Finds the letter grade
    if percent >= .9:
        return "A"
    elif percent >= .8:
        return "B"
    elif percent >= .7:
        return "C"
    elif percent >= .6:
        return "D"
    else:
        return "F"


def weighted_score(percentage, weight):
    return percentage * weight  # Returns score by weight


# Homework calculations
h_grade = round(100 * percentage_per_category(h_score_list, h_max_list), 0)
h_letter = letter_grade(h_grade / 100)
h_weighted = weighted_score(h_grade, h_weight)

# Quiz calculations
q_grade = round(100 * percentage_per_category(q_score_list, q_max_list), 0)
q_letter = letter_grade(q_grade / 100)
q_weighted = weighted_score(q_grade, q_weight)

# Test calculations
t_grade = round(100 * percentage_per_category(t_score_list, t_max_list), 0)
t_letter = letter_grade(t_grade / 100)
t_weighted = weighted_score(t_grade, t_weight)

# Final grade calculations
final_grade = round(h_weighted + q_weighted + t_weighted, 0)
final_letter = letter_grade(h_weighted + q_weighted + t_weighted)

# Displays results
print("Homework grade: %d (%s)" % (h_grade, h_letter))
print("Quiz grade: %d (%s)" % (q_grade, q_letter))
print("Test grade: %d (%s)" % (t_grade, t_letter))
print("Final score: %d (%s)" % (final_grade, final_letter))

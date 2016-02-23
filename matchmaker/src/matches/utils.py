from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db.models import Q
from questions.models import UserAnswer, Question


# User = get_user_model()

# users = User.objects.all() #[user1, user2, ....]
# all_user_answers = UserAnswer.objects.all().order_by("user__id")  #[userAnswer1, userAnswer2, ....]

# # users
# shengchen2 = users[0]
# user1 = users[1]
# userc = users[2]


#  # Matching algotithm 1, time complexity O(N^2)

def get_points(user_a, user_b):
	a_answers = UserAnswer.objects.filter(user = user_a)
	b_answers = UserAnswer.objects.filter(user = user_b)
	a_total_awarded = 0
	a_points_possible = 0
	num_question = 0
	for a in a_answers:
		for b in b_answers:
			if a.question.id == b.question.id:
				num_question += 1
				a_pref = a.their_answer
				b_answer = b.my_answer
				if a_pref == b_answer:
					'''
					awards points forc correct answer
					'''
					a_total_awarded += a.their_points
					'''
					assign total points
					'''
				a_points_possible += a.their_points
			print "%s has awarded %s points of %s  to %s" %(user_a, a_total_awarded, a_points_possible, user_b) 
	percent = a_total_awarded / Decimal(a_points_possible)
	print percent, num_question
	if percent == 0:
		percent = 0.00001
	return percent, num_question

# get_points(shengchen2, user1)
# get_points(shengchen2, userc)
# get_points(user1, userc)


# match_percentage = "%.2f" % (Decimal(a[0]) * Decimal(b[0])) ** (1/Decimal(b[1])) 
# print match_percentage

def get_match(user_a, user_b):
	a = get_points(user_a, user_b)
	b = get_points(user_b, user_a)

	#a[0] = decimal match value
	# b[1] / a[1] = number of question answered
	number_of_questions = b[1]
	match_decimal = (Decimal(a[0]) * Decimal(b[0])) ** (1 / Decimal(number_of_questions)) # geometric mean in number of question answered
	return match_decimal, number_of_questions



# Matching algorithm 2, time complexity O(N)

# def get_match(user_a, user_b):
# 	q1 = Q(useranswer__user=user_a)
# 	q2 = Q(useranswer__user=user_b)
# 	question_set1 = Question.objects.filter(q1)
# 	question_set2 = Question.objects.filter(q2)
# 	if question_set1.count() == 0:
# 		return 0.0, 0
# 	if question_set2.count() == 0:
# 		return 0.0, 0
# 	question_set = (question_set1 | question_set2).distinct()
# 	a_points = 0
# 	b_points = 0  
# 	a_total_points = 0.000001
# 	b_total_points = 0.000001
# 	questions_in_common = 0
# 	for question in question_set:
# 		try:
# 			a = UserAnswer.objects.get(user=user_a, question=question)
# 		except:
# 			a = None
# 		try:
# 			b = UserAnswer.objects.get(user=user_b, question=question)
# 		except:
# 			b = None
# 		if a and b:
# 			questions_in_common += 1
# 			if a.their_answer == b.my_answer:
# 				b_points += a.their_points
# 			b_total_points += a.their_points
# 			if b.their_answer == a.my_answer:
# 				a_points += b.their_points
# 			a_total_points += b.their_points
# 	if questions_in_common > 0:
# 		a_decimal = a_points / Decimal(a_total_points)
# 		b_decimal = b_points / Decimal(b_total_points)
# 		print b_decimal, a_decimal
# 		if a_decimal == 0:
# 			a_decimal = 0.000001
# 		if b_decimal == 0:
# 			b_decimal = 0.000001
# 		match_percentage = (Decimal(a_decimal) * Decimal(b_decimal)) ** (1/Decimal(questions_in_common))
# 		return match_percentage, questions_in_common
# 	else:
# 		return 0.0, 0











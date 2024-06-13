import random
import utils

with open('data/questions.quiz', encoding='utf-8') as qq:

    text = qq.read().split('\n\n')
    question_list = []
    for q in text:
        i = q.split('\n')
        question_list.append({i[0]: {
                                        i[0]: utils.correct_answer(i[0]), 
                                        i[1]: utils.correct_answer(i[1]), 
                                        i[2]: utils.correct_answer(i[2]), 
                                        i[3]: utils.correct_answer(i[3])
                                        }
                                })
    print()                            
    question = random.sample(question_list, 1)
    
    

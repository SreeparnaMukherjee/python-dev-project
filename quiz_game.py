#Quiz Game
import time

def quiz_game():
    questions=[{"question": "The world’s nation 5G mobile network was launched by which country?", "options": ["A) Japan", "B) India", "C) South Korea", "D) Malaysia"], "answer": "C"},
              {"question": "The green planet in the solar system is?", "options": ["A) Uranus", "B) Mars", "C) Venus", "D) Earth"], "answer": "A"},
              {"question": "Which of these is the plant important in sericulture?", "options": ["A) Cassia", "B) Legumes", "C) Mulberry", "D) Cotton"], "answer": "C"},
              {"question": "At which place on earth are there days & nights of equal length always?", "options": ["A) Equator", "B) Poles", "C) Prime Meridian", "D) Nowhere"], "answer": "A"},
              {"question": "Why is the color of papaya yellow?", "options": ["A) Lycopene", "B) Papain", "C) Carotene", "D) Caricaxanthin"], "answer": "D"}]

    total= 0
    totalqn= len(questions)#Total number of questions 
    total_time=0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        strtime= time.time()
        answerd= input("Your answer (A/B/C/D): ").strip().upper()
        time_taken= time.time()-strtime
        total_time+=time_taken#Calculation of total time taken

        if answerd== q["answer"]:
            print("Correct answer!")
            total+= 1#Calculation of total score
        else:
            print(f"Wrong answer!\nThe correct answer is {q['answer']}")

        print(f"Time taken: {time_taken:.2f} seconds\n")
        
    score=(total/totalqn)*100#Calculation of percentage scored
    print(f"You got {total} out of {totalqn} questions right!\nTotal percentage scored is({score:.2f}%)\nTotal time taken is({total_time:.2f}seconds)")
    
quiz_game()

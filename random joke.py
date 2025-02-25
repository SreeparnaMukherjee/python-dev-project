#Random Joke Generator
import random
def random_joke():
    #10 funny jokes
    jokes=["Why can't a nose be 12 inches long?\nBecause then it would be a foot.",
           "Why can’t you put two half-dollars in your pocket?\nBecause two halves make a hole, and your money will fall out!",
           "I'm reading a book on anti-gravity.\nIt's impossible to put down!",
           "I had a joke about paper today, but it was tearable.",
           "What’s the difference between the bird flu and the swine flu?\nOne requires tweetment and the other an oinkment.",
           "Some people pick their nose, but I was born with mine.",
           "What is an astronaut’s favorite part on a computer?\nThe space bar.",
           "What do you call an apology written in dots and dashes?\nRe-Morse code.",
           "What do you call an elephant that doesn’t matter? An irrelephant.",
           "You can’t trust atoms. They make up everything!"]
    
    while True:
        choice=input("Do you want to hear a joke? (yes/no):")#Give your choice
        if choice=="No" or choice=="no":
            print("Hope you liked the jokes")
            break
        else:
            i=random.randint(0,9)#Continue with the jokes
            print("Here's a joke:")
            print(jokes[i])
            
random_joke()
        




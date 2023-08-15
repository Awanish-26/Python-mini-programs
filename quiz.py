from multiprocessing.sharedctypes import Value


quiz={
    "question1":{
        "question":"What is the capital of India ?",
        "answer":"Delhi"
    },
    "question2":{
        "question":"What is the national fruit of India ?",
        "answer":"mango"
    },
    "question3":{
        "question":"What is the capital of Germany ?",
        "answer":"berlin"
    },
    "question4":{
        "question":"What is the capital of Britain ?",
        "answer":"london"
    },
    "question5":{
        "question":"What is the capital of Australia? ",
        "answer":"sydney"
    },
    "question6":{
        "question":"What is the capital of Japan",
        "answer":"tokyo"
    },
}

score=0

for key,value in quiz.items():
    print(value['question'])
    answer =input("Answer ? :")

    if answer.lower() ==value['answer'].lower():
        print("You are corret!!")
        score +=1
        print("your score is " + str(score))

    else:
        print("Wrong")
        print("The answer is " + value["answer"])
        print("your score is " + str(score))

print("You got " + str(score) + "out of 7")
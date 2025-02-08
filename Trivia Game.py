'''#Building A Trivia Game
#list of question
#store the answers
#randomly pick questions
#ask the question
#see if they are correct
#keep track of the score
#tell the user there score'''
import random #used this for picking random question bring random module
questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3",
    "What keyword is used to define a variable in Python?": "No keyword, just assign with `=`",
"Which data type is used to store decimal numbers in Python?": "float",
"What is the index of the first element in a Python list?": "0",
"Which built-in function is used to convert a string to an integer?": "int()",
"How do you check the type of a variable in Python?": "type()",
"Which function is used to remove the last element from a list?": "pop()",
"What keyword is used to define a class in Python?": "class",
"What will print(bool([])) output?": "False",
"What is the result of 5 % 2 in Python?": "1",
"What function is used to open a file in Python?": "open()",
"Which module is used to generate random numbers in Python?": "random",
"What is the purpose of the break statement in loops?": "To exit the loop",
"Which keyword is used to handle exceptions in Python?": "try",
"What function is used to find the maximum value in a list?": "max()",
"Which operator is used to check equality in Python?": "==",
"What does range(5) generate?": "0, 1, 2, 3, 4",
"Which function is used to sort a list in ascending order?": "sorted()",
"What does str.upper() do to a string?": "Converts it to uppercase",
"Which statement is used to exit a function and return a value?": "return",
"What is the default encoding format in Python 3?": "UTF-8",
"Which keyword is used to create a function with no implementation?": "pass",
"What does list.append(x) do?": "Adds `x` to the end of the list",
"How do you write a single-line comment in Python?": "#",
"What is the output of bool(0) in Python?": "False",
"Which function is used to round a floating-point number?": "round()",
"What does the is operator check in Python?": "Object identity",
"Which function is used to get the ASCII value of a character?": "ord()",
"What does enumerate() do in Python?": "Adds an index to an iterable",
"What is the result of 10 / 2 in Python?": "5.0",
"What is the default return value of a function that has no return statement?": "None",
"Which keyword is used to define an infinite loop?": "while True",
"Which module is used to work with dates and times in Python?": "datetime",
"What is the result of 3 * 'Python'?": "'PythonPythonPython'",
"Which function is used to check if a key exists in a dictionary?": "in",
"What does the continue statement do in a loop?": "Skips the current iteration and moves to the next",
"Which data structure is used to store key-value pairs?": "dictionary",
"What is the result of 10 == '10' in Python?": "False",
"Which function is used to convert a list to a set?": "set()",
"What will print(type(None)) output?": "<class 'NoneType'>",
"Which method is used to remove leading and trailing spaces from a string?": "strip()",
"What keyword is used to define an anonymous function?": "lambda",

    
}

def python_trivia_game(): # def function
    questions_list = list(questions.keys())
    total_questions = 10
    score = 0
    selected_questions = random.sample(questions_list, total_questions)
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {correct_answer}.\n")
            
    print(f"Game over! Your final score is: {score}/{total_questions}")
    
python_trivia_game()

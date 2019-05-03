# you are to create your own test based on a subject, ideally for one of your
# teachers.  If you can have one question be multiple choice from a list, you
# will receive a better mark. Ten questions minimum.

print("Hi, welcome to the grade 11 Biology test")
import time
time.sleep(1)
print("Rules:")
print("1. Only the first letter of each answer must be capitalized")
print("2. In (True or False)' questions, simply answer 'True' or 'False'")

n = input("Type: 'Im ready' to begin: ")
if n == "Im ready":
    print("You may now begin the test, Good Luck!")
    import time
    time.sleep(2)
else:
    print("lets hope you follow instructions better on the actual test... Good Luck!")
    time.sleep(2)
           

def get_questions():
    return [["1. What branch of science is the study of living organisms? ", "Biology"],
            ["2. In the organism 'Felis catus', what is the genus name? ", "Felis"],
            ["3. What is the most specific taxon? ", "Species"],
            ["4. (True or False) Archaebacteria are all eukaryotic. ", "False"],
            ["5. (True or false) Humans share around 96% of their DNA with monkeys. ", "True"],
            ["6. What kingdom do humans belong to? ", "Animalia"],
            ["7. What is the field of biology that studies the classification of living organisms? ", "Taxonomy"],
            ["8. The system in which each organism recieves a 'two-part scientific name' is called: ", "Binomial nomenclature"],
            ["9. What is the language in which the scientific names of all organisms written in? ", "Latin"],
            ["10.(True or False) There are around 9 million different species on earth. ", "True"]]

def check_question(question_and_answer):
    question = question_and_answer[0]   
    answer = question_and_answer[1]
    given_answer = input(question)
    if answer == given_answer:
        print("Correct")
        return True
    else :
        print("Incorrect, correct was:", answer)
        return False
 
def run_test(questions):
    if len(questions) == 0:
        print("No questions were given.")
        return
    index = 0
    right = 0
    while index < len(questions):
        if check_question(questions[index]): 
            right = right + 1
        index = index + 1
    print("You got", right * 100 / len(questions),
           "% right out of", len(questions))
    time.sleep(3)
 
# now let's get the questions from the get_questions function, and
# send the returned list of lists as an argument to the run_test function.
 
run_test(get_questions())

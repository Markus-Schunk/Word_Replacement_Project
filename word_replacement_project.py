def get_user_input():
    global input_sentence
    input_sentence = input("Type in your sentence:")
    global word
    word = input("Which word do you want to remove?")
    global change_word
    change_word = input("What should the replacement word be?")

def replace_word():
    final_sentence = input_sentence.replace(word, change_word)
    print(final_sentence) if input_sentence.replace(word, change_word) == True else print("Please try again!")

get_user_input()
replace_word()
from itertools import permutations, count
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    html_form = """
        <html><body>
            <h1> Enter a word to find its paragrams. App Engine is awesome! </h1>
            <h2> This is the alteration of a letter or a series of letters in a word. </h2>
            <br>
            <br>
            <form action="" method="GET">
            Text: <input type="text" name="Paragrams">
            <input type="submit" value="Find Paragrams">
                </form>
        </body></html>"""
    input_word = request.args.get("Paragrams", "")
    if input_word:
        wordsparagrams = str(find_paragram(input_word))
        # print(wordsparagrams)
    else:
        wordsparagrams = ""

    return html_form + wordsparagrams


def find_paragram(input_word):
    # input_word = input("Enter a word to find its paragrams\n")
    values = list(permutations(input_word, len(input_word)))
    print("Here is a list of the paragrams of the word " + input_word)
    count_of = 0
    paragram_list = []
    for paragram in range(len(values)):
        print(''.join(values[paragram]))
        # return ''.join(values[paragram])
        count_of += 1
        paragram_list.append(values)
    makeitastring = ','.join(str(e) for e in paragram_list)
    print("list items \n")
    print(paragram_list)
    print("Type is ", type(paragram_list))
    print("make it a string: " , makeitastring)

    num_of_paragrams = count_of
    print("Paragrams of:", input_word, " = ", num_of_paragrams)
    return "There are " + str(num_of_paragrams) + " Paragrams for " + "'\'" + str(input_word) + "'\'" + \
           " ... Here They Are: " + str(paragram_list[paragram])


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

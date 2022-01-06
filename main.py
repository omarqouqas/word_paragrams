import itertools
from flask import Flask, request, render_template


app = Flask(__name__)


def find_paragrams(word: str) -> list:
    word = word.lower()
    '''Returns list of word paragrams'''

    # Get permutations as list of tuples of letters
    permutations = list(itertools.permutations(word, len(word)))

    # Join tuples inside of list
    permutations = [''.join(permutation_tuple)
                    for permutation_tuple in permutations]

    # Get rid of duplicates
    permutations = list(set(permutations))

    return permutations


@app.route("/", methods=['GET', 'POST'])
def index():
    # Default value in case if an empty string was passed into form
    params = None

    # POST request on form submit
    if request.method == 'POST':
        # Get form data
        word = request.form['paragrams']

        paragrams_list = find_paragrams(word) if word else None
        if paragrams_list:
            paragrams_count = len(paragrams_list)
            paragrams_str = ', '.join(paragrams_list)

            # Packing parameters in dict just to be clean
            params = {
                'paragrams_count': paragrams_count,
                'word': word,
                'paragrams_str': paragrams_str,
                'paragrams_list': paragrams_list
            }

    # Render html template with jinja rendering parameters
    return render_template('index.html', params=params, )


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

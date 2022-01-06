from flask import Flask
from flask import request
from itertools import permutations, count

app = Flask(__name__)


@app.route("/")
def index():
    html_form = """
        <html><body>
            <h1> Enter a number to find out whether it is a prime number, Elastic Beanstalk is awesome! </h1>
                <div> To prove whether a number is a prime number, first try dividing it by 2,
                    and see if you get a whole number. If you do, it can't be a prime number.
                    If you don't get a whole number, next try dividing it by prime numbers: 3, 5, 7, 11 (9 is divisible by 3)
                    and so on, always dividing by a prime number. 
                </div>
            <br>
            <br>
            <form action="" method="get">
            Number: <input type="text" name="number">
            <input type="submit" value="Is it prime?">
                </form>
        </body></html>"""

    number = request.args.get("number", "")
    if number:
        isitprime = str(is_prime(number))
        # print(isitprime)
    else:
        isitprime = ""

    return html_form + isitprime


def is_prime(number):
    while True:
        try:
            if number == 2:  # 2 is considered as a prime number
                return number, " is a Prime number."
            elif int(number) == 0 or int(number) == 1:
                return number, " is not Prime "
            elif int(number) % 2 == 0 and int(number) != 2:
                return number, " is not a Prime number since ", number, " is divisive by 2", number, "/", 2, " = ", int(
                    number) / 2
            elif int(number) > 3 and int(number) % 3 == 0:
                return number, " is not a Prime number since ", number, " is divisive by 3", number, "/", 3, " = ", int(
                    number) / 3
            elif int(number) > 5 and int(number) % 5 == 0:
                return number, " is not a Prime number since ", number, " is divisive by 5", number, "/", 5, " = ", int(
                    number) / 5
            elif int(number) > 7 and int(number) % 7 == 0:
                return number, " is not a Prime number since ", number, " is divisive by 7", number, "/", 7, " = ", int(
                    number) / 7
            elif int(number) < 0:  # negative numbers are not prime
                return number, " is not a prime number since ", number, " is less than 0"
            else:
                return number, " is a Prime number since ", number, " is divisive by itself and 1"
        except ValueError:
            return number, " Is not a valid input. You need to enter an integer!"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

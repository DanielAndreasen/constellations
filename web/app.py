from glob import glob
from random import choice, random, randint

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ndu93hf2mx9r893028xj'

def get_name(fname):
    return fname.split('/')[-1].split('.')[0].title().replace('_', ' ')
images = {get_name(image): image for image in glob('static/*.jpg')}

def get_random():
    return choice([key for key in images.keys()])


def get_answers(correct, n=3):
    res = set()
    res.add(correct)
    while len(res) != n:
        res.add(get_random())
    return res


def verify_guess(form):
    parts = form.get('guess').split('-')
    return parts[0] == parts[1], parts[0]


@app.route('/', methods=['GET', 'POST'])
def main():
    constellation = get_random()
    n = 5
    if request.method == 'POST':
        is_correct, correct = verify_guess(request.form)
        if is_correct:
            flash('Yay, you guessed correct!', category='success')
        else:
            flash(f'Oh no... The real answer was {correct}', category='warning')
        return render_template('play.html',
                image=images[constellation],
                title=constellation,
                answers=get_answers(constellation, n=n))

    return render_template('play.html',
            image=images[constellation],
            title=constellation,
            answers=get_answers(constellation, n=n),
            rotation=randint(0, 359))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

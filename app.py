from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        out = len(input_text)
        return str(out)
    return render_template('index.html')

@app.route('/count_chars', methods=['POST'])
def count_chars():
    input_text = request.form['input_text']
    out = len(input_text)
    return str(out)

if __name__ == '__main__':
    app.run()

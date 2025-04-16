from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.development')


@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/')
def main():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
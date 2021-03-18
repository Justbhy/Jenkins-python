from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "hello world 2"
    # return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask

# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return 'Hello World!\n'
# if __name__ == '__main__':
#     app.run()
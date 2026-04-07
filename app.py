from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    foods = ["치킨", "피자", "햄버거", "김밥", "떡볶이", "리면", "초밥"]
    return render_template('index.html', data=foods)

if __name__ == '__main__':
    app.run(debug=True)
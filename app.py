from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rolling')
def button1_clicked():
    return render_template('pic1.html')

@app.route('/button2-clicked')
def button2_clicked():
    return render_template('pic2.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=0000)
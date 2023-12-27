from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    student_name = request.form['student_name']
    recommendations = get_recommendations(student_name)
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
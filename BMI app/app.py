from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    bmi = None
    category = None
    diet = None

    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        # BMI Categories + Diet Plan
        if bmi < 18.5:
            category = "Underweight"
            diet = "Eat more calories: milk, banana, rice, nuts. Avoid skipping meals."
        elif bmi < 25:
            category = "Normal"
            diet = "Maintain balance: vegetables, fruits, proteins. Avoid junk food."
        elif bmi < 30:
            category = "Overweight"
            diet = "Eat less sugar and oil. Prefer salads, fruits. Avoid fried food."
        else:
            category = "Obese"
            diet = "Strict diet: vegetables, boiled food. Avoid junk, sugar, fast food."

        # Chart
        labels = ['Underweight', 'Normal', 'Overweight', 'Obese']
        values = [18.5, 24.9, 29.9, 35]

        plt.figure()
        plt.bar(labels, values)
        plt.axhline(y=bmi)
        plt.title("BMI Chart")
        plt.savefig('static/bmi_chart.png')
        plt.close()

    return render_template('index.html', bmi=bmi, category=category, diet=diet)

if __name__ == '__main__':
    app.run(debug=True)
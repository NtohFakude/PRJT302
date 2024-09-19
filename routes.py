from flask import Blueprint, request, render_template
from model import make_prediction

chatbot_routes = Blueprint('chatbot_routes', __name__)

questions = [
    "What is your name?",
    "What is your age?",
    "What is your cholesterol level?",
    "What is your systolic blood pressure?",
    "What is your diastolic blood pressure?",
    "What is your heart rate?",
    "What is your BMI?",
    "What is your triglycerides level?",
    "How many hours per week do you exercise?",
    "How many days per week are you physically active?",
    "How many hours do you sleep per day?",
    "How many hours per day do you spend being sedentary?",
    "What is your sex? (Male/Female)",
    "Do you have diabetes? (Yes/No)",
    "Do you have a family history of heart disease? (Yes/No)",
    "Do you smoke? (Yes/No)",
    "Are you obese? (Yes/No)",
    "Do you consume alcohol? (Yes/No)",
    "How would you describe your diet? (Healthy/Unhealthy)",
    "Have you had any previous heart problems? (Yes/No)",
    "Do you take any medication regularly? (Yes/No)",
    "On a scale of 1-5, how would you rate your stress level?",
    "What is your income level? (Low/Medium/High)"
]

user_responses = {}

@chatbot_routes.route('/', methods=['GET', 'POST'])
def index():
    total_questions = len(questions)

    if request.method == 'POST':
        question_number = int(request.form.get('question_number', 0))
        response = request.form.get('response')
        user_responses[questions[question_number]] = response

        if question_number == total_questions - 1:
            risk, advice = make_prediction(user_responses)
            return render_template('index.html', prediction=risk, advice=advice)

        return render_template('index.html', question=questions[question_number + 1], question_number=question_number + 1, total_questions=total_questions)

    return render_template('index.html', question=questions[0], question_number=0, total_questions=total_questions)

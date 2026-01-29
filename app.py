from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)

questions = [
    {
        "question": "What type of language is Python?",
        "options": ["Low level", "High level", "Machine", "Assembly"],
        "answer": "High level"
    },
    {
        "question": "What is the framework of python ?",
        "options": ["Flask", "React", "Angular", "Django"],
        "answer": "Flask"
    },
    {
        "question": "What is the full form of html?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyperlinks Text Mark Language",
            "None"
        ],
        "answer": "Hyper Text Markup Language"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            user_ans = request.form.get(f"q{i}")
            if user_ans == q["answer"]:
                score += 1
        return render_template("result.html", score=score, total=len(questions))

    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def check_number():
    result = None
    if request.method == "POST":
        number = request.form.get("number")
        if number.isdigit():
            num = int(number)
            result = f"{num} is {'Even' if num % 2 == 0 else 'Odd'}."
        else:
            result = "Please enter a valid number."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

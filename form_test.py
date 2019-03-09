from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'df2978c7bf21501f3c8e5a7c3c642075'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def process_form():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")

# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['useremail'])



if __name__ == "__main__":
    app.run(debug=True)

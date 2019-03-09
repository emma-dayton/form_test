from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def process_form():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    return redirect("/show", name, email)

# adding this method
@app.route("/show")
def show_user(name, email):
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name=name, email=email)



if __name__ == "__main__":
    app.run(debug=True)

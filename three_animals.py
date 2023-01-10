from flask import Flask
from flask import render_template
from flask import request

animals = ["mouse", "armadillo", "caterpillar", "buffalo", "dragonfly", "eel", "platypus", "lark", "manatee", "squid"]

app = Flask(__name__)

@app.route('/')
def show_choices():
    return render_template("/choice.html", animals=animals)

@app.route('/showanimals', methods=['GET', 'POST'])
def show_results():
	if request.method == "POST":
		value_animals = request.form.to_dict()
		if len(value_animals) > 1 and len(value_animals) < 4:
			return render_template("/result.html", value_animals=value_animals)
		elif len(value_animals) == 0:
			return """No animals selected. Make a new selection at the <a href='/'>main page</a>."""
		elif len(value_animals) >= 4:
			return """  More than three animals selected. Make a new selection at the <a href='/'>main page</a>. """
	return render_template("/result.html")

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD']=True
	app.config['DEBUG'] = True
	app.config['SERVER_NAME'] = "localhost:5000"         
	app.run()

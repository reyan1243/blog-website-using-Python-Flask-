from flask import Flask, render_template,url_for
from forms import registeration_form

posts= [{

    "Name": "Reyan Ishtiaq",
    "date": "7/10/2020",
    "title": "blog1",
    "article": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident perferendis architecto dolorem aliquid ratione ipsum magnam nam mollitia consequuntur, nemo a beatae suscipit, illum molestias sit eum maiores, obcaecati illo"
}, {
    "Name": "Shayyan Ahmed",
    "date": "8/10/2020",
    "title": "blog",
    "article": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident perferendis architecto dolorem aliquid ratione ipsum magnam nam mollitia consequuntur, nemo a beatae suscipit, illum molestias sit eum maiores, obcaecati illo"

}
]

para="THis is about page"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kesalagameramazaq'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title="home")

@app.route('/about')
def about():
    return render_template('about.html',title="about")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = registeration_form()
    return render_template("reg.html", title="registeration", form=form)



if __name__==("__main__"):
    app.run(debug=True)
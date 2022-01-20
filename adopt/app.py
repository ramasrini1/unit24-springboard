from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

#toolbar = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """Show homepage links."""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
  """Show Add Pet Form"""
  form = AddPetForm()

  if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        #flash(f"Added {name} at {price}")
        new_pet = Pet(name=name, species=species, 
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

  else:
        return render_template(
            "pet_add_form.html", form=form)


@app.route("/pet-<int:uid>", methods=["GET", "POST"])
def edit_pet(uid):
    """Show user edit form and handle edit."""

    pet = Pet.query.get_or_404(uid)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    return render_template("pet_edit_form.html", form=form, pet=pet)
   
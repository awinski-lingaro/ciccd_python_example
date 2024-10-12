from flask import Blueprint

from greetings_app.src.greetings_generator import Greetings

router = Blueprint("greetings", __name__)


@router.route("/<mood>")
def show_greetings(mood):
    generator = Greetings(mood=mood)
    return f"<h1>{generator.generate_greetings()}</h1>"

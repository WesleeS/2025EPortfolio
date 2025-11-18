from flask import Blueprint, render_template

experience_bp = Blueprint('experience', __name__, url_prefix='/experience')

# used to generate the contents of the sub navbelt
subpages = [
    {"name": "MCNCE", "endpoint": "experience.mcnce"},
    {"name": "Mansfield UM", "endpoint": "experience.mansfield"},
]

@experience_bp.route('/')
def index():
    return render_template(
        "experience.html",
        html_title="Experience",
        subpages=subpages,
        page="Experience"
    )

@experience_bp.route('/mcnce/')
def mcnce():
    return render_template(
        "experience_mcnce.html",
        html_title="Experience - MCNCE",
        subpages=subpages,
        page="MCNCE"
    )

@experience_bp.route('/mansfield-center/')
def mansfield():
    return render_template(
        "experience_mansfield.html",
        html_title="Experience - Mansfield Center",
        subpages=subpages,
        page="Mansfield UM"
    )

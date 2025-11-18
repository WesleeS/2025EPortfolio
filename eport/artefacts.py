from flask import Blueprint, render_template, url_for

artefacts_bp = Blueprint('artefacts', __name__, url_prefix='/artefacts')

# used to generate the contents of the sub navbelt
subpages = [
    {"name": "Art", "endpoint": "artefacts.art"},
    {"name": "Cookbook", "endpoint": "artefacts.cookbook"},
    {"name": "Projects", "endpoint": "artefacts.projects"},
    {"name": "Capstone", "endpoint": "artefacts.capstone"},
]

@artefacts_bp.route('/')
def index():
    return render_template(
        "artefacts.html",
        html_title="Artefacts",
        subpages=subpages,
        page="Artefacts"
    )

@artefacts_bp.route('/art/')
def art():
    return render_template(
        "artefacts_art.html",
        html_title="Artefacts - Art",
        subpages=subpages,
        page="Art"
    )

@artefacts_bp.route('/cookbook/')
def cookbook():
    return render_template(
        "artefacts_cookbook.html",
        html_title="Artefacts - Cookbook",
        subpages=subpages,
        page="Cookbook"
    )

@artefacts_bp.route('/projects/')
def projects():
    return render_template(
        "artefacts_projects.html",
        html_title="Artefacts - Projects",
        subpages=subpages,
        page="Projects"
    )

@artefacts_bp.route('/capstone/')
def capstone():
    return render_template(
        "artefacts_capstone.html",
        html_title="Artefacts - APA Wiki",
        subpages=subpages,
        page="Capstone"
    )

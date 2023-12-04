from flask import Blueprint, render_template, url_for

app_blueprint= Blueprint('app_blueprint',__name__)
@app_blueprint.route('/')
def contact():
    return render_template("contact.html")
# @app_blueprint.route('/data')
# def data():
#     return render_template("data.html")

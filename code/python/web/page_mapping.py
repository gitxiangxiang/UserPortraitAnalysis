from flask import Flask, render_template


def page_mapping(app):
    app.add_url_rule('/', '', to_index)


def to_index():
    return render_template("../index.html")

# -*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('')
def upload_landing_page(temp_id, temp_content):
    pass


if __name__ == '__main__':
    app.run(debug=True)

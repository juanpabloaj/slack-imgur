#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import os
import random

from imgurpython import ImgurClient

app = Flask(__name__)


def get_imgur_image():
    client_id = os.environ.get('IMGUR_CLIENT_ID')
    client_secret = os.environ.get('IMGUR_CLIENT_SECRET')

    if client_id and client_secret:

        client = ImgurClient(client_id, client_secret)
        gallery = client.gallery()
        random_gallery_index = random.randrange(len(gallery))
        return gallery[random_gallery_index].link


@app.route('/', methods=['GET', 'POST'])
def return_imgur_image():
    if request.method == 'POST':
        req = {'text': get_imgur_image()}
        return jsonify(**req)
    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()

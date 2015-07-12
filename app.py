#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import os
import random
from utils import tag_from_text

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

app = Flask(__name__)


def random_link_from_gallery_list(gallery_list, client):
    choice = random.choice(gallery_list)

    if choice.is_album:
        images = client.get_album_images(choice.id)
        choice = random.choice(images)

    return choice.link


def get_imgur_image(text):
    client_id = os.environ.get('IMGUR_CLIENT_ID')
    client_secret = os.environ.get('IMGUR_CLIENT_SECRET')

    if client_id and client_secret:

        client = ImgurClient(client_id, client_secret)
        tag = tag_from_text(text)

        if tag:
            try:
                gallery = client.gallery_tag(tag)
                gallery = gallery.items
            except ImgurClientError:
                return 'Tag {} not found'.format(tag)
        else:

            gallery = client.gallery()

        return random_link_from_gallery_list(gallery, client)


@app.route('/', methods=['GET', 'POST'])
def return_imgur_image():
    if request.method == 'POST':
        text = request.form['text']
        req = {'text': get_imgur_image(text)}
        return jsonify(**req)
    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()

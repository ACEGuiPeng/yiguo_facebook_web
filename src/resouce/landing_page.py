# -*- coding:utf-8 -*-
import os
from flask import request, render_template, make_response, Response

from flask_restful import Resource


class LandingPage(Resource):
    decorators = {}
    '''
    http://127.0.0.1:5000/ygfbad/web/land_page
    {
        "product_name":"product_name",
        "time":"timestamp",
        "order_num":"001"
    }
    '''

    def get(self, product_name, time, order_num, file_name):

        if isinstance(file_name, str):
            if file_name.endswith('html'):
                response = make_response(render_template('{}/{}/{}/{}'.format(product_name, time, order_num, file_name),
                                                         order_num=order_num))
            else:
                file = os.path.abspath('./templates/{}/{}/{}/{}'.format(product_name, time, order_num, file_name))
                image = open(file, 'rb')
                response = Response(image, mimetype="image/jpeg")

            return response

    def post(self, product_name, time, order_num, file_name):

        return self.get(product_name, time, order_num, file_name)

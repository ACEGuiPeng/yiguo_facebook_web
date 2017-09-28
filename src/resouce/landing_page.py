# -*- coding:utf-8 -*-
import os
from flask import request, render_template, make_response, Response

from flask_restful import Resource

mapper = {
    'html': 'text/html',
    'jpeg': "image/jpeg",
    # ...
}


class LandingPage(Resource):
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
            file_path = os.path.abspath('./templates/{}/{}/{}/{}'.format(product_name, time, order_num, file_name))
            for suffix, mimetype in mapper.items():
                if file_name.endswith(suffix):
                    file = open(file_path, 'rb')
                    response = Response(file, mimetype=mimetype)
                    return response

    def post(self, product_name, time, order_num, file_name):
        return self.get(product_name, time, order_num, file_name)

# -*- coding: iso-8859-1 -*-

from flask_restx import Resource, Namespace, reqparse
from app.main import services


api = Namespace('SampleNamespace', description='Sample Namespace description')  # TODO: Change


# TODO: Change
@api.route('/sample')
@api.param('sample_param', 'Sample parameter description')
@api.response(404, 'Resource not found.')
@api.response(200, 'Resource found.')
class Sample(Resource):
    @api.doc('Sample Resource Doc')
    def get(self):
        args = self.parse_args()
        services.sample_service(args)

        if args:
            return args, 200
        else:
            return {"errors": {"sample": "Sample error."},
                    "message": "Sample error message"}, 404

    @staticmethod
    def parse_args():
        parser = reqparse.RequestParser()
        parser.add_argument('sample_param', type=str, required=True, help="Sample param help")
        return parser.parse_args()

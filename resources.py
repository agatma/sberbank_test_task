from flask import request
from flask_restful import Resource, reqparse
from typing import Dict

from utils.response_messages import INCORRECT_FILE_PATH, EXPORT_QUERY_ERROR
from service.export_service import ExportService
from service.import_service import ImportService


class Import(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "path", type=str, required=True, help=INCORRECT_FILE_PATH, location="json"
    )

    def post(self):
        try:
            file: Dict[str, str] = Import.parser.parse_args()
        except KeyError:
            return {"message": INCORRECT_FILE_PATH}, 400
        response = ImportService.import_file_to_sql(file)
        return response


class Export(Resource):
    def get(self, property: str):
        lag_num = request.args.get("lag_num", 2, type=int)
        if not isinstance(lag_num, int):
            return {"message": EXPORT_QUERY_ERROR}, 400
        response = ExportService.export_df(property, lag_num)
        return response

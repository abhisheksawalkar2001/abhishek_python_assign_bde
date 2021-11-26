from flask import Flask, jsonify
from Task_1.calling_psql_funtion import abhishek_return_dep_people

app = Flask(__name__)


@app.route('/<string:organization_id>/')
def welcome(organization_id):
    return jsonify(abhishek_return_dep_people(organization_id))


if __name__ == '__main__':
    app.run(debug=True)

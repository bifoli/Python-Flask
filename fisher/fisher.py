
from flask import Flask, make_response


app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    # 基于类的视图（即插视图）
    # status code 200, 404, 301
    # content-type http headers
    # content-type = text/html
    # Response
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.google.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    # 生产环境 nginx + uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=88)

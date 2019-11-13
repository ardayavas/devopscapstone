from flask import Flask
from logging import Logger


log = Logger(__name__)
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World, my name is Arda Yavas - Rolling 11'

if __name__ == "__main__": # pragma: no cover
    log.info("START Flask")
    app.debug = True
    app.run(host='0.0.0.0', port=80)
    log.info("SHUTDOWN Flask")
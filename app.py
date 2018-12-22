from flask import Flask
app = Flask(__name__)


@app.route('/info')
def hello():
  return "Bigfoot Classinator service"

if __name__ == '__main__':
  app.run()

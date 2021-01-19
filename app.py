import logging
import datetime
from functions import save_call_details, save_voice
import json
from flask import Flask, render_template, make_response, request
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello_world():
    app.logger.info("Logging works")
    return 'Hello, World!'

@app.route('/twiml')
def twiml():
    template = render_template('twiml.xml')
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.route('/statuscallback', methods=['GET', 'POST'])
def callback():
    if request.method == "POST":
        data = request.form
        save_call_details(json.dumps(data))
        return data

@app.route('/action')
def action():
    template = render_template('action.xml')
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response


@app.route('/gatherspeech', methods=['POST'])
def gatherspeech():
    if request.method == "POST":
        data = request.form
        speechResult = request.form['SpeechResult']
        if  "Hello, how are you" in speechResult:
            app.logger.info("Forwarding call")
            template = render_template('forward.xml')

        if "Hangup" in speechResult:
            app.logger.info("Hanging up")
            template = render_template("hangup.xml")
        app.logger.info(speechResult)
        save_voice(json.dumps(data))
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        app.logger.info("saved voice details")
        return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

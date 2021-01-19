import json
import datetime
def save_call_details(f):
    j = json.loads(f)
    string = ''
    for key in j:
        value = j[key]
        string += ("{}: {}\n".format(key, value))
    filename = 'calllogs/' + str(datetime.datetime.now()) + ".txt"
    deets = open(filename, 'w')
    deets.write(string)
    deets.close()


def save_voice(f):
    j = json.loads(f)
    string = ''
    for key in j:
        value = j[key]
        string += ("{}: {}\n".format(key, value))
    filename = 'voice/' + str(datetime.datetime.now()) + ".txt"
    voice = open(filename, 'w')
    voice.write(string)
    voice.close()

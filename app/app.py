import time, datetime, os, uuid, json
from python_json_config import ConfigBuilder

def init():
    x = datetime.datetime.now()
    print(x)

    builder = ConfigBuilder()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config = builder.parse_config(dir_path + '/' + "config.json")
    outputDirectory = config.outputDirectory

def generateDate():
    timestr = time.strftime("%Y%m%d%H%M%S")
    return timestr

def takePhoto():
    image_filename = outputDirectory + "image%s.jpg"%(generateDate())
    print("Saving photo as " +image_filename)
    command = "raspistill -vf -o {0} -n --exposure auto".format(image_filename)
    os.system(command)

try:
    init()
    takePhoto()

except Exception as ex:
    print('Exception:')
    print(ex)
from flask import Flask, request
from celery import Celery
import pyo

app = Flask(__name__)
app.config.update(CELERY_BROKER_URL='<celery_broker>')


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


class PyoTask(celery.Task):
    name = "process_temp"

    def __init__(self):
        print('init was called')
        self.server = pyo.Server().boot()
        self.sf = pyo.SfPlayer("<filename>.wav", loop=True)  # replace <filename>
        self.hr = pyo.Harmonizer(self.sf).out()
        self.ch = pyo.Chorus(self.sf).out()
        self.dist = pyo.Disto(self.sf).out()
        self.dly = pyo.Delay(self.sf).out()
        self.server.start()

    def run(self, temp):
        print(f'got {temp} on a worker')
        mod = int(temp) % 100

        self.hr.mul = mod * 0.2
        self.hr.transpo = (mod - 50) * 0.25
        self.dist.drive = mod * 0.5


celery.tasks.register(PyoTask)


@app.route('/temp', methods=['POST'])
def temp():
    data = request.get_data(as_text=True)
    print(f"Got data : {data}")
    celery.tasks['process_temp'].delay(data)
    return 'OK'

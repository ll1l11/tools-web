# -*- coding: utf-8 -*-
import time
import datetime
import pytz

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/datetime-format', methods=['GET'])
def datetime_format():
    print 'a', request.args
    t = request.args.get('t', None, type=int)
    if not t:
        t = int(time.time())

    d = datetime.datetime.utcfromtimestamp(t)
    tz_utc = pytz.timezone('UTC')
    tz_china = pytz.timezone('Asia/Shanghai')
    d_utc = tz_utc.localize(d)
    d_china = d_utc.astimezone(tz_china)

    return render_template('datetime-format.html', t=t, d_utc=d_utc.isoformat(), d_china=d_china.isoformat())
    #return render_template('datetime-format.html', t=t)


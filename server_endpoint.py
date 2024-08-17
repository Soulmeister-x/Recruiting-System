from fastapi import FastAPI
import os
from data.data import get_data


app = FastAPI()

@app.get('/')
def read_root():
    return {'data': 'Hello World'}


@app.get('/data')
def read_data():
    return get_db()


@app.get('/events')
def read_events():
    data = get_data()
    return data['data']['events']



def init_fs():
    if not 'data' in os.listdir():
        os.mkdir('data')


def init_db():
    pass


def get_db():
    data = get_data()
    return data


if __name__ == '__main__':
    print('started')

    init_fs()
    init_db()

    db = get_db()

    for i, entry in enumerate(db.get('data')):
        print('#%d:\t%s' % (i, entry))


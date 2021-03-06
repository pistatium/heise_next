from logging import getLogger

import responder
from google.cloud import datastore


client = datastore.Client()

app = responder.API()


@app.route("/test")
async def test(req, resp,):
    key = Key('test')
    item = datastore.Entity(key)
    item.update({
        'count': item.get('count', 0) + 1
    })
    key = client.put(item)
    resp.text = f'{key}: {item["count"]}'


@app.route("/")
async def root(req, resp):
    resp.content = app.template('index.html')


if __name__ == '__main__':
    app.run()

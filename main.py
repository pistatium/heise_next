import responder
from logging import getLogger


app = responder.API()


@app.route("/{greeting}")
async def greet_world(req, resp, *, greeting):
    resp.text = f"{greeting}, world!"


@app.route("/")
async def root(req, resp, *, greeting):
    resp.text = f"/"


if __name__ == '__main__':
    app.run()

""" WebApp example

Run with uWSGI:

.. code:: sh

    uwsgi --http-socket localhost:8000 \
            --mule=batch.py \
            --wsgi-file app.py \
            --enable-threads
"""
import json

from poorwsgi import Application, state
from poorwsgi.response import TextResponse

import uwsgi  # type: ignore # pylint: disable=import-error

app = application = Application("Batch test")


@app.route('/', method=state.METHOD_POST)
def add_task(req):
    """Create task and add to queue"""
    data = {'time': req.start_time, 'path': req.path}
    uwsgi.mule_msg(json.dumps(data))
    return TextResponse("Created", status_code=201)

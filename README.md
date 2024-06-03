# uwsgi-batch

Example for https://uwsgi-docs.readthedocs.io/en/latest/Mules.html

Run with uWSGI:

```bash
    uwsgi --http-socket localhost:8000 \
            --mule=batch.py \
            --wsgi-file app.py \
            --enable-threads
```
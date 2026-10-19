# br-python-app

Demo Python app that installs Aikido-patched PyPI builds. Direct dependencies are pinned to `+aikido.N` versions from `https://pypi-staging.aikido.io/1f8edf5e23989a796bf/simple/`, except `urllib3`, which stays on the plain PyPI release. Everything else is resolved from PyPI.

`ddtrace` and `uv` are Linux wheels, so they install when the app is scanned or run on Linux.

`urllib3` is pinned to two plain upstream releases: `2.0.7` (except Windows) and `1.26.5` (Windows). The Aikido fixes are `2.0.7+aikido.5` and `1.26.5+aikido.11`.

```bash
uv sync
uv run python main.py
```

| Package | Installed |
| --- | --- |
| aiomysql | 0.2.0+aikido.3 |
| asteval | 1.0.5+aikido.2 |
| authlib | 1.7.0+aikido.2 |
| black | 26.1.0+aikido.2 |
| brotli | 1.1.0+aikido.6 |
| certifi | 2023.11.17+aikido.2 |
| cryptography | 49.0.0+aikido.3 |
| ddtrace | 4.8.0+aikido.1 (sys_platform == "linux") |
| ecdsa | 0.19.1+aikido.5 |
| eventlet | 0.33.1+aikido.2 |
| filelock | 3.20.2+aikido.2 |
| flask | 3.1.2+aikido.3 |
| flask-cors | 3.0.10+aikido.2 |
| future | 1.0.0+aikido.1 |
| h11 | 0.14.0+aikido.2 |
| h2 | 4.2.0+aikido.2 |
| httplib2 | 0.31.2+aikido.2 |
| idna | 3.14+aikido.1 |
| jaraco.context | 5.3.0+aikido.7 |
| jinja2 | 3.1.5+aikido.2 |
| joserfc | 1.6.7+aikido.1 |
| jwcrypto | 1.4+aikido.2 |
| lxml | 6.0.4+aikido.5 |
| markdown | 3.4.4+aikido.1 |
| markdown-it-py | 2.1.0+aikido.5 |
| marshmallow | 3.21.3+aikido.1 |
| msgpack | 1.2.0+aikido.2 |
| multipart | 1.2.1+aikido.2 |
| numexpr | 2.8.4+aikido.4 |
| opentelemetry-instrumentation | 0.36b0+aikido.1 |
| orjson | 3.11.5+aikido.4 |
| paramiko | 2.8.1+aikido.1 |
| pdfminer.six | 20240706+aikido.2 |
| pillow | 12.2.0+aikido.7 |
| pip | 26.1.1+aikido.1 |
| protobuf | 6.31.1+aikido.5 |
| pyasn1 | 0.6.3+aikido.3 |
| pydantic-settings | 2.14.0+aikido.1 |
| pygments | 2.12.0+aikido.3 |
| pymysql | 1.1.0+aikido.2 |
| pynacl | 1.5.0+aikido.7 |
| pypdf2 | 3.0.1+aikido.2 |
| pytest | 9.0.2+aikido.3 |
| python-dotenv | 1.2.1+aikido.3 |
| python-engineio | 4.13.1+aikido.1 |
| python-multipart | 0.0.29+aikido.3 |
| python-socketio | 5.16.1+aikido.1 |
| setuptools | 79.0.1+aikido.2 |
| soupsieve | 2.8.3+aikido.1 |
| starlette | 1.3.0+aikido.1 |
| telnyx | 4.88.1+aikido.2 |
| ujson | 5.12.1+aikido.3 |
| urllib3 | 2.0.7 (sys_platform != "win32") |
| urllib3 | 1.26.5 (sys_platform == "win32") |
| uv | 0.11.11+aikido.1 (sys_platform == "linux") |
| werkzeug | 3.1.3+aikido.4 |
| wheel | 0.45.1+aikido.6 |
| zipp | 3.17.0+aikido.2 |

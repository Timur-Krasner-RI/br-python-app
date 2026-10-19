import asyncio
import tomllib
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

ROOT = Path(__file__).resolve().parent


def installed_versions() -> dict[str, str]:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())
    versions = {}
    for spec in project["project"]["dependencies"]:
        name = spec.split("==", 1)[0].split(";", 1)[0].strip()
        try:
            versions[name] = version(name)
        except PackageNotFoundError:
            continue
    return versions


async def homepage(_request: Request) -> JSONResponse:
    return JSONResponse(installed_versions())


app = Starlette(routes=[Route("/", homepage)])


async def _check() -> None:
    scope = {
        "type": "http",
        "http_version": "1.1",
        "method": "GET",
        "scheme": "http",
        "path": "/",
        "raw_path": b"/",
        "query_string": b"",
        "headers": [],
        "client": ("127.0.0.1", 0),
        "server": ("127.0.0.1", 80),
    }
    response = await homepage(Request(scope))
    versions = installed_versions()
    plain = {"urllib3": {"2.0.7", "1.26.5"}}
    missing = [
        name
        for name, installed in versions.items()
        if "+aikido." not in installed and installed not in plain.get(name, ())
    ]
    print(response.status_code)
    print(f"{len(versions)} packages")
    if missing:
        raise SystemExit(f"missing aikido builds: {missing}")
    if versions.get("urllib3") not in {"2.0.7", "1.26.5"}:
        raise SystemExit(f"urllib3 should be a plain release, got {versions.get('urllib3')}")
    if response.status_code != 200:
        raise SystemExit(response.body.decode())


def main() -> None:
    print("br-python-app demo loaded")
    asyncio.run(_check())


if __name__ == "__main__":
    main()

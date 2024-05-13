import jwt
from pathlib import Path
import datetime as dt
import sys


def sign(pk_path: Path) -> str:
    pk = pk_path.read_text(encoding='utf-8')
    payload = {'iat': dt.datetime.now(dt.UTC)}
    return jwt.encode(payload, pk, algorithm='ES256')


def main(priv_key: str):
    priv_key_path = Path(priv_key)
    assert priv_key_path.is_file()
    print(sign(priv_key_path))


if __name__ == '__main__':
    main(sys.argv[1])
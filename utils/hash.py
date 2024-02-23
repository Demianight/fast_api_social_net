import jwt

from config import settings


def encode_jwt(
        payload: dict[str, str],
        private_key: str = settings.auth_jwt.private_key.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
):
    return jwt.encode(
        payload,
        private_key,
        algorithm,
    )


def decode_jwt(
        token: str,
        public_key: str = settings.auth_jwt.public_key.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
):
    return jwt.decode(
        token,
        public_key,
        [algorithm],
    )

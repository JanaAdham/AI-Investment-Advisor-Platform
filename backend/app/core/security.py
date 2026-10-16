import bcrypt


def hash_password(password: str) -> str:
    # bcrypt only reads the first 72 bytes of a password
    raw = password.encode("utf-8")[:72]
    return bcrypt.hashpw(raw, bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    try:
        raw = password.encode("utf-8")[:72]
        return bcrypt.checkpw(raw, password_hash.encode("utf-8"))
    except ValueError:
        # stored value is not a valid bcrypt hash (e.g. sample data)
        return False
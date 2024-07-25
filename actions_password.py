import re
import hashlib


def password_verification(password, cf_password):
    if not re.findall(r'[A-Z]', password):
        return False, 'Большие буквы где?'

    if len(password) < 8 or len(password) > 40:
        return False, 'Длина пароля должна быть от 8 до 40'

    if password != cf_password:
        return False, 'пароли не совпадают'

    return True, 'ok'


def hash_password(password):
    hash_ = hashlib.sha1()
    hash_.update(bytes(password, 'utf-8'))
    return hash_.hexdigest()

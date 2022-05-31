from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xe5\xfd\xcb\xf7\x8d\x9dm"C\x08\x95\xc8\xd8:\xc9\x84'
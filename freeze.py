from app import app, df
from flask_frozen import Freezer
import os
import shutil

app.config['FREEZER_DESTINATION'] = 'static_site'
app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

@freezer.register_generator
def accom():
    for accom_id in df["ID"]:
        yield {'accom_id': accom_id}

if __name__ == '__main__':
    freezer.freeze()

    # Copy static files
    static_src = os.path.join('static')
    static_dest = os.path.join(app.config['FREEZER_DESTINATION'], 'static')
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    shutil.copytree(static_src, static_dest)

    print("Static site generated at ./static_site")

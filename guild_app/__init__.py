from flask import Flask

app = Flask(__name__)
app.secret_key = "Crimson Moon"

import guild_app.views
"""from guild_app.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    if db_session != None:
        db_session.close()"""
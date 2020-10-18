from apps.main import app

# do some production specific things to the apps
app.config['DEBUG'] = False

import counter_app
from counter_app import home_page, app, show, db

@app.router('/')
def home():
    return show(home_page)
app.run(host='0.0.0.0',port=81)
from flask import request

from epub import app

@app.route('/location_sync', methods=['POST'])
def location_sync():
    print(request.form['cfi'])
    return "Location received"
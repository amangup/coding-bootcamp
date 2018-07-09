from vintage_photo import app, initialize

class Config:
    SECRET_KEY = 'very-hard-password'
    UPLOAD_FOLDER = '/home/aman/uploads'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def main():
    initialize(Config())
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()

from fortune_teller import app, initialize


class Config:
    SECRET_KEY = 'very-hard-password'
    FORTUNES_FILEPATH = '/home/aman/fortunes.txt'


def main():
    initialize(Config())
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()

from fortune_teller import app, initialize


def main():
    initialize()
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()

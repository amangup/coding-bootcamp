from writer import app


def main():
    app.run(host='127.0.0.1', port=8080, ssl_context=('cert.pem', 'key.pem'), debug=True)


if __name__ == '__main__':
    main()

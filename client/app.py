import requests

def main():
    url = "http://server:5000/"  # обращаемся по имени сервиса из docker-compose
    response = requests.get(url)

    filename = "received.txt"
    with open(filename, "wb") as f:
        f.write(response.content)

    print("Файл получен от сервера. Содержимое:")
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()

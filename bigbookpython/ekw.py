import requests


def show_rest_code(response):
    resp_code = response.status_code
    print("response code: ", resp_code)


def request():
    # response = requests.get("https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW?komunikaty=true&kontakt=true&okienkoSerwisowe=false")
    response = requests.get("https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/pokazWydruk")
    show_rest_code(response=response)
    print(response.text)

    response = requests.post("https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW")
    show_rest_code(response=response)
    print(response.text)

    if response.status_code == "200":
        print("if - co nam zwrocilo ")
        print(response.text)
        # print(response.json())


def main():
    request()


if __name__ == "__main__":
    main()

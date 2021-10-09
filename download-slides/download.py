

import requests


def getFilename_by_url(url):
    arrs = url.split("/")
    filename = arrs[len(arrs) - 1]
    return filename


def write_file(filename, content):
    open(filename, 'wb').write(content)


def req_get_content(url):
    return requests.get(url, allow_redirects=True, verify=False)


def main():
    f = open("urls.txt", "r")
    str = f.read()
    arrs = str.split("\n")

    for url in arrs:
        print("Downloading: " + url)
        r = req_get_content(url)
        filename = getFilename_by_url(url)
        write_file(filename, r.content)


if __name__ == "__main__":
    main()

import requests
import hashlib


def request_api_data(query_char):
    # sha1形式の最初の5文字を送ると、該当するパスワードが全部返ってくる
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")

    return res


def get_password_leaks_count(hashes, hash_to_check):

    for line in hashes.splitlines():
        hash, count = line.split(":")
        if hash == hash_to_check:
            return count
    return 0

    # generatorが返ってくる
    # g = (line.split(":") for line in hashes.splitlines())
    # print(type(g))

    # list comprehension
    # hashes = [line.split(":") for line in hashes.splitlines()]
    # for hash, count in hashes:
    #     if hash == hash_to_check:
    #         return count
    # return 0


def pwned_api_check(password):
    sha1_pasword = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_pasword[:5], sha1_pasword[5:]
    res = request_api_data(first5_char)

    return get_password_leaks_count(res.text, tail)


def main():
    count = pwned_api_check("password123")
    print(count)


main()

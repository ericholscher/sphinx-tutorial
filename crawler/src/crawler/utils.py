import re


def log(url, status):
    """
    Log information about a response to the console.

    :param url: The URL that was retrieved.
    :param status: A status code for the `Response`.

    """
    if 200 <= int(status) < 300:
        prose = 'OK'
    else:
        prose = 'ERR'
    print("{prose}: {status} {url}".format(prose=prose, url=url, status=status))


def should_ignore(ignore_list, url):
    """
    Returns True if the URL should be ignored

    :param ignore_list: The list of regexs to ignore.
    :param url: The fully qualified URL to compare against.
    """
    for pattern in ignore_list:
        compiled = re.compile(pattern)
        if compiled.search(url):
            return True
    return False

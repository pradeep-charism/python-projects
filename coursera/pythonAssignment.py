import re


def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"

    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return len(result)


# raise NotImplementedError()

print(example_word_count())


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    value = re.findall('[A-Z]\\w*', simple_string)
    print(value)
    # raise NotImplementedError()


names()


def grades():
    with open("assets/grades.txt", "r") as file:
        grades = file.read()

    value = re.findall('([A-Z][a-z]+ [A-Z][a-z]+): B', grades)
    print(value)
    # raise NotImplementedError()


grades()


def logs():
    data = []
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    pattern = """(?P<host>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)
                    (\ - \ )
                    (?P<user_name>(\w*)(\S))
                    (\  \S)
                    (?P<time>\d+\S\w*\S\d+\S\d+\S\d+\S\d+\s\S\d+)
                    (\S\s\S)
                    (?P<request>\w*\s\S*\s\w*\S\d.\d*)
                 """
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        data.append(item.groupdict())
    return data
    raise NotImplementedError()


print(len(logs()))

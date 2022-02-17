def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def list_example(*mylist):
    for i in mylist:
        print(i, end=", ")


print()
list_example("a ", 'b ', 'c ')


def dict_example(**mydict):
    for i in mydict:
        print(i, ":", mydict[i])


print()
dict_example(name="dsfds", value="valuedsfasdf")


def make_incrementor(n):
    """ This is documentation
        in python
    """
    return lambda x: x + n


print()
func = make_incrementor(20)
print(func(1))
print(func(2))
print(func(3))

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    split = person.split(" ")
    return split[0] + " " + split[-1]


print(list(map(split_title_and_name, people)))

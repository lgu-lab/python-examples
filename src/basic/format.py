
def format1():
    print("--- Format : ")
    txt = 'Hello {}, var {}'
    print("txt = " + txt)
    r = txt.format('Foo','AAA')
    print("after format = " + r)
    elements = ['aa','bb','cc','dd' ] # OK
    # list = ['aa','bb']
    print("after format = " + txt.format(*elements))

def format2():
    print("--- Format with names : ")
    txt = "Hello {firstName} {lastName}"
    print("txt = " + txt)
    mydict = dict();
    mydict["lastName"] = "Zola"
    mydict["foo"] = "bar"
    mydict["firstName"] = "Emile"
    r = txt.format(**mydict)
    print("after format : " + r)

if __name__ == '__main__':
    format1()
    format2()

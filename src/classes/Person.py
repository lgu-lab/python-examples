
class Person :
    foo = "FOO" # static variable

#    def __init__(self) :
#        self.firstName = "undefined"
#        self.__lastName  = "undefined"

    def __init__(self, firstName = "?", lastName= "?") :
        self.firstName = firstName
        self.__lastName  = lastName  # private

    def getLastName(self):
        return self.__lastName
    
    def __str__(self) :
        return self.firstName + " " + self.__lastName

def main():
    print ( "foo = ", Person.foo)
    Person.foo = "aaa"
    print ( "foo = ", Person.foo)

    p = Person("Emile", "Zola")
    print(p)
    print(p.firstName)
    # print(p.lastName) # Error (private)

    p = Person()
    print(p)
    print(p.firstName)


if __name__ == '__main__':
    main()

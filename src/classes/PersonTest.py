from classes.Person import Person

def main():
    p1 = Person("Emile", "Zola")
    print(p1)
    print(" . first name = " + p1.firstName)
    # print(" . last name = " + p1.__lastName)
    print(" . getLastName() = " + p1.getLastName())
    print(p1.foo)

    Person.foo = "FOO-CHANGED"
    
    p2 = Person("Gustave", "Flaubert")
    print(p2)
    print(p2.foo)
    print(p1.foo)

if __name__ == '__main__':
    main()

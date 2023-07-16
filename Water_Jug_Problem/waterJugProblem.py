jar1 = 0
jar2 = 0


def fillJar1(c1):
    global jar1
    jar1 = c1


def fillJar2(c2):
    global jar2
    jar2 = c2


def emptyJar1():
    global jar1
    jar1 = 0


def emptyJar2():
    global jar2
    jar2 = 0


def jar1inJar2(c1, c2):
    global jar1, jar2
    q1 = jar1
    avail2 = c2 - jar2
    jar1 = max(q1 - avail2, 0)
    jar2 = min(q1 + jar2, c2)


def jar2inJar1(c1, c2):
    global jar1, jar2
    q2 = jar2
    avail1 = c1 - jar1
    jar2 = max(q2 - avail1, 0)
    jar1 = min(q2 + jar1, c1)


def waterJug():
    c1 = int(input('Enter capacity of jug1: '))
    c2 = int(input('Enter capacity of jug2: '))
    target1 = int(input('Enter target of jug1: '))
    target2 = int(input('Enter target of jug2: '))

    while jar1 != target1 or jar2 != target2:
        print('1. Fill j' + str(c1) + '\n2. Fill j' + str(c2) +
              '\n3. Empty j' + str(c1) + '\n4. Empty j' + str(c2) +
              '\n5. Empty j' + str(c1) + ' in j' + str(c2) + '\n6. Empty j' + str(c2) + ' in j' + str(c1) + '\n7. Exit')
        ch = int(input('Enter choice: '))
        if ch == 1:
            fillJar1(c1)
        elif ch == 2:
            fillJar2(c2)
        elif ch == 3:
            emptyJar1()
        elif ch == 4:
            emptyJar2()
        elif ch == 5:
            jar1inJar2(c1, c2)
        elif ch == 6:
            jar2inJar1(c1, c2)
        elif ch == 7:
            break
        print('Jug' + str(c1) + '= ' + str(jar1) + ' Jug' + str(c2) + '= ' + str(jar2))

    print('Goal State Reached')


waterJug()

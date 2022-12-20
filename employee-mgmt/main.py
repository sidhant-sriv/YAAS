import hashlib

DB_URL = "employee.txt"
admin_auth = input("Are you an admin? (y/n) ")
if admin_auth == "y":
    if input("Enter password ") == "IAMADMIN":
        admin_auth = True
else:
    admin_auth = False
print("1 Employee registration")
print("2 Employee Search")
print("3 Employee information modification")
print("4 Show all records")
if admin_auth:
    print("5 Delete record")
option = int(input())


def create_record():
    name = input("Name\n")
    designation = input("Designation\n")
    salary = input("Salary\n")
    address = input("Address\n")
    email = input("Email\n")

    mobile = input("Number\n")
    while True:
        if len(mobile) != 10:
            mobile = input("Enter valid number\n")
        else:
            break

    emergency = input("Emergency contact\n")
    parent = input("Parent's name\n")

    l = name + mobile
    id = hashlib.md5(l.encode()).hexdigest()[0:5]
    with open(DB_URL, "a+") as f:
        f.write(
            ",".join(
                [
                    id,
                    name,
                    designation,
                    salary,
                    address,
                    email,
                    mobile,
                    emergency,
                    parent,
                ]
            )
            + "\n"
        )
    return [id, name, designation, salary, address, email, mobile, emergency, parent]


def search_record(user_id):
    with open(DB_URL) as f:
        f = [i.split(",") for i in f.readlines()]
    for i in f:
        if i[0] == user_id:
            return i
    return False


def update_record(user_id):
    with open(DB_URL) as f:
        f = [i.split(",") for i in f.readlines()]
    res = []
    d = {}
    for i in f:
        d[i[0]] = i[1:]
    if search_record(user_id):

        name = input("Name\n")
        designation = input("Designation\n")
        salary = input("Salary\n")
        address = input("Address\n")
        email = input("Email\n")

        mobile = input("Number\n")
        while True:
            if len(mobile) != 10 and not mobile.isdigit():
                mobile = input("Enter valid number\n")
            else:
                break

        emergency = input("Emergency contact\n")
        parent = input("Parent's name\n")
        d[user_id] = [
            name,
            designation,
            salary,
            address,
            email,
            mobile,
            emergency,
            parent,
        ]
    for k, v in d.items():
        t = ",".join([k] + v)
        res.append(t)
    res = "\n".join(res)
    with open(DB_URL, "w") as f:
        f.write(res)


def show_records():
    with open(DB_URL) as f:
        f = [i.split(",") for i in f.readlines()]
    for i in f:
        print(" ".join(i))


def delete_record(user_id):

    with open(DB_URL) as f:
        f = [i.split(",") for i in f.readlines()]
    res = []
    d = {}
    for i in f:
        d[i[0]] = i[1:]
    if search_record(user_id):
        del d[user_id]
    for k, v in d.items():
        t = ",".join([k] + v)
        res.append(t)
    res = "\n".join(res)
    with open(DB_URL, "w") as f:
        f.write(res)


if option == 1:
    print(create_record())
elif option == 2:
    print(search_record(input("Enter the user id")))
elif option == 3:
    update_record(input("Enter user id "))
elif option == 4:
    show_records()
if admin_auth and option == 5:
    delete_record(input("Enter user id "))

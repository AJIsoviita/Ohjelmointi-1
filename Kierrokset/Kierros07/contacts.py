# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: contacts, program code template


def main():
    contacts = {"Tom": {"name": "Tom Techie",
                        "phone": "040 123546",
                        "email": "tom@tut.fi",
                        "skype": "tom_92_"},
                "Mike": {"name": "Mike Mechanic",
                         "phone": "050 123546",
                         "email": "mike@tut.fi",
                         "skype": "-Mike-M-"},
                "Archie": {"name": "Archie Architect",
                           "phone": "050 987654",
                           "email": "archie@tut.fi"}}

    contact = input("Enter the name of the contact: ")
    field = input("Enter the field name you're searching for: ")

    for i in contacts:
        if contact == i:
            for x in contacts[i]:
                if field == x:
                    print(contacts[i]['name'], ', ', field,': ', contacts[i][x], sep='')
                    return
            else:
                print('No', field, 'for', contacts[i]['name'])
                return
    else:
        print('No contact information for', contact)
    print(contacts)



main()

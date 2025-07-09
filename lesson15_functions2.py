
def create_record(name, telephone, address):
    """"create record"""
    record = {
        'name' : name,
        'phone' : telephone,
        'address' : address
    }
    return record

user1 = create_record("Vasya", "+799999999", "1street)")
user2 = create_record("Petya", "+799999991", "2street)")
print(user1)
print(user2)

print("____________________________________________________________________________")
def give_award(medal, *persons):
    """give medals to persons"""
    for person in persons:
        print("tovarich " + person.title() + " nagrazhdaetsya medalyu" + medal)
give_award(" za berlin", "Vasya", "Petya")
give_award(" za london", "Petya", "Alex")
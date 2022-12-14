from Notes import Notes

a = Notes()
a.clear_all()
a.add_note(("last", "first", 123456, "домашний"))
print(a.get_all())

a.end()

b = Notes()
b.add_note(("last2", "first2", 1234563456, "домашний2"))
# b.export_phones()
print(b.get_all())
# b.delete_by_id("0")
print(b.get_all())
# print(b.change_by_id("1", ("иванов", "first2", 1234563456, "домашний2")))
print(b.get_all())
# b.import_notes("test.csv", "csv")
# print(b.get_all())
# b.import_notes("test.db", "sql")
# print(b.get_all())
# b.import_notes("test.json", "json")
# print(b.get_all())
b.end()
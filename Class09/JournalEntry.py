import datetime


class JournalEntry:
    # class level
    last_used_id = 0
    # value shared between each object, a common value
    def __init__(self, text):
        JournalEntry.last_used_id += 1
        self.journal_id = JournalEntry.last_used_id
        self.journal_text = text
        self.journal_date = datetime.datetime.now()

# Test


my_list_of_journal = [JournalEntry("Hello"), JournalEntry("Hey"), JournalEntry("Bye")]
for j in my_list_of_journal:
    print("ID   : " + str(j.journal_id))
    print("Text : " + j.journal_text)
    print("Date : " + str(j.journal_date))
    print("*" * 20)



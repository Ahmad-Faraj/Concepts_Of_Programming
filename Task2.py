print("Enter your borrowed books in the format 'Book Title - Days Borrowed'")
book_records = []
while True:
    record = input()
    if not record:
        break
    book_records.append(record.strip())

book_dict = {}

for record in book_records:
    title, days_borrowed = record.split(" - ")
    days_borrowed = int(days_borrowed)
    book_dict[title] = book_dict.get(title, 0) + days_borrowed


def find_max_entry(dictionary):
    max_key = None
    max_value = float("-inf")
    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key, max_value

most_borrowed_book = find_max_entry(book_dict)

def find_min_entry(dictionary):
    min_key = None
    min_value = float("inf")
    for key, value in dictionary.items():
        if value < min_value:
            min_key = key
            min_value = value
    return min_key, min_value

least_borrowed_book = find_min_entry(book_dict)

total_days = sum(book_dict.values())
total_books = len(book_dict)

if total_books > 0:
    average_borrowed_days = total_days / total_books
else:
    average_borrowed_days = 0

unique_titles = set(book_dict.keys())

sorted_books = list(book_dict.items())

for i in range(len(sorted_books)):
    for j in range(i + 1, len(sorted_books)):
        if sorted_books[i][1] < sorted_books[j][1]:
            sorted_books[i], sorted_books[j] = sorted_books[j], sorted_books[i]

print("\nResults:")
if most_borrowed_book[0]:
    print(f"Most borrowed book: {most_borrowed_book[0]} ({most_borrowed_book[1]} days)")
else:
    print("No books borrowed.")

if least_borrowed_book[0]:
    print(f"Least borrowed book: {least_borrowed_book[0]} ({least_borrowed_book[1]} days)")
else:
    print("No books borrowed.")

print(f"Average days books were borrowed: {average_borrowed_days:.3f}")
print(f"Unique titles of borrowed books: {unique_titles}")
print(f"Books sorted by borrowing duration:")
for title, days in sorted_books:
    print(f"{title}: {days} days")

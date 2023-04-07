
filter_strings_with_prefix = lambda strings, prefix: [s for s in strings if s.startswith(prefix)]

strings = ["apple", "banana", "cherry", "date", "kiwi"]
prefix = "b"
filtered_list = filter_strings_with_prefix(strings, prefix)
print("words started with '{}':".format(prefix))
print(filtered_list)

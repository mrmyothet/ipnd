text = "all zip files are zipped"
first_zip = text.find("zip")
print(text.find("zip",first_zip + 1))

text = "all zip files are compressed"
print(text.find("zip",text.find("zip") + 1))

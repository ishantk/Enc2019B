import re # Regular Expressions

quote = "Search the Candle rather than cursing the darkness"
result = re.match("Search", quote)
print(result)
print(result.start())
print(result.end()) # which means less than 6 or end

print()

result = re.search("the", quote)
print(result)

print()
result = re.findall("the", quote)
print(result)
print(type(result))

print()

result = re.split("the", quote)
print(result)

print()

result = re.sub("the", "a", quote)
print(result)
print(quote)

print()
print("**************")
newQuote = "Work Hard and Get Luckier"

result = re.findall(".", newQuote)
print(result)

print()
result = re.findall("\w", newQuote)
print(result)

print()
result = re.findall("\w*", newQuote)
print(result)

print()
result = re.findall("\w+", newQuote)
print(result)

# Assignment:
# Take Input as Vehicle Number from User and validate, is it a correct number or not !!
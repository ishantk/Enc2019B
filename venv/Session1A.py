# Write Operation
# businessName = 'Johns Coffee Shop'
# businessName = 'John\'s Coffee Shop'
# businessName = r'John\'s Coffee Shop' # Raw String

# businessName = "John's Coffee Shop"
# For Multi line string use """
businessName = """John's Coffee Shop
                    Near Pristine Magnum"""
# Read Operation
print(businessName)

# Not Required: Because as main thread will finish, i.e. process finished
#               and hence, memory is cleared automatically
# del businessName

"""
message = "Hello," \
          "This is a Message" \
          "Regards," \
          "John"
"""

message = """Hello,
          This is a Message
          Regards,
          John"""

print(message)
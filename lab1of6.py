username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

#using log to define the function and using string formatting 

def log():
    username = "Kinari"
    timestamp = "4:50"
    url = "http://petshop.com/pets mammals/cats"
    log_message = "%s accessed the site %s at %s"  %(username, url, timestamp)
    return log_message
log()
print(log())

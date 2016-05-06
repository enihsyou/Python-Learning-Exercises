def check_connection(network, first, second):
    data = [set(item.split('-')) for item in network]
    friends = {first, }
    for i in range(len(network)):
        for item in data:
            if item & friends:
                friends |= item

    return second in friends


# check_connection(
# ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#  "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
# "scout2", "scout3")
# check_connection(
#     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#     "super", "scout2")
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout")

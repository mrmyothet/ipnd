def remove(somestring,sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location == -1:
        return somestring
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return(part_before + part_after)
print(remove("ding","do"))
print(remove("doomy","dooming"))

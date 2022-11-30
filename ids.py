
class Ids:
    class Chassis:
        drive_left = 0
        drive_right = 1
    
    class OtherComp:
        test_id = 1
        another_test_id = 3

class Ports:
    pass



# recursively get all attributes
def get_ids(cls):
    # ignore dunders
    attributes = [x for x in dir(cls) if not x.startswith("__")]
    ids = []
    for att in attributes:
        if type(getattr(cls, att)) == type:
            ids.extend(get_ids(getattr(cls, att)))
        else:
            ids.append(getattr(cls, att))

    return ids

# enforce no duplicate ids
def check_ids():
    all_ids = get_ids(Ids)
    dups = set([str(x) for x in all_ids if all_ids.count(x) > 1])
    if dups:
        raise ValueError("Duplicate Ids detected: " + ", ".join(dups))

if __name__ == "__main__":
    check_ids()
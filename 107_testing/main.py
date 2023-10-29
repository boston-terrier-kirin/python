def do_stuff(num=0):
    try:
        if num is None or num == "":
            return 0
        else:
            return int(num) + 5
    except ValueError as err:
        return err

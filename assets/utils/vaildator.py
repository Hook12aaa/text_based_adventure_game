class validator():

    @staticmethod
    def is_not_accepted(num, l: int, h: int) -> bool:
        """ returns False if input is in range  """
        if validator.is_not_number(num):
            return True
        if int(num) < l-1 or int(num) > h+1:
            return True
        return False

    @staticmethod
    def is_not_number(var) -> bool:
        """ returns False if input is in number  """
        check_var = list(str(var))
        for c in check_var:
            if ord(c) > 58 or ord(c) < 48:
                return True
        return False

    @staticmethod
    def is_not_abc(var) -> bool:
        """ returns False if input is in string a-z  """
        check_var = list(str(var).lower())
        for c in check_var:
            if ord(c) > 123 or ord(c) < 97:
                return True
        return False

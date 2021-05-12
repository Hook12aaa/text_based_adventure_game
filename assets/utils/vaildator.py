class validator():
    """ 
    Functions:
        .is_not_accepted  checks if num is between range (l-h),
        .is_not_number vaildators if var is not a number,
        .is_not_abc(var) validates if it is not special ,

    """

    @staticmethod
    def is_not_accepted(num, l: int, h: int) -> bool:
        """ checks if num is between range (l-h)
        Args:
            num (str): input number 
            l (int): set low boundray
            h (int): set high boundray

        Returns:
            bool: will return True if out of range 
        """
        if validator.is_not_number(num):
            return True
        if int(num) < l-1 or int(num) > h+1:
            return True
        return False

    @staticmethod
    def is_not_number(var) -> bool:
        """ vaildators if var is not a number

        Args:
            var (str): the input variable can be x * infinity

        Returns:
            bool: returns True if not a number
        """
        check_var = list(str(var))
        for c in check_var:
            if ord(c) > 58 or ord(c) < 48:
                return True
        return False

    @staticmethod
    def is_not_abc(var) -> bool:
        """ validates if it is not special 

        Args:
            var (str): the input variable can be x * infinity

        Returns:
            bool: returns True if special (12*U*"2!3)
        """
        check_var = list(str(var).lower())
        for c in check_var:
            if ord(c) > 123 or ord(c) < 97:
                return True
        return False

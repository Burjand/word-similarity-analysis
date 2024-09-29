class Math_tools():

    def is_string_number(value):

        if isinstance(value, str):

            if value.isdigit():

                return True

            try:

                float(value)
                return True
            
            except ValueError:

                return False
            
        return False
    
    
    def is_string_number_hollistic(value: str):

        characters = [x for x in value]

        for c in characters:

            if (c.isdigit()):

                return True
            
        return False
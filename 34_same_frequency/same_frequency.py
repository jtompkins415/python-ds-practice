import collections

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_list_a = str(num1)
    num_list_b = str(num2)

    counter_a = collections.Counter(num_list_a)
    counter_b = collections.Counter(num_list_b)
    
    if counter_a != counter_b:
        return False
    else:
       return True
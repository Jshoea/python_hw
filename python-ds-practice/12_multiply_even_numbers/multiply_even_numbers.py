def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    #create an element to multiply off of first
    product =1
    #iterate through nums and just keep multiplying each even num we see
    for num in nums:
        if num%2 == 0:
            product = product * num
    return product
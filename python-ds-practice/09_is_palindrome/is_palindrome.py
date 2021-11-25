def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    paliPhrase = phrase.lower().replace(' ', '')
            #these methods help to lower case and remove spaces when deciding
    return paliPhrase == paliPhrase[::-1]
        #returns true if backwards case is equal

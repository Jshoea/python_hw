def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return phrase[:1].upper()+ phrase[1:]
    #this capitalizes the index zero then gives rest of phrase
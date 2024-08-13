def prefic(string,prefix):
    for char in string:
        if char[:len(prefix)]==prefix:
            print(char)


string=['car','cat', 'carry', 'fear','center']
prefix='ca'
prefic(string,prefix)

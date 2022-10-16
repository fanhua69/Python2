def reduce(function, iterable, inirializer=None):
    it=iter(iterable)
    if(inirializer is None):
        value = next (it)
    else:
        value = inirializer
        
    for ele in it:
        value = function(value , ele)
        
    return value
# Set() in python 

Sets in Python are unordered, the add method does add elements to the set in a specific order. However, this order is not guaranteed to be sorted in ascending order.

The specific order in which the elements are added to the set depends on the internal implementation of the set data structure in Python. In practice, the order in which elements are added to a set using the add method is often related to the order in which they were created, but this is not guaranteed.

Therefore, if you want to guarantee that the elements are sorted in ascending order.

Also, the add method in a set does not guarantee any specific order of the elements. While it often happens that the elements are stored in ascending order, this is not guaranteed by the Python language.

If we want it to be sorted properly then we should do like this = 

return sorted(list(mynumber))

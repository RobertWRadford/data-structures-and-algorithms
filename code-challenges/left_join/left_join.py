class HashTable(object):

    def __init__(self, length=4):
        # Initiate our array with empty values.
        self.length = length
        self.buckets = [None] * length
    
    def hash(self, key):
        """Get the index of our array for a specific string key"""
        if not isinstance(key, str):
            raise Exception(f'{key} must be a string in order to be hashed')

        return hash(key) % self.length
        
    def set(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)

        if self.buckets[index] is not None:
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for pair in self.buckets[index]:
                # If key is found, then update
                # its current value to the new value.
                if pair[0] == key:
                    pair[1] = value
                    break
            # If no breaks was hit in the for loop, it 
            # means that no existing key was found, 
            # so we can simply just add it to the end.
            self.buckets[index].append([key, value])
        else:
            # This index is empty. We should initiate 
            # a list and append our key-value-pair to it.
            self.buckets[index] = []
            self.buckets[index].append([key, value])
    
    def get(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.buckets[index] is None:
            return None
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            for pair in self.buckets[index]:
                if pair[0] == key:
                    return pair[1]
            # If no return was done during loop,
            # it means key didn't exist.
            return None

def left_join(table_one, table_two):

    word_list = []
    for bucket in table_one.buckets:
        if bucket is not None:
            for pair in bucket:
                word_list.append([pair[0], pair[1], table_two.get(pair[0])])
    return word_list
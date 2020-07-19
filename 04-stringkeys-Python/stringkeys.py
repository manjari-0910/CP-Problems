"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
        # Your code goes here
        hv=self.calculate_hash_value(string)
        if self.table[hv]==None:
            self.table[hv] = string
        else:
            while(self.table[hv] is None):
                hv+=1
            self.table[hv] = string
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        hv=self.calculate_hash_value(string)
        if self.table[hv] == string:
            return hv
        while hv<len(self.table):
            if self.table[hv] != string:
                hv+=1
            else:
                break
        if hv>len(self.table)-1:
            return -1
        if self.table[hv] == string:
            return hv
        pass

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        return ord(string[0])*100+ord(string[1])
        pass



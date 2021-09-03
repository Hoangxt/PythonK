# # str1 = "abcd"  # Unique
# # str2 = "aca"  # Unique
# import unittest


# def unique(str):
#     # Hint: Hash table => Dict: Key-Value
#     char_set = {}

#     for char in str:
#         if char in char_set:  # ki tu da co trong char_set => False
#             return False
#         char_set[char] = True
#     return True


# class Test(unittest.TestCase):
#     dataT = [('abcd', '12ascv45', 'ace', '', '12345asdf')]
#     dataF = [('asas', '123321', 'hoanggro')]

#     def Test_unique(self):
#         # true check
#         for test_case in self.dataT:
#             actualResult = unique(test_case)
#             self.assertTrue(actualResult)
#         # false check
#         for test_string in self.dataF:
#             actual = unique(test_string)
#             self.assertFalse(actual)


# if __name__ == "__main__":
#     unittest.main()

# O(N)
import unittest


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = {}
    for char in string:
        if char in char_set:
            # Char already found in string
            return False
        char_set[char] = True

    return True


class Test(unittest.TestCase):
    # unittest provides a base class, TestCase,
    # which may be used to create new test cases.
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
    # print(unique('abcd'))

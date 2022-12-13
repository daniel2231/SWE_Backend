from unittest.mock import patch
import unittest
import app.unittest_temp.code as code

def custom_function(file_name):
    with open(file_name, 'r') as file:
        return sum(1 for _ in file)

# 참조 https://wikidocs.net/16107
class CustomTests(unittest.TestCase):
    def test(self):
        file = open('./app/unittest_temp/input.txt', 'r')
        user_input = file.read().split('\n')
        # make user_input int
        if len(user_input) == 1:
            user_input = int(user_input[0])
        else:
            user_input = tuple(map(int, user_input))
        file.close()

        file = open('./app/unittest_temp/output.txt', 'r')
        right_ans = file.read().split('\n')
        # if its a string, dont convert to int

        if len(right_ans) == 1:
            right_ans = right_ans[0]
        else:
            right_ans = tuple(map(str, right_ans))

        # typeof user_input

        # map user input inside solution
        ans = code.solution(*user_input)

        self.assertEqual(ans, right_ans)

if __name__ == '__main__':
    unittest.main()
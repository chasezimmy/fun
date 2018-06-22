"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
import string


def ways_to_decode(alphabet, s):
    if len(s) == 0 or s[0] == '0':
        return 0
    prev, prev_prev = 1, 0
    for i in range(len(s)):
        cur = 0
        if s[i] != '0':
            cur = prev
        if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
            cur += prev_prev
        prev, prev_prev = cur, prev

        print(cur)

    return prev

alphabet = dict(zip(range(1,27),string.ascii_lowercase))
message = '111'

print(ways_to_decode(alphabet, message))

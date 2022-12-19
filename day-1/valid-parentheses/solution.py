class Solution:
    def isValid(self, string: str) -> bool:
        if len(string) < 2: return False

        _open = ['(', '[', '{']
        _close = [')', ']', '}']
        parens = []

        for s in string:
            if s in _open: parens.append(s)
            elif s in _close:
                i = _close.index(s)
                try:
                    pair = parens.pop()
                    if _open.index(pair) != i: return False

                # ie no open parentheses found (len(parens) == 0) or pair not in _open
                except:
                    return False
        
        return not(len(parens))

if __name__ == '__main__':

    test_cases = ["(){}}{"]

    sol = Solution()
    for case in test_cases:
        print(sol.isValid(case))
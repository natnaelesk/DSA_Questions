def swap_case(s):
    ans= ""
    for char in s:
        val = None
        if char.isalpha():
            if char.isupper():
                val = char.lower()
            else:
                val = char.upper()
        else:
            val = char
        ans += val
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
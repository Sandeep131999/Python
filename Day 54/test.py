def max_profit(prices) -> int:
    min_price = float('inf')
    # inf - means infinity
    max_profits = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profits = max(max_profits, price - min_price)
    return max_profits

# print(max_profit([7,1,5,8,9,6]))


def is_palindrome(s: str) -> bool:
    clean_inp = []
    reverse_inp = ""
    for char in s:
        if char.isalnum():
            clean_inp.append(char.lower())
    reverse_inp = clean_inp[::-1]
    if clean_inp == reverse_inp:
        return True
    else:
        return False


print(is_palindrome("0P"))
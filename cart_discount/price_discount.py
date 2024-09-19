def main():

    #print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    print(discount([10, 4, 20]))  # Expect this to print 4

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered three or more items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """
    if len(item_prices) < 3:
        return 0
    return min(item_prices)


    #pass  # todo replace this line with your code


if __name__ == '__main__':
    main()

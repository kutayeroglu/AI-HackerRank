if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    x = tuple(n for n in integer_list)
    print(hash(x))
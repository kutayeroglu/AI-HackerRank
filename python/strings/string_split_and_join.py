def split_and_join(line):
    # write your code here
    transformed_line = line.split(" ")
    transformed_line = "-".join(transformed_line)
    return transformed_line

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print(result)
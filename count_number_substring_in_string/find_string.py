def count_substring(string, sub_string):
    count=0
    i_count = 0
    length_substring = len(sub_string)
    idx = 0
    for char in string:
        if char != sub_string[idx]:
            i_count =0
            idx = 0
            continue
        if length_substring != 1:
            idx+=1
        i_count+=1

        if length_substring == i_count:
            idx=0
            i_count=0
            if sub_string[-1] == sub_string[0] and length_substring !=1:
                idx=1
                i_count=1
            count+=1
    # print(count)
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
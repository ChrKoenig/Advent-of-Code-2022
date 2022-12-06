def find_signal(stream, buffer_size):
    buffer = [c for c in stream[:buffer_size]]
    for i, c in enumerate(stream):
        buffer.pop(0)
        buffer.append(c)
        if(len(set(buffer)) == buffer_size):
            return i+1
    
    return -1

if __name__ == "__main__":
    data = open('data/data_12_06.txt', 'r').read().split('\n')[0]
    print(find_signal(data, 4))
    print(find_signal(data, 14))



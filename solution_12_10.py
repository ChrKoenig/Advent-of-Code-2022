if __name__ == "__main__":
    data = open('data/data_12_10.txt', 'r').read().split('\n')
    cycle = 0
    signal_strength = 0
    line = 0
    command = None
    register = 1
    crt_output = ""

    while line < len(data):
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength += cycle * register
        
        if register-1 <= cycle % 40 <= register+1:
            crt_output = crt_output + "#"
        else:
            crt_output = crt_output + "."
        if (cycle+1) % 40 == 0:
            crt_output = crt_output + "\n"

        if not command:
            command = data[line]
            if command == "noop":
                command = None
                line += 1
            cycle += 1
            continue

        x = command.split(" ")[1]
        register += int(x)
        line += 1
        command = None
        cycle += 1

    print(signal_strength)
    print(crt_output)
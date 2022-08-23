def convert_to_list(behav_file):
    """Extracts behavioral data from behav.out file
    captured by lisa systemtap module.

    :param behav_file: behav.out file path.
    """
    started = False
    syscalls = []
    processes = []
    files = []

    with open(behav_file) as f:
        line = f.readline()
        while line:
            if line.startswith('SYSCALL'):
                syscall = {
                    'execname': f.readline()[:-1],
                    'name': f.readline()[:-1],
                    'pid': f.readline()[:-1],
                    'arguments': f.readline()[:-1],
                    'return': f.readline()[:-1]
                }

                # ommit initial execve from help process
                if started:
                    syscalls.append(syscall)
                else:
                    started = True

            if line.startswith('PROCESS'):
                inner = f.readline()
                if not inner:
                    break

                pid, pid_parent = inner.strip().split(':')
                process = {
                    'pid': int(pid),
                    'parent': int(pid_parent)
                }
                processes.append(process)


            if line.startswith('OPENFILE'):
                inner = f.readline()
                if not inner:
                    break

                file = inner.strip('"\n')
                files.append(file)

            line = f.readline()
    print(type(syscalls))
    print(syscalls)
    print(processes)
    print(files)


convert_to_list(f'behav.out')
#print(f'behav.out')
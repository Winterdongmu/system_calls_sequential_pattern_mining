def _analyze_behavior(self, behav_file):
    """Extracts behavioral data from behav.out file
    captured by lisa systemtap module.

    :param behav_file: behav.out file path.
    """
    started = False

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
                    self._syscalls.append(syscall)
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
                self._processes.append(process)

            if line.startswith('OPENFILE'):
                inner = f.readline()
                if not inner:
                    break

                file = inner.strip('"\n')
                self._files.append(file)

            line = f.readline()


_analyze_behavior(f'{self._file.data_dir}/behav.out')
def convert(s):
    for i in ['B', 'KB', 'MB', 'GB']:
        if s > 1024:
            s /= 1024
        else:
            size_memory = str(float("{:.2f}".format(s))) + i
            break
    return size_memory


def path(s):
    s = s.replace('/', '\\')
    return s

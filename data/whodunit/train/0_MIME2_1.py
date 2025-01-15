N, Q = map(int, input().split())
media_types = {input().split()[0]: input().split()[1] for _ in range(N)}
for _ in range(Q):
    file_name = input().strip()
    ext = file_name.split('.')[-1] if '.' in file_name else None
    print(media_types[ext] if ext in media_types else "unknown")
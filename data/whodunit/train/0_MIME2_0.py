N, Q = map(int, input().split())
media_types = {}
for _ in range(N):
    ext, media = input().split()
    media_types[ext] = media
for _ in range(Q):
    file_name = input().strip()
    if '.' in file_name:
        ext = file_name.split('.')[-1]
        print(media_types.get(ext, "unknown"))
    else:
        print("unknown")
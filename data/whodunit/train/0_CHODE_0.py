T = int(input().strip())
for _ in range(T):
    freq_seq = input().strip()
    enc_text = input().strip()
    freq_seq_sorted = sorted(freq_seq)
    enc_text_freq = sorted(list(set(enc_text.lower())), key=enc_text.lower().count)
    mapping = dict(zip(enc_text_freq, freq_seq_sorted))
    dec_text = ''
    for char in enc_text:
        if char.isalpha():
            if char.isupper():
                dec_text += mapping[char.lower()].upper()
            else:
                dec_text += mapping[char]
        else:
            dec_text += char
    print(dec_text)
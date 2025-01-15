from collections import Counter

T = int(input().strip())
for _ in range(T):
    freq_seq = input().strip()
    enc_text = input().strip()
    freq_seq_sorted = sorted(freq_seq)
    enc_text_freq = sorted(list(set(enc_text.lower())), key=enc_text.lower().count)
    mapping = {enc: dec for enc, dec in zip(enc_text_freq, freq_seq_sorted)}
    dec_text = ''.join([mapping[char.lower()].upper() if char.isupper() else mapping[char] if char.isalpha() else char for char in enc_text])
    print(dec_text)
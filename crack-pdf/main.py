import pikepdf
from tqdm import tqdm

passw = [ line.strip() for line in open("wordlist.txt") ]

for password in tqdm(passw, "Decrypting PDF"):
    try:
        with pikepdf.open("example.pdf", password=password) as pdf:
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
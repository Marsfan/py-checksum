import hashlib
import argparse

parser = argparse.ArgumentParser(description="Calculates a checksum hash for a file and compares it to a known checksum")

parser.add_argument("-a", "--algorithms", help="choose between md5, sha1, sha224, sha256, and sha512. \nIf no option is present, defaults to sha1", default="sha1")
parser.add_argument("-v", "--verbose", action='store_true', help="list the calculated and given checksums for manual double checking", default=False)
args = parser.parse_args()

file = "Null";

def md5():
    return hashlib.md5(open(file, 'rb').read()).hexdigest()

def sha1():
    return hashlib.sha1(open(file, 'rb').read()).hexdigest()

def sha224():
    return hashlib.sha224(open(file, 'rb').read()).hexdigest()

def sha256():
     return hashlib.sha256(open(file, 'rb').read()).hexdigest()

def sha512():
    return hashlib.sha512(open(file, 'rb').read()).hexdigest()

def compute(argument):
    computer = {
        "md5": md5,
        "sha1": sha1,
        "sha224": sha224,
        "sha256": sha256,
        "sha512": sha512,
    }
    func = computer.get(argument, "error")
    return func()

def main():
    global file
    print("Using %s checksum" % args.algorithms)
    file = input("Enter file to check: ")
    checksum = input("Enter known checksum: ")
    checksum = checksum.upper()
    file = file.replace(" ", "")
    calculatedChecksum = compute(args.algorithms)
    checksum = checksum.replace(" ", "")
    calculatedChecksum = calculatedChecksum.upper()
    if args.verbose:
        print(calculatedChecksum)
        print(checksum)
    if calculatedChecksum == checksum:
        print("Checksum matches")
    else:
        print("Checksum does not match, file integrity may be compromised")


main()
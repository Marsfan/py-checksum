# py-checksum

This tool allows a user to enter a file and its supposed checksum value, and will then compute the hash for the file, checking if it matches the supposed value.

It takes two arguments:

-a, --algorithms: selects the hash algorith out of  md5, sha1, sha224, sha256, and sha512, it defaults to sha1
-v, --verbose: default false, if true, it lists the given and calculated checksums for manual checking

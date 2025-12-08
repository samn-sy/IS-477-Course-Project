# this code takes in the original datasets from the City of Chicago and New York City and generates their sha256 hash?
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash string value in chunks
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

chicago_file_path = "../Original Datasets/11.7_Chicago_Food_Inspections.csv"
sha256_chicago = calculate_sha256(chicago_file_path)
assert(sha256_chicago == "16114149b50f3cb7e3c287f834110f5449c974e17580ba9088e606cfad367b76")
print(f"SHA-256 for {chicago_file_path}: {sha256_chicago}")

nyc_file_path = "../Original Datasets/11.7_New_York_City_Inspections.csv"
sha256_nyc = calculate_sha256(nyc_file_path)
assert(sha256_nyc == "21b168147714875be78c2fff248ef91137935c600e7db66666c44c285b6a4665")
print(f"SHA-256 for {nyc_file_path}: {sha256_nyc}")
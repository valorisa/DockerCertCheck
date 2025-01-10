import subprocess
import os
import sys
import datetime
import shutil
import tempfile

def check_dependencies():
    try:
        subprocess.run(["which", "codesign"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("codesign is not installed")
        sys.exit(1)

    try:
        subprocess.run(["which", "openssl"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("openssl is not installed")
        sys.exit(1)

def extract_certificates(binary_file):
    temp_dir = tempfile.mkdtemp(prefix="docker-desktop_cert_check_")
    try:
        result = subprocess.run(
            ["codesign", "-d", "--extract-certificates", binary_file],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        if result.returncode != 0:
            print(f"Failed to extract certificates from {binary_file}")
            sys.exit(1)

        certificate_details = subprocess.check_output(
            ["openssl", "x509", "-noout", "-serial", "-subject", "-issuer", "-dates", "-in", "codesign0"],
            text=True
        )

        return certificate_details, os.path.basename(binary_file)
    finally:
        shutil.rmtree(temp_dir)

def print_certificate_details(certificate_details, binary_name):
    print("-----------------------------------------------------------------")
    print(f"Certificate details for {binary_name}:")
    for line in certificate_details.splitlines():
        print(f" {line}")
    print("-----------------------------------------------------------------")
    print()

def check_certificate_serial(certificate_details, binary_name):
    if "serial=1316FD127D9A5715176591F85FFC3C66" in certificate_details:
        print(f"{binary_name} is signed with a revoked certificate")
        print("please download and install a new version of Docker Desktop")
        sys.exit(1)
    elif "serial=3EC22E699630083A" in certificate_details:
        print(f"{binary_name} is signed with a correct certificate")
        sys.exit(0)
    else:
        print(f"{binary_name} is signed with an unknown certificate")
        print("please download and install a new version of Docker Desktop")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        binary_file = "/Applications/Docker.app/Contents/Library/LaunchServices/com.docker.vmnetd"
    else:
        binary_file = sys.argv[1]

    check_dependencies()
    certificate_details, binary_name = extract_certificates(binary_file)
    print_certificate_details(certificate_details, binary_name)
    check_certificate_serial(certificate_details, binary_name)

if __name__ == "__main__":
    main()


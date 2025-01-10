# Docker Cert Check

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![GitHub Issues](https://img.shields.io/github/issues/valorisa/DockerCertCheck.svg)](https://github.com/valorisa/DockerCertCheck/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/valorisa/DockerCertCheck.svg)](https://github.com/valorisa/DockerCertCheck/pulls)

Docker Cert Check is a tool to verify the signature certificates of Docker Desktop binary files.

## Workaround Solution

Diagnose your Docker Desktop installation

To determine if you need to download and reinstall Docker Desktop, please follow the steps below.

1. Download the attached  file check.sh.txt, rename it to check.sh , and set the executable flag with . (Caution: it is never a good idea to just run shell scripts downloaded from the internet. Please take a moment to review the script before executing it.)
2. Execute the following command to verify the binary in your Docker.app application bundle. The script will exit with 0 if the certificate was correctly verified:
   ```sh
   $ ./check.sh /Applications/Docker.app/Contents/Library/LaunchServices/com.docker.vmnetd
   -----------------------------------------------------------------
   Certificate details for com.docker.vmnetd:
    serial=3EC22E699630083A
    subject=UID=9BNSXJN65R
     CN=Developer ID Application: Docker Inc (9BNSXJN65R)
     OU=9BNSXJN65R
     O=Docker Inc
     C=US
    issuer=CN=Developer ID Certification Authority
     OU=Apple Certification Authority
     O=Apple Inc.
     C=US
    notBefore=Oct  2 16:46:37 2024 GMT
    notAfter=Feb  1 22:12:15 2027 GMT
   -----------------------------------------------------------------

   com.docker.vmnetd is signed with a correct certificate
   ```
3. You can also verify files in the `/Library/PrivilegedHelperTools` folder with:
   ```sh
   ./check.sh /Library/PrivilegedHelperTools/com.docker.vmnetd
   ./check.sh /Library/PrivilegedHelperTools/com.docker.socket
   ```

If any of the above commands fail to verify the certificate, you need to download and reinstall Docker Desktop.

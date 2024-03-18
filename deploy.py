import os
import ftputil

def ftp_upload(hostname, username, password, remote_dir, local_dir):
    with ftputil.FTPHost(hostname, username, password) as host:
        for root, dirs, files in os.walk(local_dir):
            for filename in files:
                local_path = os.path.join(root, filename)
                remote_path = os.path.join(remote_dir, os.path.relpath(local_path, local_dir))
                host.upload(local_path, remote_path)

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) != 5:
        print("Usage: deploy.py <hostname> <username> <password> <remote_dir> <local_dir>")
        sys.exit(1)
    ftp_upload(*args)

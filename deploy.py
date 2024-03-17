import ftputil

def ftp_upload(hostname, username, password, remote_dir, local_dir):
    with ftputil.FTPHost(hostname, username, password) as host:
        host.makedirs(remote_dir, recreate=True)
        host.upload_if_newer(local_dir, remote_dir)

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) != 5:
        print("Usage: deploy.py <hostname> <username> <password> <remote_dir> <local_dir>")
        sys.exit(1)
    ftp_upload(*args)

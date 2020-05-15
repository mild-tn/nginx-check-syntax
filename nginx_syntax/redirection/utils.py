import subprocess

def check_nginx_syntax():
    command = ["docker", "run", "--rm", "-t", "-a", "stdout", "--name", "my-nginx", "-v", "hello.conf:/etc/nginx/:ro", "nginx:latest", "nginx", "-c", "/etc/nginx/nginx.conf", "-t"]
    result = subprocess.run(command)
    return result


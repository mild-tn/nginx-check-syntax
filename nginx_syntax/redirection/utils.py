import subprocess
import os

dirname = os.path.dirname(__file__)

def check_nginx_syntax(path_dir):
    container_path = ':/etc/nginx/conf.d/default.conf:ro'
    nginx_volume = path_dir + container_path
    command = ["docker", "run", "--rm", "-t", "-a", "stdout", "--name", "my-nginx", "-v", nginx_volume, "nginx:latest", "nginx", "-c", "/etc/nginx/nginx.conf", "-t"]
    result = subprocess.run(command)
    return result

def create_nginx_file(domain, rule, redirection_to, is_permanent, is_active, is_http_to_https):
    file_name = domain + '.conf'
    path_dir = os.path.join(dirname, '../../nginx-redirect-config/' + file_name)
    create_nginx = open(path_dir, 'x')
    nginx_check_syntax = check_nginx_syntax(path_dir)
    print (nginx_check_syntax.returncode)

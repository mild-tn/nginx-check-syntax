import subprocess
import os

dirname = os.path.dirname(__file__)

def check_nginx_syntax(path_dir, file_name):
    container_path = ':/etc/nginx/conf.d/default.conf:ro'
    continer_path_2 = ':/etc/nginx/redirect/' + file_name
    nginx_volume = path_dir + '../conf.d/default.conf' + container_path
    nginx_volume_2 = path_dir + file_name + continer_path_2
    command = [
        "docker", "run", "--rm", "-t", "-a", "stdout", "--name", "my-nginx", "-v", 
        nginx_volume, "-v", nginx_volume_2, "nginx:latest",
        "nginx", "-c", "/etc/nginx/nginx.conf", "-t"]
    result = subprocess.run(command, capture_output=True)
    return result


def create_nginx_file(domain, rule, redirection_to, is_permanent, is_active, is_http_to_https):
    file_name = domain + '.conf'
    path_dir = os.path.join(dirname, '../../nginx-redirect-config/redirect/')
    create_nginx = open(path_dir + file_name, 'a')
    create_nginx.write('rewrite ' + rule + ' ' + redirection_to + ' permanent;')
    create_nginx.close()
    nginx_check_syntax = check_nginx_syntax(path_dir, file_name)
    check_status_nginx_syntax = check_status(nginx_check_syntax.stdout.decode("utf-8"))
    os.remove(path_dir + file_name)


def check_status(nginx_status):
    message = "nginx: the configuration file /etc/nginx/nginx.conf syntax is ok\r\n"
    message += "nginx: configuration file /etc/nginx/nginx.conf test is successful\r\n"
    if nginx_status == message:
        print("Test is successful")
        return "Successful"
    else:
        print(nginx_status)
        return nginx_status

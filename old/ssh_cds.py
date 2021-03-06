import paramiko
# import socket, fcntl, struct


def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
    # print stdout.read()
    output = stdout.read()
    s.close()
    return output


def cds_init(querycmd, execmd, ip, local_ip):
    hostname = ip
    port = 22
    username = 'root'
    password = 'FxData!Cds@2016_'
    query_result = sshclient_execmd(hostname, port, username, password, querycmd)
    iptable_restart = 'service iptables restart'
    if ('-A INPUT -s %s -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT') % local_ip not in query_result:
        sshclient_execmd(hostname, port, username, password, execmd)
        sshclient_execmd(hostname, port, username, password, iptable_restart)


# def get_ip(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])


if __name__ == "__main__":
    ipaddr = ['192.168.1.104']
    local_ip = '192.168.0.56'#get_ip('br100')
    print local_ip
    for ip in ipaddr:
        print ip
        querycmd = "cat /etc/sysconfig/iptables"
        execmd = "sed -i '6i -A INPUT -s %s -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT' /etc/sysconfig/iptables" % local_ip
        cds_init(querycmd, execmd, ip, local_ip)

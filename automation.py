import subprocess
import sys
import os
import shutil
from jinja2 import Environment, FileSystemLoader
service_name = "bind9"
status_output = subprocess.run(["systemctl", "status", service_name], capture_output=True, text=True)
if not "Active: active" in status_output.stdout:
    print(f"The {service_name} service is not installed or not running.")
    sys.exit(1)

# service_name = "dnsutils"
# status_output = subprocess.run(["systemctl", "status", service_name], capture_output=True, text=True)
# if not "Active: active" in status_output.stdout:
#     print(f"The {service_name} service is not installed or not running.")
#     sys.exit(1)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('named.conf.options.tpl')
data = {
    'forwarder_dns': '8.8.8.8'
}
output = template.render(data)

with open('named.conf.options.out', 'w') as f:
    f.write(output)

new_filename = 'named.conf.options'
shutil.move('/home/rafid/custom_dns/named.conf.options.out', '/etc/bind' + '/' + new_filename)

subprocess.call(['sudo', 'systemctl', 'restart', 'bind9.service'])

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('named.conf.local.tpl')
data = {
    'domain': 'vivaltd.com',
    'first_three_octets_of_ip': '8.168.192',
    'first_octet_of_ip': '192'
}
domain = data['domain']
FIRST_OCTET_OF_IP = data['first_octet_of_ip']
output = template.render(data)

with open('named.conf.local.out', 'w') as f:
    f.write(output)

new_filename = 'named.conf.local'
shutil.move('/home/rafid/custom_dns/named.conf.local.out', '/etc/bind' + '/' + new_filename)

# new_filename = 'named.conf.local'
# shutil.move('/home/rafid/custom_dns/named.conf.local.out', '/etc/bind' + '/' + new_filename)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("db.domain.com.tpl")

data = {
    'fqdn': 'vivaltd.com.',
     'email_address': 'hmnrafid999.gmail.com.',
     'ip_address': '192.168.8.9'
}
output = template.render(data)
ip = data['ip_address']
domain = data['fqdn'][:-1]
# print(domain)

file = open('db.{}out'.format(domain), 'w')

with open('db.{}out'.format(domain), 'w') as f:
    f.write(output)

with open('db.{}out'.format(domain), 'a') as f:
    f.write(f'\nns      IN      A       {ip}\n')
    f.write(f'mun     IN      A       {ip}\n')

filename = 'db.{}out'.format(domain)
new_filename = 'db.{}'.format(domain)
shutil.move("/home/rafid/custom_dns/"+filename, '/etc/bind' + '/' + new_filename)

subprocess.run(['sudo', 'systemctl', 'restart', 'bind9.service'])

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("db.tpl")

data = {
    'fqdn': 'vivaltd.com.',
    'email_address': 'hmnrafid999.gmail.com.',
}
output = template.render(data)
# file = open('db.{}'.format(FIRST_OCTET_OF_IP), 'w')
with open('db.{}'.format(FIRST_OCTET_OF_IP), 'w') as f:
    f.write(output)

filename = 'db.{}'.format(FIRST_OCTET_OF_IP)
# print(filename)

if os.path.exists('/etc/bind/' + filename):
    os.remove('/etc/bind/' + filename)
shutil.move("/home/rafid/custom_dns/"+filename, '/etc/bind' + '/' + filename)

subprocess.run(['sudo', 'systemctl', 'restart', 'bind9.service'])
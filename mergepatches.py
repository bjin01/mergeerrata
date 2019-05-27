#!/usr/bin/python
import  argparse,  getpass,  textwrap
import xmlrpclib
from time import sleep
from datetime import datetime,  timedelta

class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()

        setattr(namespace, self.dest, values)

def checkChannels( clabel ):
    "This function checks if the given channel label is valid and exists."
    x = 0
    mylist = session_client.channel.listAllChannels(session_key)
    for m in mylist:
        if m['label'] in clabel:
            x = 1
            print("OK, the channel is valid: %s" %(clabel))
    if x == 0:
        print("The given channel label is wrong or the channel doesn't exists. exit...")
        exit()
    return
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(prog='PROG', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
This scripts merges 'security advisory' errata and the respective packages from a given channel to an given target channel. 

Sample command:

    python mergepatches.py -s sumahost.sample.com -u sumauser -p password -sc "prod-sles12-sp4-updates-x86_64" -tc "target_channel_name" -fd "11 2 2019" -td "11 5 2019" \n \

''')) 
parser.add_argument("-x", "--patch-it", action="store_true")
parser.add_argument("-s", "--server", help="Enter your suse manager host address e.g. myserver.abd.domain",  default='localhost',  required=True)
parser.add_argument("-u", "--username", help="Enter your suse manager loginid e.g. admin ", default='admin',  required=True)
parser.add_argument('-p', action=Password, nargs='?', dest='password', help='Enter your password',  required=True)
parser.add_argument("-sc", "--source_channel", help="Enter a valid source channel label name. e.g. dev-sles12sp3_x86-64 ",  required=True)
parser.add_argument("-tc", "--target_channel", help="Enter a valid target channel label name. e.g. test-sles12sp3_x86-64 ",  required=True)
parser.add_argument("-fd", "--from_date", help="Enter a valid from_date. e.g. 13. Mar, 2017 ",  required=True)
parser.add_argument("-td", "--to_date", help="Enter a valid to_date. e.g. 19. Sept, 2018 ",  required=True)
args = parser.parse_args()

print(args.from_date)
a = 0
MANAGER_URL = "http://"+ args.server+"/rpc/api"
MANAGER_LOGIN = args.username
MANAGER_PASSWORD = args.password
s_channel = args.source_channel
t_channel = args.target_channel
session_client = xmlrpclib.Server(MANAGER_URL, verbose=0)
session_key = session_client.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)
today = datetime.today()
dateTimeObj = datetime.now()
date11 = datetime.strptime(args.from_date, "%d %m %Y")
date21 = datetime.strptime(args.to_date, "%d %m %Y")
 
suma_end_date = xmlrpclib.DateTime(date21)
suma_start_date = xmlrpclib.DateTime(date11)

checkChannels(s_channel)
checkChannels(t_channel)

advisory = [ "Security Advisory"]
advisorynames = []
target_packagelist = []

source_list = session_client.channel.software.listErrata(session_key, s_channel, suma_start_date,  suma_end_date)
for s in source_list:
    if s['advisory_type'] in "Security Advisory":
        advisorynames.append(s['advisory_name'])
        packagelist = session_client.errata.listPackages(session_key,  s['advisory_name'])
        for p in packagelist:
            target_packagelist.append(p['id'])
print(advisorynames)        

session_client.channel.software.addPackages(session_key, t_channel, target_packagelist)
target_package_list = session_client.errata.clone(session_key, t_channel, advisorynames)
sleep(5)
final_pkg_list = session_client.channel.software.listAllPackages(session_key, t_channel)
print("there are %d: packages in the channel." % len(final_pkg_list))
target_errata_list = session_client.channel.software.listErrata(session_key, t_channel, suma_start_date,  suma_end_date)
for i in target_errata_list:
    if i['advisory_type'] in "Security Advisory":
        a += 1
print("/nThere are %s security patches in %s." %(a,  t_channel))
session_client.auth.logout(session_key)

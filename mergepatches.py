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

parser = argparse.ArgumentParser()
#parser.add_argument("-v", "--verbosity", action="count", default=0)
parser = argparse.ArgumentParser(prog='PROG', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
This scripts runs service pack migration for given base channel. 

Sample command:

              python patchsystems.py -s bjsuma.bo2go.home -u bjin -p suse1234 -g DEV-SLES12SP3 \n \

If -x is not specified the SP Migration is always a dryRun.
Check Job status of the system if dryrun was successful before run the above command with -x specified. ''')) 
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
#print('Current Timestamp : ', timestampStr)
 
suma_end_date = xmlrpclib.DateTime(date21)
suma_start_date = xmlrpclib.DateTime(date11)

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

#print(target_packagelist)
#print(len(target_packagelist))
#target_list = session_client.channel.software.mergeErrata(session_key, s_channel, t_channel,  advisorynames)
session_client.channel.software.addPackages(session_key, t_channel, target_packagelist)
target_package_list = session_client.errata.clone(session_key, t_channel, advisorynames)
sleep(5)
final_pkg_list = session_client.channel.software.listAllPackages(session_key, t_channel)
print("there are %d: packages in the channel." % len(final_pkg_list))
target_errata_list = session_client.channel.software.listErrata(session_key, t_channel, suma_start_date,  suma_end_date)
for i in target_errata_list:
    if i['advisory_type'] in "Security Advisory":
        print(i)
        a += 1
print("/nThere are %s security patches in %s." %(a,  t_channel))

session_client.auth.logout(session_key)

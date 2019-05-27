# mergeerrata
merge errata and packages from source channel to target channel

_I did it again :-)_
## merge errata and packages (security advisory)
Some customers need a simple script to just add certain errata and their packages from channal A to channel B. So this script is all about it.

### Usage:

```python mergepatches.py -s sumahost.sample.com -u sumauser -p password -sc "prod-sles12-sp4-updates-x86_64" -tc "target_channel_name" -fd "11 2 2019" -td "11 5 2019"```
### Help:
```
# python mergepatches.py -h
usage: PROG [-h] [-x] -s SERVER -u USERNAME -p [PASSWORD] -sc SOURCE_CHANNEL
            -tc TARGET_CHANNEL -fd FROM_DATE -td TO_DATE

This scripts merges 'security advisory' errata and the respective packages from a given channel to an given target channel. 

Sample command:

    python mergepatches.py -s sumahost.sample.com -u sumauser -p password -sc "prod-sles12-sp4-updates-x86_64" -tc "target_channel_name" -fd "11 2 2019" -td "11 5 2019" 

optional arguments:
  -h, --help            show this help message and exit
  -x, --patch-it
  -s SERVER, --server SERVER
                        Enter your suse manager host address e.g.
                        myserver.abd.domain
  -u USERNAME, --username USERNAME
                        Enter your suse manager loginid e.g. admin
  -p [PASSWORD]         Enter your password
  -sc SOURCE_CHANNEL, --source_channel SOURCE_CHANNEL
                        Enter a valid source channel label name. e.g. dev-
                        sles12sp3_x86-64
  -tc TARGET_CHANNEL, --target_channel TARGET_CHANNEL
                        Enter a valid target channel label name. e.g. test-
                        sles12sp3_x86-64
  -fd FROM_DATE, --from_date FROM_DATE
                        Enter a valid from_date. e.g. 13.3.2017
  -td TO_DATE, --to_date TO_DATE
                        Enter a valid to_date. e.g. 19.9.2018
 ```
### sample output:
```
# python mergepatches.py -s localhost -u admin -p suse1234 -sc "prod-sles12-sp4-updates-x86_64" -tc "mypatches" -fd "11.2.2016" -td "11.5.2019"
OK, the channel is valid: prod-sles12-sp4-updates-x86_64
OK, the channel is valid: mypatches
['CL-SUSE-12-SP4-2019-49', 'CL-SUSE-12-SP4-2018-2520', 'CL-SUSE-12-SP4-2018-2916', 'CL-SUSE-12-SP4-2018-2802', 'CL-SUSE-12-SP4-2018-3062', 'CL-SUSE-12-SP4-2018-2662', 'CL-SUSE-12-SP4-2018-2894', 'CL-SUSE-12-SP4-2018-3067', 'CL-SUSE-12-SP4-2018-2946', 'CL-SUSE-12-SP4-2018-1697', 'CL-SUSE-12-SP4-2018-2783', 'CL-SUSE-12-SP4-2019-222', 'CL-SUSE-12-SP4-2019-196', 'CL-SUSE-12-SP4-2019-19', 'CL-SUSE-12-SP4-2018-2991', 'CL-SUSE-12-SP4-2019-3', 'CL-SUSE-12-SP4-2018-3045', 'CL-SUSE-12-SP4-2018-2947', 'CL-SUSE-12-SP4-2019-111', 'CL-SUSE-12-SP4-2018-2549', 'CL-SUSE-12-SP4-2018-2989', 'CL-SUSE-12-SP4-2018-2868', 'CL-SUSE-12-SP4-2019-146', 'CL-SUSE-12-SP4-2018-2917', 'CL-SUSE-12-SP4-2019-284', 'CL-SUSE-12-SP4-2019-96', 'CL-SUSE-12-SP4-2019-243', 'CL-SUSE-12-SP4-2019-179', 'CL-SUSE-12-SP4-2018-3022', 'CL-SUSE-12-SP4-2018-2803', 'CL-SUSE-12-SP4-2018-2659', 'CL-SUSE-12-SP4-2018-2594', 'CL-SUSE-12-SP4-2019-128', 'CL-SUSE-12-SP4-2019-138', 'CL-SUSE-12-SP4-2019-209', 'CL-SUSE-12-SP4-2018-2846', 'CL-SUSE-12-SP4-2018-2663', 'CL-SUSE-12-SP4-2019-59', 'CL-SUSE-12-SP4-2019-132', 'CL-SUSE-12-SP4-2019-60', 'CL-SUSE-12-SP4-2018-2582', 'CL-SUSE-12-SP4-2018-2564', 'CL-SUSE-12-SP4-2019-135', 'CL-SUSE-12-SP4-2019-144', 'CL-SUSE-12-SP4-2018-2782', 'CL-SUSE-12-SP4-2019-57', 'CL-SUSE-12-SP4-2018-2542', 'CL-SUSE-12-SP4-2018-2977', 'CL-SUSE-12-SP4-2018-2548', 'CL-SUSE-12-SP4-2018-2987', 'CL-SUSE-12-SP4-2018-2772', 'CL-SUSE-12-SP4-2019-119', 'CL-SUSE-12-SP4-2018-2541', 'CL-SUSE-12-SP4-2019-241', 'CL-SUSE-12-SP4-2018-2812', 'CL-SUSE-12-SP4-2018-2824', 'CL-SUSE-12-SP4-2018-2983', 'CL-SUSE-12-SP4-2018-2766', 'CL-SUSE-12-SP4-2018-2886', 'CL-SUSE-12-SP4-2018-2648', 'CL-SUSE-12-SP4-2018-2885', 'CL-SUSE-12-SP4-2019-313', 'CL-SUSE-12-SP4-2019-336', 'CL-SUSE-12-SP4-2019-339']
there are 345: packages in the channel.
/nThere are 64 security patches in mypatches.
```

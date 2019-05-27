# mergeerrata
merge errata and packages from source channel to target channel

I did it again :-)

Some customers need a simple script to just add certain errata and their packages from channal A to channel B. So this script is all about it.

Usage:

```python mergepatches.py -s sumahost.sample.com -u sumauser -p password -sc "prod-sles12-sp4-updates-x86_64" -tc "target_channel_name" -fd "11 2 2019" -td "11 5 2019"```

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

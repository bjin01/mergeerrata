# mergeerrata
merge errata and packages from source channel to target channel

I did it again :-)

Some customers need a simple script to just add certain errata and their packages from channal A to channel B. So this script is all about it.

Usage:

```python mergepatches.py -s sumahost.sample.com -u sumauser -p password -sc "prod-sles12-sp4-updates-x86_64" -tc "target_channel_name" -fd "11 2 2019" -td "11 5 2019"```


```
When used in conjunction with indexes.conf's coldToFrozenScript, this script discards replicated buckets and moves normal buckets 
to $SPLUNK_HOME/frozenData and will attempt to create $SPLUNK_HOME/frozenData if not exists.  Enabling this script can be done per index or globally but
does require a restart of SplunkD. 

Please see indexes.conf.spec for more details.
```
import sys, os, gzip, shutil, subprocess, random
ARCHIVE_DIR = os.path.join(os.getenv('SPLUNK_HOME'), 'frozenData') #$SPLUNK_HOME/frozenData
#ARCHIVE_DIR = os.path.join('opt',frozenData') #/opt/frozenData

def archiveBucket(base, files):
    print 'Archiving bucket: ' + base
    for f in files:
        full = os.path.join(base, f)
        if os.path.isfile(full):
            os.remove(full)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: python cold2frozen.py <bucket_path>')

    if not os.path.isdir(ARCHIVE_DIR):
        try:
            os.mkdir(ARCHIVE_DIR)
        except OSError:
            sys.stderr.write("mkdir warning: Directory '" + ARCHIVE_DIR + "' already exists\n")

    bucket = sys.argv[1]
    if not os.path.isdir(bucket):
        sys.exit('Given bucket is not a valid directory: ' + bucket)

    rawdatadir = os.path.join(bucket, 'rawdata')
    if not os.path.isdir(rawdatadir):
        sys.exit('No rawdata directory, given bucket is likely invalid: ' + bucket)

    files = os.listdir(bucket)
    journal = os.path.join(rawdatadir, 'journal.gz')
    if os.path.isfile(journal):
        archiveBucket(bucket, files)
    else:
        sys.exit('No journal file found, bucket invalid:' + bucket)

    if bucket.endswith('/'):
        bucket = bucket[:-1]

    if "rb_" in bucket:
        #replicated bucket, so quit / do nothing
        quit()

    indexname = os.path.basename(os.path.dirname(os.path.dirname(bucket)))
    destdir = os.path.join(ARCHIVE_DIR, indexname, os.path.basename(bucket))

    while os.path.isdir(destdir):
        print 'Warning: This bucket already exists in the archive directory'
        print 'Adding a random extension to this directory...'
        destdir += '.' + str(random.randrange(10))

    shutil.copytree(bucket, destdir)

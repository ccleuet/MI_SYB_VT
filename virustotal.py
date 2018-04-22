import hashlib
import os
import wget

def main():
  files = [f for f in os.listdir('.') if os.path.isfile(f)]
  for f in files:
   print "File : "+ f
   hash_f=hashlib.sha256(f).hexdigest()
   url="https://www.virustotal.com/latest-scan/"+hash_f
   wget.download(url);
   print '\n'
   response=open(hash_f).read()
   if 'Detection ratio:' in response:
    index=response.find('Detection ratio:')
    print 'Detection ratio : ' + response[index+92:index+100]
   else:
    print "The file is not in VirusTotal database."
   print " -----"
   os.remove(hash_f);


main()

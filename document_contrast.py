#-*-coding:utf-8-*-
import os, time,difflib
AFILES = []
BFILES = []
COMMON = []
def getPrettyTime(state):
  return time.strftime('%y-%m-%d %H:%M:%S', time.localtime(state.st_mtime))

def dirCompare(apath,bpath):
  afiles = []
  bfiles = []
  for root, dirs , files in os.walk(apath):
    for f in files:
      afiles.append(root + "\\" + f)
  for root, dirs , files in os.walk(bpath):
    for f in files:
      bfiles.append(root + "\\" + f)
  apathlen = len(apath)
  aafiles = []
  for f in afiles:
    aafiles.append(f[apathlen:])
  bpathlen = len(bpath)
  bbfiles = []
  for f in bfiles:
    bbfiles.append(f[bpathlen:])
  afiles = aafiles
  bfiles = bbfiles
  setA = set(afiles)
  setB = set(bfiles)
  print(str(len(setA)))
  print(str(len(setB)))
  commonfiles = setA & setB
  print ("===============File with different size in '", apath, "' and '", bpath, "'===============")
  with open(os.getcwd()+'diff.txt','w') as di:
    print ("===============File with different size in '", apath, "' and '", bpath, "'===============")
  for f in sorted(commonfiles):
    sA=os.path.getsize(apath + "\\" + f)
    print sA
    sB=os.path.getsize(bpath + "\\" + f)
    print sB
    if sA==sB:
      pass
      print (f + "\t\t" + getPrettyTime(os.stat(apath + "\\" + f)) + "\t\t" + getPrettyTime(os.stat(bpath + "\\" + f)))
      print("in sa=sb")
      print(os.getcwd())
      saf=[]
      sbf=[]
      sAfile=open(apath + "\\" + f)
      iter_f=iter(sAfile)
      for line in iter_f:
        saf.append(line)
      sAfile.close()
      sBfile=open(bpath + "\\" + f)
      iter_fb=iter(sBfile)
      for line in iter_fb:
        sbf.append(line)
      sBfile.close()
      saf1=sorted(saf)
      sbf1=sorted(sbf)
      if(len(saf1)!=len(sbf1)):
        with open(os.getcwd()+'\\comment_diff.txt','a') as fp:
          print(os.getcwd())
          fp.write(apath + "\\" + f+" lines size not equal "+bpath + "\\" + f+'\n')
      else:
        for i in range(len(saf1)):
          if(saf1[i]!=sbf1[i]):
            print('into commont')
            with open(os.getcwd()+'\\comment_diff.txt','a') as fp1:
              fp1.write(apath + "\\" + f+" content not equal "+bpath + "\\" + f+'\n')
              break
    else:
      with open (os.getcwd()+'\\diff.txt','a') as di:
        di.write("File Name=%s  EEresource file size:%d  != SVN file size:%d" %(f,sA,sB)+'\n')
      print ("File Name=%s  EEresource file size:%d  != SVN file size:%d" %(f,sA,sB))
  onlyFiles = setA ^ setB
  aonlyFiles = []
  bonlyFiles = []
  for of in onlyFiles:
    if of in afiles:
      aonlyFiles.append(of)
    elif of in bfiles:
      bonlyFiles.append(of)
  for of in sorted(aonlyFiles):
    with open (os.getcwd()+'\\EEonly.txt','a') as ee:
      ee.write(of+'\n')
  for of in sorted(bonlyFiles):
    with open (os.getcwd()+'\\svnonly.txt','a') as svn:
      svn.write(of+'\n')
if __name__ == '__main__':
  FolderEE = 'D:\\tests\\'
  FolderSVN = 'D:\\test\\'
  dirCompare(FolderEE, FolderSVN)
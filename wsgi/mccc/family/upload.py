import subprocess,os,io
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile

mdbexport=os.environ['OPENSHIFT_RUNTIME_DIR']+"/libs/bin/mdb-export"
cmd = [mdbexport, '-N', 'MCCC','-I', 'mysql', 'family.mdb', 'Person']

f = NamedTemporaryFile(delete=False)
p = subprocess.Popen(cmd, stdout=f)
errcode = p.wait()
print (f.name)
f.close()
if errcode:
    errmess = p.stderr.read()
    log.error('cmd failed <%s>: %s' % (errcode,errmess))
    
# os.unlink(f.name)
# os.path.exists(f.name)


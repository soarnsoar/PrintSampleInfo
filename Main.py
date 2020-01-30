import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
import optparse




usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)

parser.add_option("-p","--py",   dest="sample_py", help="Sample python", default=False)
parser.add_option("-k","--key",   dest="keys", help="Sample key",  type='string')
parser.add_option("-v","--veto",   dest="vetokeys", help="Sample key to veto", type='string')




(options, args) = parser.parse_args()


sample_py=options.sample_py
KEY=options.keys.strip().split(',')

if options.vetokeys:
    VETOKEY=options.vetokeys.strip().split(',')
else:
    VETOKEY=False


mcm=McM(dev=False)

def GetNevent(prepid):
    
    request=mcm.get('requests',prepid)
    return request['total_events']


def GetPrepId(DAS):
    request=mcm.get('requests',query='produce='+DAS)
    return request[0]['prepid']

dir_import='/'.join(sample_py.split('/')[:-1])
#print dir_import
file_import='.'.join(sample_py.split('/')[-1].split('.')[:-1])

sys.path.append(dir_import)
exec('from '+file_import+ ' import *')




#prepid=GetPrepId('/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM')


#print prepid

#nevent=GetNevent(prepid)
#print nevent
idx=0
for sample in sorted(Samples):
    Fine=False
    for k in KEY:
        if k in sample:
            Fine=True
            break
    
    
    if VETOKEY:
        for VETO in VETOKEY:
            if VETO in sample:
                Fine=False
                break
    if not Fine:continue
            
    if not 'nanoAOD' in Samples[sample]:continue
    DAS=Samples[sample]['nanoAOD']
    prepid=GetPrepId(DAS)
    nevent=GetNevent(prepid)
    #print ""
    #print str(idx)+'.'+'\t'+sample+'\t'+str(nevent)+'\t'+DAS
    print sample+'\t'+str(nevent)+'\t'+DAS

    #if idx==1:break

    #GetPrepId()

    idx+=1
    

#SamplePythons/Autumn18_102X_nAODv6.py  SamplePythons/fall17_102X_nAODv5.py  SamplePythons/Summer16_102X_nAODv5.py

keyoption="--key QCD"
vetooption=" -v Wp,Wm,WLL,ZTo2L"

echo "===${BASH_SOURCE}==="
echo "[2016]"
python Main.py --py SamplePythons/Summer16_102X_nAODv5.py $keyoption $vetooption,bcToE,Mu
python Main.py --py SamplePythons/Summer16_102X_nAODv5.py $keyoption $vetooption,MuEnriched,EMEnriched
python Main.py --py SamplePythons/Summer16_102X_nAODv5.py $keyoption $vetooption,bcToE,EMEnriched
echo "[2017]"
python Main.py --py SamplePythons/fall17_102X_nAODv5.py $option $vetooption,bcToE,Mu
python Main.py --py SamplePythons/fall17_102X_nAODv5.py $option $vetooption,MuEnriched,EMEnriched
python Main.py --py SamplePythons/fall17_102X_nAODv5.py $option $vetooption,bcToE,EMEnriched
echo "[2018]"
python Main.py --py SamplePythons/Autumn18_102X_nAODv6.py $option $vetooption,bcToE,Mu
python Main.py --py SamplePythons/Autumn18_102X_nAODv6.py $option $vetooption,MuEnriched,EMEnriched
python Main.py --py SamplePythons/Autumn18_102X_nAODv6.py $option $vetooption,bcToE,EMEnriched


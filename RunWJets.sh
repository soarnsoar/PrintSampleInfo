#SamplePythons/Autumn18_102X_nAODv6.py  SamplePythons/fall17_102X_nAODv5.py  SamplePythons/Summer16_102X_nAODv5.py

option="--key Wjet,WJet -v TT"

echo "===${BASH_SOURCE}==="
echo "[2016]"
python Main.py --py SamplePythons/Summer16_102X_nAODv5.py $option
echo "[2017]"
python Main.py --py SamplePythons/fall17_102X_nAODv5.py $option
echo "[2018]"
python Main.py --py SamplePythons/Autumn18_102X_nAODv6.py $option


import os
import subprocess

# SUMO_HOME dizinini ayarlayın
sumo_home = r"C:\Program Files (x86)\Eclipse\Sumo"
os.environ["SUMO_HOME"] = sumo_home

# PATH değişkenine SUMO'nun bin dizinini ekleyin
os.environ["PATH"] += os.pathsep + os.path.join(sumo_home, "bin")

# SUMO ağ dosyasını ve rota dosyasını tanımlayın
net_file = "eskisehir_osb.net.xml"
trips_file = "eskisehir_osb.trips.xml"
rou_file = "eskisehir_osb.rou.xml"

# Rastgele rotalar oluşturmak için randomTrips.py aracını çalıştırın
random_trips_command = [
    "python", os.path.join(sumo_home, "tools", "randomTrips.py"),
    "-n", net_file,
    "-o", trips_file,
    "-r", rou_file,
    "--end", "3600",
    "--period", "1"
]
subprocess.run(random_trips_command)

# SUMO GUI'yi başlat ve konfigürasyon dosyasını yükle
config_file = "eskisehir_osb.sumocfg"
subprocess.run(["sumo-gui", "-c", config_file])

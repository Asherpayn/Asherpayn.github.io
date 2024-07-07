import speedtest

s = speedtest.speedtest()

print ("Testing...\n")

downloadspeed = s.download() / 1048576
uploadspeed = s.upload() / 1048576
pingresult = round(s.results.ping)

print(f"Download speed; {downloadspeed:.2f} Mbps")
print(f"Upload speed: {uploadspeed:.2f} Mbps")
print(f"Ping: {pingresult} Ms")

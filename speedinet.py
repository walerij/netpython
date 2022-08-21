import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"Speed: {(download/1024)/1024} Mb/s \n Upload Speed : {(upload/1024)/1024} Mb/s")
import speedtest, time

st = speedtest.Speedtest()

while True:
    t = time.localtime()

    if t.tm_min % 5 == 0:
        stamp = str(t.tm_year) + "/" + str(t.tm_mon) + "/" + str(t.tm_mday) + ";" + str(t.tm_hour).rjust(2, "0") + ":" + str(t.tm_min).rjust(2, "0")
        
        try:
            response = round(st.download(), 2) # bits/s
        except:
            print("Exception raised while trying to test the internet..")
        else:
            ret = stamp + ";" + str(response)

            with open("speedtest.csv", "a") as f:
                f.write(ret + "\n")
            time.sleep(60)
    time.sleep(10)
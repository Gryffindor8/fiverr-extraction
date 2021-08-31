import pandas as pd

file = open("pattern.txt")
line = file.read().replace("\t", " ")
file.close()


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


length = list(find_all(line, "Length: "))
header = list(find_all(line, "Header: "))
payload = list(find_all(line, "Payload: "))
subc = list(find_all(line, "Subscription ID ="))
tme = list(find_all(line, "2021 Apr"))

i = 0
Length = []
Header = []
pay = []
date = []
info = []
Header2 = []
Time = []
Header3 = []
for ln in length:
    try:
        Length.append(line[ln + 7:header[i]].replace(" ", ""))
        Header.append(line[header[i]:payload[i]].replace("Header:", ""))
        pay.append(line[payload[i]:tme[i + 1]].replace("\n", " ").replace("Payload:", "").replace("  ", ""))
        date.append("2021 Apr 14")
        info.append(line[subc[i]:length[i]].replace("-", "").replace("  ", "").replace("|||", "").strip())
        Header2.append((line[tme[i]:subc[i]]).replace(line[tme[i]:tme[i] + 11], "").strip())
        i = i + 1
    except:
        break

for k in Header2:
    tk = k.split(" ")
    Time.append(tk[0])
    Header3.append((" ".join(tk[3:])))
print(Length)
data = [date, Time, Header3, info, Length, Header, pay]
df = pd.DataFrame(data, index=["Date", "Time", "Header", "Info", "Length", "Header", "PayLoad"])
df = df.T
df.to_csv("Ecel.csv")

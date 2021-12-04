from datetime import datetime

print(datetime.strptime("24052010", "%d%m%Y").date())
print(datetime.strptime("09/07/1978".replace('/',''), "%d%m%Y").date())
d = datetime.now().year-50
print(d)

import requests
import csv

result = requests.get('http://localhost:9090/api/v1/query?query=sum(rate(nginx_ingress_controller_nginx_process_cpu_seconds_total{}[10m]))')

print(result.json())
f = open('monitoring-data.csv', 'w')
writer = csv.writer(f)
writer.writerow(result.json())
f.close()

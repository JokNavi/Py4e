domains = dict()
with open('mbox-short.txt') as f:
    for line in f.readlines():
        if line.startswith('From') and not line.startswith('From:'):
            adress = line.split()[1]
            domain = adress.split("@")[1]
            print(domain)
            if domain not in domains:
                domains.update({domain: 1})
            else:
                domains.update({domain: domains[domain]+1})
            
print(domains) 
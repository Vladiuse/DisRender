def read_data():
    domains_data = {}
    with open('teams_domains.ini') as file:
        for line in file:
            line = line.strip()
            team_id, domain, x, diss = line.split()
            item = {
                team_id: {
                    'domain': domain,
                    'diss': diss,
                }
            }
            domains_data.update(item)
    return domains_data


DOMAINS_DATA = read_data()

def read_gedcom(file_path):
    individuals = []
    with open(file_path, 'r') as file:
        individual = {}
        for line in file:
            level = int(line[0])
            tag = line[2:6].strip()
            value = line[7:].strip()
            
            if level == 0 and tag == 'INDI':
                if individual:
                    individuals.append(individual)
                individual = {'id': value}
            elif level == 1 and tag == 'NAME':
                individual['name'] = value
            elif level == 1 and tag == 'SEX':
                individual['sex'] = value
            elif level == 1 and tag == 'BIRT':
                individual['birth'] = {}
            elif level == 2 and tag == 'DATE':
                individual['birth']['date'] = value
            elif level == 2 and tag == 'PLAC':
                individual['birth']['place'] = value
            elif level == 1 and tag == 'DEAT':
                individual['death'] = {}
            elif level == 2 and tag == 'DATE':
                individual['death']['date'] = value
            elif level == 2 and tag == 'PLAC':
                individual['death']['place'] = value
        if individual:
            individuals.append(individual)
    return individuals

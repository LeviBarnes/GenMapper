def read_gedcom(file_path):
    individuals = []
    datemode = 'none'
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
                datemode = 'birth'
            elif level == 2 and tag == 'DATE' and datemode == 'birth':
                individual['birthdate'] = value
            elif level == 2 and tag == 'PLAC' and datemode == 'birth':
                individual['birthplace'] = value
            elif level == 1 and tag == 'DEAT':
                datemode = 'death'
            elif level == 2 and tag == 'DATE' and datemode == 'death':
                individual['deathdate'] = value
            elif level == 2 and tag == 'PLAC' and datemode == 'death':
                individual['deathplace'] = value
        if individual:
            individuals.append(individual)
    return individuals

if __name__ == "__main__":
    dots = read_gedcom("C:\\Users\\lbarnes\\Documents\\GitHub\\GenMapper\\Joseph Chandler Files-20230621T003941Z-001\\Joseph Chandler Files\\Chandler GEDcom Files - February 17, 2018\\John Jenkins and Leticia Anderson_2018-02-17.ged")
    print(dots[0])

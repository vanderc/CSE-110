with open('hr system.txt') as f:
    for line in f:
        clean_line = line.strip()
        parts = clean_line.split(' ')
        name = parts[0]
        id_number = parts[1]
        title = parts[3]
        salary = float(parts[3])
        pay_amount = salary / 24
        if title.lower() == 'engineer':
            pay_amount += 1000
        print(f'{name} (ID: {id_number}), {title} - ${pay_amount:.2f}')
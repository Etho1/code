with open('hr_system.txt') as file:
    # next()
    # file.readline()
    for line in file:
        clean_line = line.strip()
        # print(clean_line)
        line_list = clean_line.split()
        name = line_list[0]
        eyedee = line_list[1]
        job_title = line_list[2]
        salary = float(line_list[3])
        if job_title.lower() == 'engineer':
            salary = salary + 1000
        else:
            salary = salary
        paycheck = salary/26
        print(f'{name} (ID: {eyedee}), {job_title} - {paycheck:.2f}')


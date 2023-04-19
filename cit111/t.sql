select first_name,last_name,email,
right(email, length(email) - Locate('@',email)),
mid(email,locate('@',email)
most_chapters = -1
biggest_book = None
big_script = None
chosen_book = input('Which volume of scripture would you like to learn about?')
with open('books_and_chapters.txt') as file:
    for line in file:
        clean_line = line.strip()
        line_list = clean_line.split(':')
        book = line_list[0]
        chapters = int(line_list[1])
        script = line_list[2]
        # if chapters > most_chapters:
        #         most_chapters = chapters
        #         biggest_book = book
        #         big_script = script
        if script.lower() == chosen_book.lower():
            if chapters > most_chapters:
                most_chapters = chapters
                biggest_book = book
                big_script = script
        # print(f'Scripture: {script}, Book: {book}, Chapters: {chapters}')
print(f'Book with most chapters: {biggest_book}, Number of chapters: {most_chapters}')

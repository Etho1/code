-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema art_gallery
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema university
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `university` ;

-- -----------------------------------------------------
-- Schema university
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `university` DEFAULT CHARACTER SET utf8mb3 ;
USE `university` ;

-- -----------------------------------------------------
-- Table `university`.`college`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`college` ;

CREATE TABLE IF NOT EXISTS `university`.`college` (
  `college_id` INT NOT NULL AUTO_INCREMENT,
  `college_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`college_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `university`.`department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`department` ;

CREATE TABLE IF NOT EXISTS `university`.`department` (
  `department_id` INT NOT NULL AUTO_INCREMENT,
  `department_name` VARCHAR(100) NOT NULL,
  `college_id` INT NOT NULL,
  PRIMARY KEY (`department_id`),
  INDEX `fk_department_college_idx` (`college_id` ASC) VISIBLE,
  CONSTRAINT `fk_department_college`
    FOREIGN KEY (`college_id`)
    REFERENCES `university`.`college` (`college_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `university`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`course` ;

CREATE TABLE IF NOT EXISTS `university`.`course` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `course_code` VARCHAR(45) NOT NULL,
  `course_title` VARCHAR(100) NOT NULL,
  `course_credits` INT NOT NULL,
  `department_id` INT NOT NULL,
  PRIMARY KEY (`course_id`),
  INDEX `fk_course_department1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `fk_course_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `university`.`department` (`department_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `university`.`faculty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`faculty` ;

CREATE TABLE IF NOT EXISTS `university`.`faculty` (
  `faculty_id` INT NOT NULL AUTO_INCREMENT,
  `faculty_fname` VARCHAR(45) NOT NULL,
  `faculty_lname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`faculty_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `university`.`term`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`term` ;

CREATE TABLE IF NOT EXISTS `university`.`term` (
  `term_id` INT NOT NULL AUTO_INCREMENT,
  `term` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  PRIMARY KEY (`term_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `university`.`section`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`section` ;

CREATE TABLE IF NOT EXISTS `university`.`section` (
  `section_id` INT NOT NULL AUTO_INCREMENT,
  `section_number` INT NOT NULL,
  `capacity` INT NULL DEFAULT NULL,
  `course_id` INT NOT NULL,
  `term_id` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  PRIMARY KEY (`section_id`, `course_id`, `term_id`),
  INDEX `fk_section_course1_idx` (`course_id` ASC) VISIBLE,
  INDEX `fk_section_term1_idx` (`term_id` ASC) VISIBLE,
  INDEX `fk_section_faculty1_idx` (`faculty_id` ASC) VISIBLE,
  CONSTRAINT `fk_section_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `university`.`course` (`course_id`),
  CONSTRAINT `fk_section_term1`
    FOREIGN KEY (`term_id`)
    REFERENCES `university`.`term` (`term_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_faculty1`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `university`.`faculty` (`faculty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `university`.`student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`student` ;

CREATE TABLE IF NOT EXISTS `university`.`student` (
  `student_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gender` ENUM('M', 'F') NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `birthdate` DATE NOT NULL,
  PRIMARY KEY (`student_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `university`.`section_has_student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university`.`section_has_student` ;

CREATE TABLE IF NOT EXISTS `university`.`section_has_student` (
  `section_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  PRIMARY KEY (`section_id`, `student_id`),
  INDEX `fk_section_has_student_student1_idx` (`student_id` ASC) VISIBLE,
  INDEX `fk_section_has_student_section1_idx` (`section_id` ASC) VISIBLE,
  CONSTRAINT `fk_section_has_student_section1`
    FOREIGN KEY (`section_id`)
    REFERENCES `university`.`section` (`section_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_has_student_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `university`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



use university;
#QUERY 1
INSERT INTO college (college_id,college_name)
VALUES (1,'College of Physical
Science and Engineering'),(2,'College of Business and
Communication'),(3,'College of Language and
Letters');
#QUERY 2
INSERT INTO department (department_id, department_name,college_id)
VALUES (1,'Computer Information Technology',1),(2,'Economics',2),(3,'Humanities and Philosophy',3);
#QUERY 3
INSERT INTO course (course_id, course_code, course_title, course_credits, department_id)
VALUES (1, 'CIT 111', 'Intro to Databases', 3, 1),
(2,'ECON 388', 'Econometrics', 4, 2), 
(3,'ECON 150', 'Micro Economics', 3, 2),
(4,'HUM 376', 'Classical Heritage', 2, 3);
#QUERY 4
INSERT INTO student (first_name,last_name,gender,city,state,birthdate)
VALUES ('Paul', 'Miller', 'M', 'Dallas', 'TX', '1996-02-22'),
('Katie', 'Smith', 'F', 'Provo', 'UT', '1995-07-22'),
('Kelly', 'Jones', 'F', 'Provo', 'UT', '1998-06-22'),
('Devon', 'Merrill', 'M', 'Mesa', 'AZ', '2000-07-22'),
('Mandy', 'Murdock', 'F', 'Topeka', 'KS', '1996-11-22'),
('Alece', 'Adams', 'F', 'Rigby', 'ID', '1997-05-22'),
('Bryce', 'Carlson', 'M', 'Bozeman', 'MT', '1997-11-22'),
('Preston', 'Larsen', 'M', 'Decatur', 'TN', '1996-09-22'),
('Julia', 'Madsen', 'F', 'Rexburg', 'ID', '1998-09-22'),
('Susan', 'Sorensen', 'F', 'Mesa', 'AZ', '1998-08-09');
#QUERY 5
INSERT INTO faculty(faculty_fname,faculty_lname)
VALUES ('Marty', 'Morring'),
('Nate', 'Norris'),
('Ben', 'Barrus'),
('John', 'Jensen'),
('Bill', 'Barney'),
('John', 'Jensen');
#QUERY 6
INSERT INTO term(term,year)
VALUES ('Fall',2019),('Winter',2018);
#QUERY 7
INSERT INTO section(section_number,capacity, course_id, faculty_id,term_id)
VALUES (1,30,1,1,1),(1,50,3,2,1),(2,50,3,2,1),(1,35,2,3,1),(1,30,4,4,1),(2,30,1,1,2),(3,35,1,5,2),(1,50,3,2,2),(2,50,3,2,2),(1,30,4,4,2);
#QUERY 8
INSERT INTO section_has_student(section_id,student_id)
VALUES (6,7),(7,6),(7,8),(7,1),(4,5),(9,9),(2,4),(3,4),(5,4),(5,5),(1,1),(1,3),(8,9),(10,6);







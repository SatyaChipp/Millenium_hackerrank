
list_ = [1,2,3,4,['a','b','c','d']]
def func_lis(list_):
    new_list = []
    for item in list_:
        if(isinstance(item, list)):
            new_list.extend(item)
        else:
            new_list.append(item)
    return new_list
print(func_lis(list_=list_))

SELECT * FROM USER_TABLE
WHERE USERID NOT IN (
    SELECT * FROM PHOTO_TABLE as ph USER_PHOTO as us ph.PHOTO_TABLE JOIN us.USER_PHOTO ON ph.PHOTOID = us.PHOTOID
)

SELECT USERID from USER_TABLE
FULL JOIN on USER_TABLE.USERID = USER_PHOTO_TABLE.USERID
WHERE USER_PHOTO_TABLE.PHOTOID IS NULL



Design an Online University:

ProgramTABLE
(PK PprogID, CourseID)
PROGRAM NAME
prog_id
courseid (FK)
DURATION


courseTable (PK courseID)
COURSEID
name
language
dept

studentTable
ID (PK)
name
programID (FK)
courseID (FK)

ProfessorTABLE
ID (PK)
name
dept
coursid(FK)

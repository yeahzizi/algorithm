SELECT ANIMAL_ID, NAME
from ANIMAL_INS 
where ANIMAL_TYPE = "Dog" and NAME LIKE "%el%"
order by NAME
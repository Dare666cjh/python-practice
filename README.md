# python practice
START
INPUT birth_year
INPUT current_year

DECISION
IF birth_year > current_year THEN
    OUTPUT "Invalid input. Birth year cannot be in the future."
ELSE
    PROCESS (CALCULATION) age = current_year - birth_year
    OUTPUT "You are", age, "years old."
STOP IF

STOP

from ppydb import *

db = Database("example")

print(db)


class Gender(EnumCol):
    MALE = "male"
    FEMALE = "female"


table = db.create_table(
    "table",
    Int("id", AutoNum, PrimaryKey),
    Str("lastname"),
    Str("firstname", NeverEmpty),
    Gender("gender"),
)

print(table)

db.insert_values(
    table,
    (None, "Stickmin", "Henry", Gender.MALE),
    (None, "Calvin", "Charles", Gender.MALE),
    (None, "Rose", "Ellie", Gender.FEMALE),
    (None, None, "Right Hand Man", Gender.MALE),
    (None, "Petrov", "Dmitri Johannes", Gender.MALE),
    (None, "Vinschpinsilstien", "Dr.", Gender.FEMALE),
    (None, "Ladd", "Madd", Gender.MALE),
    (None, "Binderson", "Isaac", Gender.MALE),
    (None, "Esteban", "Amelia", Gender.FEMALE),
    (None, "Stone", "Abigail", Gender.FEMALE),
    (None, "Jenkins", "Clyde", Gender.MALE),
    (None, "Hamilton", "Alice", Gender.FEMALE),
)

print(
    db.table(table)
    .select(table.gender == Gender.MALE and not table.firstname.startswith("C"))
    .sort_by(table.firstname, DESC)
    .project(table.firstname, table.lastname)
)

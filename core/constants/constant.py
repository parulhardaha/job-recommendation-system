import enum

class ExperienceLevelEnum(str, enum.Enum):
    JUNIOR = 'Junior'
    INTERMEDIATE = 'Intermediate'
    SENIOR = 'Senior'

class JobTypeEnum(str, enum.Enum):
    FULL_TIME = 'Full-Time'
    PART_TIME = 'Part-Time'
    CONTRACT = 'Contract'


ExperienceLevelMapping = {
    'Junior' : "JUNIOR",
    "Intermediate": "INTERMEDIATE",
    "Senior" : "SENIOR"
}

JobTypeMapping = {
    'Full-Time': "FULL_TIME",
    'Part-Time': "PART_TIME",
    'Contract': "CONTRACT"
}
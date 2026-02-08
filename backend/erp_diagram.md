erDiagram

USER ||--|| PROFILE : has
USER ||--o{ CATEGORY : creates

PROFILE ||--o{ EDUCATION : has
PROFILE ||--o{ EXPERIENCE : has
PROFILE ||--o{ SKILL : has

CATEGORY ||--o{ JOB_DETAIL : contains

JOB_DETAIL ||--o{ SKILL : requires
JOB_DETAIL ||--o{ RESPONSIBILITY : defines
JOB_DETAIL ||--o{ QUALIFICATION : defines

USER {
    uuid uid PK
    string email
    int role
    boolean is_staff
    boolean is_superuser
}

PROFILE {
    int id PK
    uuid user_id FK
    string description
    string location
}

CATEGORY {
    int id PK
    string title
    string position
    string location
    uuid created_by FK
}

JOB_DETAIL {
    int id PK
    int category_id FK
    string job_title
    string job_level
    datetime posted_on
}

SKILL {
    int id PK
    string skill_name
}

RESPONSIBILITY {
    int id PK
    string responsibility_name
}

QUALIFICATION {
    int id PK
    string qualification_name
}

EDUCATION {
    int id PK
    string institution
    string field_study
}

EXPERIENCE {
    int id PK
    string title
    string work_type
}

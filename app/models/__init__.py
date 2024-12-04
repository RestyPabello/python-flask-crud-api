from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .teacher import Teacher
from .student import Student
from .section import Section
from .subject import Subject
from .subject_student import SubjectStudent
from .subject_teacher import SubjectTeacher
from .role import Role
from .role_type import RoleType
from .user import User
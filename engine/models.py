from pydantic import BaseModel


class PersonalInfo(BaseModel):
    name: str
    phone: str
    email: str
    github: str


Skill = str
"""Type alias for Skill, in case this gets expanded."""


class SkillCategory(BaseModel):
    name: str
    skills: list[Skill]
    hidden: bool = False


class School(BaseModel):
    name: str
    location: str
    degree: str
    major: str
    minor: str
    start_date: str
    end_date: str


class Job(BaseModel):
    name: str
    location: str
    position: str
    start_date: str
    end_date: str
    points: list[str]


class Project(BaseModel):
    name: str
    description: str
    git: str | None = None
    hidden: bool = False


class ProjectCategory(BaseModel):
    name: str
    projects: list[Project]
    hidden: bool = False


class Association(BaseModel):
    name: str
    position: str
    location: str
    start_date: str
    end_date: str


class Publication(BaseModel):
    title: str
    role: str
    publisher: str
    date: str
    id: str
    url: str


class Resume(BaseModel):
    personal: PersonalInfo
    experience: list[Job]
    education: list[School]
    skill_categories: list[SkillCategory]
    project_categories: list[ProjectCategory]
    associations: list[Association]
    publications: list[Publication]

    def __init__(
        self,
        *,
        personal: PersonalInfo,
        experience: list[Job],
        education: list[School],
        skill_categories: list[SkillCategory],
        project_categories: list[ProjectCategory],
        associations: list[Association],
        publications: list[Publication],
    ):
        # Filter-out hidden projects and project categories
        project_categories = [
            category for category in project_categories if not category.hidden
        ]

        for category in project_categories:
            category.projects = [
                project for project in category.projects if not project.hidden
            ]

        # Filter-out hidden skill categories
        skill_categories = [
            category for category in skill_categories if not category.hidden
        ]

        # Defer filtered context object to BaseModel initializer
        super().__init__(
            personal=personal,
            experience=experience,
            education=education,
            skill_categories=skill_categories,
            project_categories=project_categories,
            associations=associations,
            publications=publications,
        )

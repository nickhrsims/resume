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

    def without_email(self):
        filtered_resume = self.model_copy(deep=True)
        filtered_resume.personal.email = ""
        return filtered_resume

    def without_phone(self):
        filtered_resume = self.model_copy(deep=True)
        filtered_resume.personal.phone = ""
        return filtered_resume

    def without_github(self):
        filtered_resume = self.model_copy(deep=True)
        filtered_resume.personal.github = ""
        return filtered_resume

    def without_hidden_entries(self):
        filtered_resume = self.model_copy(deep=True)

        # Filter-out hidden projects and project categories
        filtered_resume.project_categories = [
            category
            for category in filtered_resume.project_categories
            if not category.hidden
        ]

        for category in filtered_resume.project_categories:
            category.projects = [
                project for project in category.projects if not project.hidden
            ]

        # Filter-out hidden skill categories
        filtered_resume.skill_categories = [
            category
            for category in filtered_resume.skill_categories
            if not category.hidden
        ]

        return filtered_resume

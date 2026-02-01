"""
R3sum3OS - Core Ontology Schema
Defines the semantic structure for mapping professional history to OS primitives.
"""

from typing import TypedDict, List, Optional, Union
from enum import Enum

class EntityType(Enum):
    EXPERIENCE = "experience"
    SKILL = "skill"
    PROJECT = "project"
    EDUCATION = "education"
    CERTIFICATION = "certification"
    IDENTITY = "identity"

class SkillLevel(Enum):
    NOVICE = 1
    COMPETENT = 2
    PROFICIENT = 3
    EXPERT = 4
    MASTER = 5

class ConnectionType(Enum):
    USED_IN = "used_in"          # Skill used in a Project/Job
    ACHIEVED_AT = "achieved_at"  # Certification at an Institution
    CONTRIBUTED_TO = "contributed_to"
    MAINTAINED = "maintained"

class BaseEntity(TypedDict):
    id: str
    name: str
    description: str
    metadata: dict

class Skill(BaseEntity):
    category: str  # e.g., "Backend", "DevOps", "Soft Skills"
    level: SkillLevel
    years_of_experience: float

class Experience(BaseEntity):
    organization: str
    role: str
    location: str
    start_date: str
    end_date: Optional[str]  # None if "Present"
    highlights: List[str]
    technologies: List[str]  # Foreign keys to Skill IDs

class Project(BaseEntity):
    url: Optional[str]
    repo: Optional[str]
    stack: List[str]
    impact_metrics: List[str]

class OntologySchema:
    """
    The Global Schema Registry.
    This dictates how the 'FileSystem' driver interprets JSON/YAML source files.
    """
    
    VERSION = "1.0.0"
    
    STRUCTURE = {
        "entities": {
            "type": EntityType,
            "required_fields": ["id", "name"]
        },
        "relationships": {
            "source": str,      # ID of source entity
            "target": str,      # ID of target entity
            "predicate": ConnectionType
        }
    }

    @staticmethod
    def validate_entity(entity: dict) -> bool:
        """Validates if a data object conforms to the R3sum3OS ontology."""
        required = ["id", "name", "type"]
        return all(key in entity for key in required)

    @staticmethod
    def map_to_filesystem_path(entity_type: EntityType) -> str:
        """Maps an ontology type to a virtual /dev or /home path."""
        mapping = {
            EntityType.EXPERIENCE: "/mnt/history/work",
            EntityType.SKILL: "/bin/tools",
            EntityType.PROJECT: "/home/user/projects",
            EntityType.IDENTITY: "/etc/sys/owner"
        }
        return mapping.get(entity_type, "/tmp")

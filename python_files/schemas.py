from pydantic import BaseModel, field_validator

USER_PREFIX = "user"

class DeploymentCreate(BaseModel):
    db_name: str
    username: str

    @field_validator("db_name")
    def validate_db_name(cls, v: str):
        prefix = f"{USER_PREFIX}-"
        if not v.startswith(prefix):
            raise ValueError(f"db_name must start with '{prefix}'")
        return v

    @field_validator("username")
    def validate_username(cls, v: str):
        if len(v) < 3:
            raise ValueError("username must be at least 3 characters")
        return v
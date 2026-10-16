from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.modules.users import repository as users_repository
from . import repository
from .models import UserPreference
from .schemas import UserPreferenceCreate, UserPreferenceUpdate


def _clean_goal(goal: str | None) -> str | None:
    if goal is None:
        return None
    goal = goal.strip()
    return goal or None


def create_preference(db: Session, data: UserPreferenceCreate) -> UserPreference:
    if not users_repository.get_by_id(db, data.user_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    if repository.get_by_user(db, data.user_id):
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "Preferences already exist for this user (use PUT to change them)",
        )
    pref = UserPreference(
        user_id=data.user_id, investment_goal=_clean_goal(data.investment_goal)
    )
    return repository.create(db, pref)


def get_preference(db: Session, preference_id: int) -> UserPreference:
    pref = repository.get_by_id(db, preference_id)
    if not pref:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Preference not found")
    return pref


def list_preferences(
    db: Session, user_id: str | None, skip: int, limit: int
) -> list[UserPreference]:
    return repository.list_preferences(db, user_id, skip, limit)


def update_preference(
    db: Session, preference_id: int, data: UserPreferenceUpdate
) -> UserPreference:
    pref = get_preference(db, preference_id)
    changes = data.model_dump(exclude_unset=True)
    if "investment_goal" in changes:
        changes["investment_goal"] = _clean_goal(changes["investment_goal"])
    return repository.update(db, pref, changes)


def delete_preference(db: Session, preference_id: int) -> None:
    pref = get_preference(db, preference_id)
    repository.delete(db, pref)
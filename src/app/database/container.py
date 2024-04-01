from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.database.dals.organization_dal import OrganizationDAO
from app.database.dals.organization_user_dal import UserOrganizationDAO
from app.database.dals.recording_dal import RecordingDAO
from app.database.dals.recording_week_dal import RecordingWeekDAO
from app.database.dals.user_dal import UserDAO
from app.database.database import async_engine
from app.database.services.organization_service import OrganizationService
from app.database.services.organization_user_service import UserOrganizationService
from app.database.services.recording_service import RecordingService
from app.database.services.recording_week_service import RecordingWeekService
from app.database.services.user_service import UserService


async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)()

organization_dao = OrganizationDAO(async_session)
user_organization_dao = UserOrganizationDAO(async_session)
recording_dao = RecordingDAO(async_session)
recording_week_dao = RecordingWeekDAO(async_session)
user_dao = UserDAO(async_session)

organization_service = OrganizationService(organization_dao)
user_organization_service = UserOrganizationService(user_organization_dao)
recording_service = RecordingService(recording_dao)
recording_week_service = RecordingWeekService(recording_week_dao)
user_service = UserService(user_dao)

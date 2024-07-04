from typing import Optional

from aiogram.filters.callback_data import CallbackData


class OrganizationCallbackData(CallbackData, prefix="organization-callback-data"):
    organization_id_to_be_active: int
    organization_id_to_be_inactive: Optional[int]

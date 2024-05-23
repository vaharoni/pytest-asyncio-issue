import pytest
from collections.abc import AsyncGenerator

@pytest.fixture()
async def fixture() -> AsyncGenerator[str, None]:
    yield "a"

@pytest.mark.asyncio
async def test(fixture: str):
    assert fixture == "a"
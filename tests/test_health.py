import asyncio

from httpx import ASGITransport, AsyncClient, Response

from robert.app import create_app
from robert.config import Settings


def test_health_endpoint_reports_governance_boundaries() -> None:
    app = create_app(Settings(environment="test"))

    async def get_health() -> Response:
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://testserver",
        ) as client:
            return await client.get("/health")

    response = asyncio.run(get_health())

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "robert-master-system",
        "version": "0.1.0",
        "autonomy_level": 0,
        "execution_authority": "NONE",
    }

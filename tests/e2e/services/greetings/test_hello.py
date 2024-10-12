import pytest


class TestHello:
    @pytest.mark.parametrize("mood", ["bad", "good"])
    def test_200_response(self, client, mood):
        response = client.get(f"/greetings/{mood}")
        assert response.status_code == 200

    @pytest.mark.parametrize("mood", ["unhappy", "happy"])
    def test_404_response(self, client, mood):
        response = client.get(f"/greetings/{mood}/404")
        assert response.status_code == 404

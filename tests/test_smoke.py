"""Smoke tests for the currently generated BUSY Bar SDK."""

from busybar_python_sdk import ApiClient, Configuration, VersionInfo


def test_public_client_exports_are_importable() -> None:
    assert ApiClient is not None
    assert Configuration is not None


def test_version_info_round_trip() -> None:
    model = VersionInfo.from_dict({"api_semver": "27.5.0"})

    assert model is not None
    assert model.api_semver == "27.5.0"
    assert model.to_dict() == {"api_semver": "27.5.0"}

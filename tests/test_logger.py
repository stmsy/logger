from ..config.params import DEBUG


def test_debug() -> None:
    """Check whether DEBUG is set False."""
    assert DEBUG == False

from __future__ import annotations

import importlib.metadata

import tst_tools as m


def test_version():
    assert importlib.metadata.version("tst_tools") == m.__version__

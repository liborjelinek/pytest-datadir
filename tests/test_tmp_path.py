from pathlib import Path

def ls(path):
    return list([f.name for f in path.rglob("*")])

def test_datadir_not_collide_with_tmp_path(tmp_path: Path, datadir: Path):
    assert ls(tmp_path) == []

def test_shared_datadir_not_collide_with_tmp_path(tmp_path: Path, shared_datadir: Path):
    assert ls(tmp_path) == []
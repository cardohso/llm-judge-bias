from judgebias.cache import RunCache

REQ = {"model": "m", "messages": [{"role": "user", "content": "hi"}], "temperature": 0}


def test_same_request_same_run_hits(tmp_path):
    c = RunCache(tmp_path / "c.sqlite")
    c.set(REQ, 1, "reply")
    assert c.get(REQ, 1) == "reply"


def test_other_run_misses(tmp_path):
    c = RunCache(tmp_path / "c.sqlite")
    c.set(REQ, 1, "reply")
    assert c.get(REQ, 2) is None


def test_other_request_misses(tmp_path):
    c = RunCache(tmp_path / "c.sqlite")
    c.set(REQ, 1, "reply")
    assert c.get({**REQ, "model": "other"}, 1) is None


def test_persists_across_instances(tmp_path):
    RunCache(tmp_path / "c.sqlite").set(REQ, 3, "reply")
    assert RunCache(tmp_path / "c.sqlite").get(REQ, 3) == "reply"

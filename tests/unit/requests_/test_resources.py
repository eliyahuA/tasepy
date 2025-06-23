from tasepy.requests_.resources import NoResource, DatedIndexResource


def test_no_resource():
    r = NoResource()
    assert r.resource_path == ""


def test_date_index():
    resource = DatedIndexResource(index_id=0, year=2000, month=1, day=1)
    assert resource.resource_path == r"/0/2000/1/1"

from tasepy.endpoints.factories import YAMLFactory


class TestYAMLFactory:

    def test_get_endpoints(self):
        import tasepy
        from pathlib import Path
        from tasepy.requests_.urls import Endpoints
        package_dir = Path(tasepy.__file__).parent
        yaml_path = package_dir / "endpoints" / "endpoints.yaml"
        yaml_factory = YAMLFactory(yaml_path, Endpoints)
        endpoints = yaml_factory.get_endpoints()
        assert True

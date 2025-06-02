from ..responses import ResponseComponent, Root, CodeValuePair


class ShareExposureProfile(ResponseComponent):
    share_exposure_profile: Root[CodeValuePair]

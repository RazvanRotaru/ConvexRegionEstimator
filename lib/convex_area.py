from connected_region import ConnectedRegion


class ConvexArea:
    def __init__(self, region: ConnectedRegion):
        self.region = region

    @classmethod
    def of(cls):
        return []

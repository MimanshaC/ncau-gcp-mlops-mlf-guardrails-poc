from pytest import fixture

from new_model.model.features import Featurizer


class TestFeaturizer:
    @fixture(autouse=True)
    def injector(self, test_X_y_dataset):
        self.test_X = test_X_y_dataset[1]
        self.test_y = test_X_y_dataset[2]
        self.expected_feat = test_X_y_dataset[3]

    def test_transform(self):
        feat = Featurizer()
        X = feat.transform(self.test_X)
        assert X.equals(self.expected_feat)

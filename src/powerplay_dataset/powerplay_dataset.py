"""powerplay_dataset dataset."""

import tensorflow_datasets as tfds

_DESCRIPTION = """
PowerPlay Dataset for vison correction via pole detection
"""

# IMPORTANT: THIS DATASET WAS BUILD UNDER THE ASSUMPTION THAT 3 VALUES WOULD BE USED IN THE DATASET, NOT A VALUE,
# AS SUCH DO NOT USE THIS DATASET UNLESS MODIFIED
class PowerplayDataset(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for powerplay_dataset dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    # These are the features of your dataset like images, labels ...
                    "image": tfds.features.Image(shape=(1920, 1080, 3)),
                    "label": tfds.features.ClassLabel(names=["right", "left", "center"],
                                                      doc='Whether this is a picture is aligned with the pole'),
                }
            ),
            # If there's a common (input, target) tuple from the
            # features, specify them here. They'll be used if
            # `as_supervised=True` in `builder.as_dataset`.
            # supervised_keys=("image", "label"),  # Set to `None` to disable
            # homepage="https://dataset-homepage/",
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        # TODO(powerplay_dataset): Downloads the data and defines the splits
        path = dl_manager.download_and_extract("127.00.0.1:5000/data.zip")

        return {
            "train": self._generate_examples(path=path / "train_images"),
            "test": self._generate_examples(path=path / "test_images"),
        }

    def _generate_examples(self, path):
        """Yields examples."""
        for img_path in path.glob('*.jpeg'):
            if img_path.name.startswith('left_'):
                label = "left"
            elif img_path.name.startswith('center_'):
                label = "center"
            else:
                label = "right"
            yield img_path.name, {
                'image': img_path,
                'label': label,
            }

from wand.image import Image


class Image(Image):

    def __init__(self, **kwargs):
        self.filename = kwargs.get("filename", None)
        # behind format is a setter so the extension has to be kept seperately
        self.extension = kwargs.pop("extension", None)

        super(Image, self).__init__(**kwargs)
        if self.extension:
            self.format = self.extension

    def make_blob(self):
        # wand.py is not able to convert mvg to svg
        if self.extension == 'svg' and self.filename:
            return self.filename.read()
        return super(Image, self).make_blob(self.extension)

    def append(self, other):
        self.sequence.append(other)

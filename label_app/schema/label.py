# A schema for the Gmail API label list and individual labels.
#   - Label list
#   - Individual label
# A class to hold the above variables and methods to access them.
## Path: label_app\schema\label.py
class Label:
        def __init__(self):
            self.label_list = []
            self.label = []
        def get_label_list(self):
            return self.label_list
        def get_label(self):
            return self.label
        def set_label_list(self, label_list):
            self.label_list = label_list
        def set_label(self, label):
            self.label = label
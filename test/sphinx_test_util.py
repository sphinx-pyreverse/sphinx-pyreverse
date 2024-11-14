"""
Defines mocks objects mimicking sphinx applications state for tests

Created on 22, 2020

@author: doublethefish
"""


class MockConfig:  # pylint: disable=missing-docstring,too-few-public-methods
    def __init__(self, output_ext):  # pylint: disable=missing-docstring
        if output_ext is None:
            output_ext = "png"
        self.sphinx_pyreverse_output = output_ext
        self.sphinx_pyreverse_filter_mode = None
        self.sphinx_pyreverse_class = None
        self.sphinx_pyreverse_show_ancestors = None
        self.sphinx_pyreverse_all_ancestors = None
        self.sphinx_pyreverse_show_associated = None
        self.sphinx_pyreverse_all_associated = None
        self.sphinx_pyreverse_show_builtin = None
        self.sphinx_pyreverse_module_names = None
        self.sphinx_pyreverse_only_classnames = None
        self.sphinx_pyreverse_ignore = None
        self.sphinx_pyreverse_image_max_width = 1000
        self.sphinx_pyreverse_image_scale = 1.0
        self.sphinx_pyreverse_colorized = None


class MockEnv:  # pylint: disable=missing-docstring,too-few-public-methods
    def __init__(self, output_ext):  # pylint: disable=missing-docstring
        self.srcdir = "."
        self.config = MockConfig(output_ext)


class MockDocSettings:  # pylint: disable=missing-docstring,too-few-public-methods
    def __init__(self, output_ext):  # pylint: disable=missing-docstring
        self.env = MockEnv(output_ext)


class MockDoc:  # pylint: disable=missing-docstring,too-few-public-methods
    def __init__(self, output_ext):  # pylint: disable=missing-docstring
        self.settings = MockDocSettings(output_ext)
        self.current_source = "."


class MockState:  # pylint: disable=missing-docstring,too-few-public-methods
    def __init__(self, output_ext=None):  # pylint: disable=missing-docstring
        self.document = MockDoc(output_ext)


class MockStateMachine:  # pylint: disable=missing-docstring,too-few-public-methods
    def __init__(self):  # pylint: disable=missing-docstring
        self.reporter = None

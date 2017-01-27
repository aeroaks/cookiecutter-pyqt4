from PyQt4 import QtGui

{% if cookiecutter.insert_statusbar == 'yes' -%}
class AboutDialog(QtGui.QDialog):
    """Contains the necessary elements to show helpful text in a dialog."""

    def __init__(self, parent=None):
        """Displays a dialog that shows application information."""
        super().__init__()

        self.setWindowTitle('About')
        self.resize(300, 200)

        author = QtGui.QLabel('{{ cookiecutter.full_name }}')
        author.setAlignment(Qt.AlignCenter)

        github = QtGui.QLabel('GitHub: {{ cookiecutter.github_username }}')
        github.setAlignment(Qt.AlignCenter)

        self.layout = QtGui.QVBoxLayout()
        self.layout.setAlignment(Qt.AlignVCenter)

        self.layout.addWidget(author)
        self.layout.addWidget(github)

        self.setLayout(self.layout)
{%- endif %}

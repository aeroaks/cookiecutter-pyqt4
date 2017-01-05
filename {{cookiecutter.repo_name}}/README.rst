===============================
{{ cookiecutter.package_name }}
===============================


.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}


{{ cookiecutter.project_short_description }}

Use run.py to run the GUI instance.
{{cookiecutter.application_name}}.py contains UI elements handling code for the whole window.
worker/main_worker.py contains all the logic and UI element handling for the {{cookiecutter.application_name}}.py
Logging can be used to create log of the GUI session. Log files are erased when a new session is started.

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
